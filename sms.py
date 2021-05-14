import os
from twilio.rest import Client
import sqlite3
from selenium import webdriver

conn = sqlite3.connect('database_users1.sqlite')
cursor = conn.execute("SELECT * FROM preference")
rows = cursor.fetchall()

for row in rows:
   stad = row[1]
   minprijs = row[2]
   maxprijs = row[3]
   telnr = row[4]
   database_woningen = row[5]

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = YOUR OWN SID
# auth_token = YOUR OWN AUTH TOKEN
client = Client(account_sid, auth_token)
for row in rows:

    CHROME_DRIVER_PATH = "C:\Develpment\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(f'https://www.pararius.nl/huurwoningen/{stad}/{minprijs}-{maxprijs}')
    get_number_of_woningen = driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[2]/div/div[1]/span')
    huidig_aantal_woningen = int(get_number_of_woningen.text)
    if huidig_aantal_woningen > database_woningen or huidig_aantal_woningen < database_woningen:
        message = client.messages.create(
                                      body=f'Nieuwe woning beschikbaar in {row[1]}! minimale prijs = {row[2]} en maximale prijs = {row[3]}',
                                      from_='+18329811862',
                                      to=telnr
                                  )
    # telnr moet dan op de plek van de to=
        database_woning =  cursor.fetchone(row[5])
        database_woning = huidig_aantal_woningen

        print(message.sid)