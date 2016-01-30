from members.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'description', 'open_hours', 'responsible_name', 'responsible_contact')
