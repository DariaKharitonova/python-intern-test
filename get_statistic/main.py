from type_check.type_check import check_positive
import argparse
from leaderboard.leaderboard import Leaderboard, AVAILABLE_MODES


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=AVAILABLE_MODES, required=True)
    parser.add_argument('--count', type=check_positive, default=None)
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


if __name__ == '__main__':
    main()
