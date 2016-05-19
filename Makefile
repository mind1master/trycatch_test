test:
	python test.py

cov coverage:
	coverage run test.py
	coverage report
	coverage html

flake:
	flake8 chess_challenge.py test.py

lint:
	pylint chess_challenge.py test.py

checkers: flake lint

run:
	python chess_challenge.py