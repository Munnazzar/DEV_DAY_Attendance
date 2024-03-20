from django.db import models



from mongoengine import Document,fields, StringField, EmailField, BooleanField,ReferenceField

class Participants(Document):
    comp_name = fields.StringField(required=True)
    team_name = fields.StringField(required=True)
    leader_name = fields.StringField(required=True)
    leader_phone_number = fields.StringField(required=True)
    leader_cnic = fields.StringField(required=True)
    leader_email = fields.EmailField(required=True)
    p1_name = fields.StringField(required=True)
    p1_phone_number = fields.StringField(required=True)
    p1_cnic = fields.StringField(required=True)
    p1_email =fields.EmailField(required=True)
    p2_name = fields.StringField()
    p2_phone_number = fields.StringField()
    p2_cnic = fields.StringField()
    p2_email = fields.EmailField()
    reference_code = fields.StringField(required=True)
    attendance_code = fields.StringField(required=True)


class Attendance(Document):
    participant =fields.ReferenceField(Participants)
    status = fields.BooleanField(required=True)
