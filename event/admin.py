from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	def save_model(self,request,instance,form,change):
		user=request.user
		instance=form.save(commit=false)
		if not change or not instance.author:
			instance.author=user.first_name+" "+user.last_name
		form.save_m2m()
		return instance

admin.site.register(Event, prepopulated_fields = {"slug": ("title",),})
