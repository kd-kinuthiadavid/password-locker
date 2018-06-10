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
