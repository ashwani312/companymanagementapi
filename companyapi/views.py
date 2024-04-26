from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page")
    friends = [
        "ashwani", "lokesh"
     ]
    return JsonResponse(friends, safe=False)
