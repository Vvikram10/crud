# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        image = request.FILES.get('image')

        Contact.objects.create(name=name, email=email, contact=contact, address=address, image=image)
        return redirect('contact_list')
    return render(request, 'contact_form.html')

def contact_update(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.contact = request.POST['contact']
        contact.address = request.POST['address']
        if request.FILES.get('image'):
            contact.image = request.FILES.get('image')
        contact.save()
        return redirect('contact_list')
    return render(request, 'contact_form.html', {'contact': contact})

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})
