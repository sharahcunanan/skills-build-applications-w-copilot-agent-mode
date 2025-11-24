from rest_framework import serializersfrom rest_framework import serializers



































        fields = ['_id', 'team', 'team_id', 'points']        model = Leaderboard    class Meta:    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)    team = TeamSerializer(read_only=True)class LeaderboardSerializer(serializers.ModelSerializer):        fields = ['_id', 'user', 'user_id', 'workout']        model = Workout    class Meta:    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)    user = UserSerializer(read_only=True)class WorkoutSerializer(serializers.ModelSerializer):        fields = ['_id', 'user', 'user_id', 'type', 'distance']        model = Activity    class Meta:    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)    user = UserSerializer(read_only=True)class ActivitySerializer(serializers.ModelSerializer):        fields = ['_id', 'name', 'email', 'team', 'team_id']        model = User    class Meta:    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)    team = TeamSerializer(read_only=True)class UserSerializer(serializers.ModelSerializer):        fields = ['_id', 'name']        model = Team    class Meta:class TeamSerializer(serializers.ModelSerializer):from .models import User, Team, Activity, Workout, Leaderboardfrom .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name']

class UserSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)
    class Meta:
        model = User
        fields = ['_id', 'name', 'email', 'team', 'team_id']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_id', 'type', 'distance']

class WorkoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)
    class Meta:
        model = Workout
        fields = ['_id', 'user', 'user_id', 'workout']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True)
    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'team_id', 'points']
