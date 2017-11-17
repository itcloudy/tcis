#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:test_case.py
@date:2017/11/15 13:06
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import ProjectTestCase


@receiver(pre_save, sender=ProjectTestCase)
def save_test_case(sender, instance, *args, **kwargs):
    """

    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    if instance and instance.test and instance.test.type:
        instance.type = instance.test.type
