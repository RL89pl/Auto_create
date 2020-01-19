### Auto_create
Projekt na blogu: [Automatyzacja projektow](https://rl89pl.github.io/pl/posts/automatyzacja_projektow/)


Trzeba szanować swój czas i w miarę możliwości automatyzować wszystko, co jest uciążliwe, monotonne, często powtarzalne. 
Postanowiłem ułatwić sobie pracę przy tworzeniu nowego projektu, a także szybkie rozpoczęcie pisania nawet testowego skryptu.

Przy tworzeniu projektu musiałbym wpierw utworzyć odpowiedni folder, zalogować się na github.com w celu utworzenia repozytorium, zainicjowanie go, utworzenie pliku README i przesłanie na platformę github. Dodatkowo utworzenie pustego pliku python i uruchomienie VS Code.
Trochę to czasu zajmuje, a gdyby to wszystko zastąpić wyłącznie komendą w `cmd`, lub `powershell` w formie komendy z dowolnego miejsca w systemie?
`pro.py Projekt`

### Uruchamianie skryptów

Aby uruchomić skrypt z dowolnego miejsca w systemie należy lokalizację folderu dodać do `PATH` - zmiennych środowiskowych systemu Windows.
Proponuję utworzyć folder, gdzie będą znajdować się wszystkie skrypty, które chcemy uruchomić w ten sposób.

1. W pierwszej kolejności w `Panelu sterowania` wybieramy `System`:
![System](/images/1.PNG) 
2. Następnie klikamy w `Zmienne środowiskowe`:
![Zmienne środowiskowe](/images/2.PNG) 
3. Wybieramy `Path` i edytujemy:
![Lista sieci](/images/3.PNG)
4. Dodajemy nowy wpis i podajemy pełną ścieżkę do folderu 
![Lista sieci](/images/4.PNG) 

Ważne, by ustawić uruchamianie plików `.py` bezpośrednio przez `Python` (właściwości -> uruchamiany jako `Python`)

### Skrypt do tworzenia projektów

Zgodnie z tym, co wypisałem na początku, chcemy utworzyć folder z nowym projektem, utworzyć repozytorium, przesłać go do githuba, 
oraz utworzyć pliki readme i skryptu wraz z otwarciem VS Code w folderze.

Do tworzenia miejsca dla naszego repozytorium na githubie, przyda nam się biblioteka [PyGithub](https://pygithub.readthedocs.io/en/latest/index.html)
`pip install PyGithub`

