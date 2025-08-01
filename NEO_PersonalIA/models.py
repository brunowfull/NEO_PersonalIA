from django.db import models

class UserInteraction(models.Model):
    user_name = models.CharField(max_length=100)
    interaction_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.user_name} - {self.interaction_time}'
