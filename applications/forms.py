from django import forms
from .models import JobApplication,Book


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'role', 'status', 'resume']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages'] # These must match your model

    
    def clean_company(self):
        company = self.cleaned_data['company']
        if len(company) < 3:
            raise forms.ValidationError("Company name is too short")
        return company

    def clean_role(self):
        role = self.cleaned_data['role']
        if any(char.isdigit() for char in role):
            raise forms.ValidationError("Role cannot contain numbers")
        return role