from __future__ import unicode_literals
from django.db import models
#how do we pull our user table in here?
from ..login_app.models import User

# Create your models here.
class SecretManager(models.Manager):
    def createSecret(self, form_data, user):
        secret = Secret.objects.create(
            content = form_data['content'],
            user = user,
        )

        return secret

class Secret(models.Model):
    #what are the attributes a secret has?
    content = models.TextField()
    #Related Name= a secret has a user and a user has secrets
    user = models.ForeignKey(User, related_name="secrets")
    #likes is the relationship between the user and the secret
    #a secret can be liked by many users, and a secret can have many likes
    liked_by = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SecretManager()