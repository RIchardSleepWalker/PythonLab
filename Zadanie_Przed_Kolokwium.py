# def przygotuj_pizze(dodatki, baza=None):
#     if baza is None:
#         baza = []
#     baza.append("sos pomidorowy")
#     baza.append("ser")
#     baza.extend(dodatki)
#     print(f"Pizza gotowa! Składniki: {baza}")
#
# print("--- Zamówienie 1: Capricciosa ---")
# przygotuj_pizze(["szynka", "pieczarki"])
# print("\n--- Zamówienie 2: Margherita ---")
# przygotuj_pizze([])
#
# def print_receipt(data, stawka_vat=0.23):
#     total = 0
#     print("---PARAGON---")
#     for item in data:
#         price_with_tax = item["cena_netto"] * (1 + stawka_vat)
#         total += price_with_tax
#         print(f"{item['nazwa']}... {price_with_tax}")
#         print("SUMA: " + str(total))
#
#
# produkty = [
#     {"nazwa": "Mleko", "cena_netto": 3.50},
#     {"nazwa": "Czekolada", "cena_netto": 5.20},
# ]
# print_receipt(produkty)
#
# pracownicy = [
#     {"imie": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
#     {"imie": "Piotr", "stanowisko": "Manager", "pensja": 8000},
#     {"imie": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
# ]
# lista_plac = [f"{x["imie"]} {x["pensja"]}" for x in pracownicy if x["stanowisko"] == "Specjalista"]
# print(lista_plac)
#
# zduplikowane_dane = [
#     {"id": 1, "imie": "Anna"},
#     {"id": 2, "imie": "Piotr"},
#     {"id": 1, "imie": "Anna"},
#     {"id": 3, "imie": "Zofia"},
# ]
#
# widziane_dane = set()
# unikalne_dane = [
#     (x["id"], x["imie"])
#     for x in zduplikowane_dane
#     if x["id"] not in widziane_dane and not widziane_dane.add(x["id"])
# ]
# print(unikalne_dane)
#
# licznik = 0
# print(f"Start: {licznik}, typ: {type(licznik)}")
# while round(licznik, 1) != 1.0:
#     licznik = round(licznik + 0.1, 1)
#     print(licznik)
# print(f"Koniec: {licznik}")
# from platformdirs import site_runtime_dir

# Chcemy stworzyć planszę do gry w kółko i krzyżyk 3x3
# Chcemy stworzyć planszę do gry w kółko i krzyżyk 3x3

# plansza = [['_'] * 3 for _ in range(3)]
# print("Początkowa plansza:")
# for wiersz in plansza:
#     print(wiersz)
# # Gracz stawia 'X' w lewym górnym rogu
# print("\nGracz stawia 'X' w [0][0]...")
# plansza[0][0] = 'X'
# # Jak wygląda plansza TERAZ?
# print("\nAktualna plansza:")
# for wiersz in plansza:
#     print(wiersz)


# def analizuj_oceny(lista_studentow):
#     if not lista_studentow:
#         return {"srednia": 0, "najlepszy_student": None, "unikalne_oceny": set()}
#     else:
#         srednia = sum(s["ocena"] for s in lista_studentow) / len(lista_studentow)
#
#         najlepszy_student = max(lista_studentow, key=lambda s: s["ocena"])
#
#         unikalne_oceny = {s["ocena"] for s in lista_studentow}
#
#         return {"srednia": srednia, "najlepszy_student": najlepszy_student, "unikalne_oceny": unikalne_oceny}
#
#
# dane_studentow = [
#     {"imie": "Anna", "ocena": 5},
#     {"imie": "Piotr", "ocena": 3},
#     {"imie": "Zofia", "ocena": 5},
#     {"imie": "Krzysztof", "ocena": 4},
# ]
#
# print(analizuj_oceny(dane_studentow))

# kontakty = {"Anna": "123", "Piotr": "456"}
# print(f"Początkowe kontakty: {kontakty}")
# nazwy_kontaktow = kontakty.keys()
# wartosci_kontaktow = kontakty.values()
# print(f"Pobrane nazwy: {nazwy_kontaktow}")
# print("\nDodajemy nowy kontakt 'Zofia'...")
# kontakty["Zofia"] = "789"
# print("\nJak wyglądają nazwy_kontaktow TERAZ?")
# print(list(nazwy_kontaktow))
# print(list(wartosci_kontaktow))

