from django.db import models

# Create your models here.
class periodicMessage(models.Model):
    message = models.CharField(max_length=200, blank=True)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'message {}'.format(self.message)
