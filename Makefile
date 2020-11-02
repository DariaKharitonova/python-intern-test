install:
	@poetry install
	
lint:
	poetry run flake8 get_statistic

test:
	poetry run python -m unittest -v get_statistic/test_type_check.py get_statistic/test_leaderboard.py
