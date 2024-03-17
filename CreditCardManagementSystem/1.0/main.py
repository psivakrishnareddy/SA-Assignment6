from datetime import datetime
from credit_card.credit_card import CreditCard
from credit_card.transaction import Transaction
from CreditCardManager import CreditCardManager
from account.account import Account


# Example usage

credit_card_manager = CreditCardManager()

user_account: Account = credit_card_manager.create_account("user123")

# Example session management
token = credit_card_manager.create_session("user123")
print("Session Token:", token)


# Add a credit card
card = CreditCard("1234567890123456", datetime(2025, 12, 31), "123")
user_account.add_card(card.number, card.expiration_date, card.cvv)

# Add a transaction
transaction = Transaction(user_account.user_id,100.0, datetime.now(), "Amazon")
user_account.add_transaction(100.0, datetime.now(), "Amazon")
print(credit_card_manager.list_accounts())
print(user_account.get_card(1))
print(card.get_masked_number())

# Printing the available transactions
for transaction in user_account.get_transactions():
    print(transaction)

# Validate session token
session = credit_card_manager.get_session(token)
if session:
    print("Session is valid.")
else:
    print("Session is invalid.")
    exit(0)

# Retrieve account and credit card
account: Account = credit_card_manager.get_account("user123")
print("Retrieved Account:", account.user_id)
credit_card = user_account.get_card(1)  # Assuming credit card ID is 1
print("Retrieved Credit Card:", credit_card)

# Remove account and credit card
credit_card_manager.remove_account("user123")
user_account.remove_card(1)  # Assuming credit card ID is 1



# Invalidate session token
credit_card_manager.invalidate_session(token)
