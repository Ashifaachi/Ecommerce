from django.contrib import admin

# Register your models here.
from .models import Register,State,District,Account

# Register your models here.
admin.site.register(Register),
# admin.site.register(Login),
# admin.site.register(Logout),

admin.site.register(State),
admin.site.register(District),
admin.site.register(Account),