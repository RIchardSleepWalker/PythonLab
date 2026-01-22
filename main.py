import json
import os
import re
import traceback
from encodings.quopri_codec import quopri_encode
from functools import reduce, total_ordering
import time
from _ast import arg
from operator import truediv, itemgetter
from statistics import kde_random
from traceback import print_tb
import random
import csv
import pydantic
import itertools
from datetime import datetime, timedelta
import requests, threading
import json
import multiprocessing
import time
import asyncio, aiohttp, queue
import concurrent.futures

import requests.exceptions


# def dodawanie():
#     f = input("Podaj pierwsza liczbe")
#     s = input("Podaj druga iczbe")
#     sum = int(f) + int(s)
#     return sum
#
# while True:
#     a = dodawanie()
#     if a == 2025:
#         break
# print(a)
# from pstats import func_get_function_name
# def przywitaj_sie(imie):
#     print(f"Czesc: {imie}. Milo mi Ciebie poznac")
#
# nazwa_uzytkownika = input("Podaj imie: ")
# przywitaj_sie(nazwa_uzytkownika)

# def dodaj(a,b):
#     return int(a)+int(b)
# def oblicz_pole(a,b):
#     return int(a)*int(b)
#
# a = input()
# b = input()
# wynik_dodawania = dodaj(a,b)
# print(f"Wynik dodawania to: {wynik_dodawania}")
# pole = oblicz_pole(a,b)
# print(f"Pole prostokata wynosi: {pole}")

# def witaj(name="Guest"):
#     print("Welcome " + name)
#
# witaj("Jakub")
# witaj()

# def raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
#     str = ("|=======Raport Uzytkownika=======|\n"
#            f"|    Imie: {imie}\n"
#            f"|    Stanowisko: {stanowisko}\n"
#            f"|    Miasto: {miasto}\n"
#            "|================================|\n")
#     return str
# print(raport("Jakub"))
# print(raport("Alojzy", "Data Scientist"))
# print(raport("Ferdynard", "Programista", "Krakow"))

# def splitNameAndForname(iin):
#     a,b = iin.split(' ')
#     return a, b
#
# iin = "Jan Kowalski"
# w,k = splitNameAndForname(iin)
# print(w , " zostalo rozdzielone ", k)

# def suma(num1, num2, *args):
#     return num1 + num2 + sum(args)
#
# print("Pierwsza proba (dwie wartosci, brak dodatkowych argumentow)", suma(1,2))
# print("Druga proba (dwie wartosci, dwia dodatkowe argumenty)", suma(1,2,3,4))
# print("Trzecia proba, dwie wartosci, 10 dodatkowych argumentow", suma(1,2,3,4,5,6,7,8,9,10,11,12))

# def GenRaport(**dane):
#     for key, value in dane.items():
#         print(f"{key}: {value}")
#
# inf = {
#     "name": "Jakub",
#     "age": 22,
#     "gender": "Male",
#     "residence": "Made if gold"
# }
# GenRaport(**inf)

# def dodaj(a,b):
#     return a+b
# def odejmij(a,b):
#     return a-b
# def wykonaj_operacje(a,b, func):
#     print(f"func: {func.__qualname__}")
#     return func(a,b)
#
# print(wykonaj_operacje(5,5,odejmij))
# print(wykonaj_operacje(5,5,dodaj))

# a = int(input())
# b = ((a + 1) * a + 2) * a + 3
# print(b)

# x = "GLobal"
#
# def func_out():
#     x = "Outside"
#
#     def func_ins():
#         x = "Inside"
#         print(x)
#
#     func_ins()
#     print(x)
#
# func_out()
# print(x)

# licznik = 10
#
# def modify(licznik):
#     licznik = 12
#     print(f"In function {licznik}")
#
# modify(licznik)
# print(f"Outside function {licznik}")

# def raport(name,stanowisko,miasto):
#     str = ("|=======Raport Uzytkownika=======|\n"
#            f"|    Imie: {name}\n"
#            f"|    Stanowisko: {stanowisko}\n"
#            f"|    Miasto: {miasto}\n"
#            "|================================|\n")
#     print(str)
#
# inf = {
#     "name": "Jakub",
#     "stanowisko": "Pracownik",
#     "miasto": "Myslenice"
# }
#
# raport(name = inf["name"],stanowisko = inf["stanowisko"],miasto = inf["miasto"])

# def wyslij_email(adres,temat,tresc,*,priorytet="normalny"):
#     str = (adres,temat,tresc)
#     print(str)
#
# wyslij_email("adres@gmail.com","Test komputera","Kupilam komputer i pisze do ciebie",priorytet="priorytet")

