from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

import pathlib

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "my page"
    my_context = {
        "page_title": my_title,
        "page_visits_count": page_qs.count(),
        "percent": page_qs.count() * 100 / qs.count(),
        "total_visits_count": qs.count()
    }
    
    html_response = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_response,my_context)

def my_old_home_page_view(request, *args, **kwargs):
    my_title = "my page"
    my_context = {
        "page_title": my_title
    }
    html_ = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>{page_title} Ariva Syam</h1>
        </body>
        </html>
    """.format(**my_context)
    # html_file_path = this_dir/ "home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)