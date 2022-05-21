from rest_framework import serializers
from .models import Router, Interface

class SerialRouter(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ['id', 'Hostname', 'Management_IP_address',
                  "Hardware_vendor", "Hardware_Type",
              "Software_version", "Roles", "Physical_Address"]


class SerialInterface(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ['id', 'Device', 'Name',
                  "Form_Factor"]