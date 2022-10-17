from django.contrib import admin
from .models import service,query,answer,contact
# Register your models here.
admin.site.register(service)
admin.site.register(query)
admin.site.register(answer)
admin.site.register(contact)