###########################################################
############  Create by ORASHAR on 08/05/2020  ############
###########################################################


import sys
from datetime import date
import time
import emailService
import validator
import request_handler



# setting up params
PINCODE = -1#input("enter pincode: ")

DATE = date.today()
DATE = DATE.strftime("%d-%m-%Y")

AGE_LIMIT = -1

EMAIL = ""

DELAY = 60

def inputs():

    invalid_count = 0

    pincode = input("Enter Pincode: ")
    while not validator.validate_pincode(pincode):
        invalid_count += 1
        print("invalid pincode")
        pincode = input("Enter Pincode: ")
        if(invalid_count > 10): sys.exit("Too many invalid inputs")
    global PINCODE
    PINCODE = pincode
    
    age_limit = int(input("Age limit ( 18 / 45 )"))
    while not validator.validate_agelimit:
        invalid_count += 1
        print("invalid Age limit")
        age_limit = (input("Age limit ( 18 / 45 )"))
        if(invalid_count > 10): sys.exit("Too many invalid inputs")
    global AGE_LIMIT
    AGE_LIMIT = age_limit

    email = input("Email to get notified: ")
    while not validator.validate_email(email):
        invalid_count += 1
        print("invalid Email")
        email = input("Email to get notified: ")
        if(invalid_count > 10): sys.exit("Too many invalid inputs")
    global EMAIL
    EMAIL = email


def main():

    if PINCODE == -1:
        inputs()

    # constraints
    constraints = {
        "AGE_LIMIT": AGE_LIMIT,
    }

    available_centers = {}

    res_json = request_handler.fetchData(PINCODE, DATE)
    if not res_json:
        print("Could not perform the search.")

    else:
        available_centers = request_handler.parseData(res_json, constraints)
        # If no centers available   
        if len(available_centers) == 0:
            print(f"No centers available for selected Age group")
        else:
            emailService.sendEmail(available_centers, EMAIL, PINCODE)
    

    print("Attempt done")


def timer(sec):
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"Next attempt after {remaining} seconds") 
        sys.stdout.flush()
        time.sleep(1)


if __name__ == "__main__":
    print("This program check vaccine availability every 60 seconds and notifies you via email")
    attempt = 0
    starttime=time.time()
    while True:
        attempt += 1
        sys.stdout.write(f"\rAttempt no: {attempt}\n")
        sys.stdout.flush()
        main()
        timer(DELAY)