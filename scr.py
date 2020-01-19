import sys
import os


init_path = "C:\\Skrypty\\" # folder ze skryptami

def create():
    """Skrypt w pierwszej kolejności tworzy folder z podanych argumentów podczas uruchamiania.
    Jeśli jednak nie podano, to nazwę bierze z domyślnej wartości ze zmiennej folder.
    Następnie tworzy pusty plik pythona i uruchamia Visual Code z tym folderem.
    Dzięki dodaniu do path w windows, jest możliwe uruchomienie z każdego miejsca w systemie poleceniem:
    <nazwa_skryptu.py> <nazwa_folderu>
    """
    folder = "Skrypt_X"
    if len(sys.argv) > 1:
        folder = sys.argv[1] # jeżeli podano argument przy uruchomieniu, nadaje nim nazwę folderu
    path = init_path + folder
    os.mkdir(path) 
    os.chdir(path)
    open("run.py","w").close()
    os.system("code .")

if __name__ == "__main__":
    create()