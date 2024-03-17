import datetime

class Transaction:
    """
    Represents a financial transaction using a credit card.
    """

    def __init__(self, user_id: str, amount: float, date: datetime.date, merchant: str) -> None:
        """
        Initializes a new Transaction object.

        Parameters:
            user_id: The user_id for the transaction (Str)
            amount: The transaction amount (float).
            date: The transaction date (datetime.date).
            merchant: The merchant name (str).
        """
        self.user_id: str = user_id
        self.amount: float = amount
        self.date: datetime.date = date
        self.merchant: str = merchant

    def get_transaction_details(self) -> str:
        """
        Returns a string containing the transaction details.

        Returns:
            A string with transaction details (str).
        """
        return f"Amount: {self.amount}, Date: {self.date}, Merchant: {self.merchant}"

    def set_amount(self, new_amount: float) -> None:
        """
        Updates the amount of the transaction.

        Parameters:
            new_amount: The new transaction amount (float).
        """
        self.amount = new_amount

    def set_merchant(self, new_merchant: str) -> None:
        """
        Updates the merchant for the transaction.

        Parameters:
            new_merchant: The new merchant name (str).
        """
        self.merchant = new_merchant

    def set_date(self, new_date: datetime.date) -> None:
        """
        Updates the date of the transaction.

        Parameters:
            new_date: The new transaction date (datetime.date).
        """
        self.date = new_date
