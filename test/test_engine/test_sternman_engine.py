# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：test_sternman_engine.py
@Author  ：zjy
@Date    ：2023/6/20 10:56 
"""


import unittest

from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
