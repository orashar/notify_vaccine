###########################################################
############  Create by ORASHAR on 08/05/2020  ############
###########################################################

import requests

# fetch data from url
def fetchData(PINCODE, DATE):

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={DATE}'

    res = requests.get(url, headers=headers)
    res_json = res.json()

    return res_json


# parsing json data
def parseData(res_json, constraints):
    
    available_centers = []
    count = 0

    AGE_LIMIT = constraints['AGE_LIMIT']
    centers = []
    
    try:
        centers = res_json['centers']
        for center in centers:
            sessions = center['sessions']
            for session in sessions:
                
                if AGE_LIMIT == -1:
                    count += 1
                    new_center = {}
                    new_center['name'] = center["name"]
                    new_center['min_age_limit'] = session["min_age_limit"]
                    new_center['date'] = session["date"]
                    new_center['available_capacity'] = session["available_capacity"]
                    available_centers.append(new_center)
                    # print(f'{count}- {center["name"]} with age limit {session["min_age_limit"]} on date {session["date"]} has {session["available_capacity"]} seats available')
                else:
                    if session['min_age_limit'] == AGE_LIMIT:
                        if session["available_capacity"] > 0:
                            count += 1
                            new_center = {}
                            new_center['name'] = center["name"]
                            new_center['min_age_limit'] = session["min_age_limit"]
                            new_center['date'] = session["date"]
                            new_center['available_capacity'] = session["available_capacity"]
                            available_centers.append(new_center)
                            # print(f'{count}- {center["name"]} with age limit {session["min_age_limit"]} on date {session["date"]} has {session["available_capacity"]} seats available')
    except Exception as e:
        print("No center data available", e)
    
    if count > 0:
        print(count, " center available in your area")
    return available_centers

