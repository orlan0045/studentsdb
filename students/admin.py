from django.contrib import admin
from .models import Student, Group, Journal, Exam
# Register your models here.

admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
