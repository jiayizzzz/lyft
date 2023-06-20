# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：test_nubbin_battery.py
@Author  ：zjy
@Date    ：2023/6/20 10:57 
"""


import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service_true(self):
        test_battery = NubbinBattery(date.fromisoformat("2010-05-15"), date.fromisoformat("2020-02-22"))
        self.assertTrue(test_battery.needs_service())

    def test_nubbin_battery_needs_service_false(self):
        test_battery = NubbinBattery(date.fromisoformat("2021-09-19"), date.fromisoformat("2021-11-15"))
        self.assertFalse(test_battery.needs_service())
