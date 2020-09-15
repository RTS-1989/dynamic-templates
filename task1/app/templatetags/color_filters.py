from django.template import library

register = library.Library()


@register.filter
def color_filters(value):
    if value != '-':
        if float(value) < 0:
            return 'Green'
        elif 1 < float(value) < 2:
            return 'LightCoral'
        elif float(value) > 2:
            return 'Red'
        else:
            return 'White'
