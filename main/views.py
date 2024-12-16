from django.shortcuts import render
from .models import Product

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





def generate_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    html = render_to_string('invoices/invoice_template.html', {'invoice': invoice})
    pdf = HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="invoice_{invoice_id}.pdf"'
    return response
