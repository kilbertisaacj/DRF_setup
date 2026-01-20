import os
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

RECAPTCHA_SECRET = os.getenv("RECAPTCHA_SECRET")


def recaptcha_page(request):
    print("VIEW HIT:", request.method)  
    return render(request, "recaptcha.html")


def verify_recaptcha(request):
    if request.method != "POST":
        print("Invalid request method:", request.method)
        return JsonResponse(
            {"success": False, "error": "POST required"},
            status=405
        )

    token = request.POST.get("g-recaptcha-response")
    print("Received token:", token)

    if not token:
        return JsonResponse(
            {"success": False, "error": "Missing reCAPTCHA token"},
            status=400
        )

    data = {
        "secret": RECAPTCHA_SECRET,
        "response": token,
    }

    google_response = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data=data,
        timeout=5
    )

    return JsonResponse(google_response.json())
