###########################################################
############  Create by ORASHAR on 08/05/2020  ############
###########################################################


import creds
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def formMessage(sender, receiver, PINCODE, centers_list):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Vaccine Centers Availability"
    msg['From'] = sender
    msg['To'] = receiver[0]

    text = f'Available centers for Pincode {PINCODE} are:'
    html = """\
            <html>
            <head></head>
            <body>
        """
    i = 0
    for center in centers_list:
        i += 1
        html += f"""\
                <b>{i}-</b> <h3>{center['name']}</h3><h4> ({center['date']})</h4>><br/>
                <p>Minimum Age : {center['min_age_limit']}<br/>Seats available - {center['available_capacity']}</p><br/><br/>
            """


    html += """\
                </body>
            </html>
            """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    return msg


def sendEmail(centers_list, to, PINCODE):
    sender = "omparashar15@gmail.com"
    receiver = [to]
    message = formMessage(sender, receiver, PINCODE, centers_list)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpObj.login(creds.sender_id, creds.sender_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("Email sent to ", to)
        smtpObj.quit()
    except Exception as e:
        print(f"error sending email.{e}")