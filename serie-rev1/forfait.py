from numpy import zeros


def tri(n, tab):
    test = False
    while not (test is False):
        for compteur in range(n - 1):
            if tab[compteur] > tab[compteur + 1]:
                aux = tab[compteur]
                tab[compteur] = tab[compteur + 1]
                tab[compteur + 1] = aux
                test = True
    return tab


def saisirEntierPositif(min, max):
    N = int(input())
    while not (min <= N <= max) and ((N % 2) != 0):
        N = int(input())
    return N


def saisirReelPositif():
    F = float(input())
    while F < 0:
        F = float(input())
    return F


def remplirTableau(N, T):
    for i in range(N):
        while T[i] <= 0:
            T[i] = float(input())

def calculFichier(F,R, N):
    res = F
    fichtel = 0
    i = 0
    while (fichtel < F) and (i < N):
        fichtel = fichtel + R[i]
        res = res - R[i]
        i = i + 1
    return i,res

F = saisirReelPositif()
N = saisirEntierPositif(5, 25)
T = zeros(N)
remplirTableau(N, T)
R = tri(N, T)
(i,res) = calculFichier(F,R,N)
print("avec le forfait internet", F, "MO, on peut télécharger les fichiers suivants:")
for k in range(i):
    print(k + 1, R[k], "MO")
print("Forfait restant=", res, "MO")


# autre solution
"""res = F
fichtel = 0
i = 0

print("avec le forfait internet", F, "MO, on peut télécharger les fichiers suivants:")
while (fichtel < F) and (i < N):
    print(i + 1, R[i], "MO")
    fichtel = fichtel + R[i]
    res = res - R[i]
    i = i + 1
print("Forfait restant=", res, "MO")
"""