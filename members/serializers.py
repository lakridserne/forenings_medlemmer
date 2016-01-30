from members.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'description', 'open_hours', 'responsible_name', 'responsible_contact','placename','zipcode','city','streetname','housenumber','floor','door','dawa_id','has_waiting_list')
