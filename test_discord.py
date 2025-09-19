# Logging/Alterting avec des webhooks
# Un webhook est une URL fourni par un service (Teams, Discord, etc...) qui accepte des requêtes HTTP.
# Il est donc possible d'y envoyer des informations avec la méthode POST. 
# Ci-dessous un exemple de code, avec request et logging, pour envoyer des messages sur ce salon. 

# Note : Le présent salon est temporaire et sera supprimé un jour et, avec lui, 
# le webhook associé. Merci de rester corrects dans les messages envoyés. ;)


import logging
import requests

# webhook que vous pouvez utiliser pour tester !
discord_webhook = "https://discord.com/api/webhooks/1418224972761006241/6ll0WKeGFAq31Ot_mam6bGAbY2UiMdDKcpE7gx5KAfFBP3L0dVxHKj1h6_9W5ihiYXDQ"


def discord_emit(record):
    log_entry = formatter.format(record)
    requests.post(
        discord_webhook,
        json={"content": log_entry},
        timeout=2
    )

logger = logging.getLogger("discord")
logger.setLevel(logging.CRITICAL)

formatter = logging.Formatter("[%(levelname)s] %(message)s")

handler = logging.Handler()
handler.emit = discord_emit  # on écrase la méthode au profit de notre fonction
logger.addHandler(handler)

logger.critical("URGENT !!! éteignez la VMC !!!")