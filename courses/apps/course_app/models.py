from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form_data):
        errors = []

        if len(form_data['name']) == 0:
            errors.append("Name is required")
        if len(form_data['comment']) == 0:
            errors.append('Comment is required')

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __str__(self):
        string_output = "name: {} comment: {}"

        return string_output.format(
            self.name,
            self.comment,
        )
