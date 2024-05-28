def hint_username(username):
    if len(username) > 3:
        print("the input hint is valid which is less then 3")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 char long")
        else:
            print("valid username ")
            
hint_username("alish")
    