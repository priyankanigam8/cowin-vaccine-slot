"""
this program demonstrate the use case of COWIN API (available in public domain), to view the availability of vaccine type,minimum
eligible age,available slot for a particular date and pincode.

check for COVID availabilty near you using python | covid vaccine registeration India | Python API
"""
import requests
# PINCODE = "110096"
PINCODE = "0"
while len(PINCODE) != 6:
    PINCODE = input("Enter the pincode for which you waant the status => ")
    if len(PINCODE) <6:
        print(f"{PINCODE} is shorter than its actual length")
    elif len(PINCODE) > 6:
        print(f"{PINCODE} is longer than the actual length")

# required date is user input taken by the user.
# ----------------------------------------------------------------------------------------------------------------------------------------
REQ_DATE = input("Enter the date to get status (Date format : DD-MM-YYYY) => ")
#write it inside the sting otherwise it will again give an error.
# REQ_DATE = "23-06-2021"
request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"
header = {'User-Agent' :'Chrome/91.0.4472.114 Safari/537.36'}

# we are making a request by using a get keyword from the request library

response = requests.get(request_link, headers = header)
# this is a json response
# it return the json object of a result.
raw_JSON = response.json()
#print(raw_JSON)
#we are iterating through each centers to see which centers are available
# for i in range(len(raw_JSON['centers'])):
#     print(raw_JSON['centers'][0]["name"])       #this is how we can access the particular element

Total_centers = len(raw_JSON['centers'])
print()
print("                  *>>>>>>>>>    Results     <<<<<<<<*                ")
print("-----------------------------------------------------------------------")
print(f"Date : {REQ_DATE} | Pincode : {PINCODE}")


if Total_centers != 0:
    print(f"Total centers in your area is : (Total_centers)")
else:
    print(f"Unfortunately !! Seems like no centre in this area / Kindly recheck the pincode")

print("-------------------------------------------------------------------------------------------")
print()

#calculated the length of the centers passing through a range

for cent in range(Total_centers):
    print()
    print(f"[{cent+1}] Center Name:", raw_JSON['centers'][cent]['name'])
    fee_val = raw_JSON['centers'][cent]['fee_type']
    print("-----------------------------------------------------------------------")
    print("Date      Vaccine Type      Vaccine Fee      Minimum Age       Available slot")
    print("-----------------------------------------------------------------------------")
    this_session = raw_JSON['centers'][cent]['sessions']


    for _sess in range(len(this_session)):
        print( "{0:^12} {1:^12} {2:^13} {3:^14} {4:^16} " .format(this_session [_sess]['date'],this_session[_sess]['vaccine'],fee_val,this_session[_sess]
        ['min_age_limit'], this_session[_sess]['available_capacity']))


