import requests

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import GitHubStat


class Command(BaseCommand):
    help = 'Fetches GitHub stats and saves them to the database'

    def handle(self, *args, **options):
        username = settings.GITHUB_USERNAME
        token = settings.GITHUB_TOKEN

        self.stdout.write(f"Fetching GitHub stats for user: {username}")

        try:
            stats = self.get_github_stats(username, token)

            stats_obj = GitHubStat.objects.get_or_create(pk=1)[0]
            stats_obj.stats = stats
            stats_obj.save()

            self.stdout.write(f"GitHub stats for {username}: {stats}")
        except Exception as e:
            self.stdout.write(f"Error fetching GitHub stats: {e}")

    def get_github_stats(self, username, token):
        """Get last-year contributions and commit contributions."""
        query = """
        query ($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
              }
              totalCommitContributions
            }
          }
        }
        """
        variables = {"login": username}
        headers = {"Authorization": f"Bearer {token}"}

        res = requests.post(
            'https://api.github.com/graphql',
            json={'query': query, 'variables': variables},
            headers=headers,
            timeout=15,
        )
        res.raise_for_status()
        data = res.json()

        if data.get('errors'):
            raise ValueError(f"GitHub GraphQL errors: {data['errors']}")

        user_data = data['data']['user']
        if not user_data:
            raise ValueError("GitHub user not found or token is invalid.")

        contributions_data = user_data['contributionsCollection']
        return {
            'commits': contributions_data['totalCommitContributions'],
            'contributions': contributions_data['contributionCalendar'][
                'totalContributions'
            ],
        }
