import django
from . import models
from rgbaloes.settings import BASE_DIR
from os import path


def main(request):
    template = django.template.loader.get_template(
        path.join(
            BASE_DIR,
            'rgbaloes',
            'static',
            'html',
            'main.html'))
    return django.http.HttpResponse(
        template.render(request))