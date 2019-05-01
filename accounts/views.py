from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

class SignupView(generic.CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')
