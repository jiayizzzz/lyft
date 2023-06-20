# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：battery.py
@Author  ：zjy
@Date    ：2023/6/19 19:34 
"""

from abc import ABC


class Battery(ABC):
    def needs_service(self):
        pass
