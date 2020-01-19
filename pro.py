import sys
import os
from github import Github

init_path = "C:\\Projekty\\" # folder z projektami
username = "XYZ" # login github
password = "12345"    # hasło github

def create():
    """Skrypt w pierwszej kolejności tworzy folder z podanych argumentów podczas uruchamiania.
    Jeśli jednak nie podano, to nazwę bierze z domyślnej wartości ze zmiennej folder.
    Następnie inicjuje repozytorium git, tworzy na githubie repo z nazwą folderu, 
    tworzy plik README.md i wysyła.
    Na koniec tworzy pusty plik pythona i uruchamia Visual Code z tym folderem.
    Dzięki dodaniu do path w windows, jest możliwe uruchomienie z każdego miejsca w systemie poleceniem:
    <nazwa_skryptu.py> <nazwa_projektu>
    """
    folder = "Projekt_X"
    if len(sys.argv) > 1:
        folder = sys.argv[1] # jeżeli podano argument przy uruchomieniu, nadaje nim nazwę folderu
    path = init_path + folder
    os.mkdir(path) 
    os.chdir(path)
    user = Github(username, password).get_user()
    repo = user.create_repo(folder)
    os.system("git init")
    os.system("git remote add origin https://github.com/UZYTKOWNIK/{}.git".format(folder))
    with open("README.md","w") as f:
        f.write("### "+folder)
    os.system("git add .")
    os.system('git commit -m "initial commit"')
    os.system("git push -u origin master")
    open("main.py","w").close()
    os.system("code .")

if __name__ == "__main__":
    create()