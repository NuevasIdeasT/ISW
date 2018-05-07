from django.shortcuts import render

from django.http import HttpResponse


from django.db import connections
from django.db.utils import OperationalError



def index(request):

    return HttpResponse("Hello, world. You're at the polls index.");
