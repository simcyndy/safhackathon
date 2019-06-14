# -*- coding=utf-8 -*-
"""
Services for account module models
"""
from account.models import Customer, CustomerBusinessAccount
from base.backend.servicebase import ServiceBase


class CustomerService(ServiceBase):
	"""
	Defines the CRUD operations for the Customer model, i.e:
		- get(*args, **kwargs)
		- filter(*args, **kwargs)
		- create(**kwargs)
		- update(key, **kwargs)
	"""
	manager = Customer.objects


class CustomerBusinessAccountService(ServiceBase):
	"""
	Defines the CRUD operations for the CustomerBusinessAccount model, i.e:
		- get(*args, **kwargs)
		- filter(*args, **kwargs)
		- create(**kwargs)
		- update(key, **kwargs)
	"""
	manager = CustomerBusinessAccount.objects
