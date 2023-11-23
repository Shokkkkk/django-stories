from django.db import models
from django.utils import timezone


class StoryManager(models.Manager):
    """Custom manager for stories."""

    def published(self) -> models.query.QuerySet['Story']:
        """
        Filter out unpublished stories.
        Story is considered published if it has a published_at date set,
        and it's less than current date
        """

        return self.filter(published_at__isnull=False, published_at__lt=timezone.now())

class Story(models.Model):
    """Model for stories."""
    preview_image = models.ImageField()
    preview_text = models.CharField(max_length=50)
    story_header = models.CharField(max_length=250)
    story_description = models.CharField(max_length=200, default='')
    have_story_button = models.BooleanField(default=False)
    link_story_button = models.URLField(default='')

    objects = models.Manager()

    class Meta:
        verbose_name = 'story'
        verbose_name_plural = 'stories'


class StoryUploadedFiles(models.Model):
    """Stories images mtm through model."""
    story = models.ForeignKey('Story', models.CASCADE)
    # uploaded_file = models.ForeignKey('files.UploadedFile', models.CASCADE)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    image_6 = models.ImageField()
    image_7 = models.ImageField()

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['story', 'uploaded_file'],
        #         name='unique_story_uploaded_file',
        #     ),
        # ]
        verbose_name = 'story image'
        verbose_name_plural = 'story image'
        ordering = ('-id',)
