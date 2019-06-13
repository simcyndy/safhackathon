# -*- coding: utf-8 -*-
"""
The services for Account objects/ models.

Example:
	* from account.backend.services import MasterAgentService
	* master_agent = MasterAgentService().get(agent_code='A0012')

"""
from base.backend.servicebase import ServiceBase

# from account.models import MasterAgent, Bank, ServiceProvider, Agent, AgentAccount, BankServiceProvider, \
# 	MasterAgentServiceProviderAccount, ServiceProviderAccount, MasterAgentServiceProvider, PhysicalAddress, Customer, \
# 	CustomerServiceProvider, CustomerServiceProviderAccount, TaxAgent, TaxAgentServiceProvider, \
# 	TaxAgentServiceProviderAccount, CommissionStructure, CommissionSchedule, TaxSchedule, TaxStructure, AgentAssistant, \
# 	AuthCode, AuthRequestType, GeneralSetting

from account.models import Customer, CustomerBusinessAccount


class CustomerService(ServiceBase):
	"""
	The service for handling customer model interactions.
	"""
	manager = Customer.objects


class CustomerBusinessAccountService(ServiceBase):
	"""
	The service for handling Business Account interactions.
	"""
	manager = CustomerBusinessAccount.objects
