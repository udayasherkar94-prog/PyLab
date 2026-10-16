# lucy_number
# it is combination of user names first and last char ASCII value
# divide by the month of birth date
# luck number in range (0-9)


from datetime import datetime


name = input("enter your name:")
b_date = input("enter your birth date (dd-mm-yy):")

date_obj = datetime.strptime(b_date,"%d-%m-%Y")

month = date_obj.month
month_name = date_obj.strftime("%B") 
print(month)
# print(month_name)

num_str= str(int((ord(name[0])+ord(name[-1])/month)))
print("your luck Number :",num_str[0])

