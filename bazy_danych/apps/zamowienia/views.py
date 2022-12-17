from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.produkty.decorators import StaffRequiredMixin
from .models import Faktury, Zamowienia, Szczegoly_zamowienia
from datetime import date

class AllInvoicesView(ListView):
    model = Faktury
    template_name = 'allInvoices.html'
    ordering = ['-id']

    def get_queryset(self):
        return Faktury.objects.filter(id_uzytkownika=self.request.user)

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
