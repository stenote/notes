from django.template import Library

register = Library()

@register.filter
def link(object, type='view'):
	return object.link(type)
	