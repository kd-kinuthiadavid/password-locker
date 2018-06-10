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


    # def login():
    #     print("Enter your username")
    #     username = input()
    #     print("\n")
    #     print("Enter your password")
    #     password = input()
    #     print("\n")
    #     print("Enter your email")
    #     email = input()

    def add_user():
        print("Hello There, welcome to Password Locker.")
        print("\n")
        print("Use the following shortcodes: ca - to create a account, lg - to login")
        shortcodes = input().lower()
        if shortcodes == 'ca':
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
            handle.write("\n")
            handle.write(email)
            handle.write("\n")


            handle.close()



        elif shortcodes == 'lg':
            print("create a login function")

    add_user()
