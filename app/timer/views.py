from django.http import JsonResponse
from django.shortcuts import render
from datetime import timedelta, datetime

def timer_view(request):
    return render(request, 'timer/timer.html')


def timer_api_view(request):
    if 'time' in request.GET:
        start_time = datetime.now()
        countdown_time = int(request.GET.get('time', 10))
        end_time = start_time + timedelta(seconds=countdown_time)
        request.session['end_time'] = end_time.isoformat()
        request.session.modified = True

        return JsonResponse({'time': format_time(countdown_time)})

    elif 'end_time' in request.session:
        end_time = datetime.fromisoformat(request.session['end_time'])
        remaining_time = max(0, int((end_time - datetime.now()).total_seconds()))
        print(remaining_time)
        print(format_time(remaining_time))
        return JsonResponse({'time': format_time(remaining_time)})

    return JsonResponse({'error': 'error'}, status=400)

def format_time(seconds):
    hours = int(seconds / 3600)
    rest = seconds % 3600
    minutes = int(rest / 60)
    rest = seconds % 60
    seconds = int(rest)

    return f"{hours:02}:{minutes:02}:{seconds:02}"