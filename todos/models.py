from django.db import models

from helpers.models import TrackingModels
from authentication.models import User

class Todo(TrackingModels):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_finished = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

