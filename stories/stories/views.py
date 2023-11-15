from django.http import HttpResponse, HttpResponseServerError

from .models import Story


def list_stories(request):
    """Method for show all story."""
    story = Story.objects.all()
    if not story:
        HttpResponse('You haven\'t stories.')
    return HttpResponse(story)

def add_story(request):
    """Method for adding story."""
    if request.POST:
        story = Story()
        story.preview_image = request.POST.get('preview_image')
        story.preview_text = request.POST.get('preview_text')
        story.story_header = request.POST.get('story_header')
        story.story_description = request.POST.get('story_description')
        story.stories_images = request.POST.get('stories_images')
        story.have_story_button = request.POST.get('have_story_button')
        story.link_story_button = request.POST.get('link_story_button')
        story.save()
        return HttpResponse('Added!')

    else:
        return HttpResponseServerError


def get_story(request):
    """Method for return one story."""
    story_id = request.GET.get('story_id', 1)
    if not story_id:
        return HttpResponseServerError('We don\'t have story on this id.')

    story = Story.objects.get(id=story_id)
    if not story:
        return HttpResponseServerError('We don\'t have story on this id.')

    return HttpResponse(story)