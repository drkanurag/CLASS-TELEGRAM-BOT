import time
from datetime import datetime
import pytz
import calendar
import requests

 
# Monday
classes_0 = [
   {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nGCR Link : https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "NO CLASS!"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: MOOC\nFaculty : Rajiva Divivedi\nGCR Link : https://bit.ly/DataMiningAnalytics"}
]

# Tuesday
classes_1 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : GCR Link : https://bit.ly/NeuroFuzzy\n2. Information Storage (Faculty - Medhavi Malik) : GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Indian Traditional Knowledge\nFaculty : Shalini Sharma\nGCR Link : https://bit.ly/ValueGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Competitive Professional Skills - II\nFaculty : Chandra Shekher Tyagi\nGCR Link : https://bit.ly/CPSGCR"},

    ]

# Wednesday
classes_2 = [   

    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nGCR Link = https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Ardunio\nFaculty : Manoj K Vishnoi\nGCR Link : https://bit.ly/ESDAGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Quantative Aptitude\nFaculty : Avinash Singh\nGCR Link : https://bit.ly/QuantsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Arduino Lab\nFaculty : Prashant Mani\nGCR Link : https://bit.ly/ESDAGCR"},
    
    ]

# Thursday
classes_3 = [
    
    {"time_hour" : "9", "time_min": "10" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : GCR Link : https://bit.ly/NeuroFuzzy\n2. Information Storage (Faculty - Medhavi Malik) : GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Ardunio\nFaculty : Manoj K Vishnoi\nGCR Link : https://bit.ly/ESDAGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Quantative Aptitude\nFaculty : Avinash Singh\nGCR Link : https://bit.ly/QuantsGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks Lab\nFaculty : Shiva Soni\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    
    ]

# Friday
classes_4 = [   
    
    {"time_hour" : "9", "time_min": "10" , "message" : "Class: Data Mining and Analytics\nFaculty : Rajiva Divivedi\nGCR Link = https://bit.ly/DataMiningAnalytics"},
    {"time_hour" : "10", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "11", "time_min": "10" , "message" : "Class: Mathematics\nFaculty : Shikha Bansal\nGCR Link : https://bit.ly/MathematicsGCR"},
    {"time_hour" : "12", "time_min": "10" , "message" : "Class: Formal Language and Automata\nFaculty : Abhishek Singh\nGCR Link : https://bit.ly/AutomataGCR"},
    {"time_hour" : "13", "time_min": "50" , "message" : "1. Neuro Fuzzy (Faculty - Nidhi Pandey) : GCR Link : https://bit.ly/NeuroFuzzy\n2. Information Storage (Faculty - Medhavi Malik) : GCR Link : https://bit.ly/InformationGCR"},
    {"time_hour" : "14", "time_min": "40" , "message" : "Class: Computer Networks\nFaculty : Shiva Soni\nGCR Link : https://bit.ly/ComputerNetworksGCR"},
    
   ]


# print(classes_0)

# print(time.localtime())

# print(time.localtime().tm_wday)

# print(classes_0[0]["time_hour"])


def sendMessage(msg):
    base_url = 'https://api.telegram.org/bot1974804373:AAHNUJZPvh639GHjP1u0aOBl6rgY_iPVuo0/sendMessage?chat_id=-1001259483889&text="{}"'.format(
        msg)
    requests.get(base_url)


def checker():
  
    tz_IN = pytz.timezone('Asia/Kolkata')
    datetimeIN = datetime.now(tz_IN)


    week_day = calendar.weekday(
        datetimeIN.year, datetimeIN.month, datetimeIN.day)
    time_hour = datetimeIN.time().hour
    time_min = datetimeIN.time().minute

    print("checker is running", calendar.weekday(datetimeIN.year, datetimeIN.month,
          datetimeIN.day), datetimeIN.time().hour, datetimeIN.time().minute)
    # print(time_hour,time_min,week_day)

    if time_hour == 9 and time_min == 9 :
        print("class 1 Time")
        if (week_day == 0):
            sendMessage(classes_0[0]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[0]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[0]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[0]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[0]["message"])

    if (time_hour == 10 and time_min == 9):
        print("class 2 Time")

        if (week_day == 0):
            sendMessage(classes_0[1]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[1]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[1]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[1]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[1]["message"])

    if (time_hour == 11 and time_min == 9):
        print("class 3 Time")

        if (week_day == 0):
            sendMessage(classes_0[2]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[2]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[2]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[2]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[2]["message"])

    if (time_hour == 12 and time_min == 9):
        print("class 4 Time")

        if (week_day == 0):
            sendMessage(classes_0[3]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[3]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[3]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[3]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[3]["message"])

    if (time_hour == 13 and time_min == 49):
        print("class 5 Time")

        if (week_day == 0):
            sendMessage(classes_0[4]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[4]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[4]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[4]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[4]["message"])

    if (time_hour == 14 and time_min == 39):
        print("class 6 Time")

        if (week_day == 0):
            sendMessage(classes_0[5]["message"])
        elif (week_day == 1):
            sendMessage(classes_1[5]["message"])
        elif (week_day == 2):
            sendMessage(classes_2[5]["message"])
        elif (week_day == 3):
            sendMessage(classes_3[5]["message"])
        elif (week_day == 4):
            sendMessage(classes_4[5]["message"])


sendMessage("I'm ON ! Your Friendly Neighbourhood Class Reminder😁")
print(classes_0)


while True:
   
    checker()
    time.sleep(60)