# def dekorator(func):
#     def wrapper():
#         print("Przed dekoracja:")
#         func()
#         print("Po dekoracji:")
#
#     return wrapper
#
# @dekorator
# def sayHi():
#     print("Hello world!")
#
# dekorator(sayHi())

# def loguj(func):
#     def wrapper():
#         print('Start Funkcji')
#         func()
#         print('Koniec funkcji')
#     return wrapper
#
# @loguj
# def dodawanie(a=1,b=2):
#     print(a+b)
#
# loguj(dodawanie())

# import time
#
# def mierz_czas(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         wynik = func(*args, **kwargs)
#         end = time.time()
#         print(end-start)
#         return wynik
#     return wrapper
#
# @mierz_czas
# def obliczenia(n=5):
#     for a in range(1, n + 1):
#         for b in range(a, n + 1):
#             c_kwadrat = a ** 2 + b ** 2
#             c = int(c_kwadrat ** 0.5)
#             if c ** 2 == c_kwadrat and c <= n:
#                 print(f"({a}, {b}, {c})")
#
# mierz_czas(obliczenia(5))

# def simple_generetor():
#     print("Witam")
#     yield"pierwsza wartosc"
#     print("Witam")
#     yield("druga wartosc")
#
# x = simple_generetor()
#
# print(next(x))
# print(next(x))

# def count_to_three():
#     yield 1
#     yield 2
#     yield 3
#
# x = count_to_three()
# for i in x:
#     print(i)
#     time.sleep(1)

# def fib(n):
#     a = 0
#     b = 1
#     for x in range(n):
#         yield a
#         a, b = b, a+b
#
# for x in fib(1000):
#     print(x)

# liczby = [1,2,3]
#
# kwadraty = list(map(lambda x: x ** 2, liczby))
# print(kwadraty)
#
# liczba = [1,2,3,4,5,6,7,8,9,10]
#
# parzyste = list(map(lambda x: bool(x % 2), liczba))
# print(parzyste)

# imiona = ["jan","marek","maurycy"]
#
# zw = list(map(lambda x: x.capitalize(), imiona))
# print(zw)
#
# oceny = [1,2,2,3,3,4,3,5,6,5,4,5,6,5,4,4,4,5,6,5,4,3,2,2,22,3,2]
# oc = list(map(lambda x: x >= 4, oceny))
# print(oc)

# def sprawdz_typy(func):
#     def wrapper(*args, **kwargs):
#         for i in func(*args, **kwargs):
#             print(i)
#
#     return wrapper
#
# @sprawdz_typy
# def dodaj(a=2,b=1):
#     return a,b
#
# sprawdz_typy(dodaj)

# from narzedzia_firmowe.pomiary import mierz_czas
# from narzedzia_firmowe.formatowanie import naWielkie
# import time
#
# @mierz_czas
# def dodaj(a=1,b=1):
#     return a+b
#
# print(dodaj(1,2))
#
# print(naWielkie("jakub"))

# produkty = [
#     {"nazwa": "Laptop Lenovo","cena": 8000},
#     {"nazwa": "Trytytki","cena": 12.50},
#     {"nazwa": "Laptop Mac","cena": 12000},
#     {"nazwa": "SmartWatch","cena": 2000},
#     {"nazwa": "Ladowarka","cena": 150},
# ]
#
# asort = sorted(produkty, key=lambda k: k["cena"])
# for i in range(len(asort)):
#     print(asort[i])

# grades = [4,5,3,4,5,2,4,3,4]
# ifFail = any(x < 3 for x in grades)
# ifSuccess = all(x >= 3 for x in grades)
#
# print(f"Czy jest zagrozenie? {ifFail}")
# print(f"Czy wszystko zdane? {ifSuccess}")

# numbers = [2,2,1,3,3,2,4,2,8,2,2,3,1,0]
# majorNum = reduce(lambda x,y: max(x,y), numbers)
# # majorNum = reduce(lambda x,y: x if x > y else x, numbers)
# print(majorNum)

