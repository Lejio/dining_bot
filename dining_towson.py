
import requests
import json
import os
import smtplib
from datetime import date

truegrit_user = os.environ.get("TRUEGRIT_USER")
truegrit_pass = os.environ.get("TRUEGRIT_PASS")

customer_list = ["il27770@umbc.edu"]

print(truegrit_user)
print(truegrit_pass)

with smtplib.SMTP("smtp.gmail.com", 587) as stmp:
    stmp.ehlo()
    stmp.starttls()
    stmp.ehlo()

    stmp.login(truegrit_user, truegrit_pass)

    # truegrits_location_id = '61f9d7c8a9f13a15d7c1a25e'
    truegrits_location_id = '5f2c385b0101560b7defd033'

    date = str(date.today())
    url = 'https://api.dineoncampus.com/v1/location/'+truegrits_location_id + '/periods/?platform=0&date='+date
    init_response = requests.get(url)
    json_data = json.loads(init_response.text)

    meal_periods_dict = {}
    body_msg = ""
    data_period = json_data['periods']
    for period in data_period:
        meal_periods_dict[period["name"]] = period["id"]

    for period in meal_periods_dict.keys():
        print("\n################################\n")
        body_msg += "\n################################\n\n"
        url = 'https://api.dineoncampus.com/v1/location/'+truegrits_location_id+'/periods/'+meal_periods_dict[period]+'?platform=0&date='+date
        period_response = requests.get(url)
        json_data = json.loads(period_response.text)


        data = json_data['menu']['periods']

        print("Meal Period:", data['name'],'\n')
        body_msg += "Meal Period:" + data['name'] + '\n\n'

        for category in data['categories']:
            print(category['name'])
            body_msg += category["name"] + "\n"
            for item in category['items']:
                print("\t", item['name'])
                body_msg += "\t" + item["name"] + "\n"

    subject = "Today's Menu: " + date


    msg = f"Subject: {subject} \n\n {body_msg}"

    stmp.sendmail(truegrit_user, customer_list[0], msg)

    # for i in range(len(customer_list)): #property of theo lostoski
    #     stmp.sendmail(truegrit_user, customer_list[i], msg)


