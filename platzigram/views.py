"""Platzigram views"""
# Utilities
from datetime import datetime

# Django
from django.http import HttpResponse, JsonResponse


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(
        '<h1>Oh, hi! Current server time is {now}</h1>'.format(now=now))


def sorted_numbers(request):
    """Return a json resonse"""
    # import pdb
    # pdb.set_trace()
    if request.GET:
        numbers = {'numbers': sorted(
            [int(i) for i in request.GET.get('numbers', '').split(',')]
        )}

        return JsonResponse(numbers)
    return HttpResponse('No Numbers')

# def sort_integers(request):
#     """Return a JSON response with sorted integers."""
#     numbers = [int(i) for i in request.GET['numbers'].split(',')]
#     sorted_ints = sorted(numbers)
#     data = {
#         'status': 'ok',
#         'numbers': sorted_ints,
#         'message': 'Integers sorted successfully.'
#     }
#     return HttpResponse(
#         json.dumps(data, indent=4),
#         content_type='application/json'
#     )


def say_hi(request, name):
    """Return a greeting"""
    return HttpResponse(
        '<h1>Hi, {}</h1>'.format(name.title())
    )
