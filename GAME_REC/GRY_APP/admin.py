from django.contrib import admin
from .models import Game, Comment, Watchlist, Like, Image
# Register your models here.

admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Watchlist)
admin.site.register(Like)
admin.site.register(Image)
