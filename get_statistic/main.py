from get_statistic import type_check
import argparse
from get_statistic.leaderboard import Leaderboard

parser = argparse.ArgumentPrser()
parser.add_argument('--mode', type=type_check.check_mode, required=True)
parser.add_argument('--count', type=type_check.check_positive, default=None)
parser.add_argument('--user_id', default=None)
parser.add_argument('--country', default=None)

args = parser.parse_args()

mode = args.mode
count = args.count
user_id = args.user_id
country = args.country

leaderboard = Leaderboard(mode, count, country, user_id)
result = leaderboard.get_records()
print(result)