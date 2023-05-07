from django.db import models

class Goal(models.Model):
    goal = models.CharField(max_length=300)

    def __str__(self):
        return self.goal
