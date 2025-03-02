from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.shortcuts import render
from datetime import timedelta, datetime

def timer_view(request):
    return render(request, 'timer/timer.html')


class TimerAPIView(APIView):

    def get(self, request):
        if 'time' in request.GET:
            start_time = datetime.now()
            countdown_time = int(request.GET.get('time', 10))
            end_time = start_time + timedelta(seconds=countdown_time)
            request.session['end_time'] = end_time.isoformat()
            request.session.modified = True

            return Response({'time': format_time(countdown_time)}, status=status.HTTP_200_OK)

        elif 'end_time' in request.session:
            end_time = datetime.fromisoformat(request.session['end_time'])
            remaining_time = max(0, int((end_time - datetime.now()).total_seconds()))
            request.session.modified = True
            print(format_time(remaining_time))
            return Response({'time': format_time(remaining_time)}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        if 'end_time' in request.session:
            del request.session['end_time']
            request.session.modified = True
            return Response({'message': 'Timer zresetowany'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Brak aktywnego timera do zresetowania'}, status=status.HTTP_200_OK)

class stopwatchAPIView(APIView):

    def get(self, request):
        if 'stopwatchTime' in request.GET:
            stopwatchTime = int(request.GET.get('stopwatchTime', 10))
            return Response({'stopwatchTime': format_time(stopwatchTime)}, status=status.HTTP_200_OK)
        return Response({'error': 'Missing parameter'}, status=status.HTTP_400_BAD_REQUEST)


def format_time(seconds):
    hours = int(seconds / 3600)
    rest = seconds % 3600
    minutes = int(rest / 60)
    rest = seconds % 60
    seconds = int(rest)

    return f"{hours:02}:{minutes:02}:{seconds:02}"



