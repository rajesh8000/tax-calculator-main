from .models import Faqs, User
from django.contrib import admin
from .models import Post

admin.site.register(User)
admin.site.register(Post) #Post in Admin Panel
admin.site.register(Faqs) #Faqs in Admin Panel

