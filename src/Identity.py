from src.Helper import Helper
import json


class Identity():

    def __init__(self, email, password) -> None:
        # Retrieve display name and token
        self.email = email
        self.name, self.token = Helper.authorize_identity(
            email=self.email,
            password=password
        )
        
        # Retrieve the typing data from Monkeytype
        self.typing_data = self.get_typing_data()

    def get_typing_data(self) -> dict:
        return Helper.get_typing_data(self.token)

