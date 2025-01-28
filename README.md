# Testy pierwszości

Repozytorjum skrypty prostej aplikacji, której zadaniem jest sprawdzenie, czy liczba jest pierwsza za pomocą algorytmów Solovaya-Strasena oraz Milera-Rabina. Została zrobiona na potrzeby studiów Automatyki i Robotyki w Akademi Górniczo Hutniczej. Interfejs zastał zrobiony za pomocą biblioteki PyQt5.
<p align="center">
<img src=".\zdjęcia\gui1.JPG" alt="a1" width="600" height="auto">
</p>

# Jak korzystać z aplikacji
Do sprawdzenia pierwszości liczby należy wisać ją w pole "Liczba". Można ją także wygenerować losowo z predefiniowanego zakresu. Można także wybrać liczbę iteracji, którą będzie wykonywał algorytm. Od niej zależy prawdopodobieństwo poprawności wyniku. Po kliknięciu w przycisk "Rozpocznij test" aplikacja testuje pierwszość algorytmami Solovaya-Strasena oraz Milera-Rabina.
Po kliknięciu w przycisk "Pokaż szczegóły" pokażą się istotnie fragmenty każdego algorytmu, ale trzeba wygenerować odpowiedzi jeszcze raz.

W osobnych oknach pojawiają się rezultaty obu algorytmów: 
 - numer iteracji <i>k</i>,
 - wylosowane liczby, które są potencjalnymi świadkami złożoności <i>a</i>,
 - oraz wynik algorytmu.

Prawdopodobieństwo pierwszeństwa danej liczby jest podane pod każdym oknem.

<p float="center">
  <img src=".\zdjęcia\gui2.JPG" alt="a2" width="400" height="auto">
  <img src=".\zdjęcia\gui3.JPG" alt="a3" width="400" height="auto">
</p>

Po wybraniu opcji pokaż szczegóły pokazują się też istotne kroki algorytmów oraz ich wyniki. Jeśli <i>x</i> lub <i>y</i> są równe 1 lub n-1, to liczba jest pierwsza. W przeciwnym razie jest złożona.

<p float="center">
  <img src=".\zdjęcia\gui5.JPG" alt="a5" width="400" height="auto">
  <img src=".\zdjęcia\gui4.JPG" alt="a4" width="400" height="auto">
</p>

Po kliknięciu w przycisk "zaawansowane opcje" w prawym dolnym rogu można zmienić zakres losowanych liczb a także wymusić pierwszego śwaidka złożoności <i>a</i>, który zostanie wylosowany. Musi być z podanego zakresu.

<p align="center">
<img src=".\zdjęcia\gui6.JPG" alt="a6" width="600" height="auto">
</p>


