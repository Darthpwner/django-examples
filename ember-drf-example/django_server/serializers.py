from rest_framework import serializers

from django_server import models

class SummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Summary