from django.core.cache import cache

def update_github_stats(request):
    """ Context processor to add GitHub stats to the context for all templates"""
    return {
        'github_commit_count': cache.get('github_commit_count', 0)
    }