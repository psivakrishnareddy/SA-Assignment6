import secrets
from datetime import datetime, timedelta

class Session:
    """
    Manages user sessions using token-based authentication.
    """

    def __init__(self, user_id: int) -> None:
        """
        Initializes a new Session object.

        Args:
            user_id: The user's ID (int).
        """
        self.user_id: int = user_id
        self.token: str = secrets.token_hex(16)  # Generate a random token
        self.expiration_time: datetime = datetime.now() + timedelta(hours=1)  # Set expiration time to 1 hour from now

    def is_valid(self) -> bool:
        """
        Checks if the session token is still valid.

        Returns:
            True if the token is valid, False otherwise.
        """
        return datetime.now() < self.expiration_time
