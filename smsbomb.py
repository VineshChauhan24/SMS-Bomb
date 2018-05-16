# This program was written by Robert Hartman 2018.  Do not use for illegal or malicious purposes.
# The program was written for joke purposes only.

# DIRECTIONS:
# 1. You will need to create a gmail account to use this program.
# 2. Below you will see the username and password variables.  You will need to enter the @gmail under username and the password under password.
# 3. Launch the program in terminal and follow the prompts to send texts. (Mac Example: "python smsbomb.py")
# 4. Don't be mean with it.

import smtplib as s
import getpass
import sys

username = str("textbomb27@gmail.com") #Enter the gmail account here.
password = str("bomb12345") #Enter the password here.
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)
option = raw_input("\n\nWhich carrier does the person have?\n \n 1. Verizon \n 2. AT&T \n 3. Sprint \n 4. Hail mary! (it will try every carrier) \n\nEnter a number: ")
carrier = int(option)

carrier_attack1 = "@vtext.com" #Verizon
carrier_attack2 = "@txt.att.net" #AT&T
carrier_attack3 = "@messaging.sprintpcs.com" #Sprint

v_phone = raw_input("Enter their phone number (must be ten digits. ex. 1987654212): ")

if carrier == 1:
    v_phone1 = v_phone + str(carrier_attack1)
if carrier == 2:
    v_phone1 = v_phone + str(carrier_attack2)
if carrier == 3:
    v_phone1 = v_phone + str(carrier_attack3)
if carrier == 4:
    v_phone2 = v_phone + str(carrier_attack1)
    v_phone3 = v_phone + str(carrier_attack2)
    v_phone4 = v_phone + str(carrier_attack3)

message = raw_input("Enter the message here: ")
number = raw_input("How many times do you want to send the message?: ")

if carrier == 1:
    wait_message = str("\nYour message is being sent. \nPlease wait a few seconds/minutes depending on how many messages you sent. \nThank you for your patience!\n")
    print wait_message
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone1), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone1, phone_message)
    final_message = str("Your message has been sent ") + str(number) + str(" times!\n")
    print final_message
if carrier == 2:
    wait_message = str("\nYour message is being sent. \nPlease wait a few seconds/minutes depending on how many messages you sent. \nThank you for your patience!\n")
    print wait_message
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone1), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone1, phone_message)
    final_message = str("Your message has been sent ") + str(number) + str(" times!\n")
    print final_message
if carrier == 3:
    wait_message = str("\nYour message is being sent. \nPlease wait a few seconds/minutes depending on how many messages you sent. \nThank you for your patience!\n")
    print wait_message
    phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone1), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone1, phone_message)
    final_message = str("Your message has been sent ") + str(number) + str(" times!\n")
    print final_message
if carrier == 4:
    warning_message = str("\nBecuase you are sending a hail mary, this process will take a lot longer than normal. \nThe message has to be sent to each carrier address. \nA message will appear when every message has been sent. \nThank you for your patience!\n\n")
    print warning_message
    phone_message2 = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone2), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone2, phone_message2)
    phone_message3 = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone3), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone3, phone_message3)
    phone_message4 = ("From: %s\r\nTo: %s \r\n\r\n %s" % (username, "" .join(v_phone4), "" .join(message)))
    for option in range (0, int(number)):
        obj.sendmail(username, v_phone4, phone_message4)
    hail_mary_count = int(3) * int(number)
    final_message = str("Your message has been sent ") + str(number) + str(" times! ") + str("(Technically, it was sent ") + str(hail_mary_count) + str(" times!)\n")
    print final_message

        



