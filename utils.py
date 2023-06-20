# -*- coding: UTF-8 -*-
"""
@Project ：lyft 
@File    ：utils.py
@Author  ：zjy
@Date    ：2023/6/20 10:39 
"""


def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
