# coding=utf-8
"""
Test for the API services CRUD operations
"""
from datetime import timedelta

import pytest
from django.utils import timezone
from mixer.backend.django import mixer

# noinspection SpellCheckingInspection
pytestmark = pytest.mark.django_db
#
#
# class TestATMAdministration(object):
#
# 	def test_check_account(self):
# 		account
#
# 	def test_withdrawal(self):
# 		pass
#
# 	def test_deposit(self):
# 		pass
#
#
# import module  # The module which contains the call to input
from api.backend.interfaces.atm import ATMAdministration


class TestATMAdministration(object):

	def test_check_account(self):
		# Override the Python built-in input method
		ATMAdministration.input = lambda: 'B'
		# Call the function
		output = ATMAdministration().check_account()
		assert output == '("Your current account balance is :", 852)Return to Main Menu?(yes/no)'

	def test_withdrawal(self):
		# Override the Python built-in input method
		ATMAdministration.input = lambda: 'B'
		# Call the function
		output = ATMAdministration().withdrawal(500)
		assert output == '("Your current account balance is :", 852)Return to Main Menu?(yes/no)'

	def test_deposit(self):
		# Override the Python built-in input method
		ATMAdministration.input = lambda: 'B'
		# Call the function
		output = ATMAdministration().deposit(500)
		assert output == '("Your current account balance is :", 852)Return to Main Menu?(yes/no)'

	def test_welcome_screen(self):
		# Override the Python built-in input method
		ATMAdministration.input = lambda: 'B'
		# Call the function
		output = ATMAdministration().welcome_screen(500)
		assert output == '("Your current account balance is :", 852)Return to Main Menu?(yes/no)'

	def teardown_method(self, method):
		# This method is being called after each test case, and it will revert input back to original function
		ATMAdministration.input = input
