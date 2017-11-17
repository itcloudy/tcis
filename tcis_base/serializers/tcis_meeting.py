#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:tcis_meeting.py
@date:2017/11/15 11:14
"""
from rest_framework import serializers
from ..models import TcisMeeting


class TcisMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcisMeeting
        depth = 2

