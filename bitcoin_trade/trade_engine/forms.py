from trade_engine.models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("user", "api_key", "secret")
