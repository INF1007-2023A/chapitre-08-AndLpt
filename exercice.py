#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json


# TODO: Définissez vos fonction ici
def exercice1(a, b): # le prof compare ligne par ligne et non une ligne vs toutes les autres
                     # on pouvait ne pas utiliser enumerate si pas besoin de numéroter ligne
    with open(a, 'r') as file1, open(b, 'r') as file2:
        for line in file1:
            for line1 in file2:
                if line != line1:
                    print(f"{line1} différente de {line}")
                    return
    print('les deux fichiers sont identiques')

def exercice2(fichier_copie): # prof le fait d'une façon beaucoup plus simple
    with open(fichier_copie, 'r') as file1, open('test.txt', 'w') as file2:
        for line in file1:
            for c in line:
                if c != ' ':
                    file2.write(c)
                else:
                    file2.write(c*3)

def exercice3(a): # le prof a fait d'une façon cool
    with open(a, 'r') as f1, open('D:\Semestre 1\INF1007\chapitre-08-AndLpt\data\seuils.json', 'r') as f2, open('D:\Semestre 1\INF1007\chapitre-08-AndLpt\output\notes_letter.txt', mode='w') as f3:
        seuils = json.load(f2)
        for line in f1:
            for key, value in seuils.items():
                if int(line) in range(value[0], value[1]):
                    f3.write(line.replace('\n', ' ') + key) # très vigilent ici car la ligne est de la forme 'A\n'
                    f3.write('\n')
                    break

def exercice4(): # trop compliqué même avec explications du prof j'ai rien compris
    pass

def exercice5(a): # le prof l'a fait en 3 lignes 
    reader = []
    with open(a, 'r') as f:
        for line in f:
            reader.append(line.split()) 

    number_list = []
    for line in reader:
        for elem in line:
            if elem.isdigit():
                number_list.append(float(elem))
    number_list = sorted(number_list)
    return number_list

def exercice6(a, b): # une fois de plus le prof l'a fait en quelques lignes
    with open(a, 'r') as f, open(b, 'w') as f1:
        count = 0
        for line in f:
            if (count % 2) == 0:
                f1.writelines(line)
            else:
                pass
            count += 1

                    


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")
    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".
    exercice6("text.txt", "test.txt")    




