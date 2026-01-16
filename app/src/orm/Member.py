from tina4_python.ORM import ORM
from tina4_python.ORM import IntegerField, StringField, DateTimeField

import datetime

class Member(ORM):
    id = IntegerField(primary_key=True, auto_increment=True)

