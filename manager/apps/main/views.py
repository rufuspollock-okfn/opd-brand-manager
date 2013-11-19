from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    r"""
    """

    template_name = 'main/home.jade'

    def get(self, request):
        return render(request, self.template_name)
