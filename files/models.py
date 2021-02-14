from django.db import models

class File(models.Model):
    title = models.CharField(max_length=120)
    pdf = models.FileField(upload_to="pdfs/")
  

    class Meta:
        ordering = ["title"]
    
    def __str__(self):
        return f"{self.title}"
    
