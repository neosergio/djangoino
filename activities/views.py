from rest_framework import viewsets, response, status
from rest_framework.decorators import detail_route
from .models import Activity
from .serializer import ActivitySerializer

class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class DeviceViewset(viewsets.ViewSet):
    @detail_route()
    def interact(self, request, pk=None):
        pin = int(pk)
        if pin != 1:
            log = "User %s turns ON pin %s" % (request.user, pk)
        else:
            log = "User %s turns OFF pin %s" % (request.user, pk)
        activity = Activity.objects.create(log=log, user=request.user)
        serializer = ActivitySerializer(activity)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
