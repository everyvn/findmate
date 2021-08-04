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

PURPOSE_CHOICE = [
    ('1', '창업'),
    ('2', '취미'),
    ('3', '사이드프로젝트'),
    ('4', '스터디'),
    ('5', 'ETC'),
]

class Team(BaseModel):
    name = models.CharField(max_length=20)
    short_description = models.TextField(max_length=1024)
    team_member = models.ManyToManyField(Profile)
    purpose = models.CharField(max_length=1, choices=PURPOSE_CHOICE, null=True, blank=True)
    logo = ProcessedImageField(upload_to = team_img_path,
                                   processors = [ResizeToFill(
                                       width=200, height=200, upscale=True)],
                                   format='JPEG',
                                   options={'quality':90},
                                   blank=True,
                                   null=True)
    team_detail = RichTextUploadingField(config_name='default', blank=True, null=True)

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


CAREER_LEVEL = [
    ('1', 'FRESHMAN'),
    ('2', '~2 YEARS'),
    ('3', '3~4 YEARS'),
    ('4', '5 YEARS~'),
    ('5', '10 YEARS~'),
]

class FindMember(BaseModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    essencial = models.CharField(max_length=200)
    plus = models.CharField(max_length=100)
    msg = RichTextUploadingField(config_name='default', blank=True, null=True)
    manpower = models.IntegerField()
    career = models.CharField(max_length=1, choices=CAREER_LEVEL)
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.title} of {self.team.name}"