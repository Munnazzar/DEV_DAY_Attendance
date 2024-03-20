from mongoengine import Document, StringField
from mongoengine import *
import datetime

class DevDayAttendence(Document):
    comp_name = StringField(required=True)
    team_name = StringField(required=True)
    leader_name = StringField(required=True)
    leader_phone = StringField(required=True)
    leader_cnic = StringField(required=True)
    leader_email = StringField(required=True)
    p1_name = StringField(required=True)
    p1_phone = StringField(required=True)
    p1_cnic = StringField(required=True)
    p1_email = StringField(required=True)
    p2_name = StringField(required=True)
    p2_phone = StringField(required=True)
    p2_cnic = StringField(required=True)
    p2_email = StringField(required=True)
    reference_code = StringField(required=True)
    att_code = StringField(required=True)
