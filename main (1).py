class personalfinanceApp:

    def __init__(self):
        self.balance = 0.0
        self.transactions =[]
    def add_income(self):
        amount = float(input("enter the amount of income:$"))
        self.balance += amount
        self.transactions.append(("income",amount))
        print(f"income added:$(amount:.2f)")
    def record_expensive(self):
        amount = float(input("enter the amount of expense:$"))

        if amount > self.balance:
            print("insufficient balance. please try again.")

        else:

            category = input("enter expense category(e.g., Rent,food,transport):")

            self.balance.balance -= amount

            self.transactions.append((category, -amount))

            print(f"expense recorded:$(amount:.2f) for(category)")
    def view_balance(self):
        print(f"current balance: $(self.balance:.2f)")
    
    def transcation_summary(self):

        print("\nTranscations summary:")

        for t_type, amount in self.transactions:
            print(f"(t_type): $(amount:.2f)")

        self.view_balance()

    def start(self):

        print("welcome to personal finance manager!")

        while True:
            print("\nMenu:")

            print("1. Add Income")

            print("2. Record Expense")

            print("3. View Balance")

            print("4. View Transaction summary")

            print("5. Exit")

            choice = input("select an option(1-5):")

            if choice == '1':

                self.add_income()

            elif choice == '2':
                self.record_expense()

            elif choice == '3':

                self.view_balance()

            elif choice == '4':

                self.transcation_summary()

            elif choice == '5':

                print("existing.... Thankyou for using the app!")

                break
            else:

                print("invalid option. please try again.")

if __name__ == "__main__":
    app=personalfinanceApp()

    app.start()