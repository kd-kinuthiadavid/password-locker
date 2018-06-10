
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
        print("Account created")
    elif answer == 'y':
        login()

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
                print("Forgot username or password ?")

                return False

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
