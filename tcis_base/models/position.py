#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:position.py
@date:2017/11/8 11:07
"""

from django.db import models


class Position(models.Model):
    """
    职位
    """
    name = models.CharField(max_length=20, verbose_name=u"职位", unique=True, null=False)
    description = models.TextField(verbose_name=u"职位描述", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'职位'
        verbose_name_plural = u'职位管理'