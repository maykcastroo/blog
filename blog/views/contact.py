from blog.models import Contact
from django.utils import timezone
from django.shortcuts import render, redirect
from blog.forms import ContactForm

def contact_new(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save()
			return redirect('post_list')
	else:
		form = ContactForm()
	return render(request, 'blog/contact_new.html', {'form': form})
