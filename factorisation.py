from math import sqrt
from numba import jit

@jit(nopython = True)
def factorise(nbre : float):  
    tempo_quotient = sqrt(nbre)
    int_tempo_quotient = int(tempo_quotient)
    
    print("\n")
    print("factorisation:....")

    #verification pour les carree parfaits
    if (int_tempo_quotient**2==nbre):
        nbre2=int_tempo_quotient
        print(f'{nbre2} x {nbre2} font => {nbre2*nbre2}')

    #Algorithme dans un 'try-except' pour eviter le message d'erreur en cas de division par zero
    try:
        while(int_tempo_quotient<=nbre):
            int_tempo_quotient-=1
            resultat=nbre/int_tempo_quotient
            
            p=resultat #facultatif juste pour conserver nos valeurs qlq part :)
            q=int_tempo_quotient    #idem ;)
            
            if((p*q == nbre) and p.is_integer() and q != 1):
                print(f'{q} X {p} font => {(p*q)}')

    except:
        print("")
