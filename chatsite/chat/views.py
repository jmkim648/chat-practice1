from django.shortcuts import render


def chat_list(request):
    return render(request, "chat/chat_list.html")
