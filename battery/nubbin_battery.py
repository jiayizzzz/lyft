# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：nubbin_battery.py
@Author  ：zjy
@Date    ：2023/6/19 19:38 
"""

from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
