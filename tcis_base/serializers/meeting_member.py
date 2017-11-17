#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:meeting_member.py
@date:2017/11/15 11:16
"""
from rest_framework import serializers
from ..models import MeetingMember
from .user import UserSerializer
from .tcis_meeting import TcisMeetingSerializer


class MeetingMemberSerializer(serializers.ModelSerializer):
    meeting = TcisMeetingSerializer()
    user = UserSerializer()

    class Meta:
        model = MeetingMember
        depth = 2
