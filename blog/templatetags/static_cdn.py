from django import template
from config import settings

register = template.Library()

@register.simple_tag
def static_cdn(url):
    return url.replace(settings.AWS_S3_CUSTOM_DOMAIN, settings.AWS_S3_CDN_DOMAIN)
