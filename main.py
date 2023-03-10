print "Hello, welcome to account creator."
username = raw_input("\nWhat would you like your account name to be:")
print "\nCongrats! Your username is now %s." % (username)
username = username.lower()
#Has user input a username and stores it in the variable username.
password = raw_input("\nWhat would you like your password to be?")
if not len(password) >= 8:
  while len(password) < 8:
    password = raw_input("\nYour password was not long enough. Please enter a new password:")
print """\nCongrats! Your password is now %s.""" % (password)
#Has user input a password and stores it in the variable password. The program also ensures the password is at least 8 charachters.
storage = {username : password}
#Creats a dictionary with the username as the key and the password as the value.
print "\nNow that your account has been created, let's have you log into it." 
def login():
  username_login = raw_input("\nUsername:")
  if not username_login.lower() in storage:
    while not username_login in storage:
      username_login = raw_input("\nWe could not find %s in our database. Try again:" % (username_login))
#Has the user login using their username, and will have them try again if they login with a different username then they previously enetered. 
  password_login = raw_input("\nPassword:")
  correct_password_login = storage[username]
  password_attempts = 3
  if not password_login == correct_password_login:
    while not password_login == correct_password_login and password_attempts > 0 :
      password_login = raw_input("\nPassword is incorrect. You have %s tries remaining. Password:" % (password_attempts))
      password_attempts = password_attempts - 1
#Has the user login with their password. They are given 4 tries to login. 
  if not password_login == correct_password_login:
    print("\nYou have been removed from the system due to incorrect password entries.")
    quit()
#If the password is not correct after the given 4 tries then the program is ended.
  print "\nGreat! You have been logged in!"
login()
def options():
  choices = raw_input("What would you like to do? \n1. Record Entry \n2. Log Out \nUse 1 or 2 to select your option!\n")
  if choices == "1":
   entry = raw_input("\nWhat do you want to add to your journal?")
   entry_number = 1
   entry = "\nEntry Number" + str(entry_number) + ":" + "\n" + entry
   journal = entry
   print journal
options()
