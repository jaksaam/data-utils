"""

Simple log parser utility.

Usage: 

 python3 src/parse_logs.py --file data/sample_logs.csv --num 10

"""

import argparse  # parsiranje komandne linije (--file, --format, itd.)
import pandas as pd  # pandas za lakse citanje CSV I JSON fajlova, jednostavno citanje N redova i mocne funkcije za analizu podataka

def parse_csv(file_path, num_rows):  # definicija funkcije parse_csv, primanje 2 parametra, putanja do csv fajla i broj redova za prikaz
    df = pd.read_csv(file_path)    # Čita CSV fajl sa zadate putanje, pretvara ga u DataFrame (pandas tabelu) i čuva rezultat u promenljivoj df
    print(df.head(num_rows))   # Uzimanje prvih num_rows redova iz tabele i ispisuje ih na ekran

def parse_json(file_path, num_rows):   # Definisanje fukncije parse_json 
    df = pd.read_json(file_path, lines=True)  # Radi i za običan JSON i za NDJSON, i cita ih na dva nacina, obican json i ndjson za log fajlove
    print(df.head(num_rows)) # Uzimanje prvih N redova i ispis istih


def main():  # Glavna funkcija programa, parsira arguemnte, poziva odgovarajuce funkcije
    parser = argparse.ArgumentParser(description="Parse CSV or JSON logs")  # Kreira parser za komandnu liniju, i description kada korisnik unese help da dobije tekst
    parser.add_argument("--file", required=True, help="Path to log file (CSV or JSON)")  # Dodavanje argumenata, obavezan argument i help 
    parser.add_argument("--num", type=int, default=10, help="Number of rows to show") # Dodavanje argumenata, konvertovanje u brojeve, po default 10 redova ako se ne naglasi i help
    args = parser.parse_args()   # Parsiranje argumenata iz komandne linije i cuva ih u args objekat 

# Uslovna logika da zna sta da izbaci, zavisi koji je tip od ova dva i nepostojeci ako korisnik unese nesto sto ne postoji.
    if args.file.endswith(".csv"):
        parse_csv(args.file, args.num)
    elif args.file.endswith(".jsonl"):
        parse_json(args.file, args.num)
    else:
        print("Unsupported file format. Use CSV or JSON.")

if __name__ == "__main__":  # Garancija da se main pokrece samo kad se pokrene skripta direknto
    main()  #  Ne dozvoljava da se main pokrece ako se uvozi fajl u drugi fajl

