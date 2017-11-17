#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:login.py
@date:2017/11/11 14:52
"""

from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from ..serializers import UserSerializer
from ..models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    用户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(["post"], permission_classes=[permissions.AllowAny])
    def login(self, request):
        """
        用户登录
        :param request:
        :return:
        """

        if not request.user.is_authenticated:
            form = AuthenticationForm(request, request.data)
            if form.is_valid():
                user = form.user_cache
                login(request, user)
                return Response(UserSerializer(instance=user).data)
            return Response(u"用户名或密码错误",
                            status=status.HTTP_403_FORBIDDEN)
        return Response(UserSerializer(instance=request.user).data)

    @list_route(["get"], permission_classes=[permissions.AllowAny])
    def logout(self, request):
        """
        用户登出
        :param request:
        :return:
        """
        logout(request)

        return Response(u"退出成功", status.HTTP_200_OK)

    @list_route(["post"], permission_classes=[permissions.IsAdminUser])
    def reset_password(self, request):
        """
        用户登出
        :param request:
        :return:
        """

        post_data = request.data
        password = post_data.get("password", None)
        confirm_password = post_data.get("confirm_password", None)
        user_id = post_data.get("user_id", None)
        if password != confirm_password:
            return Response(u"密码不一致", status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.save()
        except Exception:
            return Response(u"用户不存在", status.HTTP_400_BAD_REQUEST)
        return Response(u"修改成功", status.HTTP_200_OK)

    @list_route(['post'], permission_classes=[permissions.IsAdminUser])
    def user_active(self, request):
        """
        用户是否有效操作
        :param request:
        :return:
        """
        user_ids = request.data.get("user_ids", [])
        try:
            is_active = request.data.is_active
            User.objects.filter(id__in=user_ids).update(is_active=is_active)
            return Response(u"修改成功", status.HTTP_200_OK)
        except Exception:
            return Response(u"缺少必须数据", status.HTTP_400_BAD_REQUEST)

