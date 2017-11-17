#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:server.py
@date:2017/11/10 10:07
"""
from django.db import models


class Server(models.Model):
    """
    服务器管理
    """
    name = models.CharField(max_length=20, verbose_name=u"服务器名称")
    ip = models.IPAddressField(verbose_name=u"服务器IP地址")
    system = models.CharField(max_length=20, verbose_name=u"服务器系统")