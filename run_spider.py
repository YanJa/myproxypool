import os
import django
from myproxy.utils.fetch import crwal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proxypool.settings")
django.setup()


if __name__ == '__main__':
    crwal()
