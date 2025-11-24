from django.test import TestCasefrom django.test import TestCase

























        self.assertEqual(Leaderboard.objects.count(), 1)    def test_leaderboard(self):        self.assertEqual(Workout.objects.count(), 1)    def test_workout(self):        self.assertEqual(Activity.objects.count(), 1)    def test_activity(self):        self.assertEqual(Team.objects.count(), 1)    def test_team(self):        self.assertEqual(User.objects.count(), 1)    def test_user(self):        Leaderboard.objects.create(team=marvel, points=100)        Workout.objects.create(user=tony, workout='Ironman training')        Activity.objects.create(user=tony, type='run', distance=5)        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)        marvel = Team.objects.create(name='Team Marvel')    def setUp(self):class BasicModelTest(TestCase):from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', distance=10)
        self.assertEqual(activity.type, 'run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        workout = Workout.objects.create(user=user, workout='Pushups')
        self.assertEqual(workout.workout, 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(leaderboard.points, 50)
