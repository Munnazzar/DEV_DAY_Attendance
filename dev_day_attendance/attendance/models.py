from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member_1st(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    cnic = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Member_2nd(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    cnic = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.name
class TeamLeader(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    cnic = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team} - {self.date} - Present: {self.is_present}"
