from django.db import models


class Usuario(models.Model):
    login = models.CharField(default=None, max_length=255, unique=True)
    nome = models.CharField(default=None, max_length=255)
    sobrenome = models.CharField(default=None, max_length=255)
    email = models.EmailField(default=None, max_length=255, unique=True)
    password = models.CharField(default=None, max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.login
