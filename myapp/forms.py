from django	import forms
from django.forms import ModelForm
from .models import publisher




TOPIC_CHOICES = (
	 ('general', 'general enquiry'),
	 ('bug', 'bug report'),
	 ('suggestions', 'Suggestions'),



	)

PUB_CHOICES = (
	 ('general', 'general enquiry'),
	 ('bug', 'bug report'),
	 ('suggestions', 'Suggestions'),



	)

# class pubform(forms.Form):
# 	topic = forms.ChoiceField(choices=PUB_CHOICES)
# 	message = forms.CharField(widget=forms.Textarea(), initial='Replace this with feedback from pubform')
# 	sender = forms.EmailField(required=False)



class contactform(forms.Form):
	topico = forms.ChoiceField(choices=TOPIC_CHOICES)
	message = forms.CharField(widget=forms.Textarea(), initial='Replace this with feedback from contactform')
	sender = forms.EmailField(required=True)

	def clean_message(self):
		

		mes = self.cleaned_data.get('message',  '')
		numwords = len(mes.split())
		if numwords < 4:
		   raise forms.ValidationError("not enough words")
		return mes

	def clean_sender(self):

		snd = self.cleaned_data.get('sender', '')
		if snd == 'me@gmail.com':
			raise forms.ValidationError("not this email")
		return snd



class pubform(ModelForm):
	class Meta:
		model = publisher
		fields = ['name', 'address', 'city', 'state', 'country', 'website']