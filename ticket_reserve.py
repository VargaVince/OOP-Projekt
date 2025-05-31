from abc import ABC, abstractmethod

class LegiTarsasag:

    def __init__(self, legitarsasag_nev):
        self.legitarsasag_nev = legitarsasag_nev
        self.jaratok = []
    
    def szabad_jaratok_kiiras(self):
        print(f'A(z) {self.legitarsasag_nev} szabad jaratai: ')
        for j in self.jaratok:
            if (0 in j.helyek):
                print(j)

    def teli_jaratok_kiiras(self):
        print(f'A(z) {self.legitarsasag_nev} teli jaratai: ')
        for j in self.jaratok:
            if not (0 in j.helyek):
                print(j)
    
class Jarat(ABC):

    @abstractmethod
    def __init__(self, jaratszam, celallomas, jegyar, legitarsasag:LegiTarsasag, idopont, repulesi_ido):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.legitarsasag = legitarsasag
        legitarsasag.jaratok.append(self)
        self.idopont = idopont
        self.helyek = [0, 0, 0, 0, 0, 0]
        self.foglalas_lista = []
        self.repulesi_ido = repulesi_ido

    @abstractmethod
    def foglalas_lista_kiiras(self):
        if self.foglalas_lista.__len__() == 0: print('Ezen a jaraton meg nincs foglalas.')
        else: 
            print('Az adott jarat foglalasai: ')
            for f in self.foglalas_lista:
                print(f)

    @abstractmethod
    def ures_helyek_kiiras(self):
        if not (0 in self.helyek):
            print('Sajnaljuk, a jarat betelt, kerjuk valasszon masik jaratot.')
        else:
            print('Szabad ulesek sorszamai: ')
            for i in range(len(self.helyek)):
                if self.helyek[i] == 0:
                    print(i + 1)

    @abstractmethod
    def __str__(self):
        return 'Legitarsasag: {}, Jaratszam: {}, Celallomas: {}, Jegyar: {}, Idopont: {}, Repulesi ido: {} perc'.format(self.legitarsasag.legitarsasag_nev, self.jaratszam, self.celallomas, self.jegyar, self.idopont, self.repulesi_ido)

class BelfoldiJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar, legitarsasag, idopont, repulesi_ido):
        super().__init__(jaratszam, celallomas, jegyar, legitarsasag, idopont, repulesi_ido)

    def ures_helyek_kiiras(self):
        return super().ures_helyek_kiiras()
    
    def foglalas_lista_kiiras(self):
        return super().foglalas_lista_kiiras()

    def __str__(self):
        return super().__str__()

class NemzetkoziJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar, legitarsasag, idopont, repulesi_ido):
        super().__init__(jaratszam, celallomas, jegyar, legitarsasag, idopont, repulesi_ido)

    def foglalas_lista_kiiras(self):
        return super().foglalas_lista_kiiras()
    
    def ures_helyek_kiiras(self):
        return super().ures_helyek_kiiras()

    def __str__(self):
        return super().__str__()

class JegyFoglalas():

    @property
    def celallomas(self):
        return self.jarat.celallomas
    
    @property
    def idopont(self):
        return self.jarat.idopont
    
    @property
    def jaratszam(self):
        return self.jarat.jaratszam
    
    def __init__(self, jarat: Jarat, hely):
        self.jarat = jarat
        self.hely = hely

    def foglal(self):
        if not (0 in self.jarat.helyek):
            print('Sajnaljuk, a jarat betelt, kerjuk valasszon masik jaratot.')
        elif self.jarat.helyek[self.hely - 1] == 1:
            print('Sajnaljuk, a valasztott hely foglalt, kerjuk valasszon masik helyet.')
        else: 
            self.jarat.helyek[self.hely - 1] = 1
            self.jarat.foglalas_lista.append(self)
            print(f'Hely sikeresen lefoglalva. Koszonjuk, hogy a {self.jarat.legitarsasag.legitarsasag_nev}-t valasztotta.')
            print('Az on foglalasa: ')
            print(self)

    def lemond(self):
        if self not in self.jarat.foglalas_lista:
            print('Sajnaljuk, ilyen foglalas nem letezik.')
        else:
            print('Foglalas lemondva.')
            self.jarat.helyek[self.hely] = 0
            self.jarat.foglalas_lista.remove(self)

    def __str__(self):
        return self.jarat.__str__() + f', Hely: {self.hely}'


sajat_foglalasok = []
uticel_szures = []
idopont_szures = []
jaratszam_szures = []

separator = '------------------------------------'

def uticel_kivalasztas(szuro: list):

    celallomas = input('Kerjuk valasszon uticelt: ')
    print(separator)

    while uticel_szures == []:
        for j in szuro:
            if j.celallomas == celallomas:
                uticel_szures.append(j)
        if uticel_szures == []: celallomas = input('Nincs ilyen uticel, kerjuk adjon meg masikat:')
    print('Kivalasztott jaratok: ')
    for j in uticel_szures: print(j)
    print(separator)

def idopont_kivalasztas():

    idopont = input('Kerjuk adja meg az idopontot (eeee-hh-nn formaban): ')
    print(separator)
    while idopont_szures == []:
        for j in uticel_szures:
            if j.idopont == idopont: 
                idopont_szures.append(j)
        if idopont_szures == []: idopont = input('Nincs ilyen idopontban ilyen jarat, kerjuk adjon meg masikat:')
    print('Kivalasztott jaratok: ')
    for j in idopont_szures: print(j)
    print(separator)

