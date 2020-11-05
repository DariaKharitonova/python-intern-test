import unittest
import json
from get_statistic.leaderboard.leaderboard import Leaderboard


class TestLeaderboard(unittest.TestCase):
    def test_mode_get_records(self):
        """
          Leaderboard.getRecord() if defined only mode argument should return first 20 records # noqa: E501
        """
        leaderboard = Leaderboard('r_wo', None, None, None)
        result = leaderboard.get_records()
        result_list = json.loads(result)
        self.assertEqual(len(result_list), 20, 'should return 20 records')

    def test_count_getRecords(self):
        """
          Leaderboard.get_record() should return the same count of values that we define in constructor argument. # noqa: E501
        """
        count = 17
        leaderboard = Leaderboard('r_wo', count, None, None)
        result = leaderboard.get_records()
        result_list = json.loads(result)
        self.assertEqual(len(result_list), count,
                         f'should return {count} records')

    def test_country_get_records(self):
        """
          Leaderboard.get_records should return int value if we put country argument in constructor # noqa: E501
        """
        country = 'ru'
        leaderboard = Leaderboard('r_wo', None, country, None)
        result = leaderboard.get_records()
        self.assertIsInstance(result, int, 'should return int')

    def __get_user_id(self):
        leaderboard = Leaderboard('r_wo', None, None, None)
        result = leaderboard.get_records()
        result_list = json.loads(result)
        first_record = result_list[0]
        return first_record['user_id']

    def test_user_id_get_records(self):
        """
          Leaderboard.get_records should return info about user_id we put in constructor # noqa: E501
        """
        user_id = self.__get_user_id()
        leaderboard = Leaderboard('r_wo', None, None, user_id)
        result = leaderboard.get_records()
        result_list = json.loads(result)
        self.assertEqual(len(result_list), 9,
                         'should return props of user profile')
        self.assertEqual(result_list['user_id'], user_id,
                         'should be the same user_id')

    def test_wrong_user_id_get_records(self):
        """
          Leaderboard.getRecords should print a message and exit program if user_id is not in a list of records  # noqa: E501
        """
        leaderboard = Leaderboard('r_wo', None, None, 'not exist')
        with self.assertRaises(UserWarning):
            leaderboard.get_records()
