from members.models import Department, Activity
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id','name', 'description', 'open_hours', 'responsible_name'
            , 'responsible_contact','placename','zipcode','city','streetname'
            ,'housenumber','floor','door','dawa_id','has_waiting_list')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','name','open_hours','responsible_name'
            ,'responsible_contact','placename','zipcode','city','streetname'
            ,'housenumber','floor','door','dawa_id','description','instructions'
            ,'start_date','end_date','signup_closing','open_invite'
            ,'price_in_dkk','max_participants','max_age','min_age')
