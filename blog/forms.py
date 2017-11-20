from django import forms
from .models import Post, Contact

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'subtitle', 'text', 'image', 'tags')

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('name', 'email', 'phone', 'message',)