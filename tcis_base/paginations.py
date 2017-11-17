#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:paginations.py
@date:2017/11/9 11:15
"""
from rest_framework import pagination


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 10000
    page_size_query_param = 'page_size'
