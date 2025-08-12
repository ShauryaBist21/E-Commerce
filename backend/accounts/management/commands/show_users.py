from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Show user statistics and list all users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--recent',
            action='store_true',
            help='Show only recent users (last 10)',
        )

    def handle(self, *args, **options):
        total_users = User.objects.count()
        today_users = User.objects.filter(date_joined__date=date.today()).count()
        this_week_users = User.objects.filter(
            date_joined__gte=timezone.now() - timezone.timedelta(days=7)
        ).count()

        self.stdout.write(
            self.style.SUCCESS(f'=== USER STATISTICS ===')
        )
        self.stdout.write(f'Total users: {total_users}')
        self.stdout.write(f'Users created today: {today_users}')
        self.stdout.write(f'Users created this week: {this_week_users}')
        self.stdout.write('')

        if options['recent']:
            users = User.objects.order_by('-date_joined')[:10]
            self.stdout.write(
                self.style.SUCCESS(f'=== RECENT 10 USERS ===')
            )
        else:
            users = User.objects.all().order_by('-date_joined')
            self.stdout.write(
                self.style.SUCCESS(f'=== ALL USERS ===')
            )

        for user in users:
            status = "ACTIVE" if user.is_active else "INACTIVE"
            self.stdout.write(
                f'ID: {user.id} | Username: {user.username} | '
                f'Email: {user.email} | Status: {status} | '
                f'Joined: {user.date_joined.strftime("%Y-%m-%d %H:%M")}'
            )
