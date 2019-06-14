# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.backend.interfaces.atm import ATMAdministration
from base.backend.utils import get_request_data
lgr = logging.getLogger(__name__)


# Create your views here.
@csrf_exempt
def operate_atm(request):
	"""
	Endpoint for operating an ATM.
	@param request: Django HTTP request.
	@type request: WSGIRequest
	@return: JsonResponse with the response code obtained from processing this request.
	@rtype: JsonResponse
	"""
	try:
		# request_data = get_request_data(request)
		# choice = request_data.get('choice', None)
		return JsonResponse(ATMAdministration().welcome_screen())
	except Exception as e:
		lgr.exception('operate_atm Exception: %s', e)
	return JsonResponse({'code': '800.005.006'})
