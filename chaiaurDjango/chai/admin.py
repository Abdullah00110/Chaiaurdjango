from django.contrib import admin
from .models import ChaiVariety, Contact

@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname' , 'lastname' , 'email' ,  'subject' , 'message'  )
    search_fields = ('firstname' , 'lastname' ,  'email' , 'subject'   )
    # list_display_links = ('firstname' , 'lastname' ,  'email' )

# Register your models here.
admin.site.register(ChaiVariety)
# admin.site.register(Contact , ContactAdmin)