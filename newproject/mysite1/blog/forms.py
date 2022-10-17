from django import forms
from . models import service,query

class edit_service(forms.ModelForm):
    class Meta:
        model = service
        fields = ('service_name','service_provider','service_contact','service_cost')

class edit_query(forms.ModelForm):
    class Meta:
        model = query
        fields = ('query_category','query_question')