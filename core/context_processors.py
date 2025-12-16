from .models import Category

def categories(request):
    """
    Make categories available to all templates (e.g. for navigation)
    """
    return {
        'all_categories': Category.objects.all().order_by('name')
    }