# def splaszcz_liste(elementy):
#     splaszczona = []
#     for elem in elementy:
#         if isinstance(elem, list):
#             splaszczona.extend(splaszcz_liste(elem))
#         else:
#             splaszczona.append(elem)
#     return splaszczona
#
# zagniezdzona_lista = [1, [2, 3], 4, [5, [6, 7]]]
# print(zagniezdzona_lista)
# print(splaszcz_liste(zagniezdzona_lista))

# def znajdz_wartosc(dane, szukany_klucz):
#     for klucz,wartosc in dane.items():
#         if klucz == szukany_klucz:
#             return wartosc
#
#         if isinstance(wartosc, dict):
#             wynik = znajdz_wartosc(wartosc, szukany_klucz)
#             if wynik is not None:
#                 return wynik
#     return None
#
# konfiguracja = {
#     "uzytkownik": "admin",
#     "baza_danych": {
#         "host": "localhost",
#         "port": 5432,
#         "credentials": {
#             "user": "db_user",
#             "password": "secret_password"
#         }
#     }
# }
#
# haslo = znajdz_wartosc(konfiguracja, "password")
# print(f"Znalezione hasło: {haslo}")

#1.1A
# def dodaj_tag(tag,tagi=None):
#     if tagi is None:
#         tagi = []
#     tagi.append(tag)
#     return tagi
# print(dodaj_tag("python"))
# print(dodaj_tag("pragmowanie"))
#1.2A
# kontakty = {"Anna": "123","Piotr":"456"}
# nazwy = kontakty.keys()
# kontakty["Zofia"] = "789"
# print(list(nazwy))
#1.1B
# liczby = [10,-5,-15,20,30]
# liczby = [x for x in liczby if x > 0]
#
# print(liczby)
# koszyk = [
#     {"nazwa": "Mleko","cena":3.50,"kategoria":"Nabial"},
#     {"nazwa": "Czekolada","cena":5.20,"kategoria":"Slodycze"},
#     {"nazwa": "Ser","cena":4.8,"kategoria":"Nabial"}
# ]
#
# def analizuj_koszyk(lista_produktow,prog_darmowej_dostawy):
#     if lista_produktow is None:
#         return {"wartosc_calkowita":0,"najdrozszy_produkt":None,"kategorie":[],"darmowa_dostawa":False}
#     else:
#         wc = sum(s["cena"] for s in lista_produktow)
#
#         np = max(lista_produktow, key=lambda s: s["cena"])
#
#         kat = list(set(s["kategoria"] for s in lista_produktow))
#
#         dd = wc >= prog_darmowej_dostawy
#
#         return {"wartosc_calkowita":wc,"najdrozszy_produkt":np,"kategorie":kat,"darmowa_dostawa":dd}
#
#
# wynik = analizuj_koszyk(koszyk,15)
# print(wynik)
# studenci = [
#     {"imie":"Anna","srednia_ocen":4.5,"kierunek":"Informatyka"},
#     {"imie":"Piotr","srednia_ocen":3.8,"kierunek":"Automatyka"},
#     {"imie":"Anna","srednia_ocen":4.9,"kierunek":"Informatyka"}
# ]
# def analizuj_grupe(studenci,prog_stypendium):
#     if studenci == []:
#         return {"srednia_grupy":0,"student_z_najwysza_srednia":None,"kierunki":[],"stypendium_grupowe":False}
#     else:
#         sg = round(sum(s["srednia_ocen"] for s in studenci),2)
#         nzns = max(studenci,key=lambda s: s["srednia_ocen"])
#         k = list(set(s["kierunek"] for s in studenci))
#         s = prog_stypendium <= sg
#         return {"srednia_grupy":sg,"student_z_najwysza_srednia":nzns,"kierunki":k,"stypendium_grupowe":s}
#
# wynik = analizuj_grupe(studenci,4.2)
# print(wynik)
# a = [x["imie"] for x in studenci if x["kierunek"] == "Informatyka"]
# print(a)
# struktura_firmy = {
#     "imie": "Anna (CEO)",
#     "podwladni": [
#         {"imie": "Piotr (Manager)","podwladni":[
#             {"imie":"Krzysztof (Specjalista","podwladni":[]},
#             {"imie":"Zofia (Specjalista)","podwladni":[]},
#         ]},
#         {"imie":"Marek (Manager)","podwladni":[]}
#     ]
# }
# def zlicz_wszystkich_pracownikow(firma):
#     a = 1
#     for i in firma["podwladni"]:
#         a += zlicz_wszystkich_pracownikow(i)
#     return a
# print(f"Liczba pracownikow wynosi: {zlicz_wszystkich_pracownikow(struktura_firmy)}")





















