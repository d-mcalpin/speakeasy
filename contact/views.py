from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse


def contact_us(request):
    """ Display contact us form and handle sending of email on POST request """
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject,
                          message,
                          from_email,
                          ["cocktail.delivery.speakeasy@gmail.com"]
                          )
                messages.success(request, "Email sent!")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact_success")
        else:
            messages.error(request,
                           "Sorry, couldn't send your email. "
                           "Please ensure form is valid"
                           )

    context = {
        "form": form,
    }

    return render(request, "contact/contact.html", context)


def contact_success(request):
    return render(request, "contact/contact-success.html")
