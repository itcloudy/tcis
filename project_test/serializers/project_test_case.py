#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_case.py
@date:2017/11/15 15:10
"""
from rest_framework import serializers
from ..models import ProjectTestCase


class ProjectTestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTestCase
        depth = 1
        fields = "__all__"