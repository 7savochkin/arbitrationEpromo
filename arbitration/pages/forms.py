from django import forms
from django.core.mail import EmailMessage

from arbitration import settings


class ContactUsForm(forms.Form):
    """Form for validating contact data and send to company email"""
    name = forms.CharField(max_length=200, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-input'}),
                           error_messages={'required': 'Please enter your name'})
    email = forms.EmailField(required=True,
                             error_messages={'required': 'Please enter your email'})
    phone = forms.CharField(max_length=18, required=True,
                            error_messages={'required': 'Please enter your phone'})
    message = forms.CharField(required=True, widget=forms.Textarea,
                              error_messages={'required': 'Please enter your message'})

    def prepare_email_subject(self):
        """Method for create subject by validated data"""
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')

        subject = (f'Contact Form Submission from {name},'
                   f' Email - {email}')

        return subject

    def prepare_email_message(self):
        """Method for create email message by validated_data"""
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        message_content = self.cleaned_data.get('message')

        message_data = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Message": message_content,
        }

        message = "\n".join("{0}: {1}".format(key, val) for key, val in message_data.items())
        return message

    def send_email(self):
        """Method for sending contact mail"""
        from_email = settings.EMAIL_HOST
        to_email = [settings.ADMIN_EMAIL]
        reply_to = [self.cleaned_data["email"]]
        email_subject = self.prepare_email_subject()
        message = self.prepare_email_message()

        EmailMessage(
            email_subject, message,
            from_email,  # Send from (your website)
            to_email,  # Send to (your admin email)
            reply_to=reply_to  # Email from the form to get back to
        ).send()
