from django.contrib import admin
from .models import Book, Department, Employee, ImageCollection, User


admin.site.register(User)
admin.site.register(Employee)
admin.site.register(ImageCollection )
admin.site.register(Department )
admin.site.register(Book )
