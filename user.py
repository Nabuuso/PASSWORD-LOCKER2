class user:
    """
    Class that generates new instances of users.
    """
    user_list = [] #empty account list
    def _init_ (self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
        user.user_list.append(self)
        
    
   

  