# from dataclasses import dataclass
#
#
# @dataclass
# class PunktData:
#     x: int
#     y: int
#
#
# class BrakPunktowZyciaError(Exception):
#     pass
#
#
# class NieujemnaLiczba:
#     def __set_name__(self, owner, name):
#         self._name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self._name, 0)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             value = 0
#         instance.__dict__[self._name] = value
#
#
# class IteratorEkwipunku:
#     def __init__(self, items):
#         self._items = items
#         self._index = 0
#
#     def __next__(self):
#         if self._index >= len(self._items):
#             raise StopIteration
#
#         item = self._items[self._index]
#         self._index += 1
#         return item
#
#     def __iter__(self):
#         return self
#
#
# class Ekwipunek:
#     def __init__(self, items=None):
#         self._items = items if items is not None else []
#
#     def __iter__(self):
#         return IteratorEkwipunku(self._items)
#
#     def addItem(self, item):
#         self._items.append(item)
#
#     def __repr__(self):
#         return f"Ekwipunek({self._items})"
#
#     def showItems(self):
#         for item in self:
#             print(item)
#
#
# @total_ordering
# class Gracz:
#     liczba_graczy = 0
#
#     def liczba():
#         print(f"Liczba graczy: {Gracz.liczba_graczy}")
#
#     @staticmethod
#     def sprawdz_poprawnosc_imienia(imie):
#         if imie is None:
#             return False
#         else:
#             return True
#
#     def __eq__(self, other):
#         if isinstance(other, Gracz):
#             if self.imie == other.imie:
#                 return True
#             else:
#                 return False
#         else:
#             print("Obiekty sa inne")
#
#     def __init__(self, imie="Gracz", hp="100"):
#         self.imie = imie
#         self._hp = hp
#         self.ekwipunek = Ekwipunek()
#         Gracz.liczba_graczy += 1
#
#     def __lt__(self, other):
#         if not isinstance(other, Gracz):
#             return NotImplemented
#         return self.hp < other.hp
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, wartosc):
#         if wartosc < 0:
#             self._hp = 0
#         else:
#             self._hp = wartosc
#
#     def __str__(self):
#         return f"{self.imie} {self.hp}"
#
#     def __repr__(self):
#         return f"Gracz(imie={self.imie},hp={self.hp})"
#
#     def status(self):
#         print(f"Gracz | {self.imie} | {self.hp} HP |")
#
#     def getDamage(self):
#         a = random.randint(1, 25)
#         self.hp -= a
#         print(f"{self.imie} otrzymal {a} obrazenia!")
#
#
# class Wojownik(Gracz):
#     sila = NieujemnaLiczba()
#
#     @classmethod
#     def stworz_berserka(cls, imie):
#         return cls(imie, 200, 1.25)
#
#     def __init__(self, imie="Marek", hp="200", sila=1.5):
#         super().__init__(imie, hp)
#         self.sila = sila
#
#     def __add__(self, other):
#         return Wojownik(imie=self.imie + other.imie, hp=self.hp + other.hp, sila=self.sila + other.sila)
#
#     def __str__(self):
#         return f"{super().__str__()} {self.sila}"
#
#     def atakuj(self):
#         if self.hp > 0:
#             print(f"{self.imie} atakuje!")
#         else:
#             raise BrakPunktowZyciaError(f"{self.imie} nie moze atakowac!")
#
#     def status(self):
#         super().status()
#         print(f"      |Moja sila wynosi: {self.sila}|")
#
#     def attack(self):
#         super().attack() * self.sila
#
#     def attack(self):
#         a = random.randint(10, 35) * self.sila
#         print(f"{a} zadanych obrazen!")
#
#
# class Mag(Gracz):
#     mana = NieujemnaLiczba()
#
#     def __init__(self, imie="Franek", hp="75", mana=250):
#         super().__init__(imie, hp)
#         self.mana = mana
#
#     def status(self):
#         super().status()
#         print(f"      |Moja mana wynosi: {self.mana}|")
#
#     def castSpell(self):
#         b = random.randint(1, 10)
#         self.mana -= b
#         a = random.randint(20, 30) + b
#         print(f"{a} zadanych obrazen! Koszt many: {b}")


# gracz1 = Gracz("Jerzy", 100)
# gracz1.status()
# gracz1.__str__()
# print(gracz1.__str__())
# print(gracz1.__repr__())
# gracz1.getDamage()
# gracz1.status()
# print(gracz1.__str__())
# print(gracz1.__repr__())
# print(Gracz.liczba_graczy)
# gracz2 = Gracz("Maurycy", 200)
# Gracz.liczba()
# gracz3 = Wojownik("Adam", 200, 1.5)
# gracz3.status()
# gracz3.attack()
# gracz4 = Mag("Franek", 75,300)
#
# druzyna = [gracz1, gracz2, gracz3,gracz4]
# for gracz in druzyna:
#     gracz.status()

# gracz5 = Gracz("Jerzy", 100)
# gracz5.hp = -20
# gracz5.status()

