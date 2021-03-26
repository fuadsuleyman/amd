from django.template import Library
from django.conf import settings
register = Library()
from product.models import Category



@register.simple_tag
def get_navbar():
    category_list = Category.objects.order_by('created_at')
    
    # last_s_index = len(meny_list_main) - 2
    context = {
        'api_url': settings.API_URL,
        'category_list': category_list,
        # 'last_second_index': last_s_index
    }
    return context


# @register.filter
# def index(indexable, i):

#     return value
