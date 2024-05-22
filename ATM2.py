user_pin = 2508
user_balance = 97000.00
user_name = "Ms. Shubham Ukirde"
print("Welcome to your bank account", user_name, end = "\n\n")

choice = 5
#choice..
while (True):
    print("\t********************************")
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change PIN")
    print("\t\t5. Return Card")
    print("\t********************************")
    choice = int(input("Enter number to proceed > "))
    print('\n')
    print('\t***********************************')
    


    if choice == 0:        #logout(cancel)                                                               #...1 st if & else
        print("Exiting...")
        
        print("You have been logged out. Thank you!\n\n") 
        break
    elif choice in (1,2,3,4,5):  ### enter pin                                                            #...1 st if & else  
        
        while (True):
            input_pin = int(input("Please enter your 4-digit PIN > "))
        
            if input_pin == user_pin:  # check the pin                                                    #...2nd if & else
                print("Account Proccesing!\n\n")
                
                if choice == 1: # check balance                                                            #...3rd if & else                                                           
                    print("Loading Account Balance...")
                
                    print("Your current balance is Rs.", user_balance, end = "\n")
                    break
                elif choice == 2:  #withdraw                                                               #...3rd if & else   
                    print("Opening Cash Withdrawal...")
                    

                    while(True):                                                                           #....withdraw loop
                        withdraw_amt = float(input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Yes/Not > ")
                            if confirm in ('Yes', 'yes'):
                                user_balance-=withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.", user_balance, end = "\n")
                                break

                            else:
                        
                                
                                print("Transaction Cancelled!\n\n")
                                break
                    
                    break

                elif choice == 3: # deposit                                                                    #...3rd if & else   
                    print("Loading Cash Deposit...")
                    

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Yes/Not > ")
                    if confirm in ('Yes', 'yes'): 
                        user_balance+=deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end = "\n")
                    else:
                        print("Cancelling transaction...")
                        print("Transaction Cancelled!\n\n")
                                
                    break

                    
                elif choice == 4: #change pin                                                                          #...3rd if & else   
                    print("Loading PIN Change...")
                    

                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    user_pin = pin_new # confirm th e new pin
                    print("PIN changed successfully! \n")
                    

                    

                    break

                else:                                                                                        
                    print("Loading Card Return...")
                    print("Returning your ATM Card")
        

                    break

            else:                                                                                                  #...3rd if & else   
                print("PIN incorrect! Try Again...",end = "\n\n")   

        else:                                                                                                      #...2nd if & else
            print("Exiting...")
            print("You have been logged out. Thank you Shubham Sir...!\n\n")
            break
            

    else:                                                                                                           #...1 st if & else
        print("Invalid input!")
        print("\t\t Enter 0 to Logout and Exit!")
        continue
