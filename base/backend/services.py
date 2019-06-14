# -*- coding: utf-8 -*-
"""
This is the service module from which all CRUD base services are declared.
"""
from base.backend.servicebase import ServiceBase
from base.models import AccountType, State, StateCategory


class AccountTypeService(ServiceBase):
	"""
	AccountType model CRUD services
	"""
	manager = AccountType.objects


class StateService(ServiceBase):
	"""
	State model CRUD services
	"""
	manager = State.objects


class StateCategoryService(ServiceBase):
	"""
	StateCategory model CRUD services
	"""
	manager = StateCategory.objects
