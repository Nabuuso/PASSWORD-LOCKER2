import user
from user import user

def main():
    
    while True:
        print("welcome to password locker!!!")
        print('\n')
        print("select a short code to navigate through: to create new user use 'nu': To login to your account 'lg' to exit")
        short_code = input().lower()
        print('\n')
    
        if short_code == 'nu':
            print('create username')
            created_user_name = input()
            
            print('create password')
            created_user_password =input()
            
            print('confirm password')
            confirm_password =input
    
            while confirm_password!= created_user_password:
                print("invalid password did not match!!")
                print("enter your password")
                created_user_password =input()
                print("confirm paswword")
                confirm_password =input()
                
            else:
                print(f"congratulations {created_user_name}! account creation successful")
                print('\n')
                print("proceed to login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()
                
            while entered_username!= created_user_name or entered_password!= created_user_password:
                print("invalid username or password")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()
        
            else:
                print(f"welcome: {entered_username} to your account")
                print('\n')
    
        elif short_code == 'lg': 
            print("welcome")
            print("Enter user name")
            default_user_name =input()
            print("Enter password")
            default_user_password =input()
            print('\n')
    
            while default_user_name!= 'testuser' or default_user_password!= '12345':
                print("wrong userName or password.username 'testuser' and pasword '12345'")
                print("Enter user name")
                default_user_name =input()
                print("Enter password")
                default_user_password =input()
                print('\n')
        
            else:
                print("login success")
                print('\n')
                print('\n')
        
        elif short_code =="ex":
            break

        else:
            print("Enter valid code to continue")
    
if __name__ == '_main_':
    main()
