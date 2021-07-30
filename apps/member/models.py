from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.db.models import Count
from django.conf import settings
from apps.core.models import BaseModel

# Create your models here.


def mem_img_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ' '.join(arr)
    extension = filename.split('.')[-1]
    return 'member/profile/{}.{}'.format(pid, extension)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True)
    picture = ProcessedImageField(upload_to = mem_img_path,
                                processors=[ResizeToFit(width=150, upscale=False)],
                                format='JPEG',
                                options={'quality':90},
                                blank=True,
                                null=True,
                                )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_count = User.objects.count()
        print(user_count)
        Profile.objects.create(user=instance, name="Mate %s" %(user_count))


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()