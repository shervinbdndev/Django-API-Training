from django.shortcuts import render
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse







class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request=request,
            template_name='index/index.html',
            context={
                'title': 'خوش آمدید',   
            },
        )