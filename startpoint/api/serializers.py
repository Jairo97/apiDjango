from rest_framework.serializers import ModelSerializer
from startpoint.models import ConsultaCliente


class ConsultaClienteSerializer(ModelSerializer):
    class Meta:
        model = ConsultaCliente
        fields = ['id', 'nome', 'cidade', 'numero_celular']
