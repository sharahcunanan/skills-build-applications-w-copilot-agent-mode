from django.contrib import adminfrom django.contrib import admin








admin.site.register(Leaderboard)admin.site.register(Workout)admin.site.register(Activity)admin.site.register(Team)admin.site.register(User)from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)
