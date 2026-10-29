def operation():
 bal=5000
 while True:
  print("1. Check Balance")
  print("2. Deposite Money")
  print("3. Withdraw money")
  print("4. Exit")
  try:
   choice=int(input("What you want to perform: "))
  except ValueError:
    print("Choice must be in number")
    break
  if choice==1:
    print("Your balance is",bal)
  elif choice==2:
    amt=int(input("Enter Deposite amount: "))
    if amt>0:
      bal=bal+amt
      print("Amount is succesfully Deposited")
    else:
        print("Enter a positve amt")
           
  elif choice==3:
    amt=int(input("Enter withdraw amount: "))
    if amt>0:
        if bal<amt:
           print("Insufficient balance")
        else:
            bal = bal-amt
            print("Amount is succesfully withdrawn")
    else:
        print("Enter a positve amt")
  elif choice==4:
    print("Thank You")
    break
  else:
    print("Invalid Choice")


print("Welcome to Divya's Bank")
details={}
while True:
  print("1.Sign in(if you have account already)")
  print("2.Sign up(if you don't have account)")
  n=int(input("Enter your choice:- "))
  if n==2:
   username=input("Enter your username: ")
   password=input("Enter your password: ")
   details[username]=password
   
  elif n==1:
    username=input("Enter your username:- ")
    if username in details:
      password=input("Enter password: ")
      if details[username]==password:
         print("Login successfull")
         operation()
         break
      else:
         print("Incorrect password")
         break
    else:
      print("Username doesn't found")
      break
