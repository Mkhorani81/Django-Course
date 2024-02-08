from django import template
from ..models import Categoty

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگو"


@register.inclusion_tag("blog/partials/categoryNavbar.html")
def categoryNavbar():
    return {
        "category" : Categoty.objects.filter(status=True)
    }


@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link": f"account:{link_name}",
        "content": content,
        "classes": classes,
    }