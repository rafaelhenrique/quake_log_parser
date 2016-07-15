test:
	py.test --cov-config .coveragerc --cov . --cov-report term-missing

test-matching:
	py.test . -k $(test) --pdb

requirements:
	pip install -r requirements.txt
