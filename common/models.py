from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True

class MediaFile(BaseModel):
    media_type = models.CharField(max_length=50, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        ('other', 'Other')
    ], default='other', verbose_name="Media Type")

    file = models.FileField(upload_to="files")
    news = models.ManyToManyField(
        'news.News',
        related_name='media_files',
        blank=True,
        verbose_name="Related News"
    )

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _("Media File")
        verbose_name_plural = _("Media Files")