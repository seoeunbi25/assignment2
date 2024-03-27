from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="images/", null=True)
    
    def __str__(self):
        return self.title