import datetime
from gettext import translation
from typing import List, Optional
from account.account import Account
from account.database import AccountDatabase
from session import Session
from credit_card.database import CreditCardDatabase

class CreditCardManager:
    """
    Provides an interface for manipulating Account objects.
    """
    def __init__(self):
        self.account_db = AccountDatabase()
        self.credit_card_db = CreditCardDatabase()
        self.sessions = {}

    def create_account(self, user_id: str) -> Account:
        """
        Creates a new account for the given user ID.

        Parameters:
        - user_id (str): The ID of the user.

        Returns:
        - Account: The created Account object.
        """
        self.account_db.add_account(user_id)

        return Account(self.account_db.get_account_by_user_id(user_id)[1])

    def get_account(self, user_id: str)  -> Account:
        """
        Retrieves the account for the given user ID.

        Parameters:
        - user_id (str): The ID of the user.

        Returns:
        - Account: The retrieved Account object if found, else None.
        """
        return Account(self.account_db.get_account_by_user_id(user_id)[1])

    def remove_account(self, user_id: str):
        """
        Removes the account for the given user ID.

        Parameters:
        - user_id (str): The ID of the user.
        """
        account = self.get_account(user_id)
        if account:
            self.account_db.delete_account(account.user_id)  

    def list_accounts(self) -> List[str]:
        """
        Returns a list of all user IDs with accounts.

        Returns:
        - List[str]: List of user IDs with accounts.
        """
        return [account[1] for account in self.account_db.get_all_accounts()]

    def create_session(self, user_id: str) -> str:
        """
        Creates a new session for the given user ID.

        Parameters:
        - user_id (str): The ID of the user.

        Returns:
        - str: The token associated with the created session.
        """
        session = Session(user_id)
        self.sessions[user_id] = session
        return session.token

    def get_session(self, token: str) -> Session:
        """
        Retrieves the session associated with the given token.

        Parameters:
        - token (str): The session token.

        Returns:
        - Session: The retrieved Session object if found and valid, else None.
        """
        for session in self.sessions.values():
            if session.token == token and session.is_valid():
                return session
        return None

    def invalidate_session(self, token: str):
        """
        Invalidates the session associated with the given token.

        Parameters:
        - token (str): The session token.
        """
        for user_id, session in self.sessions.items():
            if session.token == token:
                del self.sessions[user_id]
                break
        

            
    # def authenticate_user(self, user_id, password):
    #     """
    #     Authenticates the user with the given user ID and password.

    #     Parameters:
    #     - user_id (str): The ID of the user.
    #     - password (str): The password for the user.

    #     Returns:
    #     - bool: True if authentication is successful, False otherwise.
    #     """
    #     account = self.account_db.get_account_by_user_id(user_id)
    #     if account:
    #         hashed_password = account[2]  # Assuming password hash is stored in the third column
    #         if self._verify_password(password, hashed_password):
    #             return True
    #     return False

    # def authorize_session(self, user_id):
    #     """
    #     Generates and returns a session token for the authenticated user.

    #     Parameters:
    #     - user_id (str): The ID of the user.

    #     Returns:
    #     - str: The generated session token.
    #     """
    #     session_token = secrets.token_hex(16)
    #     self.sessions[user_id] = session_token
    #     return session_token

    # def is_authorized(self, user_id, session_token):
    #     """
    #     Checks if the user with the given user ID has an active session with the provided session token.

    #     Parameters:
    #     - user_id (str): The ID of the user.
    #     - session_token (str): The session token to be verified.

    #     Returns:
    #     - bool: True if the user is authorized, False otherwise.
    #     """
    #     return user_id in self.sessions and self.sessions[user_id] == session_token

    # def _hash_password(self, password):
    #     """
    #     Hashes the provided password using SHA-256.

    #     Parameters:
    #     - password (str): The password to be hashed.

    #     Returns:
    #     - str: The hashed password.
    #     """
    #     return sha256(password.encode()).hexdigest()

    # def _verify_password(self, password, hashed_password):
    #     """
    #     Verifies the provided password against the hashed password.

    #     Parameters:
    #     - password (str): The password to be verified.
    #     - hashed_password (str): The hashed password.

    #     Returns:
    #     - bool: True if the password matches the hashed password, False otherwise.
    #     """
    #     return hashed_password == self._hash_password(password)
