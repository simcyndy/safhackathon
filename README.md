ATM Machine

[![N|Solid](https://www.drupal.org/files/issues/ddocs-3.gif)](https://docs.google.com/spreadsheets/d/1INSlOjEKIf4q_UXiSpsn_lKb8VHZKI3XWxlIkIAOawM/edit#gid=0)

ATM Machine
================

Application for ATM Machines - Check Account Balance, Deposit Funds, Withdraw Funds

Python 2.7
---------

Install Python 3.0 from [Python download page](https://www.python.org/downloads/)



To run the program :

1. Run the command : python atm.py
2. See the magic happen! :-)

+++++++++++++++++++++++++
TO RUN TESTS
+++++++++++++++++++++++++



Install Dependencies
---------------------

	pip install django
  
Usage
-----------
	python manage.py runserver
  
Make and Apply Migrations
----------- 

	#make migrations
	python manage.py makemigrations

	#apply migrations
	python manage.py migrate
  
 Tests
-----------
Install required plugins for testing

	pip install pytest
	pip install pytest-django
	pip install git+git://github.com/mverteuil/pytest-ipdb.git
	pip install pytest-cov
	pip install mixer
	
Run the tests
---------------
	py.test
