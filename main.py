from twilio.rest import Client
import csv
from datetime import date

account_sid = "AC972791418f909d0dfb8e6d3939fb83d0"
auth_token = "833b7bdc3e4e5fb707b183033a04deef"
client = Client(account_sid, auth_token)

STARTING_DATE = date(2020, 5, 11)

def send_love(event, context):
    print("Sending love...")
    with open("frases.csv") as csvfile:
        phrases = []
        readCSV = csv.reader(csvfile, delimiter=",")
        for row in readCSV:
          phrases.append(row)
        today = date.today()
        delta = today - STARTING_DATE
        number_of_phrases = len(phrases)
        phrases_left = number_of_phrases - delta.days
        chosen_phrase = phrases[delta.days]
        if phrases_left <= 5:
            alert_message = f"Faltan {phrases_left} día(s) para renovar disney-bot de Viri."
            client.messages.create(
                to="+522491637747", from_="+13237161581", body=alert_message
            )
        formatted_phrase = f"Con amor, de Gabo\n\n{chosen_phrase[0]} - {chosen_phrase[1]}"
        client.messages.create(
            to="+525514990083", from_="+13237161581", body=formatted_phrase
        )
    print("Love sent!")
