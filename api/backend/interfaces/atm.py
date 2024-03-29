# coding=utf-8
"""
The ATM interface
"""
import logging
from decimal import Decimal

lgr = logging.getLogger(__name__)


def check_account():
	"""Function to check account balance."""

	global account_balance
	print("Your current account balance is :", account_balance)


def withdrawal(
		withdrawal_amount, max_withdrawal_for_day = Decimal(50000),
		max_withdrawal_per_transaction = Decimal(20000), max_withdrawal_frequency = 3):
	"""
	Withdraws amount from account
	:param withdrawal_amount: the amount to be withdrawn
	:type: Decimal
	:param max_withdrawal_for_day: the maximum amount to be withdrawn for the day
	:type: Decimal
	:param max_withdrawal_per_transaction: the max withdrawal per transaction
	:type: Decimal
	:param max_withdrawal_frequency: the maximum withdrawal frequency
	:type: int
	:return:
	"""
	try:
		global withdrawal_total
		global withdrawal_frequency
		global account_balance
		if withdrawal_amount > max_withdrawal_per_transaction:
			print('Failed.You Are above the Maximum Transactional Limit.Maximum limit is 20,000')
			return
		if withdrawal_amount + withdrawal_total > max_withdrawal_for_day:
			print('Failed. You have reached the Maximum Amount allowed for Withdrawal for the day. Try Again Tommorrow')
			return
		if withdrawal_frequency + 1 > max_withdrawal_frequency:
			print('Failed. You have reached Maximum Withdrawal Frequencies for the day')
			return
		if account_balance - withdrawal_amount < 0:
			print('Failed. Cannot withdraw when balance is less than withdrawal amount')
			return
		account_balance -= withdrawal_amount
		withdrawal_total += withdrawal_amount
		withdrawal_frequency += 1
		print('[ You have Successfully withdrawn: %s]\n\n' % withdrawal_amount)
		print('[ New Account Balance: %s]\n\n' % account_balance)
		return
	except Exception as e:
		lgr.exception("Withdrawal Error:%s", e)
		return


def deposit(
		deposit_amount, max_deposit_for_day = Decimal(150000), max_deposit_per_transaction = Decimal(40000),
		max_deposit_frequency = 4):
	"""
	Deposits an amount in the Account
	:param deposit_amount: the amount to be deposited
	:type: Decimal
	:param max_deposit_for_day: the maximum deposit for the day
	:type: Decimal
	:param max_deposit_per_transaction: the maximum deposit per transaction
	:type: Decimal
	:param max_deposit_frequency: the maximum deposit frequency
	:type: int
	:return:
	"""
	try:
		global deposit_total
		global deposit_frequency
		global account_balance
		if deposit_amount > max_deposit_per_transaction:
			print('Failed.You Are above the Maximum Transactional Limit.Maximum limit is 40,000')
			return
		if deposit_amount + deposit_total > max_deposit_for_day:
			print('Failed. You have reached the Maximum Amount allowed for Deposit for the day. Try Again Tommorrow')
			return
		if deposit_frequency + 1 > max_deposit_frequency:
			print('Failed. You have reached Maximum Deposit Frequencies for the day')
			return
		account_balance += deposit_amount
		deposit_total += deposit_amount
		deposit_frequency += 1
		print('[ You have Successfully deposited: %s]\n\n' % deposit_amount)
		print('[ New Account Balance: %s]\n\n' % account_balance)
		return
	except Exception as e:
		lgr.exception("Deposit Error:%s", e)


def format_print():
	"""Shouldn't have to explain this.."""

	return '-' * 50


def welcome_screen():
	"""Main function of the program"""
	print format_print()
	print (
		"""
		Welcome to the SafHackathon Bank!
			Options include:
		    [ B ] View Account Balance
		    [ D ] Deposit funds
		    [ W ] Withdraw funds
		    [ Q ] Quit
	    """
	)
	print format_print()

	choice = str(raw_input(
		"Enter a character to perform an operation:"))
	if choice == "B":
		print (
			"*****************************************CHECK BALANCE*********************************************")
		check_account()
		print format_print()
	elif choice == "D":
		print (
			"*****************************************DEPOSIT FUNDS*********************************************")
		amount = float(input("Enter an amount to deposit: "))
		deposit(deposit_amount = amount)
	elif choice == "W":
		print (
			"*****************************************WITHDRAW FUNDS*********************************************")
		amount = float(input("Enter an amount to withdraw: "))
		withdrawal(withdrawal_amount = amount)
	elif choice == "Q":
		ended = (raw_input("Are you sure you want to quit? (yes/no)")).lower()
		if ended == "yes":
			print("Goodbye....")
			exit(0)
		return
	else:
		print("Invalid option,Please try again")


if __name__ == '__main__':
	# Global variables
	account_balance = 0.00
	deposit_total = 0.00
	deposit_frequency = 0
	withdrawal_total = 0.00
	withdrawal_frequency = 0
	while True:
		welcome_screen()
