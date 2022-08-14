from django.db import models

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome_user = models.CharField(max_length=255)
    email_user = models.EmailField(default=None, max_length=255)

    def __str__(self):
        return self.nome_user