import time
print("please enter your card")
time.sleep(5)

password=1234
istrue=True
pin=int(input("Enter your pin here: "))

balance=5000

if pin==password:
    print("""1==check the balance \n 2==withdrawl the amount \n 3==deposit the amount \n 4==exit""")
   

    try:
        option=int(input("enter your choice: "))
    except:
        print("enter valid option")
    
    if option==1:
        print(f"your current balance is {balance}")
    if option==2:
        withdrawl_amount=int(input("enter the amount to withdraw: "))
        balance=balance-withdrawl_amount
        print(f"{withdrawl_amount} is debited to your account")
        print(f"now your current balance is {balance}")
    if option==3:
        deposit_amount=int(input("enter the deposited amount: "))
        balance=deposit_amount+balance
        print(f"Your available balance is {balance}")
    if option==4:
        istrue=False
     
else:
    print("enter the valid password !")
        














# print("___________WELCOME_______________ \n")

# print("  __Enter your card plz__")

# amount=1000

# bankmenu={
#     "for debite the amount" : 1,
#     "for credit the amount" : 2,
#     "for show availble balance":3
# }

# a=int(input("please enter the 1 to show our services : "))

# if a==1:
#     print("  for debite the amount : 1 \n  for credit the amount:  2 \n  for show availble balance:3")
# else :
#     print("Inavalid synatax")

# b=int(input("Chose the service :"))

# if b==1:
#     c=int(input("enter the debited amount: "))
#     if amount < c:
#         print("Your balance is low")
#     else:
#       amount=amount-c
#     print("your remaining balance is : ", amount)
# elif b==2:
#     d=int(input("enter the credited amount : "))
#     amount=amount+d
# elif b==3:
#     print(amount)

# print("THANK you")