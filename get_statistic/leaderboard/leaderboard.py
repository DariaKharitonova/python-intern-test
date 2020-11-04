import sys
import requests
import json

API_BASE_URL = "https://www.diabotical.com/"


AVAILABLE_MODES = [
    "r_macguffin",
    "r_wo", "r_rocket_arena_2",
    "r_shaft_arena_1",
    "r_ca_2",
    "r_ca_1"
]


class Leaderboard:
    def __init__(self, mode, count, country, user_id):
        self.mode = mode
        self.count = count
        self.country = country
        self.user_id = user_id

    def __get_stats(self):
        try:
            req = requests.get(f"{API_BASE_URL}/api/v0/stats/leaderboard",
                               [["mode", self.mode]])
            req.raise_for_status()
            response = req.json()
            return response["leaderboard"]
        except (requests.exceptions.RequestException, KeyError):
            print('Service not available right now. Please try later.')

    def __handle_count(self, records):
        return records[:self.count]

    def __handle_country(self, records):
        filtered_records = [
            record for record in records if record['country'] == self.country]
        return len(filtered_records)

    def __handle_user_id(self, records):
        for record in records:
            if record['user_id'] == self.user_id:
                return record

    def get_records(self):
        records = self.__get_stats()
        if self.count is not None:
            records = self.__handle_count(records)
        if self.country is not None:
            return self.__handle_country(records)
        if self.user_id is not None:
            records = self.__handle_user_id(records)
            if records is None:
                return f'User with id {self.user_id} not found'
        return json.dumps(records, indent=2)
