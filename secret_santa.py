import configparser
import copy
import random
from collections import namedtuple
from email.mime.text import MIMEText
import smtplib

Participant = namedtuple('Participant', ['name', 'email'])

PARTICIPANTS = [
#    Participant("Anabel", "anabel.mendt@gmail.com"),
#    Participant("Rodrigo", "rodrigocidad@gmail.com"),
#    Participant("Daniel", "dmendt@gmail.com "),
#    Participant("Cristal", "cristalboza@gmail.com"),
    Participant("Tamara", "tammymendt@gmail.com"),
    Participant("Lorenzo", "lorenzofundaro@gmail.com"),
    Participant("Lorenzo Test", "lorenzofundaro+test@gmail.com"),
#    Participant("Lis Maria", "administracion@santaclaramg.com"),
#    Participant("Roberto", "rfundaro@gmail.com"),
#    Participant("Ursula", "uehrma@gmail.com")
]


def create_secret_santa(participant_list):

    secret_santa_dict = {}
    secret_santa_list = copy.deepcopy(participant_list)

    participant = participant_list[0]

    while len(secret_santa_list) > 1:
        while True:
            candidate = random.choice(secret_santa_list)
            if candidate.name != participant.name and secret_santa_dict.get(
                    candidate.name, None) != participant:
                secret_santa_dict[participant.name] = candidate
                secret_santa_list.remove(candidate)
                participant = candidate
                break

    secret_santa_dict[participant.name] = participant_list[0]

    return secret_santa_dict


def create_secret_santa_email(secret_santa, gift_reciever_name):

    message = '''
    Bienvenido al amigo secreto de la Navidad 2018 {secret_santa}!\n

    Haremos un pequeño intercambio de regalo el 24.12.2018. El regalo puede ser algo
    hecho a mano o comprado con un valor entre 20 y 30 euros.\n

    Tu amigo secreto es: {gift_reciever_name}
    '''.format(secret_santa=secret_santa.name, gift_reciever_name=gift_reciever_name)

    msg = MIMEText(message)

    msg['Subject'] = 'Navidad 2018: Amigo Secreto'
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

    secret_santa = create_secret_santa(PARTICIPANTS)

    for gift_reciever, secret_santa in secret_santa.items():

        email_message = create_secret_santa_email(secret_santa, gift_reciever)
        send_email(gmail_username, gmail_password, secret_santa.email, email_message)
