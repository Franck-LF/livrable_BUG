import os
import logging
from logging.handlers import SMTPHandler
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv('GMAIL_USER'), os.getenv('PASSWORD'))


# Configuration du logger
logger = logging.getLogger("mon_logger")
logger.setLevel(logging.ERROR)  # Seuls les logs >= ERROR seront envoyés

# Configuration de l'envoi d'email
mail_handler = SMTPHandler(
    mailhost=("smtp.gmail.com", 587),     # serveur SMTP et port
    fromaddr="f7lefur@gmail.com",           # adresse d'expédition
    toaddrs=["f7lefur@gmail.com"],          # destinataires
    subject="Alerte : une erreur est survenue",
    credentials=(os.getenv('GMAIL_USER'), os.getenv('PASSWORD')),  # login SMTP
    secure=()  # active STARTTLS (laisser vide pour SSL/TLS déjà activé)
)

# Ajouter le handler au logger
logger.addHandler(mail_handler)

# Exemple d'erreur qui déclenche l'envoi d'un mail
try:
    1 / 0
except ZeroDivisionError:
    logger.error("Division par zéro détectée !")
