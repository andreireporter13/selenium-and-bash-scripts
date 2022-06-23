#!/bin/bash


echo '...'
echo 'Hello, Friend!'
echo '...'
echo 'Are we testing something today?'
echo '...'


# Condition for my first script;
echo '
1. Run test for ideisioferte.ro;
2. Run test for webautomation.ro;
3. Run test for publi24.ro for search something;
0. Exit.
'

# read function, in python this function is -eq input()
read a

# run ideisioferte.ro test;
if [[ $a -eq 1 ]]
then
	cd .. 
	source selenium-automation/bin/activate
	cd selenium-automation

	# run python code for testing webautomation.ro;
	python3 1_selenium_test.py

	# deactivate venv;
	deactivate

# second test;
elif [[ $a -eq 2 ]]
then 
	cd .. 
	source selenium-automation/bin/activate
	cd selenium-automation
	
	# run python code for testing ideisioferte.ro;
	python3 2_selenium_test.py

	# deactivate venv;
	deactivate

# third test;
elif [[ $a -eq 3 ]]
then 
	cd .. 
	source selenium-automation/bin/activate
	cd selenium-automation

	# run python code for testing google.com;
	python3 3_selenium_test_search.py

	# deactivate venv;

# exit
elif [[ $a -eq 0 ]]
then 
	exit
	
fi
