import os
import random
from typing import Optional


# odpowiedzialność Osoby 3 wedug proponowanego podziału

# "Tworzy zapis do pliku csv"
# Tworzy plik Dane.csv w podanym folderze
# Plik jest dwuliniowy postaci: nagłówek i odpowiednio losowane dane
def csv_write(sciezka_folderu: str) -> str:
    # Upewniam się, że folder istnieje
    os.makedirs(sciezka_folderu, exist_ok=True)
    sciezka_pliku = os.path.join(sciezka_folderu, "Dane.csv")

    # Losuję wartości z zadanych przedziałów
    model = random.choice(["A", "B", "C"])  # Model w {A, B, C}
    wynik = random.randint(0, 1000)         # Wynik   0-1000
    czas = f"{random.randint(0, 1000)}s"    # Czas 0-1000s

    # Formatuję zgodnie z zadaniem
    naglowek = "Model; Wynik; Czas;\n"
    dane = f"{model} ; {wynik} ; {czas};\n"

    with open(sciezka_pliku, "w", encoding="utf-8") as f:
        f.write(naglowek)
        f.write(dane)

    return sciezka_pliku



# "Tworzy odczyt z pliku csv"
# Zwraca czas z pliku Dane.csv TYLKO jeśli Model == 'A'.
# W przeciwnym wypadku zwraca 0. Jeśli plik nie istnieje, zwraca None
def csv_read(sciezka_folderu: str) -> Optional[int]:
    sciezka_pliku = os.path.join(sciezka_folderu, "Dane.csv")

    # Gdy pliku nie ma na dysku
    if not os.path.exists(sciezka_pliku):
        return None

    with open(sciezka_pliku, "r", encoding="utf-8") as f:
        linie = [l.strip() for l in f.readlines() if l.strip()]

    # Jeśli plik jest pusty lub uszkodzony
    if len(linie) < 2:
        return 0

    # Rozbijam drugi wiersz po średnikach
    # np. "A ; 17 ; 465s;" -> ['A', '17', '465s']
    wartosci = [w.strip() for w in linie[1].split(";") if w.strip()]

    if len(wartosci) >= 3:
        model = wartosci[0]
        czas_str = wartosci[2]

        # Interesuje mnie tylko i wyłącznie Model A
        if model == "A":
            # Usuwam 's' z końca i zamienieniam tekst na liczbę
            return int(czas_str.rstrip("s"))

    return 0
