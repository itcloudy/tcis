#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/9 16:34
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import ProjectMember


@receiver(pre_save, sender=ProjectMember)
def save_project_member(sender, instance, *args, **kwargs):
    """

    :param sender:
    :param instance:
    :param args:
    :param kwargs:
    :return:
    """
    if instance and instance.member and instance.member.position:
        instance.position = instance.member.position


