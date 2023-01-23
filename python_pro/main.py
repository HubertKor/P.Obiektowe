from rownoleglobok import Rownoleglobok
from kwadrat import Kwadrat

rown1 = Rownoleglobok(19,29,39)
rown2 = Kwadrat(10,"czerwony")

print(rown1.pobierz_pole())
print(rown1.pobierz_obwod())
print(rown1.duplikuj_ze_skala(2))

print(rown2)
lista1 = Kwadrat.generuj_kwadrat(['czerwony','zielony'])
print(lista1[1])

