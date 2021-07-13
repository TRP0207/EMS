from django import forms
from .models import Employee, Leave


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_staff', 'is_active',
                   'date_joined']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(ProfileForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
        exclude = ['is_approved']


class LeaveApprovalForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'
