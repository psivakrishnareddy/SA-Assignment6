import sqlite3
from typing import List, Tuple, Optional

class AccountDatabase:
    def __init__(self, db_name: str = 'accounts.db') -> None:
        """
        Initialize the AccountDatabase object.

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
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                user_id TEXT
            )
        ''')
        self.connection.commit()

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()

    def add_account(self, user_id: str) -> None:
        """
        Add an account to the database.

        Parameters:
        - user_id (str): The ID of the user associated with the account.
        """
        self.cursor.execute('''
            INSERT INTO accounts (user_id)
            VALUES (?)
        ''', (user_id,))
        self.connection.commit()

    def get_account_by_id(self, account_id: int) -> Optional[Tuple[int, str]]:
        """
        Retrieve an account by its ID from the database.

        Parameters:
        - account_id (int): The ID of the account.

        Returns:
        - Tuple[int, str]: A tuple containing the account ID and user ID,
          or None if no account with the given ID exists.
        """
        self.cursor.execute('SELECT * FROM accounts WHERE user_id=?', (account_id,))
        account = self.cursor.fetchone()
        return account

    def get_account_by_user_id(self, user_id: str) -> Optional[Tuple[int, str]]:
        """
        Retrieve an account by its associated user ID from the database.

        Parameters:
        - user_id (str): The ID of the user associated with the account.

        Returns:
        - Tuple[int, str]: A tuple containing the account ID and user ID,
          or None if no account with the given user ID exists.
        """
        self.cursor.execute('SELECT * FROM accounts WHERE user_id=?', (user_id,))
        return self.cursor.fetchone()

    def get_all_accounts(self) -> List[Tuple[int, str]]:
        """
        Retrieve all accounts from the database.

        Returns:
        - List[Tuple[int, str]]: A list of tuples containing account ID and user ID.
        """
        self.cursor.execute('SELECT * FROM accounts')
        return self.cursor.fetchall()

    def update_account(self, account_id: int, user_id: str) -> None:
        """
        Update an account in the database.

        Parameters:
        - account_id (int): The ID of the account to update.
        - user_id (str): The updated user ID associated with the account.
        """
        self.cursor.execute('''
            UPDATE accounts
            SET user_id=?
            WHERE id=?
        ''', (user_id, account_id))
        self.connection.commit()

    def delete_account(self, account_id: int) -> None:
        """
        Delete an account from the database.

        Parameters:
        - account_id (int): The ID of the account to delete.
        """
        self.cursor.execute('DELETE FROM accounts WHERE user_id=?', (account_id,))
        self.connection.commit()
