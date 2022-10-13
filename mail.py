# send cipher code to your friends via email

import smtplib


def send_mail(receiver, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('avihanarya111@gmail.com', 'ffrsdndlhqfztncy')
    server.sendmail('avihanarya111@gmail.com', receiver, message)
    print('mail sent!\n\n')
