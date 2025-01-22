from rest_framework import viewsets
from .models import (
    Client, Warehouse, Plans, Order
)
from .serializers import (
    ClientsSerializer
)


class ClientsApiView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

