D={'Manju':'Loo','nathan':'kuku','renu':'juu'}
condition =True
while(condition):
    user_name=input("Enter your name:")
    if user_name in D.keys():
        print("Your username is valid")
    else:
        print("Your username is invalid")
    pwd=input("Enter your password:")
    if D.get(user_name)==pwd:
        print("Your password is valid")
    else:
        print("Your password is invalid")    
        
    print("If you want to sign in again: YES/NO")
    Input=input()
    if(Input =="YES"):
        condition=True
    else:
        condition=False
