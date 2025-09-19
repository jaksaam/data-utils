# Linux Cheatsheet

## 📂 Navigacija
- `pwd` – prikaži trenutni direktorijum
- `ls` – lista fajlova
- `ls -l` – detaljan prikaz fajlova
- `ls -a` – prikaži i skrivene fajlove
- `cd <folder>` – promeni direktorijum
- `cd ~` – idi u home direktorijum
- `cd ..` – idi jedan nivo iznad

## 📜 Rad sa fajlovima
- `touch fajl.txt` – napravi prazan fajl
- `echo "tekst" >> fajl.txt` – dodaj tekst u fajl
- `cat fajl.txt` – prikaži ceo fajl
- `less fajl.txt` – pregled fajla sa skrolovanjem
- `head -n 5 fajl.txt` – prvih 5 linija
- `tail -n 5 fajl.txt` – poslednjih 5 linija

## 🔍 Pretraga u fajlovima
- `grep "tekst" fajl.txt` – traži linije koje sadrže "tekst"
- `grep -i "tekst" fajl.txt` – isto, ali ignoriše velika/mala slova
- `grep -r "tekst" ./` – traži rekurzivno kroz direktorijume

## ⚙️ Obrada teksta
- `awk '{print $1}' fajl.txt` – prikaži prvu kolonu
- `awk '{print $1, $3}' fajl.txt` – prikaži prvu i treću kolonu
- `sed 's/staro/novo/' fajl.txt` – zameni prvi pojavljeni string u svakoj liniji
- `sed 's/staro/novo/g' fajl.txt` – zameni sva pojavljivanja u liniji

## 🔒 Dozvole
- `ls -l` – prikaži dozvole fajlova
- `chmod 644 fajl.txt` – vlasnik čita/piše, ostali samo čitaju
- `chmod +x skripta.sh` – dodaj izvršnu dozvolu

## 🖥️ Procesi
- `top` – prikaži aktivne procese
- `htop` – napredniji pregled (instalacija: `sudo apt install htop`)
- `ps aux` – prikaži sve procese
- `kill <PID>` – ubij proces po ID-u

## 🔧 Servisi (systemd)
- `systemctl status <ime>` – status servisa
- `systemctl start <ime>` – pokreni servis
- `systemctl stop <ime>` – zaustavi servis
- `systemctl restart <ime>` – restartuj servis
- `systemctl enable <ime>` – uključi auto-start
- `systemctl disable <ime>` – isključi auto-start
