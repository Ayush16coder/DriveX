from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    # User Fields
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    # Profile Fields
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    mobile = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    
    aadhaar_number = forms.CharField(max_length=20, required=True)
    aadhaar_image = forms.FileField(required=True)
    
    # Owner Specific
    profile_photo = forms.FileField(required=False)
    payment_qr = forms.FileField(required=False)

    license_type = forms.ChoiceField(choices=UserProfile.LICENSE_CHOICES, required=True)
    license_number = forms.CharField(max_length=20, required=True)
    license_image = forms.FileField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email'] # Use email as username
        user.set_password(self.cleaned_data['password'])
        
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data['role'],
                mobile=self.cleaned_data['mobile'],
                address=self.cleaned_data['address'],
                dob=self.cleaned_data['dob'],
                aadhaar_number=self.cleaned_data['aadhaar_number'],
                aadhaar_image=self.cleaned_data['aadhaar_image'],
                license_type=self.cleaned_data['license_type'],
                license_number=self.cleaned_data['license_number'],
                license_image=self.cleaned_data['license_image'],
                profile_photo=self.cleaned_data.get('profile_photo'),
                payment_qr=self.cleaned_data.get('payment_qr')
            )
        return user
