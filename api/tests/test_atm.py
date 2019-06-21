# coding=utf-8

import unittest

from mock import patch
from unittest import TestCase
from api.backend.interfaces import atm


class TestAnswer(TestCase):
	def test_balance_return_val(self):
		with patch('__builtin__.raw_input', return_value = 'B') as _raw_input:
			self.assertEqual(atm.check_account(), 'Your current account balance is : 0.00')
			_raw_input.assert_called_once_with('Enter a character to perform an operation:')
