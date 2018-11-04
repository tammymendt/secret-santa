import configparser
import copy
import random
from collections import namedtuple
from email.mime.text import MIMEText
import smtplib

Participant = namedtuple('Participant', ['name', 'email'])


def create_secret_santa(participant_list):

    secret_santa = {}
    random.shuffle(participant_list)

    for i, participant in enumerate(participant_list):
        secret_santa[participant.name] = participant_list[(i+1)%len(participant_list)]

    return secret_santa

def create_secret_santa_email(secret_santa, gift_reciever_name):

    message = '''
    Hola {secret_santa}! Bienvenido al amigo secreto de la Navidad 2018 :)\n

    Haremos un pequeño intercambio de regalo el 24.12.2018. El regalo puede ser algo
    hecho a mano o comprado con un valor entre 20 y 30 euros.\n

    Tu amigo secreto es: {gift_reciever_name}
    '''.format(secret_santa=secret_santa.name.capitalize(),
               gift_reciever_name=gift_reciever_name.capitalize())

    msg = MIMEText(message)

    msg['Subject'] = 'Navidad 2018: Amigo Secreto (VERSION FINAL)'
    msg['To'] = secret_santa.email
    msg = msg.as_string()

    return msg


def send_email(username, password, recipient_email, message):

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(username, password)
    session.sendmail(username, recipient_email, message)
    session.quit()


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('config.ini')

    gmail_username = config['Gmail']['user']
    gmail_password = config['Gmail']['app_password']

    participants = []
    for participant_name, participant_email in config['Participants'].items():
        participants.append(Participant(participant_name, participant_email))

    secret_santa = create_secret_santa(participants)
    print(secret_santa)

    for gift_reciever, secret_santa in secret_santa.items():

        email_message = create_secret_santa_email(secret_santa, gift_reciever)
        send_email(gmail_username, gmail_password, secret_santa.email, email_message)
