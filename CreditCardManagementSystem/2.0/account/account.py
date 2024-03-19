
from datetime import datetime
import random
import string
from typing import Optional, Tuple, List
from credit_card.database import CreditCardDatabase, TransactionDatabase
from credit_card.transaction import Transaction

class Account:
    """
    Manages a collection of CreditCard and Transaction objects for a user.
    """
    def __init__(self, user_id: str):
        """
        Initializes an Account object.

        Parameters:
        - user_id (str): The ID of the user.
        """
        self.user_id: str = user_id
        self.credit_card_db: CreditCardDatabase = CreditCardDatabase()
        self.transaction_db: TransactionDatabase = TransactionDatabase()
        self.balance: float = 0.0

    def add_card(self, number: str, expiration_date: str, cvv: str) -> None:
        """
        Adds a new credit card to the account.

        Parameters:
        - number (str): The credit card number.
        - expiration_date (str): The expiration date of the credit card.
        - cvv (str): The CVV code of the credit card.
        """
        self.credit_card_db.add_credit_card(number, expiration_date, cvv)

    def remove_card(self, card_id: int) -> None:
        """
        Removes a credit card from the account.

        Parameters:
        - card_id (int): The ID of the credit card to remove.
        """
        self.credit_card_db.delete_credit_card(card_id)

    def get_card(self, card_id: int):
        """
        Retrieves a credit card by its ID.

        Parameters:
        - card_id (int): The ID of the credit card to retrieve.

        Returns:
        - CreditCard: The retrieved CreditCard object if found, else None.
        """
        return self.credit_card_db.get_credit_card_by_id(card_id)

    def add_transaction(self, amount: float, date: str, merchant: str) -> None:
        """
        Adds a new transaction to the account.

        Parameters:
        - amount (float): The amount of the transaction.
        - date (str): The date of the transaction.
        - merchant (str): The merchant associated with the transaction.
        """
        self.transaction_db.add_transaction(self.user_id, amount, date, merchant)

    def remove_transaction(self, transaction_id: int) -> None:
        """
        Removes a transaction from the account.

        Parameters:
        - transaction_id (int): The ID of the transaction to remove.
        """
        self.transaction_db.delete_transaction(transaction_id)

    def get_transactions(self) -> List[Tuple]:
        """
        Retrieves all transactions associated with the account.

        Returns:
        - List[Transaction]: A list of Transaction objects representing the transactions.
        """
        return self.transaction_db.get_transactions_by_user_id(self.user_id)
    
    
    def get_balance_v2(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, 
                       transaction_type: Optional[str] = None, merchant: Optional[str] = None) -> float:
        """
        Retrieves the current account balance based on specified criteria for filtering transactions.

        Parameters:
        - start_date (datetime, optional): The start date of the date range filter.
        - end_date (datetime, optional): The end date of the date range filter.
        - transaction_type (str, optional): The type of transactions to include (e.g., 'purchase', 'refund').
        - merchant (str, optional): The merchant to include in the balance calculation.

        Returns:
        - float: The current account balance based on the specified criteria.
        """
        transactions = self.transaction_db.get_transactions_by_user_id(self.user_id)
        filtered_transactions = self._filter_transactions(transactions, start_date, end_date, transaction_type, merchant)
        balance = sum(transaction[2] for transaction in filtered_transactions)  # Assuming amount is stored in the third column
        return balance

    def _filter_transactions(self, transactions: List[Tuple], start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, 
                             transaction_type: Optional[str] = None, merchant: Optional[str] = None) -> List[Tuple]:
        """
        Filters transactions based on specified criteria.

        Parameters:
        - transactions (list): List of transactions to filter.
        - start_date (datetime, optional): The start date of the date range filter.
        - end_date (datetime, optional): The end date of the date range filter.
        - transaction_type (str, optional): The type of transactions to include (e.g., 'purchase', 'refund').
        - merchant (str, optional): The merchant to include in the filter.

        Returns:
        - list: Filtered list of transactions.
        """
        filtered_transactions = transactions
        if start_date:
            filtered_transactions = [t for t in filtered_transactions if t[3] >= start_date]  # Assuming date is stored in the fourth column
        if end_date:
            filtered_transactions = [t for t in filtered_transactions if t[3] <= end_date]  # Assuming date is stored in the fourth column
        if transaction_type:
            filtered_transactions = [t for t in filtered_transactions if t[4] == transaction_type]  # Assuming transaction type is stored in the fifth column
        if merchant:
            filtered_transactions = [t for t in filtered_transactions if t[5] == merchant]  # Assuming merchant is stored in the sixth column
        return filtered_transactions

    def update_balance(self, transaction: Transaction) -> None:
        """
        Updates the balance based on a transaction amount.

        Parameters:
            transaction (Transaction): The transaction object to update the balance.
        """
        if transaction.payment_processed:
            self.balance += transaction.amount
        else:
            self.balance -= transaction.amount

    def enable_two_factor_authentication(self) -> None:
        """
        Enables two-factor authentication for the account.
        """
        self.two_factor_enabled = True
        self.generate_verification_code()

    def disable_two_factor_authentication(self) -> None:
        """
        Disables two-factor authentication for the account.
        """
        self.two_factor_enabled = False
        self.verification_code = None

    def generate_verification_code(self) -> None:
        """
        Generates a random verification code for two-factor authentication.
        """
        self.verification_code = ''.join(random.choices(string.digits, k=6))  # Generate a 6-digit code

    def validate_verification_code(self, verification_code: str) -> bool:
        """
        Validates the provided verification code for two-factor authentication.

        Parameters:
        - verification_code (str): The verification code provided by the user.

        Returns:
        - bool: True if the verification code is valid, False otherwise.
        """
        return self.two_factor_enabled and verification_code == self.verification_code

    def enable_two_factor_authentication(self, user_id: str) -> None:
        """
        Enables two-factor authentication for the specified user account.

        Parameters:
        - user_id (str): The ID of the user account.
        """
        account = self.account_db.get_account_by_user_id(user_id)
        if account:
            account.enable_two_factor_authentication()

    def disable_two_factor_authentication(self, user_id: str) -> None:
        """
        Disables two-factor authentication for the specified user account.

        Parameters:
        - user_id (str): The ID of the user account.
        """
        account = self.account_db.get_account_by_user_id(user_id)
        if account:
            account.disable_two_factor_authentication()

    def verify_authentication_code(self, user_id: str, verification_code: str) -> bool:
        """
        Verifies the provided verification code for two-factor authentication.

        Parameters:
        - user_id (str): The ID of the user account.
        - verification_code (str): The verification code provided by the user.

        Returns:
        - bool: True if the verification code is valid, False otherwise.
        """
        account = self.account_db.get_account_by_user_id(user_id)
        if account:
            return account.validate_verification_code(verification_code)
        return False