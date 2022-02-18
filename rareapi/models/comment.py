from django.db import models
class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment_post")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="comment_author")
    subject = models.CharField(max_length=200, default="subject")
    content = models.CharField(max_length=1000)
    created_on = models.DateField(auto_now_add=True)