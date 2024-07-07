from django.contrib import admin
from .models import card_details,student,courses,teacher
# Register your models here.
admin.site.register(card_details)
admin.site.register(student)
admin.site.register(courses)
admin.site.register(teacher)