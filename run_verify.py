# coding=utf-8
import os
import django

from myproxy.utils.VerifyProxy import verify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proxypool.settings")
django.setup()


if __name__ == '__main__':
    verify()
