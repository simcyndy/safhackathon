# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from base.models import AccountType, State, BaseModel


class Customer(BaseModel):
	""" Customer e.g. Jane Doe Example"""
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	other_name = models.CharField(max_length = 20, null = True, blank = True)
	gender = models.CharField(max_length = 1, choices = (('M', 'Male'), ('F', 'Female')), default = 'M')
	email = models.EmailField(max_length = 20, null = True, blank = True)
	identity_number = models.CharField(max_length = 20, unique = True)
	language_code = models.CharField(max_length = 5, default = 'en')
	date_of_birth = models.DateField(null = True, blank = True)
	state = models.ForeignKey(State)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)


class CustomerBusinessAccount(object):
	"""
	Define BusinessAccount model. e.g. Jane Doe Other Loan Available - 6700
	"""
	customer = models.ForeignKey(Customer)
	account_type = models.ForeignKey(AccountType)
	available = models.DecimalField(max_digits = 25, decimal_places = 2, default = 0.00)
	current = models.DecimalField(max_digits = 25, decimal_places = 2, default = 0.00)
	reserved = models.DecimalField(max_digits = 25, decimal_places = 2, default = 0.00)
	uncleared = models.DecimalField(max_digits = 25, decimal_places = 2, default = 0.00)
	charge = models.DecimalField(max_digits = 25, decimal_places = 2, default = 0.00)
	state = models.ForeignKey(State)

	def __str__(self):
		return '%s %s' % (self.account_type, self.state)
