from django.shortcuts import render, redirect
from .forms import PublicationForm
from .models import ONG

def create_publication(request, ong_id):
    ong = ONG.objects.get(id=ong_id)
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.ong = ong
            publication.save()
            # Redireciona para a página da ONG
            return redirect('ong_detail', ong_id=ong.id)
    else:
        form = PublicationForm()
    return render(request, 'create_publication.html', {'form': form, 'ong': ong})
