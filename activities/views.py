from rest_framework import viewsets, status, response
from rest_framework.decorators import detail_route
from pyfirmata import Arduino
from .models import Activity
from .serializers import ActivitySerializer

PORT = '/dev/cu.usbmodem1421'

board = Arduino(PORT)

class ActivityViewset(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class DeviceInteraction(viewsets.ViewSet):
    @detail_route()
    def interact(self, request, pk=None):
        pin = int(pk)
        if board.digital[pin].read() != 1:
            board.digital[pin].write(1)
            log = "User %s turns ON pin %s" % (request.user, pin)
        else:
            board.digital[pin].write(0)
            log = "User %s turns OFF pin %s" % (request.user, pin)
        activity = Activity.objects.create(log=log, user=request.user)
        serializer = ActivitySerializer(activity)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
