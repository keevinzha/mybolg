#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/20 09:14
# @Author  : wgPython
# @File    : mysql_setting.py
# @Software: PyCharm
# @Desc    :
"""

"""

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'Gky@981021',
    },
}
