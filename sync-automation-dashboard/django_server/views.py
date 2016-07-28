from django_server.models import *
from django_server.serializers import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import Http404, JsonResponse
from rest_framework import status, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from pyrui import RUI

# class SummaryView(generic.DetailView):
#     model = models.Summary

# summary_view = SummaryView.as_view()

# class SummarySetView(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Summary.objects.all()
#     serializer_class = serializers.SummarySerializer

# Summary
class SummaryList(generics.ListCreateAPIView):
	"""
	Abstracts GET, POST, and DELETE, which can be accessed from "localhost:8000/summary/"
	"""
	queryset = Summary.objects.all()
	serializer_class = SummarySerializer

	def delete(self, request, format=None):
		self.queryset.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SummaryDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Abstracts GET, PUT, and DELETE, which can be accessed from "localhost:8000/summary/<id>"
	"""
	queryset = Summary.objects.all()
	serializer_class = SummarySerializer