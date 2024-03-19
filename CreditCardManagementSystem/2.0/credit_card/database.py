import sqlite3
from typing import List, Tuple, Optional

class CreditCardDatabase:
    def __init__(self, db_name: str = 'credit_cards.db') -> None:
        """
        Initialize the CreditCardDatabase object.

        Parameters:
        - db_name (str): The name of the SQLite database file.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """
        Create necessary tables if they don't exist in the database.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS credit_cards (
                id INTEGER PRIMARY KEY,
                number TEXT,
                expiration_date TEXT,
                cvv TEXT
            )
        ''')
        self.connection.commit()

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()

    def add_credit_card(self, number: str, expiration_date: str, cvv: str) -> None:
        """
        Add a credit card to the database.

        Parameters:
        - number (str): The credit card number.
        - expiration_date (str): The expiration date of the credit card.
        - cvv (str): The CVV code of the credit card.
        """
        self.cursor.execute('''
            INSERT INTO credit_cards (number, expiration_date, cvv)
            VALUES (?, ?, ?)
        ''', (number, expiration_date, cvv))
        self.connection.commit()

    def get_credit_card_by_id(self, card_id: int) -> Optional[Tuple[int, str, str, str]]:
        """
        Retrieve a credit card by its ID from the database.

        Parameters:
        - card_id (int): The ID of the credit card.

        Returns:
        - Tuple[int, str, str, str]: A tuple containing the credit card ID, number, expiration date, and CVV,
          or None if no credit card with the given ID exists.
        """
        self.cursor.execute('SELECT * FROM credit_cards WHERE id=?', (card_id,))
        return self.cursor.fetchone()

    def get_all_credit_cards(self) -> List[Tuple[int, str, str, str]]:
        """
        Retrieve all credit cards from the database.

        Returns:
        - List[Tuple[int, str, str, str]]: A list of tuples containing credit card ID, number, expiration date, and CVV.
        """
        self.cursor.execute('SELECT * FROM credit_cards')
        return self.cursor.fetchall()

    def update_credit_card(self, card_id: int, number: str, expiration_date: str, cvv: str) -> None:
        """
        Update a credit card in the database.

        Parameters:
        - card_id (int): The ID of the credit card to update.
        - number (str): The updated credit card number.
        - expiration_date (str): The updated expiration date of the credit card.
        - cvv (str): The updated CVV code of the credit card.
        """
        self.cursor.execute('''
            UPDATE credit_cards
            SET number=?, expiration_date=?, cvv=?
            WHERE id=?
        ''', (number, expiration_date, cvv, card_id))
        self.connection.commit()

    def delete_credit_card(self, card_id: int) -> None:
        """
        Delete a credit card from the database.

        Parameters:
        - card_id (int): The ID of the credit card to delete.
        """
        self.cursor.execute('DELETE FROM credit_cards WHERE id=?', (card_id,))
        self.connection.commit()




class TransactionDatabase:
    """
    A class for interacting with a SQLite database to store and manage transaction data.
    """

    def __init__(self, db_name: str = 'transactions.db') -> None:
        """
        Initializes a connection to the SQLite database for transactions.

        Args:
            db_name (str, optional): The name of the database file. Defaults to 'transactions.db'.
        """
        self.connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        """
        Creates the 'transactions' table in the database if it doesn't already exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                amount REAL,
                date TEXT,
                merchant TEXT
            )
        ''')
        self.connection.commit()

    def close(self) -> None:
        """
        Closes the connection to the database.
        """
        self.connection.close()

    def add_transaction(self, user_id: str, amount: float, date: str, merchant: str) -> None:
        """
        Adds a new transaction record to the database.

        Args:
            user_id (str): The ID of the user who made the transaction.
            amount (float): The transaction amount.
            date (str): The date of the transaction (in a format suitable for storage in a TEXT column).
            merchant (str): The merchant for the transaction.
        """
        self.cursor.execute('''
            INSERT INTO transactions (user_id, amount, date, merchant)
            VALUES (?, ?, ?, ?)
        ''', (user_id, amount, date, merchant))
        self.connection.commit()

    def get_transactions_by_user_id(self, user_id: str) -> list[tuple]:
        """
        Retrieves all transactions for a specific user from the database.

        Args:
            user_id (str): The ID of the user for whom to retrieve transactions.

        Returns:
            list[tuple]: A list of tuples where each tuple represents a transaction record
                (id, user_id, amount, date, merchant).
        """
        self.cursor.execute('SELECT * FROM transactions WHERE user_id=?', (user_id,))
        return self.cursor.fetchall()

    def delete_transaction(self, transaction_id: int) -> None:
        """
        Deletes a transaction record from the database based on its ID.

        Args:
            transaction_id (int): The ID of the transaction to be deleted.
        """
        self.cursor.execute('DELETE FROM transactions WHERE id=?', (transaction_id,))
        self.connection.commit()
