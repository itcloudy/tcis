#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/9 16:45
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import Project


@receiver(pre_save, sender=Project)
def save_project(sender, instance, *args, **kwargs):
    """

    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """



