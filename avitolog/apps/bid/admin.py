from django.contrib import admin

# Register your models here.
from .models import Bid, Client, Executor

admin.site.register(Bid)
admin.site.register(Executor)
admin.site.register(Client)

