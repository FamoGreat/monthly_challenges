from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


month_challenge = {
    "january": "Cut out added sugars and drink at least 2L of water daily.",
    "february": "Control portion sizes by using smaller plates and eating mindfully.",
    "march": "Avoid junk food, fried food, and processed snacks.",
    "april": "Walk at least 10,000 steps daily and take the stairs instead of the elevator.",
    "may": "Drink at least 3L of water daily and replace sugary drinks with herbal tea.",
    "june": "Increase protein intake and reduce carbs for better weight management.",
    "july": "Stop eating at least 3 hours before bedtime to improve digestion.",
    "august": "Exercise for at least 30 minutes daily, including cardio and strength training.",
    "september": "Eliminate alcohol, sodas, and sugary drinks from your diet.",
    "october": None,
    "november": "Practice mindful eating by chewing slowly and avoiding distractions.",
    "december": "Make healthier choices during the holidays while balancing indulgence with exercise."
}


# Create your views here.
def index(request):
    months = list(month_challenge.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def month_challenge_by_number(request, month):
    months = list(month_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = month_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        raise Http404()
