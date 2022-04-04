![Affenschreib WPM Bot](logo.png)

Python application to grab monkeytype typing test data and extract personal bests for multiple accounts to send notifications to a telegram channel, whenever a new personal best is reached.

### Setup

The main script wpm.py is supposed to be run scheduled within an virtual environment, where the schedule frequency equals the update frequency for checking for new personal bests.

`python3 -m venv venv`
`pip install -r requirements.txt`

Next copy the blank config file and replace the placeholder with credential pairs for the accounts to be monitored.
In addition to that replace the token and chat ID placeholders for the telegram bot to be used and the setup is done:

`source venv/bin/activate`
`python wpm.py`
