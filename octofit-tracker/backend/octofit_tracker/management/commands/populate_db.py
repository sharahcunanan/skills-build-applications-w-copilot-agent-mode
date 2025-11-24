from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Populating octofit_db with test data...'))

        # Connect to MongoDB directly for index and collection management
        client = MongoClient(host='localhost', port=27017)
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboards.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', ASCENDING)], unique=True)

        # Use Django ORM for data insertion
        Team.objects.all().delete()
        User.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        Activity.objects.create(user=tony, type='run', distance=5)
        Activity.objects.create(user=steve, type='cycle', distance=20)
        Activity.objects.create(user=bruce, type='swim', distance=2)
        Activity.objects.create(user=clark, type='fly', distance=100)

        Workout.objects.create(user=tony, workout='Ironman training')
        Workout.objects.create(user=steve, workout='Shield practice')
        Workout.objects.create(user=bruce, workout='Batcave workout')
        Workout.objects.create(user=clark, workout='Kryptonian strength')

        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated successfully.'))
