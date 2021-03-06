from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.db.models import Count
from django.conf import settings
from apps.core.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

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
    name = models.CharField(max_length=45, blank=True)
    short_desc = models.CharField(max_length=200, blank=True, null=True)
    options = models.CharField(max_length=200, blank=True, null=True)
    picture = ProcessedImageField(upload_to = mem_img_path,
                                processors=[ResizeToFit(width=150, upscale=False)],
                                format='JPEG',
                                options={'quality':90},
                                blank=True,
                                null=True,
                                )
    detail = RichTextUploadingField(config_name='default', blank=True, null=True)
    skills = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url
    
    @property
    def longitude(self):
        return self.point[0]

    @property
    def latitude(self):
        return self.point[1]

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_count = User.objects.count()
        print(user_count)
        Profile.objects.create(user=instance, name="Mate %s" %(user_count))


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CVCategory(BaseModel):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    def __str__(self):
        return f"{self.title}"


POSITION = [
    ('1', '??????'),
    ('2', '??????'),
    ('3', '??????'),
    ('4', '??????'),
    ('5', '??????'),
    ('6', '??????'),
    ('7', '?????? ??????'),
    ('8', '??????'),
]

EDU_SELECT = [
    ('1', '??????'),
    ('2', '????????????'),
    ('3', '??????'),
    ('4', '??????'),
    ('5', '??????'),
]

class CVItem(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(CVCategory, on_delete=models.CASCADE, default=None)
    # Company
    company = models.CharField(max_length=100, blank=True, null=True)
    company_start_date = models.DateField(blank=True, null=True)
    company_end_date = models.DateField(blank=True, null=True)
    company_career = models.CharField(max_length=100, choices=POSITION, blank=True, null=True)
    # Education
    education = models.CharField(max_length=100, blank=True, null=True)
    education_status = models.CharField(max_length=100, choices=EDU_SELECT, blank=True, null=True)
    education_major = models.CharField(max_length=100, blank=True, null=True)
    # Projects
    projects = models.CharField(max_length=100, blank=True, null=True)
    projects_date = models.DateField(blank=True, null=True)
    projects_desc = models.TextField(blank=True, null=True)
    # Self intro
    intro = models.TextField(blank=True, null=True)
    # license
    license_list = models.CharField(max_length=100, blank=True, null=True)
    license_list_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.category} of {self.profile.name}"
