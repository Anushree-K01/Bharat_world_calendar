from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime, timezone, timedelta

# Time zone dictionary
utc_offsets = {
    'new york': -4 if 3 <= datetime.now(timezone.utc).month <= 11 else -5,
    'san francisco': -7 if 3 <= datetime.now(timezone.utc).month <= 11 else -8,
    'utc': 0,
    'london': 1,
    'dubai': 4,
    'bangalore': 5.5,
    'singapore': 8,
    'tokyo': 9,
    'sydney': 10 if 3 <= datetime.now(timezone.utc).month <= 11 else 11,
    'wellington': 12 if 3 <= datetime.now(timezone.utc).month <= 11 else 13
}
def index(request):
    return render(request, "datetimeapp/index.html")

# Django view function
def get_time(request):
    city_name = request.GET.get("city_name", "").strip().lower()

    if city_name in utc_offsets:
        utc_time = datetime.now(timezone.utc)
        local_time = utc_time + timedelta(hours=utc_offsets[city_name])
        formatted_time = local_time.strftime('%d-%m-%Y, %I:%M:%S %p')

        return JsonResponse(
            {"city": city_name.title(),
            "local_time": formatted_time
            })
    
    return JsonResponse({"error": "City not found. Please enter a city from the list."}, status=404)