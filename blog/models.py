# blog/models.py
from django.db import models
from django.contrib.auth.models import User

# (Your existing Post model goes here)
class Post(models.Model):
    # ... (content remains the same)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    STATUS_CHOICES = ((0, 'Draft'), (1, 'Publish'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# NEW Image Model
class PostImage(models.Model):
    # Link back to the Post. If the Post is deleted, all its images are also deleted (CASCADE).
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    
    # Field to handle the uploaded image file. 
    # Uploads will go into MEDIA_ROOT/blog/
    image = models.ImageField(upload_to='blog/')
    
    # Optional field to provide a description for accessibility/SEO
    caption = models.CharField(max_length=255, blank=True)
    
    # Optional field to order the images (e.g., primary image first)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.post.title}"
