from django import forms


from .models import Router,Interface


class UserRegisterForm(forms.ModelForm):


    class Meta:
        model = Router
        fields = ['id', 'Hostname', 'Management_IP_address',
                  "Hardware_vendor", "Hardware_Type",
              "Software_version", "Roles", "Physical_Address"]

class InterfaceForm(forms.ModelForm):


    class Meta:
        model = Interface
        fields = ['id', 'Device', 'Name',
                  "Form_Factor"]


