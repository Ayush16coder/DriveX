from django import forms
from django.contrib.auth.models import User
from DriveX.models import UserProfile

class RenterProfileForm(forms.ModelForm):
    # User Fields
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = UserProfile
        fields = ['mobile', 'address', 'profile_photo', 'payment_qr']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(RenterProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super(RenterProfileForm, self).save(commit=False)
        if commit:
            profile.save()
            # Update User fields
            user = profile.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.save()
        return profile
