from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'homepage/home.html')


def cayman(request):
    return render(request, 'homepage/cayman.html')


def porsche911(request):
    return render(request, 'homepage/911.html')


def taycan(request):
    return render(request, 'homepage/taycan.html')


def panamera(request):
    return render(request, 'homepage/panamera.html')


def macan(request):
    return render(request, 'homepage/macan.html')


def cayenne(request):
    return render(request, 'homepage/cayenne.html')


def financial_services(request):
    return render(request, 'homepage/fin.html')


def service(request):
    return render(request, 'homepage/ser.html')


def testdrive(request):
    return render(request, 'homepage/testdrive.html')


def credit(request):
    return render(request, 'homepage/credit.html')


def standard(request):
    return render(request, 'homepage/standard.html')


def standard_used(request):
    return render(request, 'homepage/standard_used.html')


def special_credit(request):
    return render(request, 'homepage/special_credit.html')


def insurance(request):
    return render(request, 'homepage/insurance.html')


def leasing(request):
    return render(request, 'homepage/leasing.html')


def servicing(request):
    return render(request, 'homepage/servicing.html')


def seasonal_checks(request):
    return render(request, 'homepage/seasonal_checks.html')


def spares(request):
    return render(request, 'homepage/spares.html ')


def tequipment(request):
    return render(request, 'homepage/tequipment.html')


def rights(request):
    return render(request,  'homepage/rights.html')


def data_processing_policy(request):
    return render(request, 'homepage/data_processing_policy.html')


def contacts(request):
    return render(request, 'homepage/contacts.html')