# gracz6 = Gracz("Barbara", 250)
# gracz6.ekwipunek.addItem("miecz")
# gracz6.ekwipunek.addItem("prowiant")
# gracz6.ekwipunek.addItem("kilof")
# gracz6.ekwipunek.showItems()

# gracz7 = Wojownik.stworz_berserka("Marek")
# gracz7.status()
#
# gracz8 = Gracz("Anastazy",25)
#
# k = Gracz.sprawdz_poprawnosc_imienia(gracz8.imie)
# print(k)
#
# graczA = Gracz("Adam",100)
# graczB = Gracz("Adam",100)
#
# graczC = Wojownik("Cecylia",125,1.1)
# graczD = Wojownik("Bogumil",100,1.2)
#
# graczE = graczD + graczC
# print(graczA == graczB)
# print(graczE)
# gracz1 = Gracz("Jerzy", 100)
# gracz2 = Gracz("Maurycy", 200)
# gracz3 = Wojownik("Adam", 200, 1.5)
# gracz4 = Mag("Franek", 75,300)
#
# druzyna = [gracz1, gracz2, gracz3, gracz4]
#
# posortowani = sorted(druzyna)
# for g in posortowani:
#     print(g)
# w = Wojownik("Adam", 200, sila=-50)
# m = Mag("Zenek", 75, mana=-999)
#
# print(w.sila)   # 0
# print(m.mana)
# gracz52 = Wojownik("Bryniek",0, 2.4)
# gracz52.atakuj()
# gracz0 = Gracz("Jelezaweta",68)
# graczV = Gracz("Wukong",1500)
# print(gracz0 == graczV)
# print(gracz0 != graczV)
# print(gracz0 <= graczV)
# print(gracz0 >= graczV)
# eq = Ekwipunek()
# eq.addItem("miecz",0)
# eq.addItem("luk",1)
# eq.addItem("prowiant",2)
# eq.showItems()
# eq = Ekwipunek()
# eq.addItem("miecz")
# eq.addItem("luk")
# eq.addItem("prowiant")
# eq.showItems()
# for item in eq:
#     print(next(item))
#
# class Bron:
#     dostepne_ulepszenia = []
#
#     def __init__(self, nazwa):
#         self.nazwa = nazwa
#
#     def dodaj_ulepszenie(self, ulepszenie):
#         self.dostepne_ulepszenia.append(ulepszenie)
#
#     def __repr__(self):
#         return f"{self.nazwa} (ulepszenia: {self.dostepne_ulepszenia})"
#
# class Miecz(Bron): pass
# class Topor(Bron): pass
#
# miecz = Miecz("Stalowy Miecz")
# topor = Topor("Krasnoludzki Topór")
# print(f"Przed modyfikacją: {miecz}, {topor}")
# miecz.dodaj_ulepszenie("Ostrzenie")
# print(f"Po modyfikacji: {miecz}, {topor}")

# class PunktLekki:
#     __slots__=('x','y')
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __dict__(self):
#         return {"x":self.x, "y":self.y}
#
# p = PunktLekki(1,2)
# print(p.x)
# print(p.y)
# p.z = 3
# print(p.z)
# print(p.__dict__)

# plik = open("dziennik.txt","w")
# plik.write("Pierwszy wpis\n")
# plik.write("Wszystko dziala?\n")
# plik.close()
#
# plik = open("dziennik.txt","r")
# zawartosc = plik.read()
# plik.close()
# print(zawartosc)
#
# plik = open("dziennik.txt","a")
# plik.write("Dodaje kolejną linię")
# plik.close()
#
# plik = open("dziennik.txt","r")
# a = plik.read()
# plik.close()
# print(a)
# def oblicz_rok_urodzenia(sciezka):
#     try:
#         with open(sciezka,"r") as file:
#             try:
#                 a = int(file.read())
#                 print(f"Twoj rok urodzenia to: {2025-a}")
#             except ValueError:
#                 print("BLAD, Zawartosc liku nie jest poprawna liczba!")
#     except FileNotFoundError:
#         print("BLAD, Nie znaleziono pliku!")
#
# sciezka = "wiek.txt"
# with open(sciezka,"w") as file:
#     file.write("25")
#     file.close()
#
# oblicz_rok_urodzenia(sciezka)

# with open("dziennik_with.txt","w") as f:
#     f.write("Test1")
#
# with open("dziennik_with.txt","r") as f:
#     a = f.read()
#     print(a)
#
# with open("dziennik_with.txt","a") as f:
#     f.write("\nTest2")
#
# with open("dziennik_with.txt","r") as f:
#     a = f.read()
#     print(a)

