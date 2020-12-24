from django.test import TestCase
import re
# Create your tests here.
account="13312345678"

if (re.match(r"^1[3456789]\d{9}$", account)):
    print(222)