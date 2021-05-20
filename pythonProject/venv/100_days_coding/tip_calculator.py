bill_amount = float(input("Enter the bill amount :"))
percentage = int(input("Enter tip percenteage (10,12,15)%"))
num_of_persons = int(input("Number of person sharing the bill :"))
tip = ((bill_amount * percentage)/100)/num_of_persons
amount_each_person = (bill_amount / num_of_persons)+tip
roumded_bill = ("{:.2f}".format(amount_each_person))
print(f"Amount from each person {roumded_bill}")


