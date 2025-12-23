from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=30)
    about_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading
    
class SocialLinks(models.Model):
    platform = models.CharField(max_length=25)
    link = models.URLField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Social Links"

    def __str__(self):
        return self.platform
