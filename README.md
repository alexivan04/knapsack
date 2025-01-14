# README - Proiect Analiza Algoritmilor: Problema Rucsacului

## Conținutul Arhivei

Această arhivă conține implementarea proiectului "Problema Rucsacului", realizată de Ivan Alexandru, Trufaș Rareș și Stîngă Cristina - grupa 322CC, Facultatea de Automatică și Calculatoare, Universitatea POLITEHNICA București. Structura arhivei este următoarea:

```
- knapsack.py                    # Fișierul sursă cu implementarea algoritmilor
- /tests
    - /category1               # Set de teste pentru categoria 1
    - /category2               # Set de teste pentru categoria 2
- requirements.txt             # Fișier cu dependințele proiectului
- README.md                   # Acest fișier
```

## Cum se pot evalua soluțiile

Pentru a rula și evalua soluțiile implementate, urmați pașii de mai jos:

### Cerințe preliminare

1. Asigurați-vă că aveți instalat Python 3.14 sau o versiune compatibilă.
2. Instalați eventualele pachete suplimentare utilizând comanda:
   ```bash
   pip install -r requirements.txt
   ```
   *(Notă: Fișierul requirements.txt va fi prezent doar dacă sunt dependințe externe.)*

### Pași pentru rulare

1. Rulați fișierul `knapsack.py` pentru a testa algoritmii implementați, pe setul de date deja dat:
   ```bash
   python knapsack.py
   ```
   Acesta va rula algoritmii pe seturile de date de testare și va afișa rezultatele obținute.
   Outputul se va afla in folderul `outputs/`.

2. Pentru a genera un nou set de date, rulați scriptul de generare a testelor:
   ```bash
   python generate_tests.py
   ```
   Acesta va crea un set de teste nou, pe care îl puteți folosi pentru a evalua algoritmii.
   Puteti, de asemenea, modifica valorile din script pentru a genera teste custom.

   ```python
    num_tests = 30         # Numarul de teste de generat
    max_items = 32         # Numarul maxim de obiecte
    max_capacity = 200     # Capacitatea maxima a rucsacului
    max_weight = 40        # Greutatea maxima a unui obiect
    max_value = 50         # Valoarea maxima a unui obiect


## Modul de Generare a Testelor

Testele au fost concepute pentru a asigura o acoperire exhaustivă a posibilelor scenarii de execuție, luând în considerare următoarele categorii:

1. **Categoria 1:**
   - Număr variabil de obiecte (n) și capacitate fixă (G).
   - Testele au fost generate prin selectarea unor greutăți și valori aleatorii pentru obiecte, într-un interval prestabilit (e.g., greutăți între 1 și 50, valori între 10 și 500).

2. **Categoria 2:**
   - Capacitate variabilă (G) și număr fix de obiecte (n).
   - Obiectele au fost generate aleatoriu, iar capacitățile rucsacului au fost setate astfel încât să varieze de la limite mici (e.g., 10) la valori mari (e.g., 1000), pentru a testa limitele algoritmilor.

### Metodologie de Generare

- Am utilizat un script Python dedicat, care generează automat testele pe baza unor parametri configurați:
  - Numărul de obiecte.
  - Intervalele de greutăți și valori.
  - Capacitatea maximă a rucsacului.
- Scriptul creează fișiere de testare în format text, fiecare conținând:
  - Prima linie: numărul de obiecte și capacitatea rucsacului.
  - Liniile următoare: greutatea și valoarea fiecărui obiect.

### Exemple

Un exemplu de fișier generat pentru categoria 1:
```
5 50
10 60
20 100
30 120
40 160
50 200
```
Acesta definește 5 obiecte și o capacitate a rucsacului de 50.

Testele acoperă scenarii precum:
- Obiecte cu greutăți și valori similare (pentru testarea diferențelor minore în decizii).
- Obiecte foarte mici sau foarte mari în raport cu capacitatea rucsacului.
- Capacități variabile care forțează algoritmii să ia decizii bazate pe eficiență (valoare/greutate).

## Surse Externe Utilizate

Pe parcursul dezvoltării acestui proiect, am consultat următoarele surse:

1. **Probleme de algoritmi**: 
   - [PbInfo: Rucsac1](https://www.pbinfo.ro/probleme/1886/rucsac1)
   - [Infoarena: Rucsac](https://www.infoarena.ro/problema/rucsac)

2. **Materiale de învățare:**
   - [GeeksForGeeks: Introduction to Knapsack Problem](https://www.geeksforgeeks.org/introduction-to-knapsack-problem-its-types-and-how-to-solve-them/)

3. **Resurse universitare**:
   - Cursuri și laboratoare de la Facultatea de Automatică și Calculatoare.

## Notă Finală

Proiectul oferă o analiză detaliată a metodei de rezolvare a problemei rucsacului, folosind trei algoritmi principali: programare dinamică, backtracking și greedy. Pentru detalii suplimentare despre implementare și rezultatele obținute, consultați fișierul `docs/raport_proiect.pdf`.

