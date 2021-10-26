class Credentials:
    """
    Class that will generate new instances of credentials
    """

    credentials_detail = []

    def __init__(self, user_name, password,platform) ->None:
        self.user_name = user_name
        self.password = password
        self.platform = platform

    def append_credentials(self):
        Credentials.user_credentials.append(self)
        
