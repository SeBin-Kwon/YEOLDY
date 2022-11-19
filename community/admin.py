from django.contrib import admin
from .models import QnA,Review,Photo
# Register your models here.
admin.site.register(QnA)
admin.site.register(Review)
admin.site.register(Photo)