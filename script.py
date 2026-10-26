import json
import random
from pathlib import Path
from csv_handler import csv_read, csv_write

# Część zadania przeznaczona na osobę 2 (i 4)

# Funkcja dostaje liczbę 4 cyfrowych kodów reprezentujących ścieżki podane
# przez użytkownika o następującym składzie: cdmm (Czas / Dzień / Miesiąc Miesiąc)
# Funkcja odszyfrowuje kody i przekształca je na ścieżki.
# Zmienna bool is_reading zawiera informacje czy użytkownik chce odczytać
# wartości z plików w danych folderach czy utworzyć nowe.
# Zmienna Filetype zawiera informacje czy użytkownik chce operować na
# plikach typu json, csv czy obu. Może przyjąć wartości json, csv, both.

def execute_paths(path_list, is_reading, filetype='json'):
    exit_result = 0
    for structure in path_list:
        month = structure % 100
        if month == 1:
            month = 'Styczeń'
        elif month == 2:
            month = 'Luty'
        elif month == 3:
            month = 'Marzec'
        elif month == 4:
            month = 'Kwiecień'
        elif month == 5:
            month = 'Maj'
        elif month == 6:
            month = 'Czerwiec'
        elif month == 7:
            month = 'Lipiec'
        elif month == 8:
            month = 'Sierpień'
        elif month == 9:
            month = 'Wrzesień'
        elif month == 10:
            month = 'Październik'
        elif month == 11:
            month = 'Listopad'
        elif month == 12:
            month = 'Grudzień'
        else:
            month = 'InvalidMonth'
        structure //= 100
        day = structure % 10
        if day == 1:
            day = 'poniedziałek'
        elif day == 2:
            day = 'wtorek'
        elif day == 3:
            day = 'środa'
        elif day == 4:
            day = 'czwartek'
        elif day == 5:
            day = 'piątek'
        elif day == 6:
            day = 'sobota'
        elif day == 7:
            day = 'niedziela'
        else:
            day = 'invalidDay'
        structure //= 10
        if structure == 1:
            time = 'rano'
        elif structure == 2:
            time = 'wieczorem'  # przed mym domem wystawie ekran i wyświetlę film
        else:
            time = 'invalidTime'
        if (not month == 'invalidMonth') and (not day == 'invalidDay') and (not time == 'invalidTime'):
            # --- SEKCJA ODCZYTU ---
            if is_reading:
                if filetype in ['json', 'both']:
                    path = make_path('json', month, day, time)
                    exit_result += json_read(path)

                if filetype in ['csv', 'both']:
                    path = make_path('csv', month, day, time)
                    wynik_csv = csv_read(str(path.parent))
                    if wynik_csv is not None:
                        exit_result += wynik_csv  # Dodajemy zapisaną zmienną, by nie czytać pliku 2 razy

            # --- SEKCJA TWORZENIA ---
            elif filetype == 'json':
                path = make_path(filetype, month, day, time)
                json_write(path)
            elif filetype == 'csv':
                path = make_path(filetype, month, day, time)
                csv_write(str(path.parent))
            elif filetype == 'both':
                path_j = make_path('json', month, day, time)
                json_write(path_j)
                path_c = make_path('csv', month, day, time)
                csv_write(str(path_c.parent))

    if is_reading:
        return exit_result
    return None

# Funkcja składa odpowiednie nazwy katalogów, aby utworzyć ścieżkę.
# filetype = json / csv -> typ pliku, na którym będziemy działać
# month / day / time odpowiednie katalogi.

def make_path(filetype, month, day, time = 'rano'):
    path = Path(month)
    if not path.exists():
        path.mkdir()
    path /= day
    if not path.exists():
        path.mkdir()
    path /= time
    if not path.exists():
        path.mkdir()
    path /= 'Dane.' + filetype
    return path

# Funckja odczytuje wartość "Czas" pliku json o pozycji
# określonej zmienną path, jeżeli wartość 'Model' w tym pliku to 'A'
# Jeżeli plik o danej ścieżce nie istnieje, zwraca 0

def json_read(path, model = 'A'):
    if not path.exists():
        return 0
    with open(path, 'r') as file:
        data = json.load(file)
        time_word = data['Czas']
        time_int = 0
        if data['Model'] == model:
            for letter in time_word:
                if '0' <= letter <= '9':
                    time_int = time_int * 10 + int(letter) - int('0')
        return time_int

# Funkcja zapisuje losowo wygenerowane dane do pliku json
# o ścieżce zdefiniowanej przez zmienną path

def json_write(path):
    model = random.choice(['A', 'B', 'C'])
    result = random.randint(0, 1000)
    time = str(random.randint(0, 1000)) + 's'
    data = {
        'Model': model,
        'Wynik': result,
        'Czas': time
    }
    with open(path, 'w') as file:
        json.dump(data, file)