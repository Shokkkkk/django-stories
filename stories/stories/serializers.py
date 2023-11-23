from rest_framework import serializers

from .models import Story


class UploadedFileSerializer:
    pass


class StorySerializer(serializers.ModelSerializer):
    """Story serializer."""

    # images = serializers.ImageField(many=True)

    class Meta:
        model = Story
        fields = ['id', 'preview_image', 'preview_text', 'story_header',]