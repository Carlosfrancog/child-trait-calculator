from time import sleep


# Variaveis
###################

cads = list()

dad = dict()
mom = dict()
son = dict()

while True:
    dad.clear()
    mom.clear()
    son.clear()

    # CADASTRO DOS PAIS
    ###################################################################################
    dad['PAI'] = str(input('DIGA O NOME DO PAI: ')).replace(" ", "").upper()
    dad['OLHO'] = str(input('''DIGA A COR DOS OLHOS DO PAI [V/C/A] 
                            V = verde
                            C = Castanho
                            A = Azul
                            :''')).strip().upper()[0]
    while dad['OLHO'] not in 'VvCcAa':
        print('ERRO! OPÇÃO INVÁLIDA.')
        dad['OLHO'] = str(input('''DIGA A COR DOS OLHOS DO PAI [V/C/A] 
                            V = verde
                            C = Castanho
                            A = Azul
                            :''')).strip().upper()[0]



    dad['CABELO'] = str(input('''DIGA A COR DO CABELO DO PAI [C/L]
                                C = Castanho
                                L = Loiro
                                :''')).strip().upper()[0]

    while dad['CABELO'] not in 'CcLl':
        print('ERRO! OPÇÃO INVÁLIDA.')
        dad['CABELO'] = str(input('''DIGA A COR DO CABELO DO PAI [C/L]
                                C = Castanho
                                L = Loiro
                                :''')).strip().upper()[0]


    dad['ETINIA'] = str(input('''DIGA A ETINIA DO PAI [B/P]
                                B = Branco
                                P = Preto
                                :''')).strip().upper()[0]

    while dad['ETINIA'] not in 'PpBb':
        print('ERRO! OPÇÃO INVÁLIDA.')
        dad['ETINIA'] = str(input('''DIGA A ETINIA DO PAI [B/P]
                                B = Branco
                                P = Preto
                                :''')).strip().upper()[0]


    if dad['OLHO'] == 'V':
        dad['OLHO'] = 'VERDE'

    elif dad['OLHO'] == 'C':
        dad['OLHO'] = 'CASTANHO'

    elif dad['OLHO'] == 'A':
        dad['OLHO'] = 'AZUL'

    if dad['CABELO'] == 'C':
        dad['CABELO'] = 'CASTANHO'
    elif dad['CABELO'] == 'L':
        dad['CABELO'] = 'LOIRO'

    if dad['ETINIA'] == 'B':
        dad['ETINIA'] = 'BRANCO'

    elif dad['ETINIA'] == 'P':
        dad['ETINIA'] = 'PRETO'
        
        



    mom['MÃE'] = str(input('DIGA O NOME DA MÃE: ')).replace(" ", "").upper()

    mom['OLHO'] = str(input('''DIGA A COR DOS OLHOS DO MÃE [V/C/A] 
                            V = verde
                            C = Castanho
                            A = Azul
                            :''')).strip().upper()[0]
    while mom['OLHO'] not in 'VvCcAa':
        print('ERRO! OPÇÃO INVÁLIDA.')
        mom['OLHO'] = str(input('''DIGA A COR DOS OLHOS DO MÃE [V/C/A] 
                            V = verde
                            C = Castanho
                            A = Azul
                            :''')).strip().upper()[0]



    mom['CABELO'] = str(input('''DIGA A COR DO CABELO DO MÃE [C/L]
                                C = Castanho
                                L = Loiro
                                :''')).strip().upper()[0]

    while mom['CABELO'] not in 'CcLl':
        print('ERRO! OPÇÃO INVÁLIDA.')
        mom['CABELO'] = str(input('''DIGA A COR DO CABELO DO MÃE [C/L]
                                C = Castanho
                                L = Loiro
                                :''')).strip().upper()[0]


    mom['ETINIA'] = str(input('''DIGA A ETINIA DO MÃE [B/P]
                                B = Branco
                                P = Preto
                                :''')).strip().upper()[0]

    while mom['ETINIA'] not in 'PpBb':
        print('ERRO! OPÇÃO INVÁLIDA.')
        mom['ETINIA'] = str(input('''DIGA A ETINIA DO MÃE [B/P]
                                B = Branco
                                P = Preto
                                :''')).strip().upper()[0]
    


    if mom['OLHO'] == 'V':
        mom['OLHO'] = 'VERDE'

    elif mom['OLHO'] == 'C':
        mom['OLHO'] = 'CASTANHO'

    elif mom['OLHO'] == 'A':
        mom['OLHO'] = 'AZUL'


    if mom['CABELO'] == 'C':
        mom['CABELO'] = 'CASTANHO'

    elif mom['CABELO'] == 'L':
        mom['CABELO'] = 'LOIRO'


    if mom['ETINIA'] == 'B':
        mom['ETINIA'] = 'BRANCO'

    elif mom['ETINIA'] == 'P':
        mom['ETINIA'] = 'PRETO'
    ###################################################################################


    # CADASTRO DO FILHO
    ###################################################################################
    son['FILHO'] = str(input('DIGA O NOME DA CRIANÇA: ')).replace(" ", "").upper()
    
    sex_son = str(input('''
    DIGITE F SE A CRIANÇA FOR MENINA
    DIGITE M SE A CRIANÇA FOR MENINO
    :''')).strip().upper()[0]


    while sex_son not in 'FfMm':
        print('OPÇÃO INVÁLIDA!')
        sleep(0.5)
        sex_son = str(input('''
    DIGITE F SE A CRIANÇA FOR MENINA
    DIGITE M SE A CRIANÇA FOR MENINO
    :''')).strip().upper()[0]


    if sex_son in 'F':
        sex_son = 'FEMININO'
    elif sex_son in 'M':
        sex_son = "MASCULINO"

    son['SEXO'] = sex_son[:]

    # OLHO
    #####################################################################################
    if dad['OLHO'] == 'CASTANHO':
        if mom['OLHO'] == 'CASTANHO':
            son['OLHO'] = 'CASTANHO'
    if dad['OLHO'] == 'CASTANHO':
        if mom['OLHO'] == 'VERDE':
            son['OLHO'] = 'CASTANHO'
    if dad['OLHO'] == 'CASTANHO':
        if mom['OLHO'] == 'AZUL':
            son['OLHO'] = 'CASTANHO'


    if dad['OLHO'] == 'VERDE':
        if mom['OLHO'] == 'CASTANHO':
            son['OLHO'] = 'CASTANHO'
    if dad['OLHO'] == 'VERDE':
        if mom['OLHO'] == 'VERDE':
            son['OLHO'] = 'VERDE'
    if dad['OLHO'] == 'VERDE':
        if mom['OLHO'] == 'AZUL':
            son['OLHO'] = 'VERDE'

    
    if dad['OLHO'] == 'AZUL':
        if mom['OLHO'] == 'CASTANHO':
            son['OLHO'] = 'CASTANHO'
    if dad['OLHO'] == 'AZUL':
        if mom['OLHO'] == 'VERDE':
            son['OLHO'] = 'VERDE'
    if dad['OLHO'] == 'AZUL':
        if mom['OLHO'] == 'AZUL':
            son['OLHO'] = 'AZUL'
    ###################################################################################


    # CABELO ##########################################################################

    if dad['CABELO'] == 'CASTANHO':
        if mom['CABELO'] == 'CASTANHO':
            son['CABELO'] = 'CASTANHO'

    if dad['CABELO'] == 'CASTANHO':
        if mom['CABELO'] == 'LOIRO':
            son['CABELO'] = 'CASTANHO'

    
    if dad['CABELO'] == 'LOIRO':
        if mom['CABELO'] == 'CASTANHO':
            son['CABELO'] = 'CASTANHO'

    if dad['CABELO'] == 'LOIRO':
        if mom['CABELO'] == 'LOIRO':
            son['CABELO'] = 'LOIRO'

   ##################################################################################### 
    
    # Etinia ###########################################################################
    if dad['ETINIA'] == 'BRANCO':
        if mom['ETINIA'] == 'BRANCO':
            son['ETINIA'] = 'BRANCO'

    if dad['ETINIA'] == 'BRANCO':
        if mom['ETINIA'] == 'PRETO':
            son['ETINIA'] = 'PARDO'

    if dad['ETINIA'] == 'PRETO':
        if mom['ETINIA'] == 'PRETO':
            son['ETINIA'] = 'PRETO'

    if dad['ETINIA'] == 'PRETO':
        if mom['ETINIA'] == 'BRANCO':
            son['ETINIA'] = 'PARDO'
    ###################################################################################


    # ESCREVER NO TXT
    ###################################################################################   
    file = open('txt.txt', 'a')
    lines_1 = [dad, mom, son]
    with open ("txt.txt", 'a') as file:
            for line_1 in lines_1:
                file.write(str('+'*5))
                file.write(str(line_1))
                file.write(str('\n'))
            file.write(str('-='*55))
            file.write(str('\n'))
    ###################################################################################
    sleep(0.5)


    # NOVO CADASTRO
    ###################################################################################
    cads.append(dad.copy())
    cads.append(mom.copy())
    cads.append(son.copy())

    while True:
        back = str(input('DESEJA FAZER UM  NOVO CADASTRO? [S/N]')).strip().upper()[0]
        if back in 'SN':
            break
        print("ERRO! RESPONDA APENAS S OU N.")


    if back == 'N':
        break
    ###################################################################################


print('-=' *30)
for e in cads:
    print(f'O FILHO DE:{dad["PAI"]} e {mom["MÃE"]} chama-se: {son["FILHO"]}')
    print(f'{son["FILHO"]} é do sexo {son["SEXO"]}, sua etinia {son["ETINIA"]}, seus olhos são da cor {son["OLHO"]} e seu cabelo é {son["CABELO"]}')
print('-=' *30)




'''
DESENVOLVIDO POR:
intagram: @carlin_fg
Twitter: @ZinCrZin
'''