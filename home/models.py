from django.db import models



class ContactMessage(models.Model):

    name =  models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
