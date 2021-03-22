import time

from django.core.cache import cache
from django.test import TestCase

# Create your tests here.
tuple_time = time.strptime("2020/12/16 14:46:40", "%Y/%m/%d %H:%M:%S")
print(tuple_time)
print(time.mktime(tuple_time))