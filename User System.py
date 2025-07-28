users={}
print("---------USER SYSTEM---------")
print("1-  create account  \n 2- log in \n 3- exit")
number=int(input("Enter a number: "))
while number != 3:

  if number not in [1 , 2 , 3]:
    print("Invalid number")
  
  elif number == 1:
    username=input("username: ")
    if username in users:
      print("username already exists")
    else:
      password=input("password: ")
      repas=input("rewrite the password: ")
      if password != repas:
                print("Passwords do not match.")
      elif len(repas) < 8 :
        print("Password must be at least 8 characters long.")
      else:
        has_digit = any(char.isdigit() for char in password)
        has_letter = any(char.isalpha() for char in password)
        if not (has_digit and has_letter):
            print("Password must contain at least one letter and one digit.")
        else:
            users[username]=password
            print("Account created successfully")
  elif number == 2:
    username=input("username: ")
    password=input("password: ")
    if username in users and users[username]== password:
      print("Login successful")
      
      
      n= int(input("1-view account information\n2-change password\n3-Sign out\n"))
      while n != 3:
        if n == 1:
          print("username is:",username)
          print("password is:",users[username])
        
        elif n == 2:
          pass2= input("Enter your new password: ")
          if len(pass2) < 8 :
            print("Password must be at least 8 characters long.")
          else:
            has_digit = any(char.isdigit() for char in pass2)
            has_letter = any(char.isalpha() for char in pass2)
            
            if not (has_digit and has_letter):
              print("Password must contain at least one letter and one digit.")
            else:
              users[username]=pass2
              print("Password changed successfully")
        else:
          print("invalid number")
        n= int(input("1-view account information\n2-change password\n3-Sign out\n"))


      print("Logged out successfully")
      
    else:
      print("Invalid username or password")

  try:
    number=int(input("Enter a number: "))
  except ValueError:
      print("Invalid input. Please enter a number.")
print("Exiting the system")