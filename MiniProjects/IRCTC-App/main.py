# class
# constructor
# train_schedule
# 


import requests

class IRCTC:

    def __init__(self):


        user_input = input(""" how would you to proceed?
        !. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule""")

        if user_input == "1":
            print("live train status")
        elif user_input =="2":
            print("PNR")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("enter the train number:")
        self.fetch_data(train_no)

    def fetch_data(self,train_no):
        api_key = "30c382602bfa67c8a7c580e6cfe2bech"
        url = f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/{api_key}/TrainNumber/{train_number}/"
        data = requests.get("url")  

        data = data.json()
        print(data['Route'])

        for i in data['Route']:
            print(i['StationCode'])  