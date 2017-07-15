# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer
from pyfirmata import Arduino

PORT = '/dev/cu.usbmodem1421'

board = Arduino(PORT)

# Create your views here.
class ActivityList(APIView):
    """
    List all activities
    """
    serializer_class = ActivitySerializer

    def get(self, request, format=None):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def device_interaction(request, pk):
    """
    Interact with device
    """
    if request.method == 'GET':
        pin = int(pk)
        if board.digital[pin].read() != 1: # Could be None or 0
            board.digital[pin].write(1)
            log = "Pin %s encendido por %s" % (pin, request.user)
        else:
            board.digital[pin].write(0)
            log = "Pin %s apagado por %s" % (pin, request.user)
        activity = Activity.objects.create(log_text = log, user=request.user)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
