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
        self.sessions = {}

    def is_valid(self) -> bool:
        """
        Checks if the session token is still valid.

        Returns:
            True if the token is valid, False otherwise.
        """
        return datetime.now() < self.expiration_time
    
    def authorize_session(self, user_id: str) -> str:
        """
        Generates and returns a session token for the authenticated user.

        Parameters:
        - user_id (str): The ID of the user.

        Returns:
        - str: The generated session token.
        """
        session_token: str = secrets.token_hex(16)
        self.sessions[user_id] = session_token
        return session_token

    def is_authorized(self, user_id: str, session_token: str) -> bool:
        """
        Checks if the user with the given user ID has an active session with the provided session token.

        Parameters:
        - user_id (str): The ID of the user.
        - session_token (str): The session token to be verified.

        Returns:
        - bool: True if the user is authorized, False otherwise.
        """
        return user_id in self.sessions and self.sessions[user_id] == session_token