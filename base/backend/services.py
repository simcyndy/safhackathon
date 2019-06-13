# -*- coding: utf-8 -*-
"""
This is the service module from which all CRUD base services are declared.
"""
from base.backend.servicebase import ServiceBase
from base.models import AccountType, BalanceType, NotificationType, \
	RuleProfileCommand, RuleProfile, State, StateCategory, Tax, TransactionAccountTypeRuleProfile, TransactionType, \
	EntryType, Region, IdentityType, TransferType, ExecutionProfile, Theme


class AccountTypeService(ServiceBase):
	"""
	AccountType model CRUD services
	"""
	manager = AccountType.objects


class BalanceTypeService(ServiceBase):
	"""
	AccountType model CRUD services
	"""
	manager = BalanceType.objects


class IdentityTypeService(ServiceBase):
	"""
	IdentityType model CRUD services
	"""
	manager = IdentityType.objects


class CommissionService(ServiceBase):
	"""
	Commission model CRUD services
	"""
	manager = Commission.objects


class NotificationTypeService(ServiceBase):
	"""
	NotificationType model CRUD services
	"""
	manager = NotificationType.objects


class RuleProfileCommandService(ServiceBase):
	"""
	RuleProfileCommand model CRUD services
	"""
	manager = RuleProfileCommand.objects


class RuleProfileService(ServiceBase):
	"""
	RuleProfile model CRUD services
	"""
	manager = RuleProfile.objects


class ExecutionProfileService(ServiceBase):
	"""
	ExecutionProfile model CRUD services
	"""
	manager = ExecutionProfile.objects


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


class TaxService(ServiceBase):
	"""
	StateCategory model CRUD services
	"""
	manager = Tax.objects


class TransactionAccountTypeRuleProfileService(ServiceBase):
	"""
	TaxSchedule model CRUD services
	"""
	manager = TransactionAccountTypeRuleProfile.objects


class TransactionTypeService(ServiceBase):
	"""
	TransactionType model CRUD services
	"""
	manager = TransactionType.objects


class TransferTypeService(ServiceBase):
	"""
	TransferType model CRUD services
	"""
	manager = TransferType.objects


class EntryTypeService(ServiceBase):
	"""
	EntryType model CRUD services
	"""
	manager = EntryType.objects


class RegionService(ServiceBase):
	"""
	Region model CRUD services
	"""
	manager = Region.objects


class ThemeService(ServiceBase):
	"""
	Service for the Theme model
	"""
	manager = Theme.objects
