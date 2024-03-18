
from ast import List
from credit_card.database import CreditCardDatabase, TransactionDatabase
from credit_card.transaction import Transaction

class Account:
    """
    Manages a collection of CreditCard and Transaction objects for a user.
    """
    def __init__(self, user_id):
        self.user_id: str = user_id
        self.credit_card_db = CreditCardDatabase()
        self.transaction_db = TransactionDatabase()
        self.balance: float = 0.0

    def add_card(self, number, expiration_date, cvv):
        """
        Adds a new credit card to the account.

        Parameters:
        - number (str): The credit card number.
        - expiration_date (str): The expiration date of the credit card.
        - cvv (str): The CVV code of the credit card.
        """
        self.credit_card_db.add_credit_card(number, expiration_date, cvv)

    def remove_card(self, card_id):
        """
        Removes a credit card from the account.

        Parameters:
        - card_id (int): The ID of the credit card to remove.
        """
        self.credit_card_db.delete_credit_card(card_id)

    def get_card(self, card_id):
        """
        Retrieves a credit card by its ID.

        Parameters:
        - card_id (int): The ID of the credit card to retrieve.

        Returns:
        - CreditCard: The retrieved CreditCard object if found, else None.
        """
        return self.credit_card_db.get_credit_card_by_id(card_id)

    def add_transaction(self, amount, date, merchant):
        """
        Adds a new transaction to the account.

        Parameters:
        - user_id (Str): the id for the user
        - amount (float): The amount of the transaction.
        - date (str): The date of the transaction.
        - merchant (str): The merchant associated with the transaction.
        """
        self.transaction_db.add_transaction(self.user_id,amount, date, merchant)

    def remove_transaction(self, transaction_id):
        """
        Removes a transaction from the account.

        Parameters:
        - transaction_id (int): The ID of the transaction to remove.
        """
        self.transaction_db.delete_transaction(transaction_id)

    def get_transactions(self) -> List:
        """
        Retrieves all transactions associated with the account.

        Returns:
        - List[Transaction]: A list of Transaction objects representing the transactions.
        """
        return self.transaction_db.get_transactions_by_user_id(self.user_id)
    
    def get_balance(self) -> float:
        """
        Returns the current account balance.

        Returns:
            The current balance (float).
        """
        return self.balance
