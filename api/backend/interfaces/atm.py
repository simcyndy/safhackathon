# coding=utf-8
"""
The ATM interface
"""
import logging
from decimal import Decimal
from account.models import Customer as customer
from account.models import CustomerBusinessAccount as customer_business_account

lgr = logging.getLogger(__name__)

from random import randint

# The amount of money that will be processed each time
# taken from randint()
account_balance = randint(0, 200000)


class ATMAdministration:
	"""
	The class for ATM Administration functionality.
	# Enter  Amount
	# Customer Account: opening_balance, current_balance, available_balance, total
	# Check if  amount has reached max_deposit_for_day/ max_withdrawal_for_day
	# Check if  amount has reached max_deposit_per_transaction / max_withdrawal_per_transaction
	# Check if the frequency for the day has reached
	"""

	def check_account(self):
		"""Function to check account balance."""

		print("Your current account balance is :", account_balance)
		choice = raw_input("Return to Main Menu?(yes/no) ").lower()
		if 'yes' in choice:
			self.welcome_screen()
		else:
			return "Thankyou for banking with us.Come Again!"

	def withdrawal(
			self, withdrawal_amount, max_withdrawal_for_day = Decimal(50000), max_withdrawal_per_transaction = Decimal(
				20000),
			max_withdrawal_frequency = 3):
		"""
		Withdraws amount from bank
		:param withdrawal_amount:
		:param max_withdrawal_for_day:
		:param max_withdrawal_per_transaction:
		:param max_withdrawal_frequency:
		:return:
		"""
		try:
			if withdrawal_amount < max_withdrawal_for_day:
				if withdrawal_amount < max_withdrawal_per_transaction:
					withdrawal_frequency = 0
					if withdrawal_frequency < max_withdrawal_frequency:
						if withdrawal_amount > customer_business_account.available:
							withdrawal_frequency += withdrawal_frequency
							customer_available_balance = customer_business_account.available
							customer_available_balance -= withdrawal_amount
							return customer_available_balance
						return "You Don't Have Enough Money in your Account to Withdraw"
					return "You have reached Maximum Withdrawal Frequencies for the day"
				return "You Are above the Maximum Transactional Limit"
			return "You have reached the Maximum Withdrawal for the day"
		except Exception as e:
			lgr.exception("Withdrawal Error:%s", e)
			return {'code': '500.00.001'}

	def deposit(
			self, deposit_amount, max_deposit_for_day = Decimal(150000), max_deposit_per_transaction = Decimal(40000),
			max_deposit_frequency = 4):
		"""
		Deposits an amount in the Customer Account
		:param deposit_amount: the amount to be deposited
		:param max_deposit_for_day:
		:param max_deposit_per_transaction:
		:param max_deposit_frequency:
		:return:
		"""
		try:
			if deposit_amount < max_deposit_for_day:
				if deposit_amount < max_deposit_per_transaction:
					deposit_frequency = 0
					if deposit_frequency < max_deposit_frequency:
						deposit_frequency += deposit_frequency
						customer_available_balance = customer_business_account.available
						customer_available_balance += deposit_amount
						return customer_available_balance
					return "You have reached Maximum Deposit Frequencies for the day"
				return "You Are above the Maximum Transactional Limit"
			return "You have reached the Maximum Deposit for the day"
		except Exception as e:
			lgr.exception("Deposit Error:%s", e)
			return {'code': '500.00.001'}

	def welcome_screen(self, choice):
		"""Main function of the program"""

		print (
			"**********************************************************************************************************")
		print ("""
			Welcome to the SafHackathon Bank!
		    Options include:
		    [ B ] View Account Balance
		    [ D ] Deposit funds
		    [ W ] Withdraw funds
		    [ Q ] Quit
		""")

		choice = str(raw_input("Enter an operation  :'B'(Balance), 'D'(Deposit), 'W'(Withdraw), or'Q'(Quit) : "))
		if choice == "B":
			self.check_account()
		elif choice == "D":
			amount = float(input("Enter an amount to deposit: "))
			self.deposit(deposit_amount = amount)
			choice = raw_input("Would you like to deposit more money? ").lower()
			if 'no' in choice:
				return "Thankyou for banking with us.Come Again!!"
			else:
				self.deposit(deposit_amount = amount)
		elif choice == "W":
			amount = float(input("Enter an amount to deposit: "))
			self.withdrawal(withdrawal_amount = amount)
			choice = raw_input("Would you like to withdraw more money? ").lower()
			if 'no' in choice:
				return {'code': "500.00.002", "data": {"info": "Thankyou for banking with us.Come Again"}}
			else:
				self.withdrawal(withdrawal_amount = amount)
		elif choice == "Q":
			ended = (input("Are you sure you want to quit? (y/n)"))
			if ended.lower() == "y":
				return "Thankyou for banking with us.Come Again!"
		else:
			return "Invalid option,Please try again"

	if __name__ == '__main__':
		welcome_screen()
