import requests
import json
import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from prettytable import PrettyTable
from email.mime.text import MIMEText
class location:

    # Constructor
    def __init__(self):
        self.location = "N/A"
        self.url = "N/A"
        self.day = "N/A"

    def __init__(self, location, url, day):
        self.location = str(location)
        self.url = str(url)
        self.day = day


    # accessors (one line to save space)
    def getLocation(self): return self.location

    def getUrl(self):
        return self.url

    def getDay(self): return self.day

    # mutators
    def setLocation(self, newLocation): self.location = newLocation

    def setUrl(self):
        self.url = url + date

    def setDay(self, newDay):
        self.day = newDay

    # other methods
    # def display(self):
    #     print("%20s" % self.date)
    #     print("%20s" % self.month)
    #     print("%20s" % self.day)
    #     print("%20d" % self.year)

    def getJson(self, url):
        init_response = requests.get(url)
        json_data = json.loads(init_response.text)
        return json_data
