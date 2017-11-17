#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:index.py
@date:2017/11/8 13:55
"""
from django.shortcuts import render


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return render(request, 'index.html')
