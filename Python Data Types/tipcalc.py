print("Welcome to tip calculator!!!!!")
total = float(input("What was the total bill amount ? $ "))
tip = float(input("What percent tip would you like to give? ex.10?"))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip = total * tip_percent
total_bill = total + total_tip

total_per_person = total_bill / people

final_total_pp = round(total_per_person,2)

print(f"Each person should pay ${total_per_person} ")






# create a restaurant tip calculator
# ask for the total bill amount
# ask for the tip percentage
# ask for the number of the people the bill will be split between
# print("Welcome to restaurant tip calculator :")
# total_amt = int(input("Enter the total bill amount :"))
# tip_per = int(input("Enter the tip percentage :"))
# total_bill_people = int(input("Enter the total bill payer person :"))
# tip_per = total_amt * 100 / total_bill_people
# tip_per = total_amt * tip_per
# total_bill = total_amt + tip_per
# total_bill_people = total_amt / total_bill_people
# total_bill_people = round(total_bill_people,2)
# print(f"Each person should pay {total_bill_people} ")

