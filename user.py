from typing import List


class user:
    """
    Class that generates new instances of users.
    """
    user_list = [] #empty account list
    def __init__ (self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def append_user(self):
        """
        method to save user in the list
        """
        user.user_list.append(self)
    
    @classmethod
    def display_data(cls):
        """
        display objects in the list
        """
        return user.user_list
            
    @classmethod
    def getsingleinstance(cls):
        list = cls.user_list
        for i in list:
            print(i.__dict___)
        

# x = user('Betty', "!@#$")
# x.append_user()
# print(x.user_name)
# print(x.user_list)
# y=x.display_data()
# print(y)
# x.getsingleinstance()