# class NiepoprawnaIloscProduktuError(ValueError):
#     pass
#
# def dodaj_do_koszyka(produkt,ilosc):
#     try:
#         if ilosc <= 0:
#             raise NiepoprawnaIloscProduktuError("Ilosc produktow musi byc dodatnia!")
#         else:
#             print("Dodano do koszyka!")
#     except NiepoprawnaIloscProduktuError as e:
#         print(f"BLAD! {e}")
#
# dodaj_do_koszyka("Maslo",-2)

# class MiernikCzasu:
#     def __enter__(self):
#         self.start = (time.perf_counter())
#         print("Rozpoczynam pomiar")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.koniec = time.perf_counter() - self.start
#         print(round(self.koniec,2))
#
# with MiernikCzasu() as m:
#     suma = sum(n for n in range(100000000))

# class BezpiecznyZapis:
#     def __init__(self,sciezka):
#         with open("sciezka.tmp",'w') as f:
#             self.sciezka = f
#
#     def __enter__(self):
#         f = open("sciezka.tmp","w")
#         f.write(str(self.sciezka))
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         f.close()
#         if exc_type is None:
#             os.rename("sciezka.tmp",self.sciezka)
#         else:
#             os.remove("sciezka.tmp")
#
# with open("konfiguracja.txt","w") as f:
#     f.write("Colowiek\nJeszcze\nHaslo123456372796231")
#
# with BezpiecznyZapis("konfiguracja.txt") as f:
#     f.write("Cos nowego")
# try:
#     with open("log.txt","r", encoding="utf-8") as f:
#         a = 0
#         for line in f:
#             if "ERROR" in line:
#                 a = a + 1
#     print(a)
# except FileNotFoundError:
#     print("BLAD, Nie znaleziono pliku!")

# class IgnorujBledy:
#     def __init__(self):
#         self.bledy_do_ignorowania = (ValueError,TypeError)
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type.issubclass(self.bledy_do_ignorowania):
#             return True
#         else:
#             return False
#
# with IgnorujBledy((ValueError,TypeError)) as ignoruj:
#     int("abc")

# from pathlib import Path
# import datetime
#
# folder = Path('Raporty_Dzienne')
# sciezka = folder / f"{datetime.date.today()}" / "raport.txt"
# sciezka.parent.mkdir(parents=True, exist_ok=True)
# tresc = f"Raport testowy {datetime.date.today()}"
# sciezka.write_text(tresc, encoding="utf-8")
# content = sciezka.read_text(encoding="utf-8")
# print(content)
# import pickle
#
# class StanGry():
#     def __init__(self, nazwa_gracza: str = "Gracz", punkty: int = 10, ekwipunek: list = ["kilof"]):
#         self.nazwa_gracza = nazwa_gracza
#         self.punkty = punkty
#         self.ekwipunek = ekwipunek
#
#     def __repr__(self):
#         return f"{self.nazwa_gracza} {self.punkty} {self.ekwipunek}"
#
# Gracz1 = StanGry()
# print(Gracz1)
#
# with open("stan_gry.pkl", "wb") as f:
#     pickle.dump(Gracz1,f)
#
# with open("stan_gry.pkl", "rb") as f:
#     wczytany_stan = pickle.load(f)
#     print(wczytany_stan)
#     print(type(wczytany_stan))

# import csv
#
# def wczytaj_pracownikow(sciezka_pliku: str):
#     wyniki = []
#
#     try:
#         with open(sciezka_pliku, "r", newline="", encoding="utf-8") as f:
#             reader = csv.DictReader(f)
#
#             for nr_wiersza, wiersz in enumerate(reader, 2):
#                 try:
#                     wiersz['pensja'] = int(wiersz['pensja'])
#                     wyniki.append(wiersz)
#                 except ValueError:
#                     print(f"Ostrzeżenie: błędna pensja w wierszu {nr_wiersza}")
#                 except KeyError:
#                     print(f"Duże ostrzeżenie: brak kolumny w wierszu {nr_wiersza}")
#
#     except FileNotFoundError:
#         print("Nie ma pliku!")
#
#     return wyniki
#
#
# pracownicy = wczytaj_pracownikow("pracownicy.csv")
# print(pracownicy)

