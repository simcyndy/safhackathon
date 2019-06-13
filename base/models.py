# -*- coding: utf-8 -*-
"""
Base Models
"""
from __future__ import unicode_literals

import uuid

from django.db import models


class BaseModel(models.Model):
	"""
	Define repetitive methods to avoid cycles of redefining in every model.
	"""
	id = models.UUIDField(max_length = 100, default = uuid.uuid4, unique = True, editable = False, primary_key = True)
	date_modified = models.DateTimeField(auto_now = True)
	date_created = models.DateTimeField(auto_now_add = True)

	class Meta(object):
		abstract = True


class GenericBaseModel(BaseModel):
	"""
	Define repetitive methods to avoid cycles of redefining in every model.
	"""
	name = models.CharField(max_length = 100)
	description = models.TextField(max_length = 255, blank = True, null = True)

	class Meta(object):
		abstract = True


class StateCategory(GenericBaseModel):
	"""
	Defines the different categories for system states e.g. General, Transaction, User etc.
	"""

	def __unicode__(self):
		return u'%s ' % self.name

	class Meta(object):
		verbose_name_plural = "State categories"
		unique_together = ('name',)


class State(GenericBaseModel):
	"""
	Defines the different states used in the system e.g. Active, Disabled etc
	"""
	state_category = models.ForeignKey(StateCategory)

	def __unicode__(self):
		return u'%s ' % self.name

	class Meta(object):
		ordering = ('state_category__name', 'name')
		unique_together = ('state_category', 'name')


class AccountType(GenericBaseModel):
	"""
	Defines the different account types used by agents e.g. Utility, Holding, Commissions, etc.
	"""
	state = models.ForeignKey(State)

	def __unicode__(self):
		return u'%s ' % self.name

	class Meta(GenericBaseModel.Meta):
		unique_together = ('name',)


def default_state():
	"""
	Helper function to return the active state directly in a model.
	@return: The Active state.
	@rtype: State | None
	"""
	# noinspection PyBroadException
	try:
		return State.objects.get(name = 'Active')
	except Exception:
		pass
	return None


def approval_pending_state():
	"""
	Helper function to return the approval pending state directly in a model.
	@return: The Approval Pending state.
	@rtype: State | None
	"""
	# noinspection PyBroadException
	try:
		return State.objects.get(name = 'Approval Pending')
	except Exception:
		pass
	return None
