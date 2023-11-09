from django.http import HttpResponse, HttpResponseServerError


def list_stories(request):
    """Method for show all story."""
    return HttpResponse('Тут тебе вернутся все сторьки, что хранятся в базе!')

def add_story(request):
    """Method for adding story."""
    success = True
    if success:
        return HttpResponse('Добавлено!')

    else:
        return HttpResponseServerError


def get_story(request):
    """Method for return one story."""
    story_id = request.GET.get('story_id', 1)
    output = 'Сториз {0}'.format(story_id)
    return HttpResponse(output)