#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:parent_tree.py
@date:2017/11/11 11:00
"""
from django.db.models import Max, F, Value, Count, Q
from django.core.exceptions import ObjectDoesNotExist


def parent_tree(save_obj, object_class):
    if not(save_obj and object_class):
        return save_obj

    if not save_obj.id:
        # 上级项目是否存在
        if save_obj.parent:
            parent = save_obj.parent
            # 存在上级项目，由于是新增，故左右差为1，插入的查为2
            diff = 2
            object_class.objects.filter(parent_right__gt=parent.parent_right). \
                exclude(id=parent.id).update(parent_left=F('parent_left') + diff)

            object_class.objects.filter(parent_right__gte=parent.parent_right).\
                update(parent_right=F('parent_right') + diff)
            # 重新获得上级项目，得到最新的右值
            parent = object_class.objects.get(id=save_obj.parent.id)
            save_obj.parent_left = parent.parent_right - 2
            save_obj.parent_right = parent.parent_right - 1
        else:
            # 不存在上级项目，直接在系统中找最大的
            obj = object_class.objects.all().order_by('-parent_right')
            obj = obj and obj[0]
            if obj:
                save_obj.parent_left = obj.parent_right + 1
                save_obj.parent_right = obj.parent_right + 2
            else:
                save_obj.parent_left = 0
                save_obj.parent_right = 1
    else:
        # 更新，判断原有parent是否存在
        try:
            old_obj = object_class.objects.get(id=save_obj.id)
            # 修改，获得当前项目的左右差值
            diff = old_obj.parent_right - old_obj.parent_left + 1
            # 上级项目都存在
            if old_obj.parent and save_obj.parent:
                # 上级项目修改
                if old_obj.parent.id != save_obj.parent.id:
                    parent = save_obj.parent
                    object_class.objects.filter(parent_right__gt=parent.parent_right). \
                        exclude(id=parent.id).update(parent_left=F('parent_left') + diff)
                    object_class.objects.filter(parent_right__gte=parent.parent_right).update(
                        parent_right=F('parent_right') + diff)
                    # 获得上级项目的所有子项目最大的parent_right
                    max_child = object_class.objects.\
                        filter(parent_left__gt=parent.parent_left, parent_right__lt=parent.parent_right).\
                        order_by("-parent_right")
                    max_child = max_child and max_child[0]
                    # 变更的上级项目存在子项目
                    if max_child:
                        object_class.objects.\
                            filter(parent_left__gte=save_obj.parent_left, parent_right__lte=save_obj.parent_right).\
                            update(parent_right=F('parent_right') + max_child.parent_right,
                                   parent_left=F('parent_left') + max_child.parent_right)
                    else:
                        object_class.objects. \
                            filter(parent_left__gte=save_obj.parent_left, parent_right__lte=save_obj.parent_right). \
                            update(parent_right=F('parent_right') + parent.parent_right,
                                   parent_left=F('parent_left') + parent.parent_right)
            else:
                # 原有上级项目存在，修改时不存在
                if old_obj.parent:
                    # 直接在系统中找最大的
                    max_obj = object_class.objects.order_by('-parent_right')
                    max_obj = max_obj and max_obj[0]
                    if max_obj:
                        object_class.objects. \
                            filter(parent_left__gt=save_obj.parent_left, parent_right__lt=save_obj.parent_right). \
                            update(parent_right=F('parent_right') + max_obj.parent_right - diff + 1,
                                   parent_left=F('parent_left') + max_obj.parent_right - diff + 1)
                        save_obj.parent_left = max_obj.parent_right + 1
                        save_obj.parent_right = max_obj.parent_right + diff + 1
                # 原项目上级不存在，修改时存在
                if save_obj.parent:
                    object_class.objects.filter(parent_right__gt=save_obj.parent.parent_right). \
                        exclude(id=save_obj.parent.id).update(parent_left=F('parent_left') + save_obj.parent_right)
                    object_class.objects.filter(parent_right__gte=save_obj.parent.parent_right).update(
                        parent_right=F('parent_right') + save_obj.parent_right)

                    max_child = object_class.objects. \
                        filter(parent_left__gt=save_obj.parent.parent_left, parent_right__lt=save_obj.parent.parent_right). \
                        order_by("-parent_right")
                    max_child = max_child and max_child[0]
                    # 变更的上级项目存在子项目
                    if max_child:
                        object_class.objects. \
                            filter(parent_left__gt=save_obj.parent_left, parent_right__lt=save_obj.parent_right). \
                            update(parent_right=F('parent_right') + max_child.parent_right - diff + 1,
                                   parent_left=F('parent_left') + max_child.parent_right - diff + 1)
                        save_obj.parent_left = max_child.parent_right + 1
                        save_obj.parent_right = max_child.parent_right + diff + 1

        except ObjectDoesNotExist:
            pass
    return save_obj
