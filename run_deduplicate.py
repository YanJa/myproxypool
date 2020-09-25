# coding=utf-8
import os
import django
from myproxy.utils.SortDt import sort

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proxypool.settings")
django.setup()


if __name__ == '__main__':
    sort()

