from core.models import GitHubStat

def update_github_stats(request):
    """ Context processor to add GitHub stats to the context for all templates"""
    
    git_stats = GitHubStat.objects.first()
    github_commits = git_stats.stats.get('commits', 0)


    return {
        'github_commits': github_commits
    }