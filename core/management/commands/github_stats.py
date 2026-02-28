import requests

from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import GitHubStat

class Command(BaseCommand):
    help = 'Fetches GitHub stats and saves them to the database'

    def handle(self, *args, **options):
        username = settings.GITHUB_USERNAME
        token = settings.GITHUB_TOKEN

        self.stdout.write(f"Fetching GitHub stats for user: {username}")

        try:
            stats = self.get_github_stats(username, token)
            
            # Save to database
            stats_obj = GitHubStat.objects.get_or_create(pk=1)[0]
            stats_obj.stats = stats
            stats_obj.save()
            
            self.stdout.write(f"GitHub stats for {username}: {stats}")

        except Exception as e:
            self.stdout.write(f"Error fetching GitHub stats: {e}")
    
    def get_github_stats(self, username, token):
        """Get GitHub stats including total contributions and commits using GitHub's GraphQL API"""

        query = """
        query ($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
              }
            }
            repositories(first: 100, orderBy: {field: UPDATED_AT, direction: DESC}) {
              nodes {
                defaultBranchRef {
                  target {
                    ... on Commit {
                      history(first: 0) {
                        totalCount
                      }
                    }
                  }
                }
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
        
        contributions = data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
        
        # Sum commits from all repositories
        total_commits = 0
        for repo in data['data']['user']['repositories']['nodes']:
            if repo['defaultBranchRef'] and repo['defaultBranchRef']['target']:
                commit_count = repo['defaultBranchRef']['target']['history']['totalCount']
                total_commits += commit_count
        
        return {
            'commits': total_commits,
            'contributions': contributions
        }