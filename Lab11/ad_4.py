import xml.dom.minidom as xml

class BankAccount:
    def __init__(self, name: str, surname: str, account_number: str, type: str, balance: float):
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.type = type
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f} zł")

def save_to_file(accounts: list["BankAccount"]):
    doc = xml.Document()

    root = doc.createElement("BankAccounts")
    doc.appendChild(root)

    for account in accounts:
        acc_el = doc.createElement("BankAccount")
        root.appendChild(acc_el)

        def add_element(name, value):
            el = doc.createElement(name)
            el.appendChild(doc.createTextNode(str(value)))
            acc_el.appendChild(el)

        add_element("Name", account.name)
        add_element("Surname", account.surname)
        add_element("AccountNumber", account.account_number)
        add_element("Type", account.type)
        add_element("Balance", f"{account.balance:.2f}")

    with open("accounts.xml", "w", encoding="utf-8") as file:
        file.write(doc.toprettyxml(indent="    "))


accounts = [
    BankAccount("John", "Doe", "111", "Savings", 1200.50),
    BankAccount("Anna", "Smith", "222", "Checking", 800.00)
]

save_to_file(accounts)
