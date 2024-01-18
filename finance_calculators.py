import math

# Welcome message and menu for the Finance Calculator
while True:
    print("\nHello and welcome to the Finance Calculator! Finance calculator options:\n")
    print("Investment - to calculate the amount of interest you will earn on your investment")
    print("Bond - to calculate the amount you will have to pay on a home loan")
    print("End - to end the Finance Calculator \n")

    option = input("Enter either 'Investment', 'Bond', or 'End' from the menu above to proceed:\n > ").lower()

    # Block of code executed based on the investment, bond, or end options the user selects
    if option == "end":
        print("\nThank you for using the Finance Calculator! Have a good day :).\n")
        break

    # Option for investment: User inputs
    elif option == "investment":
        investment = float(input("How much money are you depositing?\n > £ "))
        interest = float(input("What interest rate should be used (enter only the number)?\n > % ")) / 100
        years = float(input("How many years do you plan to invest?\n > "))
        rate_type = input("Please select: How do you want to calculate? 'simple' or 'compound' interest?\n > ").lower()

        # Investment calculations: simple or compound
        simple = investment * (1 + (interest * years))
        compound = investment * math.pow((1 + interest), years)

        if rate_type == "simple":
            print(f"\nThank you! Your return on investment, with a simple interest rate, will yield: £{simple:,.2f}\n")
        elif rate_type == "compound":
            print(f"\nThank you! Your return on investment, with a compound interest rate, will yield: £{compound:,.2f}\n")
        else:
            print("\nYou did not enter a viable option for this calculation. Please re-submit.\n")

    # Option for bond: User inputs
    elif option == "bond":
        bond = float(input("Please enter the present value of the house.\n > "))
        interest_bond = (float(input("What interest rate should be used (enter only the number)?\n > ")) / 100) / 12
        months = float(input("How many months do you plan to take to repay the bond?\n > "))

        # Bond calculation
        bond_repayment = (interest_bond * bond) / (1 - (1 + interest_bond) ** (-months))
        print(f"\nThank you! Your monthly bond repayment will be: £{bond_repayment:,.2f}\n")

    else:
        print("\nYou did not enter a viable option for this calculation. Please re-submit.\n")