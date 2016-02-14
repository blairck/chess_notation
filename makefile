status:
	env/bin/pylint src/ -rn --rcfile=pylint_config.txt
	env/bin/pylint test/ -rn --rcfile=pylint_config.txt
	env/bin/coverage run test/run_tests.py
	env/bin/coverage report