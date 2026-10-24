import json
import random
from pathlib import Path

def execute_paths(paths, is_reading, filetype = 'json'):
    exit_result = 0
    for structure in paths:
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
            month = 'Lipiec'
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
            time = 'wieczorem' # przed mym domem wystawie ekran i wyświetle film
        else:
            time = 'invalidTime'
        if (not month == 'invalidMonth') and (not day == 'invalidDay') and (not time == 'invalidTime'):
            path = make_path(filetype, month, day, time)
            if is_reading:
                exit_result += json_read(path)
            else:
                json_write(path)
    if is_reading:
        return exit_result
    return None

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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paths = [1112, 1704, 1821, 2303]
    print(execute_paths(paths, True))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
