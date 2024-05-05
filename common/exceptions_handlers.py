from django.shortcuts import render


def handler_server_error(request):
    return render(request, 'server-error-500.html')


def page_not_found(request, exception):
    return render(request, 'page-not-found-error.html')
