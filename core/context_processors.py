from core.models import GitHubStat

def update_github_stats(request):
    """Context processor to add GitHub stats to the context for all templates"""
    git_stats = GitHubStat.objects.first()
    
    if git_stats:
        github_commits = git_stats.stats.get('commits', 0)
        github_contributions = git_stats.stats.get('contributions', 0)
    else:
        github_commits = 0
        github_contributions = 0

    return {
        'github_commits': github_commits,
        'github_contributions': github_contributions,
    }