from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import dp_knapsack

@csrf_exempt
def optimize_itinerary_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            destinations = data.get('destinations', [])
            capacity = data.get('budget', 0)

            if not isinstance(destinations, list) or not isinstance(capacity, int):
                return JsonResponse({'error': 'Invalid input'}, status=400)

            max_value = dp_knapsack(destinations, capacity)
            return JsonResponse({'max_value': max_value}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def render_index_page(request):
    return render(request, "api/index.html")
