from django.shortcuts import render

def blog_page(request):
    return render(request, "all_blogs.html", {})