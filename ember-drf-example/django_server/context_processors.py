from django_server.models import Category


def categories(request):
    return {'categories': Category.objects.all()}
