from django.db import models


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30, blank=True, null=False)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    starttime = models.TimeField()
    endtime = models.TimeField()
    is_interviewer = models.IntegerField(default=0)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['firstname', 'middlename', 'lastname'], name='unique_name')
        ]


