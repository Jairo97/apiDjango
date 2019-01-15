from .serializers import ConsultaClienteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from startpoint.models import ConsultaCliente



class ConsultaClienteViewSet(ModelViewSet):
    serializer_class = ConsultaClienteSerializer
    permission_classes= (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )
    queryset = ConsultaCliente.objects.all()
