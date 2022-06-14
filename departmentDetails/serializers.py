from rest_framework import serializers
from departmentDetails.models import Level


class LevelSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='departmentdetails-detail', lookup_field='pk')

    class Meta:
        model = Level
        fields = (
            'id',
            'url',
            'name',
            'slug_name',
            'created',
            'subject'
        )

    def get_subject(self, obj):

        if not hasattr(obj, 'id'):
            return None
        # can alter the data of an instance using obj
        return obj.get_subject()
