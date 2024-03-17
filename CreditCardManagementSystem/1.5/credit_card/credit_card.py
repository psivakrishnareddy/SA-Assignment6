from datetime import datetime
class CreditCard:
    """
    Represents a credit card with details.
    """
    def __init__(self, number, expiration_date, cvv):
        self.number = number  # (Store masked for security in practice)
        self.expiration_date = expiration_date
        self.cvv = cvv  # (Store securely using hashing or encryption)

    def get_masked_number(self):
        """
        Returns a masked version of the credit card number (e.g., XXXX-XXXX-XXXX-1234).
        """
        return f"****-****-****-{self.number[-4:]}"

    def is_expired(self):
        """
        Checks if the credit card is expired based on the expiration date.
        """
        return datetime.now() > self.expiration_date

    def set_expiration_date(self, new_expiration_date):
        """
        Updates the expiration date of the credit card.
        """
        self.expiration_date = new_expiration_date

    def set_cvv(self, new_cvv):
        """
        Updates the CVV of the credit card.
        """
        self.cvv = new_cvv