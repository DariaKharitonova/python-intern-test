install:
	@poetry install
	
lint:
	poetry run flake8 get_statistic	
