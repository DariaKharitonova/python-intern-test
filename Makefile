install:
	@poetry install
	
lint:
	poetry run flake8 get_statistic

test:
	poetry run python3 -m unittest -v get_statistic/type_check/test_type_check.py get_statistic/leaderboard/test_leaderboard.py
