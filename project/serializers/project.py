#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/9 10:20
"""
from rest_framework import serializers
from ..models import Project
from tcis_base.serializers import UserSerializer
import datetime


class ProjectSerializer(serializers.ModelSerializer):
    manager = UserSerializer()
    percentage = serializers.SerializerMethodField(read_only=True)
    parent_left = serializers.IntegerField(read_only=True)
    parent_right = serializers.IntegerField(read_only=True)


    def get_percentage(self, obj):
        """
        获得时间进度百分比
        :param obj:
        :return:
        """
        percentage = 0
        if obj.start_date and obj.end_date:
            all_days = (obj.end_date - obj.start_date).days
            past_days = (datetime.date.today() - obj.start_date).days
            percentage = int(past_days * 100 / all_days)
        return percentage

    class Meta:
        model = Project
        depth = 2
        fields = "__all__"


