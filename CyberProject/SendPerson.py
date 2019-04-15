import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#PLEASE INSERT YOUR OWN EMAIL INFO HERE 
def Send(Person):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"
    receiver_email = "receiver.edu"
    password = "PASSWORD"
    #ENTER INFO ABOVE
    attachment = 'tempPic.jpg'
    #message_text = "test"
    context = ssl.create_default_context()
    msg= MIMEMultipart('related')
    msg['Subject'] = Person.Name
    msg['From'] = sender_email
    msg['To'] = receiver_email
    body = Person.EmailContent()
    msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (body, attachment), 'html')  
    msg.attach(msgText)   # Added, and edited the previous line

    fp = open(attachment, 'rb')                                                    
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))
    msg.attach(img)

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    
