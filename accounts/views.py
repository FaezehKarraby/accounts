from django.views.generic import CreateView
from accounts.forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
