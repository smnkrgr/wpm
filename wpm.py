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
    emails = Helper.parse_conf_list(config.get("main", "emails"))
    passwords = Helper.parse_conf_list(config.get("main", "passwords"))
    rl_names = Helper.parse_conf_list(config.get("main", "rl_names"))
    identities = []
    for i in range(len(emails)):
        identities.append(Identity(
            email=emails[i],
            password=passwords[i],
            rl_name=rl_names[i]
        ))

    Event("Checking for new PBs...")
    for identity in identities:
        new_pbs = identity.get_new_pbs()
        if new_pbs != {}:
            Event("There are "+str(len(new_pbs))+" new PBs.")
        else:
            Event("No new PBs.")
            break

        # Create the telegram bot and send new pbs
        token = config.get("telegram", "token")
        chat_id = config.get("telegram", "chat_id")
        bot = TelegramBot(token=token, chat_id=chat_id)
        for pb in new_pbs:
            bot.format_and_send_new_pb(new_pbs[pb], identity.get_rl_name())
