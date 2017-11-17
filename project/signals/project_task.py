#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/9 16:46
"""

from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import ProjectTask


@receiver(pre_save, sender=ProjectTask)
def save_project_task(sender, instance, *args, **kwargs):
    """

    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
