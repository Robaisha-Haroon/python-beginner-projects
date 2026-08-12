Contact = {} 
# loop for infinity
while True: 
    choice = int(input("""\nWhat would you like to do:
1. Add contact 
2. Find contact 
3. Exit\n""")) 
# conditional statements  
    if choice == 1: 
        name = input("Enter your name\n").title().strip() 
        phone = int(input("Enter your number\n")) 
        email = input("Enter your email address\n").strip() 
      # Nested conditional statements
        if name == "" and phone == "" and email == "": 
            print("All information are required") 
        else: 
            Contact[name] = { 
                "Phone:": phone, 
                "Email:": email 
            } 
            print("Contact has been successfully added!") 
            
    elif choice == 2: 
        search_name = input("Enter the name you want to find\n").title().strip() 
       # Nested conditional statements  
        if search_name in Contact: 
            print("Contact has been found") 
            print("Name:", search_name) 
            print("Phone:", Contact[search_name]["Phone:"]) 
            print("Email:", Contact[search_name]["Email:"]) 
        else: 
            print("Contact not found") 
            
    elif choice == 3: 
        print("Contact book closed successfully") 
        break 
    else: 
        print("Invalid choice. Enter from 1, 2, 3")
