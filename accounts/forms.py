from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


'''class CreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user')
            super(CreateForm, self).__init__(*args, **kwargs)

        def clean_title(self):
            title = self.cleaned_data['title']
            if Profile.objects.filter(user=self.user, title=title).exists():
                raise forms.ValidationError('same title')
            return title
'''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
