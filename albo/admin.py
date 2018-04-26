from django.contrib import admin
from .models import Team, Competition, User, Player, Role, Bonus

# Register your models here.

admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(User)
admin.site.register(Player)
admin.site.register(Role)
admin.site.register(Bonus)