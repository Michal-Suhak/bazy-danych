from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Faktury, Zamowienia, Szczegoly_zamowienia
from datetime import date

@login_required
def all_invoices(request):
    invoices = Faktury.objects.filter(id_uzytkownika=request.user.pk).values()
    new_invoices = []
    for i in range(invoices.count()):
        order = invoices[i].get('id_zamowienia_id')
        products = Szczegoly_zamowienia.objects.filter(id_zamowienia=order)
        new_invoices.append({'id': invoices[i].get('id'),
                             'id_zamowienia_id': invoices[i].get('id_zamowienia_id'),
                             'kwota': invoices[i].get('kwota'),
                             'data_wystawienia': invoices[i].get('data_wystawienia'),
                            'products': products})

    context = {'invoices': new_invoices}
    return render(request, 'allInvoices.html', context)

@login_required
def overall_order(request):
    active_order = Zamowienia.objects.filter(id_uzytkownika=request.user, zakonczone=False)
    total_cost = 0

    if active_order:
        orders_list = Szczegoly_zamowienia.objects.filter(id_zamowienia__in=active_order)
        sum = 0
        for i in orders_list:
            sum += i.id_produktu.cena;
        

        if request.method == 'POST':
            for item in orders_list:
                total_cost += item.id_produktu.cena * item.ilosc
            Faktury.objects.create(
                id_uzytkownika = request.user,
                id_zamowienia = active_order.first(),
                kwota = total_cost,
                data_wystawienia = date.today()
            )
            active_order.update(zakonczone=True)
            return redirect('home')

        context = {'orders_list': orders_list, 'active_order': active_order, 'sum': sum}
        return render(request, 'orderSummary.html', context)

    
    return render(request, 'emptyOrder.html')
