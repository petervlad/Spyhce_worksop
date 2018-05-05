from django.db import models

# Create your models here.


class TaskItem(models.Model):
	title = models.CharField(max_length=255)
	done = models.BooleanField(default=False)
	due_date = models.DateField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	owner = models.ForeignKey("auth.user", models.CASCADE,null=True, blank=True)