from datetime import datetime

class CreditCard:
    """
    Represents a credit card with details.
    """

    def __init__(self, number: str, expiration_date: datetime, cvv: str):
        """
        Initializes a CreditCard object.

        Parameters:
        - number (str): The credit card number.
        - expiration_date (datetime): The expiration date of the credit card.
        - cvv (str): The CVV (Card Verification Value) of the credit card.
        """
        self.number: str = number  # (Store masked for security in practice)
        self.expiration_date: datetime = expiration_date
        self.cvv: str = cvv  # (Store securely using hashing or encryption)

    def get_masked_number(self) -> str:
        """
        Returns a masked version of the credit card number (e.g., XXXX-XXXX-XXXX-1234).

        Returns:
        - str: The masked credit card number.
        """
        return f"****-****-****-{self.number[-4:]}"

    def is_expired(self) -> bool:
        """
        Checks if the credit card is expired based on the expiration date.

        Returns:
        - bool: True if the credit card is expired, False otherwise.
        """
        return datetime.now() > self.expiration_date

    def set_expiration_date(self, new_expiration_date: datetime) -> None:
        """
        Updates the expiration date of the credit card.

        Parameters:
        - new_expiration_date (datetime): The new expiration date.
        """
        self.expiration_date: datetime = new_expiration_date

    def set_cvv(self, new_cvv: str) -> None:
        """
        Updates the CVV of the credit card.

        Parameters:
        - new_cvv (str): The new CVV.
        """
        self.cvv: str = new_cvv
