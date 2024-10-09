from django import forms
from django.forms import ModelForm
from .models import List_model

class UserTodoList(ModelForm):
    class Meta:
        model = List_model
        fields = ["day_tasks", "prioritet", "completed_task",]# "date_start"], "date_finish"]

    def clean(self):
        cleaned_data = super().clean()
        #date_start = cleaned_data.get("date_start")
        #date_finish = cleaned_data.get("date_finish")
        print(cleaned_data)
        return cleaned_data
