class Credentials:
    """
    Class that will generate new instances of credentials
    """

    user_credentials = []

    def __init__(self, user_name, password,platform) ->None:
        self.user_name = user_name
        self.password = password
        self.platform = platform

    def append_credentials(self):
        Credentials.user_credentials.append(self)
        
    @classmethod
    def generate_password(cls, length):
        characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
        return "".join(random.choice(characters)for i in range(length))

y = Credentials("Facebook", 'Betty', 000)
print(y)
z=y.generate_password(32)
print(z)
