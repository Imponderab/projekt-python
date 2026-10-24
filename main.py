import argparse
from script import execute_paths

MIESIACE_NUM = {
    "styczen": 1, "luty": 2, "marzec": 3, "kwiecien": 4, "maj": 5, "czerwiec": 6,
    "lipiec": 7, "sierpien": 8, "wrzesien": 9, "pazdziernik": 10, "listopad": 11, "grudzien": 12
}
DNI_NUM = {"pn": 1, "wt": 2, "sr": 3, "czw": 4, "pt": 5, "sb": 6, "nd": 7}
KOLEJNOSC_DNI = ["pn", "wt", "sr", "czw", "pt", "sb", "nd"]


def main():
    parser = argparse.ArgumentParser(description="Główny skrypt zarządzający projektem")
    parser.add_argument("-m", "--miesiace", nargs="+", required=True)
    parser.add_argument("-d", "--dni", nargs="+", required=True)
    parser.add_argument("-p", "--pory", nargs="*", default=[])

    tryb_group = parser.add_mutually_exclusive_group(required=True)
    tryb_group.add_argument("-t", "--tworz", action="store_true")
    tryb_group.add_argument("-o", "--odczyt", action="store_true")

    parser.add_argument("-c", "--csv", action="store_true")
    parser.add_argument("-j", "--json", action="store_true")

    args = parser.parse_args()

    # Ustalanie typu plików (csv, json, lub oba naraz)
    if args.csv and args.json: filetype = 'both'
    elif args.json: filetype = 'json'
    else: filetype = 'csv'

    kody_partnera = []
    idx_pory = 0

    # Przetłumaczenie argumentów tekstowych na kody matematyczne
    for miesiac_str, zakres_dni_str in zip(args.miesiace, args.dni):
        month_num = MIESIACE_NUM.get(miesiac_str.lower(), 0)
        zakres = zakres_dni_str.lower().strip()

        if "-" in zakres:
            start, end = zakres.split("-")
            i_start, i_end = KOLEJNOSC_DNI.index(start), KOLEJNOSC_DNI.index(end)
            if i_start <= i_end:
                skroty = KOLEJNOSC_DNI[i_start : i_end + 1]
            else:
                skroty = KOLEJNOSC_DNI[i_start:] + KOLEJNOSC_DNI[: i_end + 1]
        else:
            skroty = [zakres]

        for skrot in skroty:
            day_num = DNI_NUM[skrot]
            if idx_pory < len(args.pory):
                time_num = 2 if args.pory[idx_pory].lower() in ["w", "wieczor", "wieczorem"] else 1
            else:
                time_num = 1

            kod = (time_num * 10 + day_num) * 100 + month_num
            kody_partnera.append(kod)
            idx_pory += 1

    # Wywołanie głównej logiki wyciągniętej z pliku script.py
    if args.tworz:
        execute_paths(kody_partnera, False, filetype)
        print(f"Pomyślnie wygenerowano pliki dla kodów: {kody_partnera}")
    elif args.odczyt:
        wynik = execute_paths(kody_partnera, True, filetype)
        print(f"Łączny czas dla Modelu A: {wynik}s")


if __name__ == "__main__":
    main()
