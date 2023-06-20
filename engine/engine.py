# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：engine.py
@Author  ：zjy
@Date    ：2023/6/19 19:26 
"""

from abc import ABC


class Engine(ABC):
    def needs_service(self):
        pass
