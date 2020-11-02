import sys
import requests
import json

API_BASE_URL = "https://www.diabotical.com/"


class Leaderboard:
    def __init__(self, mode, count, country, user_id):
        self.mode = mode
        self.count = count
        self.country = country
        self.user_id = user_id

    def __getStats(self):
        try:
            req = requests.get(f"{API_BASE_URL}/api/v0/stats/leaderboard", [["mode", self.mode]])
            req.raise_for_status()
            response = req.json()
            return response["leaderboard"]
        except requests.exceptions.RequestException:
            print('Service not available right now. Please try later.')

    def __countHandler(self, records):
        return records[:self.count]

    def __countryHandler(self, records):
        filtered_records = [record for record in records if record['country'] == self.country]
        return len(filtered_records)

    def __userIdHandler(self, records):
        for record in records:
            if record['user_id'] == self.user_id:
                return record
        print(f'User with id {self.user_id} not found')
        sys.exit()

    def getRecords(self):
        records = self.__getStats()
        if self.count is not None:
            records = self.__countHandler(records)
        if self.country is not None:
            return self.__countryHandler(records)
        if self.user_id is not None:
            records = self.__userIdHandler(records)
        return json.dumps(records, indent=2)
