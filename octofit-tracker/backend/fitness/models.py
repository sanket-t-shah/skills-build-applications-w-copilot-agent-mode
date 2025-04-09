from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ActivityLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.activity_type} on {self.date}"
