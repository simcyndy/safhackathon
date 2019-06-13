# coding=utf-8
"""
The URLs file for API endpoints.
"""

from django.conf.urls import include, url
from api.views import operate_atm

urlpatterns = [
	url(r'^operate_atm/$', operate_atm)
]
