# from django.db.models import fields
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'height', 'weight', 'goal_weight']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'weight', 'goal_weight']
        