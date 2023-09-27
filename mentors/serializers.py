from rest_framework import serializers

from mentors.models import Ustoz, Mijoz


class UstozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ustoz
        fields = '__all__'


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'
