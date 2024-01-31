from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class new_page(forms.Form):
    page = forms.CharField(label="New_page")


def get_page(request, title):
    content = util.get_entry(title)
    if content != None:
        return render(request, "encyclopedia/view.html", {
            "Content": content
        } )
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Page not found"
        })
    
def get_search(request):
    query = request.GET.get('q')
    content = util.get_entry(query)
    if content != None:
        return render(request, "encyclopedia/view.html", {
            "Content": content
        } )
    else:
        return render(request, "encyclopedia/error.html", {
            "error": "Page you have searched is not available"
        })

def add_page(request):
    return render(request, "encyclopedia/add.html")

def save_page(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) == None:
            util.save_entry(title, content)
            content_url = reverse('content', args=[title])
            return HttpResponseRedirect(reverse('content', args=[title]))
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "File Already Exists, change the page title"
            })
    else:
        return HttpResponse("Invalid request", status=400)




