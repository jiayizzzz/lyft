# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：serviceable.py
@Author  ：zjy
@Date    ：2023/6/20 10:43 
"""


from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
