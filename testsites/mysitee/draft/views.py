from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Draft
from .forms import FormPage
from django.views.generic import UpdateView, DeleteView
# Create your views here.

def index(request):
    note = Draft.objects.all()
    notes = {'note': note, 'title': 'Cписок черновиков'}
    return render(request, template_name='draft/index.html', context=notes)


def get_page(request, id):
    note = Draft.objects.filter(id=id)
    return render(request, template_name='draft/page.html', context={'note': note, })

# запись данных из формы в бд
def form_page(request):
    if request.method == 'POST':
        form = FormPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormPage()
    return render(request, template_name='draft/form_page.html', context={'form': form})

class PageUpdateView(UpdateView):
    model = Draft
    template_name = 'draft/form_page.html'
    form_class = FormPage

class PageDeleteView(DeleteView):
    model = Draft
    success_url = '/draft/'
    template_name = 'draft/text_delete.html'
