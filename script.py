import json
import random
from pathlib import Path

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
    print(json_read(Path("Luty")))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
