# ATM Machine System

from bank_system import BankSystem
from account import Account

bank = BankSystem()

def main_menu():
    print("\n🏦 Welcome to ATM Machine System")
    print("1. Create Account")
    print("2. Login to Account")
    print("3. Exit")

while True:
    main_menu()
    choice = input('Enter choice: ')

    if choice == '1':
        acc_num = input('Enter Account Number: ')
        name = input('Enter your name: ')
        pin = input('Set 4-digit PIN: ')
        acc = bank.create_account(acc_num, name, pin)
        print('✅ Account created successfully!' if acc else '❌ Account already exists!')

    elif choice == '2':
        acc_num = input('Enter Account Number: ')
        pin = input('Enter PIN: ')
        user = bank.authenticate(acc_num, pin)

        if user:
            print(f"\n🎉 Welcome, {user.name}!")
            while True:
                print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Delete Account\n6. Logout")
                opt = input("Choose option: ")

                if opt == '1':
                    print(f'💰 Balance: {user.check_balance()}')

                elif opt == '2':
                    amt = float(input('Enter deposit amount: '))
                    if user.Deposit(amt):  # corrected from Deposit() to deposit()
                        bank.save_data()
                        print("✅ Deposit successful!")
                    else:
                        print("❌ Invalid amount.")

                elif opt == '3':
                    amt = float(input("Enter withdraw amount: "))
                    if user.withdraw(amt):
                        bank.save_data()
                        print("✅ Withdrawal successful!")
                        print(f'Remaining balance is: {user.balance}')
                    else:
                        print("❌ Insufficient balance.")


                elif opt == '4':
                   new_pin = input("Enter new 4-digit PIN: ")
                   user.pin = new_pin
                   bank.save_data()
                   print('🔁 PIN updated successfully!')
                
                elif opt == '5':
                    confirm = input('Are you sure you want to delete your account? (yes/no):')
                    if confirm.lower() == 'yes':
                        bank.balance.remove(user)
                        bank.save_data()
                        print('❌ Account deleted successfully!')
                        break
                elif opt == '6':
                    print('🔒 Logged out.')
                    break

                else:
                    print('⚠️ Invalid option.')

        else:
            print("❌ Authentication failed. Try again.")

    elif choice == '3':
        print('👋 Goodbye!')
        break

    else:
        print('⚠️ Invalid choice. Try again.')