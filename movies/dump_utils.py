# import smtplib
# from email.message import EmailMessage
# from django.conf import settings

# def send_mail(subject, body, recipient_list):
#     try:
#         email_address = settings.EMAIL_HOST_USER
#         email_password = settings.EMAIL_HOST_PASSWORD

#         if email_address is None or email_password is None:
#             # no email address or password
#             # something is not configured properly
#             print("Did you set email address and password correctly?")
#             return False

#         # create email
#         msg = EmailMessage()
#         msg['Subject'] = subject
#         msg['From'] = email_address
#         msg['To'] = [recipient_list]
#         msg.set_content(body)

#         # send email
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#             smtp.login(email_address, email_password)
#             smtp.send_message(msg)
#             smtp.quit()
#         return True
#     except Exception as e:
#         print("Problem during send email")
#         print(str(e))
#     return False
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from django.conf import settings


# def send_mail(
#     subject,
#     body,
#     sender,
#     receivers,
#     server_address,
# ):
#     username = settings.EMAIL_HOST_USER
#     password = settings.EMAIL_HOST_PASSWORD
#     """Sends an email to the specified receivers using an Exchange server."""
#     message = MIMEMultipart()
#     message["From"] = sender
#     message["To"] = ",".join(receivers)
#     message["Subject"] = subject
#     message.attach(MIMEText(body))

#     server = smtplib.SMTP(server_address, 587)
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(sender, receivers, message.as_string())
#     server.quit()
