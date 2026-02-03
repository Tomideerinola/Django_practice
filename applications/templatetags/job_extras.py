# applications/templatetags/job_extras.py
from django import template

register = template.Library()  # This tells Django "these are template filters"

@register.filter
def status_badge(value):
    """Return a CSS class based on job status"""
    if value.lower() == 'employed':
        return 'badge-success'
    elif value.lower() == 'leave':
        return 'badge-warning'
    else:
        return 'badge-secondary'
