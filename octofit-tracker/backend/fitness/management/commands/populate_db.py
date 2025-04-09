from django.core.management.base import BaseCommand
from fitness.models import UserProfile, ActivityLog
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with sample data for testing'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], int(settings.DATABASES['default']['PORT']))
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.fitness_userprofile.drop()
        db.fitness_activitylog.drop()

        # Clear existing data
        UserProfile.objects.all().delete()
        ActivityLog.objects.all().delete()

        # Create sample users
        users = [
            UserProfile(name='Alice', email='alice@example.com', points=100),
            UserProfile(name='Bob', email='bob@example.com', points=150),
            UserProfile(name='Charlie', email='charlie@example.com', points=200),
        ]
        UserProfile.objects.bulk_create(users)

        # Save users individually to ensure they are saved before being referenced
        for user in users:
            user.save()

        # Create sample activities
        activities = [
            ActivityLog(user=users[0], activity_type='Running', duration=30),
            ActivityLog(user=users[1], activity_type='Cycling', duration=60),
            ActivityLog(user=users[2], activity_type='Swimming', duration=45),
        ]
        ActivityLog.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))