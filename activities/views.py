from rest_framework import viewsets, response, status
from .models import Activity
from .serializer import ActivitySerializer


class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