def jaratszam_kivalasztas():

    jaratszam = int(input('Kerjuk adja meg a kivalasztott jaratszamot: '))
    print(separator)
    while jaratszam_szures == []:
        for j in idopont_szures:
            if j.jaratszam == jaratszam: 
                jaratszam_szures.append(j)
        if jaratszam_szures == []: jaratszam = int(input('Nincs ilyen jaratszam, kerjuk adjon meg masikat:'))
    print('Kivalasztott jarat: ')
    print(jaratszam_szures[0])
    print(separator)

def hely_kivalasztas():

    jaratszam_szures[0].ures_helyek_kiiras()
    print(separator)
    
    hely = int(input('Kerjuk adja meg a kivalasztott helyet: '))
    while jaratszam_szures[0].helyek[hely - 1] == 1:
        print('Kerjuk valasszon szabad helyet: ')
    return hely

RyanAir = LegiTarsasag('RyanAir')
#WizzAir = LegiTarsasag('WizzAir')

jarat1 = NemzetkoziJarat(1, 'London', 25000, RyanAir, '2025-07-01', 180)
jarat2 = BelfoldiJarat(2, 'Debrecen', 9000, RyanAir, '2025-06-23', 35)
jarat3 = NemzetkoziJarat(3, 'Basel', 30000, RyanAir, '2025-08-10', 120)
jarat4 = NemzetkoziJarat(1, 'London', 24000, RyanAir, '2025-07-08', 180)

foglalas1 = JegyFoglalas(jarat1, 1)
foglalas2 = JegyFoglalas(jarat1, 2)
foglalas3 = JegyFoglalas(jarat1, 3)
foglalas4 = JegyFoglalas(jarat1, 5)
foglalas5 = JegyFoglalas(jarat1, 6)
foglalas6 = JegyFoglalas(jarat4, 5)

foglalas1.jarat.helyek[foglalas1.hely - 1] = 1
foglalas1.jarat.foglalas_lista.append(foglalas1)
foglalas2.jarat.helyek[foglalas2.hely - 1] = 1
foglalas2.jarat.foglalas_lista.append(foglalas2)
foglalas3.jarat.helyek[foglalas3.hely - 1] = 1
foglalas3.jarat.foglalas_lista.append(foglalas3)
foglalas4.jarat.helyek[foglalas4.hely - 1] = 1
foglalas4.jarat.foglalas_lista.append(foglalas4)
foglalas5.jarat.helyek[foglalas5.hely - 1] = 1
foglalas5.jarat.foglalas_lista.append(foglalas5)
foglalas6.jarat.helyek[foglalas6.hely - 1] = 1
foglalas6.jarat.foglalas_lista.append(foglalas6)

def foglalas_program():

    szabad_jaratok = []
    for j in RyanAir.jaratok: 
        if 0 in j.helyek:
            szabad_jaratok.append(j)

    RyanAir.szabad_jaratok_kiiras()
    print(separator)

    uticel_kivalasztas(szabad_jaratok)
    idopont_kivalasztas()
    jaratszam_kivalasztas()
    hely = hely_kivalasztas()

    foglalas = JegyFoglalas(jaratszam_szures[0], hely)
    foglalas.foglal()
    sajat_foglalasok.append(foglalas)

def lemondas_program():

    print('Sajat foglalasok: ')
    for f in sajat_foglalasok: print(f)
    print(separator)
    
    uticel_kivalasztas(sajat_foglalasok)
    idopont_kivalasztas()
    jaratszam_kivalasztas()
    
    for f in sajat_foglalasok:
        if f.jarat == jaratszam_szures[0].jarat: sajat_helyek.append(f.hely)
        print(f.jarat)
        print(jaratszam_szures[0])
    
    print('Kerjuk valassza ki, melyik helyet szeretne lemondani: ')
    for s in sajat_helyek: print(s)

    hely = int(input())
    while hely not in sajat_helyek:
        hely = int(input('Kerjuk sajat foglalasanak helyet adja meg: '))
    
    foglalasok = []
    for f in sajat_foglalasok:
        if f.jarat == jaratszam_szures[0].jarat and f.hely == hely:
            foglalasok.append(f)
    foglalasok[0].lemond()
    sajat_foglalasok.remove(foglalasok[0])


print('Udvozoljuk.')
kilep = False

while not kilep:

    lista = input('Megnezi sajat foglalasait? ')
    if lista.lower() == 'igen':
        for f in sajat_foglalasok: print(f)

    foglalas = input('Megkezd uj foglalast? ')
    if foglalas.lower() == 'igen':
        uticel_szures = []
        idopont_szures = []
        jaratszam_szures = []
        foglalas_program()
    
    lemondas = input('Lemond egy meglevo foglalast? ')
    if lemondas.lower() == 'igen':
        uticel_szures = []
        idopont_szures = []
        jaratszam_szures = []
        sajat_helyek = []
        lemondas_program()

    vege = input('Kilep a programbol? ')
    if vege.lower() == 'igen': 
        kilep = True
        print('Viszlat!')
