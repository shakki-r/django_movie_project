from django.contrib import admin
from .models import Genres,Movies,Review
# Register your models here.


admin.site.register(Genres)




class CreateMovie(admin.ModelAdmin):
    list_display = ['title','slug','added_user','release_date','actor','genres']
    prepopulated_fields = {'slug': ('title',)}
    list_editable=['actor']


admin.site.register(Movies,CreateMovie)


admin.site.register(Review)