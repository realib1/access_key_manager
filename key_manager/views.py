from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import AccessKey
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "base.html")

# Create your views here.
class KeyListview(LoginRequiredMixin, ListView):
    model = AccessKey
    template_name = 'keymanager/keylist.html'

    def get_queryset(self):
        return AccessKey.objects.filter(user=self.request.user)


class KeyDetailView(LoginRequiredMixin, DetailView):
    model = AccessKey
    template_name = 'keymanager/key_details.html.html'
