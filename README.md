# Testy pierwszości

# uruchomienie z pliku wykonywalnego

plik wykonywalny został utworzony na dwa sposoby - jako jeden plik oraz jako folder, w każdym przypadku należy dwukrotnie kliknąć na plik GUI2.exe, by uruchomić aplikację

# uruchomienie z plików źródłowych
By urochomić projekt należy zainstalować python3 oraz wykonać komendę

python GUI2.py

wymagane paczki

pyqt5 - instalacja komendą

pip install PyQt5

# Jak korzystać z aplikacji
By sprawdzić pierwszość danej liczby można wpisać ją w polę "liczba". Można ją także wygenerować losowo z predefiniowanego zakresu.
Można także wybrać liczbę iteracji, którą będzie wykonywał algorytm. Po kliknięciu w przycisk "Rozpocznij test" algorytm testuje pierwszość algorytmami Solovaya-Strasena oraz Milera-Rabina.
Po kliknięciu w przycisk "Pokaż szczegóły" pokażą się istotnie fragmenty każdego algorytmu, lecz trzeba wygenerować odpowiedzi jeszcze raz.

W osobnych oknach pojawiają się kolejne iteracje algorytmów: wylosowane liczby, które są potencjalnymi świadkami złożoności wybranej liczby oraz wynik algorytmu. Na koniec zliczane jest prawdopodobieństwo pierwszeństwa danej liczby, które jest podane pod każdym oknem.

Po kliknięciu w przycisk "zaawansowane opcje" w prawym dolnym rogu można zadań zakres losowanych liczb a także wymusić pierwszą liczbę, która zostanie wylosowana. Liczba ta musi być z podanego zakresu.

