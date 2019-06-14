# coding=utf-8

import pytest
import mock
# from mixer.backend.django import mixer
from api.backend.interfaces import atm

# noinspection SpellCheckingInspection
pytestmark = pytest.mark.django_db


def test_check_account():
	with mock.patch.object(__builtins__, 'input', lambda: 'B'):
		assert atm.check_account() == 'expected_output'
