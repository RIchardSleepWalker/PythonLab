def dodaj(a:int,b:int) -> int:
    return a+b

def dziel(a:int,b:int) -> float:
    try:
        return a/b
    except ValueError:
        return 0

def srednia(liczby: list[float]) -> float | None:
    if liczby == []:
        return None
    else:
        return sum(liczby)/len(liczby)