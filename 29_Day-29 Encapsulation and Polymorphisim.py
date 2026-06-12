class SecureWallet:
    def __init__(self, cash):
        self.__balance = cash  # Private attribute prefix (Double underscore protects variables)

    def check_funds(self):
        return f"Balance: ${self.__balance}"

wallet = SecureWallet(500)
# print(wallet.__balance) # Raises AttributeError
print(wallet.check_funds())
