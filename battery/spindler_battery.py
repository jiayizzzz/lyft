# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：spindler_battery.py
@Author  ：zjy
@Date    ：2023/6/19 19:35 
"""

from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
