from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


@receiver(post_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    # print(sender.username)
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()


class Post(models.Model):
    create_at = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"post-{self.id}: {self.title}"


class Comment(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment-{self.id}: {self.body[:30]}"
