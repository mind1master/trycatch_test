test:
	python test.py

cov coverage:
	coverage run test.py

flake:
	flake8 chess_challenge.py test.py

lint:
	pylint chess_challenge.py test.py

checkers: flake lint

run:
	python chess_challenge.py