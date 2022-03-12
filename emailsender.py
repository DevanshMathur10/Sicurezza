import smtplib
import os
from email.message import EmailMessage
import pandas as pd
from maps import coords

filename="data.csv"
df = pd.read_csv(filename)

EMAIL_ADDRESS=os.environ.get('PYMAIL')
EMAIL_PASSWORD=os.environ.get('PYPASS')

def sendpass(nameget):
    contacts=[]
    if nameget in df["name"].values:
        correct_pin = df[df["name"] == nameget]["ec1"].values[0]
        correct_pin1 = df[df["name"] == nameget]["ec2"].values[0]
        contacts.append(correct_pin)
        contacts.append(correct_pin1)
    body='HELP!'
    message=EmailMessage()
    message['Subject']="EMERGENCY"
    message['From']=EMAIL_ADDRESS
    message['To']=contacts
    message.set_content(body)
    message.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">HELP!!</h1>
            <h2 style="color:Red;">"""+str(coords[0])+" , "+str(coords[1])+'\n'+"""</h2>
        </body>
    </html>
    """,subtype='html')

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)

