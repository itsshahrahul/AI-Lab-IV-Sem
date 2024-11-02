class LoanEligibilitySystem:
    def __init__(self):
        age = int(input("Enter your age: "))
        income = int(input("Enter your income: "))
        self.check_eligibility(age, income)

    def check_eligibility(self, age, income):
        if age >= 18 and income >= 25000:
            print("You are eligible for a loan")
        elif age < 18:
            print("You must be at least 18 years old to apply for a loan")
        else:
            print("You must have an income of at least 25000 to apply for a loan")

def main():
    loan = LoanEligibilitySystem()

if __name__ == "__main__":
    main()
