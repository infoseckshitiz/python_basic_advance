# def hint_username(username):
#     if len(username) > 3:
#         print("Invalid username it mus be less then 3 char")
#     else:
#         print("valid username")
# hint_username("alis")


# in this program user should input atlist 3 character and must be 15 char 
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username Must be at least 3 character long :)")
#     elif len(username) > 15:
#         print("Invalid username Must be at most 15 character long :)")
#     else:
#         print("Valid username")
        
# hint_username("ks")

# def cast_vote(age):
#     if age < 18:
#         print("You cant cast vote ")
#     else:
#         print("You can vote ")
# cast_vote(16)

def is_grater():
 a = int(input("Enter the value of a :)"))
 b = int(input("Enter the value of b :)"))
 c = int(input("Enter the value of c :)"))

 if a > b and a > c:
    print(f"A is grater with a value {a}")
 elif b > a and b > c:
    print(f"B is grater with a value of {b}")
 else:
    print(f"C is grater with a value of {c}")
    
is_grater()