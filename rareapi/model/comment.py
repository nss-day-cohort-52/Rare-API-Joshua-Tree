from tkinter import CASCADE
from django.db import models

class Comment(models.Model):
    post = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="comment_post")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="comment_author")
    content = models.CharField()
    created_on = models.DateField(auto_now_add=True)