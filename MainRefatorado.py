import time

class GeneticParents():

    def __init__(self, nome_pai, nome_mae) -> None:

        self.cads = list()
        self.dad = {
            'nome': nome_pai
        }
        self.mom = {
            'nome': nome_mae
            }
        self.son = dict()
    
    @staticmethod
    def limpando_espacos(string_text):
        """ 
        Nesta função vou receber o texto tirar os espaços e deixar em
        Caps lock"""

        # Devolvendo o texto formatado
        return string_text.upper().strip()
   
    def cadastro_pais(self):

        # Limpando os espaços e deixando em CAPS LOCK
        formatador_texto = self.limpando_espacos

        # Pegando os dados do pai
        def get_pais_genes(dicionario_pai_mae):

            # Enquanto OLHO não for Vv-Cc-Aa repita
            while True:
                dicionario_pai_mae['eyes'] = input('''\nDIGA A COR DOS OLHOS DO PAI [V/C/A] 
                                V = verde
                                C = Castanho
                                A = Azul
                                :''')
                if dicionario_pai_mae['eyes'] in 'VvCcAa':
                    break
                print('Opção invalida \n')
            
            # Adicionando cabelo
            while True:
                dicionario_pai_mae['hair'] = formatador_texto(input('''DIGA A COR DO CABELO DO PAI [C/L]
                                    C = Castanho
                                    L = Loiro
                                    :'''))
                if dicionario_pai_mae['hair'] in 'CcLl':
                        break
                print('Opção invalida \n')
            
            # Adicionando etinia
            while True:
                dicionario_pai_mae['etinia'] = formatador_texto(input('''DIGA A ETINIA DO PAI [B/P]
                                B = Branco
                                P = Preto
                                    :'''))
                if dicionario_pai_mae['etinia'] in 'PpBb':
                        break
                print('Opção invalida \n')
        
        # Descobrindo Os tons de olhos,cabelos, e etc..
        def quais_caracteristicas_pais(pessoa):


            def cor_olho(dicionario_pai_mae):

                if dicionario_pai_mae['eyes'] == 'V':
                    dicionario_pai_mae['eyes'] = 'VERDE'

                elif dicionario_pai_mae['eyes'] == 'C':
                    dicionario_pai_mae['eyes'] = 'CASTANHO'

                elif dicionario_pai_mae['eyes'] == 'A':
                    dicionario_pai_mae['eyes'] = 'AZUL'

            def cor_cabelo(dicionario_pai_mae):

                if dicionario_pai_mae['hair'] == 'C':
                    dicionario_pai_mae['hair'] = 'CASTANHO'

                elif dicionario_pai_mae['hair'] == 'L':
                    dicionario_pai_mae['hair'] = 'LOIRO'
                    
            def cor_etnia(dicionario_pai_mae):

                if dicionario_pai_mae['etinia'] == 'B':
                    dicionario_pai_mae['etinia'] = 'BRANCO'

                elif dicionario_pai_mae['etinia'] == 'P':
                    dicionario_pai_mae['etinia'] = 'PRETO'

            cor_olho(pessoa)
            cor_cabelo(pessoa)
            cor_etnia(pessoa)

        # Uma tupla com os dois dicionários, para usa-los no for e não
        # Ter que repetir o código
        mom_and_dad = (self.dad,self.mom) # TUPLAAAA

        # Descobrindo os Genes Do pai e mãe
        for pessoa in mom_and_dad:
            print("==== Cadastrando os dados da {pessoa} ====")

            get_pais_genes(pessoa)
            quais_caracteristicas_pais(pessoa)

            # dando um espaço
            print("\n\n")
                
    def cadastro_filho(self):

        # Limpando os espaços e deixando em CAPS LOCK
        formatador_texto = self.limpando_espacos
        
        # Nome do garoto
        self.son['FILHO'] = formatador_texto(input('DIGA O NOME DA CRIANÇA: '))

        # Sexo do filho
        sex_son =''

        while True: 
            sex_son = formatador_texto(input('''
            DIGITE F SE A CRIANÇA FOR MENINA
            DIGITE M SE A CRIANÇA FOR MENINO
            :'''))

            # Se o sexo estiver entre FfMm irá quebrar o WHILE COM BREAK
            if sex_son in 'FfMm':
                break

            # Se não estiver manda a mensagem abaixo e reinicia o looping
            print('OPÇÃO INVÁLIDA')
        
        if sex_son in "F":
            sex_son = "FEMININO"
        elif sex_son in 'M':
            sex_son = "MASCULINO"

        self.son['SEXO'] = sex_son




if __name__ == "__main__":

    biologia = GeneticParents("Afonso"," Lila")
    biologia.cadastro_pais()
  