# import csv
#
# sprzedaz = [
#     {"produkt":"Jablko","sprzedana_ilosc":8732198,"przychody":100000000},
#     {"produkt":"Samochiod","sprzedana_ilosc":8,"przychody":120000},
#     {"produkt":"Wiaderko","sprzedana_ilosc":372,"przychody":9920},
# ]
#
# def zapisz_raport_sprzedazy(sciezka_pliku: str, dane: list):
#     if dane == []:
#         print("Pusto!")
#     else:
#          pobieram_dane = list(dane[0].keys())
#          with open(sciezka_pliku, "w", newline="",encoding="utf-8") as f:
#             writer = csv.DictWriter(f, fieldnames=pobieram_dane)
#             writer.writeheader()
#             writer.writerows(dane)
#
# zapisz_raport_sprzedazy("raport.csv",sprzedaz)

# import json
#
# def wczytaj_konfiguracje(sciezka_pliku:str):
#     try:
#         with open(sciezka_pliku,"r",encoding="utf-8") as f:
#             dane = json.load(f)
#             return dane
#     except FileNotFoundError:
#         print("Nie moge znalesc pliku!")
#     except json.JSONDecodeError:
#         print("Problem z formaten JSON")
#
# a = wczytaj_konfiguracje("konfiguracja.json")
# print(type(a))

# moje_dane = {
#     "ulubiony_kolor":"niebieski",
#     "ulubiona_potrawa":"barszcz",
#     "ulubione_zwierze":"Pies",
# }
#
# def zapisz_jako_json(dane, sciezka):
#     try:
#         with open(sciezka, "w", encoding="utf-8") as f:
#             json.dump(dane, f, ensure_ascii=False, indent=4)
#     except IOError:
#         print("Problem z zapisem na dysku!")
#
# zapisz_jako_json(moje_dane, "plik.json")

# import json
# from pydantic import BaseModel, ValidationError
#
# class SpecyfikacjaModel(BaseModel):
#     procesor: str
#     ram_gb: int
#
# class ProduktModel(BaseModel):
#     nazwa_produktu: str
#     id_produktu: str
#     cena: float
#     dostepny: bool
#     tagi: list[str]
#     specyfikacja: SpecyfikacjaModel
#
#
# def wczytaj_i_waliduj_produkt(sciezka: str) -> "ProduktModel | None":
#     try:
#         with open(sciezka, "r", encoding="utf-8") as f:
#             dane = json.load(f)
#         try:
#             # Pydantic v2 fallback (jeśli parse_obj nie istnieje)
#             return ProduktModel.model_validate(dane)
#
#         except FileNotFoundError:
#             print(f"Błąd: nie znaleziono pliku: {sciezka}")
#             return None
#         except json.JSONDecodeError:
#             print(f"Błąd: niepoprawny format JSON w pliku: {sciezka}")
#             return None
#         except ValidationError as e:
#             print("Błąd walidacji danych:")
#             print(e)
#             return None
#
#
# # --- TEST (b) ---
# produkt = wczytaj_i_waliduj_produkt("produkt.json")

# listaDict = [
#     {
#         "id": 1,
#         "name": "Jakub",
#         "email": "franek@gmail.con",
#         "phone": "+48277388299",}
# ]
#
# import io, csv
#
# def generuj_raport_csv_w_pamieci(dane: list[dict]):
#     plik_w_pamieci = io.StringIO()
#     pola = list(dane[0].keys())
#     writer = csv.DictWriter(plik_w_pamieci, fieldnames=pola)
#     writer.writeheader()
#     writer.writerows(dane)
#     plik_w_pamieci.seek(0)
#     return plik_w_pamieci
#
# def czytaj_zaw_plik(plik):
#     print(plik.read())
#
# a = generuj_raport_csv_w_pamieci(listaDict)
#
# czytaj_zaw_plik(a)

# import logging
# 
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     filename='parser.log',
#     filemode='w'
# )
# 
# linie_do_przetworzenia = ["INFO: Uruchomiono system","DEBUG: Sprawdza status","WARNING: Niski poziom baterii","ERROR: Nie mozna polaczyc z serwerem"]
# 
# def przetworz_logi(linie: list):
#     for x in linie:
#         x_clear = x.strip()
#         if x.startswith("INFO"):
#             logging.info(x_clear.removeprefix("INFO: "))
#         elif x.startswith("DEBUG"):
#             logging.debug(x_clear.removeprefix("DEBUG: "))
#         elif x.startswith("WARNING"):
#             logging.warning(x_clear.removeprefix("WARNING: "))
#         elif x.startswith("ERROR"):
#             logging.error(x_clear.removeprefix("ERROR: "))
#         else:
#             logging.warning(f"Nierozpoznana linia {x_clear}")
# 
# przetworz_logi(linie_do_przetworzenia)
# with open("parser.log","r") as f:
#     print(f.read())

