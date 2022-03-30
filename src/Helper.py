from src.Event import Event
import requests
import os
import sys


class Helper():

    @staticmethod
    def print_header() -> None:
        print("")
        print("            __  __            _____      _              _ _")
        print("     /\    / _|/ _|          / ____|    | |            (_) |")
        print("    /  \  | |_| |_ ___ _ __ | (___   ___| |__  _ __ ___ _| |__")
        print("   / /\ \ |  _|  _/ _ \ '_ \ \___ \ / __| '_ \| '__/ _ \ | '_ \\")
        print("  / ____ \| | | ||  __/ | | |____) | (__| | | | | |  __/ | |_) |")
        print(" /_/    \_\_|_|_|_\___|_| |_|_____/ \___|_|_|_|_|_ \___|_|_.__/")
        print(" \ \        / /  __ \|  \/  | |  _ \ / __ \__   __|")
        print("  \ \  /\  / /| |__) | \  / | | |_) | |  | | | |")
        print("   \ \/  \/ / |  ___/| |\/| | |  _ <| |  | | | |")
        print("    \  /\  /  | |    | |  | | | |_) | |__| | | |")
        print("     \/  \/   |_|    |_|  |_| |____/ \____/  |_|")
        print("")

    @staticmethod
    def request_token(email, password) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux xidentitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyB5m_AnO575kvWriahcF1SFIWp8Fj3gQno',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'x-client-version': 'Firefox/JsCore/9.6.0/FirebaseCore-web',
            'Origin': 'https://monkeytype.com',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }
        json_data = {
            'returnSecureToken': True,
            'email': email,
            'password': password,
        }

        response = requests.post('https://api.monkeytype.com/results', headers=headers, json=json_data)
        return response.text


# Print header upon import
Helper.print_header()
