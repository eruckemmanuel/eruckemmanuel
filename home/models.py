from django.db import models



class ContactMessage(models.Model):

    name =  models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class Project(models.Model):

    name = models.CharField(max_length=1000)
    description = models.TextField()
    date = models.DateField(auto_now=False)
    url = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(upload_to='projects/images/')


    def __str__(self):
        return self.name
