from django.contrib import admin
from .models import Book, StudentExtra, IssuedBook

# Register your models here.

# Admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
	pass  # No custom configuration, using default admin settings

# Registering the Book model with the Django admin site
admin.site.register(Book, BookAdmin)


# Admin configuration for the StudentExtra model
class StudentExtraAdmin(admin.ModelAdmin):
	pass  # No custom configuration, using default admin settings

# Registering the StudentExtra model with the Django admin site
admin.site.register(StudentExtra, StudentExtraAdmin)


# Admin configuration for the IssuedBook model
class IssuedBookAdmin(admin.ModelAdmin):
	pass  # No custom configuration, using default admin settings

# Registering the IssuedBook model with the Django admin site
admin.site.register(IssuedBook, IssuedBookAdmin)