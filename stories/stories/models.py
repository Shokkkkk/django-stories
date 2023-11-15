from django.db import models

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

class StoryImages(models.Model):
    """Model for stories images."""
    story = models.ForeignKey(Story, on_delete=models.PROTECT)
    image_1 = models.ImageField()
    image_2 = models.ImageField()
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    image_6 = models.ImageField()
    image_7 = models.ImageField()
