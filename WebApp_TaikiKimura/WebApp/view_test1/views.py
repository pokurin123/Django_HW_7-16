from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = {
        "message":"こんにちは",
        "sample":"TemplateViewサンプル"
    }
    return render(request, 'view_test1/member_list.html',text)