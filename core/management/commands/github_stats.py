import requests

from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings

class Command(BaseCommand):
    help = 'Fetches GitHub stats and caches them for display on the portfolio'

    def handle(self, *args, **options):
        username = settings.GITHUB_USERNAME
        token = settings.GITHUB_TOKEN

        self.stdout.write(f"Fetching GitHub stats for user: {username}")

        try:
            total = self.get_commit_count(username, token)
            cache.set('github_commit_count', total, timeout=3600)  # Cache for 1 hour
            self.stdout.write(f"Total commits for {username}: {total}")

        except Exception as e:
            self.stdout.write(f"Error fetching GitHub stats: {e}")
    
    def get_commit_count(self, username, token):
        """Get the total commit count for the user using GitHub's GraphQL API """

        # total contributions query to get total commits in the last year
        query = """
        query ($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
              }
            }
          }
        }
        """
        variables = {"login": username}
        headers = {"Authorization": f"Bearer {token}"}  

        res = requests.post(
            'https://api.github.com/graphql',
            json={'query': query, 'variables': variables},
            headers=headers
        )

        res.raise_for_status()
        data = res.json()
        return data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']