from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, ResizeToFill
from django.db.models import Count
from django.conf import settings
from apps.core.models import BaseModel
from apps.member.models import Profile
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


def team_img_path(instance, filename):
    from random import choice
    import string
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ' '.join(arr)
    extension = filename.split('.')[-1]
    return 'team/{}.{}'.format(pid, extension)


class Team(BaseModel):
    name = models.CharField(max_length=64)
    short_description = models.TextField(max_length=1024)
    team_member = models.ManyToManyField(Profile)
    logo = ProcessedImageField(upload_to = team_img_path,
                                   processors = [ResizeToFill(
                                       width=200, height=200, upscale=True)],
                                   format='JPEG',
                                   options={'quality':90},
                                   blank=True,
                                   null=True)

    def __str__(self):
        return '%s' % self.name


REG_STATUS = [
    ('1', 'REGISTERED'),
    ('2', 'APPROVE'),
    ('3', 'REJECT'),
]


class RegisteredMember(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=REG_STATUS, null=True)
    msg = RichTextUploadingField(config_name='default', blank=True, null=True)

    def __str__(self):
        return f"{self.user} request for {self.team.name}"