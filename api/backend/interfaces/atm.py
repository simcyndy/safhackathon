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
	choice = raw_input("Return to Main Menu?(yes/no) ").lower()
	if 'yes' in choice:
		welcome_screen()
	else:
		print("Thank you for Banking with us.Come Again!")


def withdrawal(
		withdrawal_amount, max_withdrawal_for_day = Decimal(50000),
		max_withdrawal_per_transaction = Decimal(20000), max_withdrawal_frequency = 3):
	"""
	Withdraws amount from account
	:param withdrawal_amount:
	:param max_withdrawal_for_day:
	:param max_withdrawal_per_transaction:
	:param max_withdrawal_frequency:
	:return:
	"""
	try:
		global withdrawal_total
		global withdrawal_frequency
		global account_balance
		if (withdrawal_amount + withdrawal_total) < max_withdrawal_for_day:
			if withdrawal_amount < max_withdrawal_per_transaction:
				if withdrawal_frequency < max_withdrawal_frequency:
					withdrawal_frequency += withdrawal_frequency
					account_balance -= withdrawal_amount
					print('[ You have Successfully withdrawn: %s]\n\n' % withdrawal_amount)
					print('[ New Account Balance: %s]\n\n' % account_balance)
					return
				print ("You have reached Maximum Withdrawal Frequencies for the day")
				return
			print("You Are above the Maximum Transactional Limit")
			return
		print("You have reached the Maximum Withdrawal for the day")
		return
	except Exception as e:
		lgr.exception("Withdrawal Error:%s", e)
		return


def deposit(
		deposit_amount, max_deposit_for_day = Decimal(150000), max_deposit_per_transaction = Decimal(40000),
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
		global deposit_total
		global deposit_frequency
		global account_balance
		if (deposit_amount + deposit_total) < max_deposit_for_day:
			if deposit_amount < max_deposit_per_transaction:
				if deposit_frequency < max_deposit_frequency:
					deposit_frequency += deposit_frequency
					account_balance += deposit_amount
					print('[ You have Successfully deposited: %s]\n\n' % deposit_amount)
					print('[ New Account Balance: %s]\n\n' % account_balance)
					return
				print ("You have reached Maximum Deposit Frequencies for the day")
				return
			print("You Are above the Maximum Transactional Limit.Maximum limit is 40,000")
			return
		print("You have reached the Maximum Deposit for the day")
		return
	except Exception as e:
		lgr.exception("Deposit Error:%s", e)


def format_print():
	return "*" * 150


def welcome_screen():
	"""Main function of the program"""
	printed = format_print()
	print(printed)
	# print (
	# 	"********************************************************************************************************")
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
	print(printed)

	choice = str(raw_input(
		"Enter a character to perform an operation:"))
	if choice == "B":
		print (
			"*****************************************CHECK BALANCE*********************************************")
		check_account()
		print(printed)
	elif choice == "D":
		print (
			"*****************************************DEPOSIT FUNDS*********************************************")
		amount = float(input("Enter an amount to deposit: "))
		deposit(deposit_amount = amount)
		choice = raw_input("Would you like to deposit more money? (yes/no)").lower()
		if 'no' in choice:
			print "Thankyou for banking with us.Come Again!!"
			print ("********************************************************************************************")
		else:
			amount = float(input("Enter an amount to deposit: "))
			deposit(deposit_amount = amount)
	elif choice == "W":
		amount = float(input("Enter an amount to deposit: "))
		withdrawal(withdrawal_amount = amount)
		choice = raw_input("Would you like to withdraw more money? ").lower()
		if 'no' in choice:
			return {"data": {"info": "Thankyou for banking with us.Come Again"}}
		else:
			withdrawal(withdrawal_amount = amount)
	elif choice == "Q":
		ended = (input("Are you sure you want to quit? (y/n)"))
		if ended.lower() == "y":
			return "Thankyou for banking with us.Come Again!"
		welcome_screen()
	else:
		return "Invalid option,Please try again"


if __name__ == '__main__':
	# Global variables
	account_balance = 0.00
	deposit_total = 0.00
	deposit_frequency = 0
	withdrawal_total = 0.00
	withdrawal_frequency = 0
	welcome_screen()
