class useraccount:
    """
    Class that generates new instances of users.
    """
    account_list = [] #empty account list
    
    def __init__(self,account_name,user_name,password,email):
         self.account_name = account_name
         self.user_name = user_name
         self.password = password
         self.email = email
    def save_account(self): 
        
        '''
        save_account method saves account objects into account_list
        '''
        useraccount.useraccount_list.append(self)
    def delete_account(self):
            '''
            delete_account method deletes a saved account from the account_list
            '''
            
            useraccount.useraccount_list.remove(self)    
    @classmethod
    def find_by_name(cls,name):
        for useraccount in cls.account_list:
            if useraccount.account_name == name:
                return useraccount 
    
    @classmethod
    def account_exist(cls,name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.password == name:
                    return account

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list    
   

         