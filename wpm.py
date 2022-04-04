from src.Helper import Helper
from src.Event import Event
from src.Identity import Identity
from src.TelegramBot import TelegramBot
from backports import configparser


if __name__=='__main__':
    # Load the config file
    Event("Loading the config...")
    conf_file = "config.ini"
    config = configparser.ConfigParser()
    try:
        config.read(conf_file)
        Event("Config loaded!", is_success=True)
    except Exception as e:
        message = "Config could not be loaded: " + str(e)
        Event(message, is_error=True, exit=True)

    # Authenticate and get typing data
    email = config.get("main", "email")
    password = config.get("main", "password")
    identity = Identity(
        email=email,
        password=password
    )
    new_pbs = identity.get_new_pbs()
    Event("Checking for new PBs...")
    if new_pbs != {}:
        Event("There are "+str(len(new_pbs))+" new PBs.")
    else:
        Event("No new PBs. Exiting..")
        exit(0)


    # Create the telegram bot and send new pbs
    token = config.get("telegram", "token")
    chat_id = config.get("telegram", "chat_id")
    bot = TelegramBot(token=token, chat_id=chat_id)
    for pb in new_pbs:
        bot.format_and_send_new_pb(new_pbs[pb], "ass")
