#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:permission.py
@date:2017/11/15 17:54
"""
from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        depth = 2
        fields = "__all__"