# class WlasnyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         biezaca_wartosc = self.start
#         while biezaca_wartosc < self.end:
#             yield biezaca_wartosc
#             biezaca_wartosc = biezaca_wartosc + 1


# class WlasnyRangeIterator:
#
#     def __init__(self, wlasny_range_obj):
#         self.wlasny_range_obj = wlasny_range_obj
#         self.biezaca_wartosc = wlasny_range_obj.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.biezaca_wartosc < self.wlasny_range_obj.end:
#             self.biezaca_wartosc+=1
#             return self.biezaca_wartosc
#         else:
#             raise StopIteration

# moj_zakres = WlasnyRange(1,837)
# for liczba in moj_zakres:
#     print(liczba)

# def czytaj_duzy_csv(sciezka_pliku: str):
#     with open(sciezka_pliku,"r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for wiersz in reader:
#             wiersz["wiek"] = int(wiersz["wiek"])
#             yield wiersz

# for osoba in czytaj_duzy_csv("dane.csv"):
#     if osoba["wiek"] > 40:
#         print(f"{osoba['imie']} {osoba['nazwisko']} ")

# osoby_po_30 = (x for x in czytaj_duzy_csv("dane.csv") if x["wiek"] > 30 )
# opis = (f"{y['imie']} {y['nazwisko']}".upper() for y in osoby_po_30)
# for z in opis:
#     print(z)

# sortedList = sorted(czytaj_duzy_csv("dane.csv"), key=lambda x: x["nazwisko"][0])
# group = groupby(sortedList,key=lambda x: x["nazwisko"][0])
# for litera, osoby_w_grupie in group:
#     suma_wiekow = 0
#     licznik = 0
#
#     for osoba in osoby_w_grupie:   # tu "zużywamy" iterator grupy
#         suma_wiekow += osoba["wiek"]
#         licznik += 1
#
#     srednia = suma_wiekow / licznik if licznik else 0
#     print(f"{litera}: {srednia:.2f}")

# iter_analiza1,iter_analiza2 = itertools.tee(czytaj_duzy_csv("dane.csv"),2)
# SortIter1 = sorted(iter_analiza1, key=lambda x: x["wiek"])
# for x in SortIter1:
#     if f"{x["imie"]}{x['nazwisko']}" < max:
#         max = f"{x["imie"]}{x['nazwisko']}"
#     else:
#         continue

# def czytaj_logi(sciezka: str):
#     with open(sciezka,"r") as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 yield line
#
# filtr1 = (linia for linia in czytaj_logi("logs.txt") if 400 <= int(linia.split()[-2]) <= 499)
#
# dane_ruchu = ((l.splir()[0], int(l.split()[1])) for l in filtr1)\
#
# posortowane_dane = sorted(dane_ruchu, key=itemgetter(0))
#
# ruch_per_ip = (
# (ip, sum(item[1] for item in grupa))
#     for ip, grupa in itert00pslfrubt)porotwojaje++daje, ket
# )

# def monitor_temperatury(prog_alarmowy):
#     try:
#         suma = 0
#         licznik = 0
#         srednia = 0
#         while(True):
#             odczyt = yield srednia
#             if odczyt is None:
#                 licznik = 0
#                 suma = 0
#             else:
#                 suma += odczyt
#                 licznik +=1
#                 srednia = suma/licznik
#                 if srednia >= prog_alarmowy:
#                     print("UWAGA, reaktor sie topi")
#     finally:
#         print(f"Czujnik wylaczony")
#
# gen = monitor_temperatury(100)
# next(gen)
#
# print(f"Aktualna srednia: {gen.send(None)}")
# print(f"Aktualna srednia: {gen.send(30)}")
# print(f"Aktualna srednia: {gen.send(90)}")
# print(f"Aktualna srednia: {gen.send(270)}")
# print(f"Aktualna srednia: {gen.send(30)}")
# print(f"Aktualna srednia: {gen.send(30)}")
# print(f"Aktualna srednia: {gen.send(3)}")
# print(f"Aktualna srednia: {gen.send(0.832567)}")

# def parsuj_logi(path:str)->dict:
#     with open(path,"r") as file:
#         line = file.read()
#         wzor1 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#         adres = re.findall(wzor1,line)
#         wzor2 = r'" (\d{3})'
#         kod = re.findall(wzor2,line)
#         return {f'adresy ip: {adres} kod: {kod}' }
#
# print(parsuj_logi("logi.txt"))

