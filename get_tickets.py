import time
import datetime
import smtplib
from selenium import webdriver
from playsound import playsound

incognito = webdriver.ChromeOptions().add_argument("--incognito")
driver = webdriver.Chrome("./chromedriver", options=incognito) # windows only

desired_dates = ['2019-11-04', '2019-11-05', '2019-11-06', '2019-10-31', '2019-11-19']

while True:
    driver.get("https://www.showclix.com/event/TheDailyShowwithTrevorNoah")
    try:
        dates = driver.execute_script("return dates_avail")
        for date in dates.keys():
            if date in desired_dates:
                print("Found date: ", date, " @ ", datetime.datetime.now())

                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login("", "")
                server.sendmail(
                    "",
                    "",
                    "Subject: Daily Show tickets available\n\nhttps://www.showclix.com/event/TheDailyShowWithTrevorNoah")
                server.quit()

                while True:
                    playsound('./alarm.mp3')

    except (ValueError, Exception):
        print("Something went wrong...")
        driver.close()
        driver = webdriver.Chrome("./chromedriver", options=incognito)

    time.sleep(30)

driver.close()
