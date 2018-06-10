import random
def all():
    print("Already have an account?(y/n)")
    answer = input().lower()
    if answer == 'n':
        print("Enter your Name:")
        username = input()
        print("\n")
        print("Enter A password")
        password = input()
        print("\n")
        print("Enter your email")
        email = input()
        print("\n")


        handle = open("credentials.txt","a")

        handle.write(username)
        handle.write(" ")
        handle.write(password)
        handle.write(" ")
        handle.write(email)
        handle.write("\n")


        handle.close()
        print("Account created succesfully\n Would you like to do more with Password Locker!(y/n)")
        response = input().lower()
        if response == 'y':
            generate_account()

        else:
            print("be sure to come back if you'd like to save a password, have a good day!")

    elif answer == 'y':
        login()



def generate_account():
    print("Which account would you like to save a password for?")
    account_to_be_saved = input()
    print("Enter 'auto'- for an auto-generated password or 'type'- to type in your own password")
    choice = input()
    if choice == 'auto':
        reversed_account_name = account_to_be_saved[::-1]
        r = str(random.randint(0,50))
        password = reversed_account_name + r
        print(f"your new password is {password}")
        handle = open("credentials.txt","a")

        handle.write(account_to_be_saved)
        handle.write(" ")
        handle.write(password)
        handle.write(" ")



        handle.close()
    else:
        print("type in your password")
        password = input()




def login():
    print("Enter your username")
    username = input()
    print("\n")
    print("Enter your password")
    password = input()
    print("\n")
    print("Enter your email")
    email = input()
    for line in open("credentials.txt", "r").readlines():
            myVar = line.split()
            if username == myVar[0] and password == myVar[1]:
                print("login succesfull")

                return True
            else:
                print("Forgot password ?(y/n)")
                response = input().lower()
                if response == 'y':
                    print("Enter your username")
                    username = input()
                    for line in open("credentials.txt", "r").readlines():
                        my_file = line.split()

                        to_be_printed = my_file[1]
                        username1 = my_file[0]
                        if username == username1:
                            print(f"your password is {to_be_printed}")
                        else:
                            # print("that username doesn't exist")
                            login()
                            # return False
                else:
                    print("try again then")

                # return False

class User:

    """
    Class that generates new instances of Users
    """
    User_list = []

    def __init__(self,username,password,email):

      # """
      # init method that defines properties for our objects
      # """

        self.username = username
        self.password = password
        self.email = email









    # def add_user(self):
    #     print("Hello There, welcome to Password Locker.")
    #     print("\n")
    #     print("Use the following shortcodes: ca - to create a account, lg - to login")
    #     shortcodes = input().lower()
    #
    #     if shortcodes == 'ca':
    #
    #
    #
    #     elif shortcodes == 'lg':
    #         login()
    #
    #
    #         user = User()


    all()
