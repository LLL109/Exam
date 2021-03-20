from django.core.cache import cache
from django.test import TestCase

# Create your tests here.
quiz_id=1
question_index = 1
cache_key = f"quiz_id_{quiz_id}:question_index"
cache.set(cache_key,[1,2,3,4,5,6],10)
print(cache.get(cache_key))