# def analizuj_czas_logow(path:str)->timedelta | None:
#     with open(path,"r") as file:
#         line = file.read()
#         data = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
#         gotowa_data = re.findall(data,line)
#         format = "%d/%b/%Y:%H:%M:%S"
#         objDateTime = [datetime.strptime(gotowa_date, format) for gotowa_date in gotowa_data]
#         if(objDateTime is None):
#             return None
#         min_czas = min(objDateTime)
#         max_czas = max(objDateTime)
#         timedelta = max_czas - min_czas
#         return timedelta
#
# print(analizuj_czas_logow("logi.txt"))

# import requests
# import threading
# import time
# import json
#
# def pobierz_kurs(waluta:str):
#     url = f"https://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
#     print("Rozpoczynanie pobierania")
#     response = requests.get(url)
#     response.raise_for_status()
#     dane = response.json()
#     kurs = dane['rates'][0]['mid']
#     print(f"{waluta} Kurs: {kurs}")
#     print("Koniec pobierania")
#
# waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']
#
# start_time = time.perf_counter()
#
# for waluta in waluty:
#     pobierz_kurs(waluta)
#
# end_time = time.perf_counter()
# czas_bez = end_time - start_time
# print(f"Pełen czas to: {czas_bez}")
#
# start_thread = time.perf_counter()
# watki = []
# for waluta in waluty:
#     t = threading.Thread(target=pobierz_kurs, args=(waluta,))
#     watki.append(t)
#     t.start()
#
# for t in watki:
#     t.join()
#
# end_thread = time.perf_counter()
# czas_thr = end_thread - start_thread
# print(f"Czas to: {czas_thr}")

# dostepne_bilety = 5
#
# def kub_bilet(kliend_id):
#     global dostepne_bilety
#     with blokada:
#         if dostepne_bilety>0:
#             dostepne_bilety -= 1
#             print(f"Klient {kliend_id} kupil bilet, zostalo {dostepne_bilety}")
#         else:
#             print(f"Klient {kliend_id} odszedl z kwitkiem")
#
# blokada: blokada = threading.Lock()
# watki = []
# for i in range(10):
#     t = threading.Thread(target=kub_bilet, args=(i,))
#     watki.append(t)
#
# for t in watki:
#     t.start()
#
# for t in watki:
#     t.join()

# def ciezka_praca(n: int) -> int:
#     return sum(range(n))
#
# if __name__ == "__main__":
#     dane = [100000000 + i for i in range(10)]
#     start_seq = time.perf_counter()
#     wynik_seq = [ciezka_praca(n) for n in dane]
#     end_seq = time.perf_counter()
#     print(f"Czas wykonania: {end_seq - start_seq}")
#
#     start_mult = time.perf_counter()
#     with multiprocessing.Pool() as pool:
#         wynik_mult = pool.map(ciezka_praca, dane)
#     end_mult = time.perf_counter()
#     print(f"Czas wykonania: {end_mult - start_mult}")

# async def pobierz_kurs(session, waluta):
#     async with session.get(f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json") as resp:
#         print("Rozpoczynanie pobierania")
#         dane = await resp.json()
#         kurs = dane['rates'][0]['mid']
#         print(f"{waluta} Kurs: {kurs}")
#         print("Koniec pobierania")
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']
#         zadania = [pobierz_kurs(session, waluta) for waluta in waluty]
#         waluty = await asyncio.gather(*zadania)
#
# asyncio.run(main())

# kolejka = queue.Queue()
# def producent():
#     for i in range(1,6):
#         kolejka.put(f"Zgloszenie {i}")
#         print(f"Dodano do kolejki zadanie: {i}")
#
# def konsument():
#     while True:
#         time.sleep(1)
#         zadanie = kolejka.get()
#         print(f"Przetwarzam zadanie: {zadanie}")
#         kolejka.task_done()
#
# if __name__ == "__main__":
#     w_konsumenta = threading.Thread(target=konsument)
#     w_producenta = threading.Thread(target=producent)
#     w_konsumenta.start()
#     w_producenta.start()
#     kolejka.join()
#     print("Koniec")

def pobierz_kurs(waluta:str):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    print("Rozpoczynanie pobierania")
    response = requests.get(url)
    response.raise_for_status()
    dane = response.json()
    kurs = dane['rates'][0]['mid']
    print(f"{waluta} Kurs: {kurs}")
    print("Koniec pobierania")

waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(pobierz_kurs, waluty)

end_time = time.perf_counter()
czas_thr = end_time - start_time
print(f"Czas to: {czas_thr}")