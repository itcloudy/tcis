#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_case_history.py
@date:2017/11/15 15:10
"""
from rest_framework import serializers
from ..models import ProjectTestCaseHistory


class ProjectTestCaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTestCaseHistory
        depth = 1
        fields = "__all__"
