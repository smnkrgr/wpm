from src.Helper import Helper
from src.Event import Event
from src.Identity import Identity
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
