from django.db import models


class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    login_user = models.CharField(default=None, max_length=255, unique=True)
    nome_user = models.CharField(default=None, max_length=255)
    sobrenome_user = models.CharField(default=None, max_length=255)
    email_user = models.EmailField(default=None, max_length=255, unique=True)
    password_user = models.CharField(default=None, max_length=255)
    active_user = models.BooleanField(default=True)

    def __str__(self):
        return self.login_user
