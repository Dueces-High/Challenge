from django.db import models


class Router(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    Hostname = models.CharField(max_length=100, unique=True)
    Management_IP_address = models.CharField(max_length=30)
    Hardware_vendor = models.CharField(max_length=30)
    Hardware_Type = models.CharField(max_length=30)
    Software_version = models.CharField(max_length=30)
    RoleChoice = (("access", "access"),
        ("distribution", "distribution"),
        ("core", "core"),
        ("router", "router"))
    Roles = models.CharField(null=True, max_length=100, choices=RoleChoice)

    Physical_Address = models.CharField(max_length=500)

    def __str__(self):
        return self.Hardware_vendor + self.Hardware_Type


class Interface(models.Model):
    Device = models.ForeignKey(Router, null=True, on_delete=models.DO_NOTHING)
    Name = models.CharField(max_length=500)


    FFoptions = (

        ("virtual", "virtual"),
        ("1G", "1G"),
        ("10G", "10G"),
        ("100G", "100G"))


    Form_Factor = models.CharField(max_length=90, null=True, choices=FFoptions)

    def __str__(self):
        return self.Name

class Intermediate(models.Model):

    Name = models.ManyToManyField(Interface)
