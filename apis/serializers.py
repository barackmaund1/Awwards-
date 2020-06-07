from rest_framework import serializers
from users import models
from awward import models

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'contacts',
            'bio'
        )
        model = models.Profile

      