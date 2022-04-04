from src.Helper import Helper
import json
import os


class Identity():

    def __init__(self, email, password, rl_name) -> None:
        # Retrieve display name and token
        self.email = email
        self.rl_name = rl_name
        self.name, self.token = Helper.authorize_identity(
            email=self.email,
            password=password
        )
        
        # Retrieve the typing data from Monkeytype
        self.typing_data = self.get_typing_data()

        # Retrieve the entries that are marked as pbs
        self.pbs = self.extract_pbs()

        # Save pbs if there is no entry for the identity yet
        # Compare to previous if there is an entry
        self.new_pbs = self.compare_to_previous_pbs()

    def get_typing_data(self) -> dict:
        return Helper.get_typing_data(self.token)

    def get_new_pbs(self) -> dict:
        return self.new_pbs
    
    def get_rl_name(self) -> str:
        return self.rl_name

    def extract_pbs(self) -> dict:
        pbs = {}
        for typing_test in self.typing_data:
            if "isPb" in typing_test:
                pbs[typing_test['_id']] = typing_test
        return pbs
    
    def compare_to_previous_pbs(self) -> dict:
        # New pbs list to be populated
        new_pbs = {}
        previous_pbs = {}
        # If there is no entry save
        path = os.path.join("pbs", self.name)
        if not os.path.exists(path):
            Helper.save_dict(path, self.pbs)
            return new_pbs
        # If there is an entry, compare with current
        else:
            previous_pbs = Helper.load_dict(path)
        # Populate with new pbs if existent
        for pb in self.pbs:
            if pb not in previous_pbs.keys():
                new_pbs[pb] = self.pbs[pb]
        # Save the current pbs for the next execution
        Helper.save_dict(path, self.pbs)
        return new_pbs


