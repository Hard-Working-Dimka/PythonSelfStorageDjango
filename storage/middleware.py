from django.utils.timezone import now
from storage.models import Order


class UpdateOverdueOrdersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.update_overdue_orders()
        response = self.get_response(request)
        return response

    def update_overdue_orders(self):
        overdue_orders = Order.objects.filter(status='in_storage', end_date__lt=now())
        for order in overdue_orders:
            order.status = 'overdue'
            order.save()
