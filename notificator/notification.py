import email
import smtplib

def notificator(subject,text,where_to_mail):
    s = smtplib.SMTP_SSL('smtp.mail.ru',465)
    print("starting")

    email = 'notificator.cve@bk.ru'
    passwd = "pass"

    print("logging in")
    s.login(f"{email}", f"{passwd}")

    msg = 'Subject: {}\n\n{}'.format(subject,text)

    print("sending mail")
    s.sendmail(f"{email}", where_to_mail, msg)
    print("sent")
    s.quit()

if __name__ == "__main__":
    notificator("New CVE.","Hello dear user. New CVE is now available. Please undertake necessary remediation regarding your product!","amitullayev@gmail.com")