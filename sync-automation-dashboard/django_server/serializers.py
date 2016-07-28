from rest_framework import serializers

from django_server import models

class SummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Summary
		fields = ('total_runs', 'total_tests', 'average_yield', 'created_at')

	def create(self, validated_data):
		"""
		Create and return a new `Summary` instance, given the validated data.
		"""
		return Summary.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Summary` instance, given the validated data.
		"""
		instance.save()
		return instance