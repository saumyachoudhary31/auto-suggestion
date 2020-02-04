from django.contrib import admin

# Register your models here.

from .models import MyModel
from .forms import MyModelForm

class BookAdmin(admin.ModelAdmin):
	list_display = [
					"color"
				]
	
	
	form = MyModelForm

admin.site.register(MyModel, BookAdmin)
