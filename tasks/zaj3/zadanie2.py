# -*- coding: utf-8 -*-


def merge(path1, path2, out_file):
    """
    Funkcja pobiera nazwy dwóch plików z n-gramami (takie jak w poprzedmim
    zadaniu) i łączy zawartość tych plików i zapisuje do pliku w ścieżce ``out``.

    Pliki z n-gramami są posortowane względem zawartości n-grama.

    :param str path1: Ścieżka do pierwszego pliku
    :param str path2: Ścieżka do drugiego pliku
    :param str out_file:  Ścieżka wynikowa

    Testowanie tej funkcji na pełnych danych może być mało wygodne, możecie
    stworzyć inną funkcję która działa na dwóch listach/generatorach i testować
    ją.

    Naiwna implementacja polegałaby na stworzeniu dwóch słowników które
    zawierają mapowanie ngram -> ilość wystąpień i połączeniu ich.

    Lepsza implementacja ładuje jeden z plików do pamięci RAM (jako słownik
    bądź listę) a po drugim iteruje.

    Najlepsza implementacja nie wymaga ma złożoność pamięciową ``O(1)``.
    Podpowiedź: merge sort. Nie jest to trywialne zadanie, ale jest do zrobienia.
    """

    import csv

    with open(str(path1), 'r') as file, open(str(path2), 'r') as file2:
       r1 = csv.reader(file, dialect=csv.unix_dialect)
       r2 = csv.reader(file2, dialect=csv.unix_dialect)

       lista1_ngramow = []
       lista1_wystapien = []
       lista2_ngramow = []
       lista2_wystapien = []


       for line in r1:
          lista1_ngramow.append(line[0])
          lista1_wystapien.append(int(line[1]))

       for line in r2:
          lista2_ngramow.append(line[0])
          lista2_wystapien.append(int(line[1]))

    from collections import defaultdict

    dict = defaultdict(lambda : 0)

    for i in range(len(lista1_ngramow)):
        dict[ lista1_ngramow[i] ] += lista1_wystapien[i]

    for i in range(len(lista2_ngramow)):
        dict[ lista2_ngramow[i] ] += lista2_wystapien[i]

    lista = []

    for i in dict.items():
       lista.append(i)

    #return sorted(lista, key=lambda x: x[0], reverse=False)

    lista = sorted(lista, key=lambda x: x[0], reverse=False)

    with open(str(out_file), 'w') as f:
       w = csv.writer(f, dialect=csv.unix_dialect)
       w.writerows([[ii, jj] for ii,jj in lista])




if __name__ == '__main__':

    merge(
        '/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_0.xmlascii.csv',
        '/opt/pwzn/zaj3/enwiki-20140903-pages-articles_part_1.xmlascii.csv',
        '/tmp/mergeout.csv')