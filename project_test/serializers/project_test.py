#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test.py
@date:2017/11/15 13:19
"""

from rest_framework import serializers
from ..models import ProjectTest


class ProjectTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTest
        depth = 1
        fields = "__all__"
