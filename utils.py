"""
Utils for test environment and data preparation
Last updates: 9/24/18
author: Alex Bogdanovich
"""
# -*- coding: utf-8 -*-

import pandas as pd


def get_excel_data(file_name='tests/test_data.xlsx', sheet_name='Sheet1'):
    """read excel file via pandas lib and return data"""

    test_data = []
    data = pd.read_excel(file_name, sheet_name=sheet_name)
    for i in data.index:
        test_data.append((data['id'][i], data['name'][i], data['email'][i]))
    return test_data


comments_data = get_excel_data()