#1.1A
# def dodaj_tag(tag,tagi=None):
#     if tagi is None:
#         tagi = []
#     tagi.append(tag)
#     return tagi
#
# print(dodaj_tag('Python'))
# print(dodaj_tag('C++'))
#1.1A
# kontakty = {"Anna":123,"Piotr":456}
# nazwy = kontakty.keys()
# kontakty["Zofia"] = "789"
# print(list(nazwy))
#1.2A
# liczby = [10,-5,-15,20,30]
# for liczba in liczby[:]:
#     if liczba < 0:
#         liczby.remove(liczba)
#
# print(liczby)
#1.2B
# macierz = [[0]*3 for _ in range(3)]
# macierz[0][0] = 1
# print(macierz)
# koszyk = [
#     {"nazwa": "Mleko","cena":3.50,"kategoria":"Nabial"},
#     {"nazwa": "Czekolada","cena":5.20,"kategoria":"Slodycze"},
#     {"nazwa": "Ser","cena":4.8,"kategoria":"Nabial"}
# ]
#
# def analizuj_koszyk(lista_produktow,prog_darmowej_dostawy):
#     if lista_produktow == []:
#         return {"wartosc_calkowita": 0, "najdrozszy_produkt": None, "kategorie": [], "darmowa_dostawa": False}
#     else:
#         wc = sum(s["cena"] for s in lista_produktow)
#         np = max(lista_produktow, key=lambda s: s["cena"])
#
#         k = list(set(s["kategoria"] for s in lista_produktow))
#
#         dd = prog_darmowej_dostawy <= wc
#
#         return {"wartosc_calkowita": wc, "najdrozszy_produkt": np, "kategorie": k, "darmowa_dostawa": dd}
#
# wynik = analizuj_koszyk(koszyk,10)
# print(wynik)
# w = [s["nazwa"].upper() for s in koszyk if s["kategoria"] == "Nabial"]
# print(w)

# studenci = [
#      {"imie":"Anna","srednia_ocen":4.5,"kierunek":"Informatyka"},
#      {"imie":"Piotr","srednia_ocen":3.8,"kierunek":"Automatyka"},
#      {"imie":"Marek","srednia_ocen":4.9,"kierunek":"Informatyka"}
# ]
# def analizuj_grupe(studenci,prog_stypendium):
#     if studenci == []:
#         return {"srednia_grupy":0,"student_z_najwysza_srednia":None,"kierunki":[],"stypendium_grupowe":False}
#     else:
#         sg = sum(s["srednia_ocen"] for s in studenci)/len(studenci)
#         szns = max(studenci, key=lambda s: s["srednia_ocen"])
#         szns = szns["imie"]
#
#         k = list(set([s["kierunek"] for s in studenci]))
#
#         s = prog_stypendium <= sg
#
#         return {"srednia_grupy": sg, "student_z_najwysza_srednia": szns, "kierunki": k, "stypendium_grupowe": s}
#
#
# print(analizuj_grupe(studenci,20))
# a = [len(s["imie"]) for s in studenci if s["kierunek"]=="Informatyka"]
# print(a)

# struktura_firmy = {
#     "imie": "Anna (CEO)",
#     "podwladni": [
#         {"imie": "Piotr (Manager)","podwladni":[
#             {"imie":"Krzysztof (Specjalista","podwladni":[]},
#             {"imie":"Zofia (Specjalista)","podwladni":[]},
#         ]},
#         {"imie":"Marek (Manager)","podwladni":[]}
#     ]
# }
# def zlicz_wszystkich_pracownikow(firma):
#     a = 1
#     for x in firma["podwladni"]:
#         a += zlicz_wszystkich_pracownikow(x)
#     else:
#         return a
#
# print(zlicz_wszystkich_pracownikow(struktura_firmy))