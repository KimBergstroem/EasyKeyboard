from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculating the price with quantity 
    so the subtotal is correct in shopping bag
    """
    return price * quantity