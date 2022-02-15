from django.db import models

<<<<<<< HEAD

class Tags(models.Model):
    label = models.CharField(max_length=200)
    
=======
class Tag(models.Model):
    label = models.CharField(max_length=50)
>>>>>>> main
