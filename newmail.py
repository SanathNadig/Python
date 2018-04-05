'''
code to send email anonymously to a recipient
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

from_addr = "SanathManjunath.Nadig@in.bosch.com"
subject = 'Important notification to all users'
 
def mailer(to_addr,msg_body):
    '''
    function to send a mail to the recipients
    arg1: list of all recipients as a list
    arg2: message text to be communicated to all recipients as a string
    '''
    if not isinstance(to_addr, list) or not isinstance(msg_body, str):
        raise TypeError('Please provide the first argument as a list and the second argument as a string.')
    
    message = MIMEMultipart()
    message['From'] = from_addr
    message['To'] = ','.join(to_addr)
    message['Subject'] = subject
    email_body = 'This is an auto-generated email. Please do not reply.\n\n' + msg_body + \
                 '\n\n-------end of message-------'
    
    message.attach(MIMEText(email_body,'plain'))
    text = message.as_string()
    
    #we use the Bosch server to communicate the mails
    server_name = 'rb-smtp-int.bosch.com:25'
    server = smtplib.SMTP(server_name)
    server.starttls()
    server.ehlo()
    server.sendmail(from_addr, to_addr, text)
    server.quit()
    print ('Email sent')


if __name__ == "__main__":
    mailer(["AbhijitKedari.Patil@in.bosch.com"],'' )
    