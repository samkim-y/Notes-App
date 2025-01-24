from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #autonowadd automatically populates when creating new instance
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="notes") #foreignkey links user to data that belongs to the user
                                                                                      #ondelete automatically deletes all user's notes if user is deleted
                                                                                      #related name = field name to add to user to reference their notes (user.notes)  
    def __str__(self):
        return self.title


    