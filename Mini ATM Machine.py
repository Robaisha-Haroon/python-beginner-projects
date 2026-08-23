# Mini ATM machine

# Storing account information
account= {
    "Name" : "Robaisha",
    "Balance" : 70000,
    "Pin": 1234
}
# Ask for pin
take_pin= int(input("Enter your pin:\n"))
if take_pin == account["Pin"]:
    print("Valid Pin number")
    print("=========== Welcome To Your ATM Account =========== ")
    # Ask for choice
    while True:
        choice= int(input("""What would you like to do:
        1. Check Balance
        2. Deposite the cash
        3. Withdrawal the cash
        4. Exit\n"""))
        # Show the balance
        if choice == 1:
            print("Your total balance is:", account["Balance"])
       # Ask for deposite money
        elif choice == 2:
            deposite_amount= int(input("How much amount you want to deposite?\n"))
           # Deposite money must be greater than 0
            if deposite_amount > 0:
                print("Deposite has been transferred successfully\n")
                account["Balance"]+= deposite_amount
                print("Your new balance is ", account["Balance"])
            else:
                print("Invalid balance")
       # Ask for withdrawal cash
        elif choice == 3:
            withdrawal_amount= int(input("How much balance you want to withdraw?\n"))
           # Withdrawal cash must be greater than 0 and, less or equal to actual balance
            if withdrawal_amount > 0 and withdrawal_amount <= account["Balance"]:
                print("Withdraw ammount has been transferred successfully")
                account["Balance"] -= withdrawal_amount
                print("Your new balance is ", account["Balance"])  
            else:
                print("Transaction failed: Invalid amount")
        # Exit from loop
        elif choice == 4:
            print("Thankyou for visiting")
            break
        # Ask for choose between valid choice
        else:
            print("Invalid choice. Choose between 1 to 4")          
else:
     print("Invalid Pin number")   
