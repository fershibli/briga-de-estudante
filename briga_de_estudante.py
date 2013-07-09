from __future__ import print_function
# -*- coding: cp1252 -*-
#--Import--#
#use o python 2.7.4 que e coisa de macho!!!!!!11!!!!!1!!onze!!!! - Lucas Sabiao
import random
import ConfigParser
import pickle
import time
import os

#ASSISTA DEVIL SURVIVOR 2

def escrever(tempo_entre_letras,string,tempo_apos_string=0):
    for letra in string:
        print(letra,end='')
        time.sleep(tempo_entre_letras)
    time.sleep(tempo_apos_string)

class Item(object):
    def __init__(self, nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, preco, tipo):
        self.nome = nome
        self.status=[]#atq[0], def[1], agi[2], luk[3], taxarecuperacao[4], vidamaxima[5], vidaatual[6]
        self.status.append(ataque)
        self.status.append(defesa)
        self.status.append(agilidade)
        self.status.append(sorte)
        self.status.append(taxarecuperacao)
        self.status.append(vidamaxima)
        self.status.append(vidaatual)
        self.preco = preco
        self.tipo = tipo

#nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, preco, tipo #####: nulo
desequipado = [Item("Nada", 0,0,0,0, 0,0,0, 0, "roupa"),Item("Nada", 0,0,0,0, 0,0,0, 0, "capa"),Item("Nada", 0,0,0,0, 0,0,0, 0, "luva"),Item("Nada", 0,0,0,0, 0,0,0, 0, "anel"),Item("Nada", 0,0,0,0, 0,0,0, 0, "arma"),Item("Nada", 0,0,0,0, 0,0,0, 0, "calcado"),Item("Vazio", 0,0,0,0, 0,0,0, 0, "inventario")]
equipamento_inicial = [Item("Pijama", 0,0,0,2, 5,0,0, 5, "roupa"),Item("Uniforme Estudantil", 0,1,0,0, 0,0,0, 20, "roupa"),Item("Lapis Apontado", 3,0,0,1, 0,0,0, 2, "arma"),Item("Chinelos", 0,0,0,-5, 0,0,0, 5,"calcado"),Item("Tenis Simplorio", 0,1,2,0, 0,0,0, 50, "calcado")]

class Personagem(object):
    def __init__(self, nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, dinheiro, furtar, identificacao, disponivel, roupa, capa, luva, anel, maos, calcado):
        self.status = [] #atq[0], def[1], agi[2], luk[3], taxarecuperacao[4], vidamaxima[5], vidaatual[6]
        self.nome = nome
        self.status.append(ataque)
        self.status.append(defesa)
        self.status.append(agilidade)
        self.status.append(sorte)
        self.status.append(taxarecuperacao)
        self.status.append(vidamaxima)
        self.status.append(vidaatual)
        self.identificacao = identificacao
        self.disponivel = disponivel
        self.dinheiro = dinheiro
        self.furtar = furtar
        if (self.identificacao!="inimigo"):
            self.inventario = [],[]
            self.equipamento = [] #roupa[0], capa[1], luva[2], anel[3], maos[4], calcado[5], vazio[6]
            numero=1
            while numero<31:
                self.inventario[0].append(numero)
                self.inventario[1].append(desequipado[6])
                numero+=1
            self.equipamento.append(roupa)
            self.equipamento.append(capa)
            self.equipamento.append(luva)
            self.equipamento.append(anel)
            self.equipamento.append(maos)
            self.equipamento.append(calcado)
            self.equipamento.append("vazio")
            w=0
            while w<6:
                x=0
                while x<7:
                    self.status[x]+=self.equipamento[w].status[x]
                    x+=1
                w+=1
            
#-- _aliados_ --#
aliado_jogador = Personagem("NULO", 10,8,1,1, 0,100,100, 0,0, 1, True, equipamento_inicial[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], equipamento_inicial[3])
aliado_reserva = aliado_jogador
aliado_headbanger = Personagem("Lutador Headbanger", 1200,800,50,50, 100,10000,10000, 0,0, 3, False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
aliado_garota = Personagem("Garota", 25,20,1,1, 0,300,300, 25,0, 2, False, equipamento_inicial[1], desequipado[1], desequipado[2], desequipado[3], equipamento_inicial[2], equipamento_inicial[4])
#nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, dinheiro, identificacao, roupa, capa, luva, anel, maos, calcado
#-- _inimigos_ --#
adversario_inimigo = Personagem("Inimigo", 10,8,1,1, 0,100,100, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
narrador_inimigo = Personagem("Narrador", 15,8,5,1, 5,100,100, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
bebado_inimigo = Personagem("Bebado", 4,4,0,0, -10,500,110, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
mulher_prantos = Personagem("Mulher aos Prantos", 15,15,0,10, -5,150,155, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
mulher_toalha = Personagem("Mulher de Toalha", 20,20,5,5, 0,800,800, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
mane_bone = Personagem("Mane de Bone", 10,5,10,1, 0,100,100, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
senhor_doente = Personagem("Senhor Doente", 5,3,-3,3, -1,110,110, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
garoto_oponente = [Personagem("Garoto Irritado", 10,10,10,10, 10,100,100, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Garoto Fracote", 3,10,2,2, 0,100,100, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Garoto Convencido", 8,12,5,10, 0,110,110, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Garoto Serio", 30,25,10,5, 0,200,200, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Garoto Forte", 150,100,20,20, 0,2000,2000, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Garoto, um Homem", 1500,1000,50,50, 0,20000,20000, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])]
gangue_comparsa = [Personagem("Bandido", 300,100,20,20, 0,2500,2500, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Motoqueiro Comparsa", 3000,10,10,-5, 0,50,50, 0,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])]
estudante_brigento = [Personagem("Estudante Briguento", 5,12,2,2, 0,110,110, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 13,4,5,1, 0,130,130, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 8,8,2,1, 0,100,100, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 10,8,5,5, 0,120,120, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 20,2,6,6, 6,666,666, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 30,15,5,5, 5,360,360, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 50,30,10,10, 10,550,550, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 90,70,15,15, 15,790,790, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 180,100,20,20, 20,1500,1500, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Estudante Briguento", 300,200,40,40, 40,320,3200, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])]
arruaceiro_oponente = [Personagem("Arruaceiro", 5,12,2,3, 2,200,200, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 12,5,3,2, 2,200,200, 2,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 12,12,2,2, 2,200,200, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 5,5,2,12, 2,200,200, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 5,5,12,2, 2,200,200, 3,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 10,24,2,2, 4,200,200, 4,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 24,10,4,2, 4,200,200, 4,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 24,24,2,2, 4,200,200, 4,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 10,10,5,5, 50,200,200, 4,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 25,25,5,5, 4,200,200, 4,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 15,36,4,6, 4,400,400, 10,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 36,15,6,4, 4,400,400, 10,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 36,36,4,4, 4,400,400, 10,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 15,15,4,12, 4,400,400, 10,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 15,15,12,4, 4,400,400, 10,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 20,48,8,8, 8,400,400, 40,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 48,20,8,4, 8,400,400, 40,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 48,48,4,4, 8,400,400, 40,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 20,20,10,10, 50,400,400, 40,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5]),Personagem("Arruaceiro", 50,50,10,10, 8,400,400, 40,0, "inimigo", False, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])]
#narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento

#-- _itens_ --#
#nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, preco, tipo
#-- _consumivel_ --#
pedaco_pizza = [Item("Pedaco Pequeno de Pizza", 0,0,0,0, 0,0,50, 5, "consumivel"),Item("Pedaco de Pizza", 0,0,0,0, 0,0,100, 12, "consumivel"),Item("Meia Pizza", 0,0,0,0, 0,0,200, 26, "consumivel")]
pizza_inteira = [Item("Pizza Inteira", 0,0,0,0, 0,0,400, 54, "consumivel"),Item("Pizza Grande", 0,0,0,0, 0,0,600, 80, "consumivel"),Item("Pizza Gigante", 0,0,0,0, 0,0,800, 170, "consumivel"),Item("Pizza Gigante (recheio extra)", 0,0,0,0, 0,0,1000, 200, "consumivel")]
lanches_cantina = [Item("Risole", 0,0,0,0, 0,0,25, 2.50, "consumivel"),Item("Coxinha", 0,0,0,0, 0,0,30, 2.50, "consumivel"),Item("X-Burger", 0,0,0,0, 0,0,80, 7.50, "consumivel"),Item("X-Salada", 0,0,0,0, 0,0,95, 8.50, "consumivel"),Item("X-Bacon", 0,0,0,0, 0,0,110, 8.50, "consumivel"),Item("X-Tudo", 0,0,0,0, 0,0,150, 15, "consumivel"),Item("X-Tudo Gigante", 0,0,0,0, 0,0,300, 40, "consumivel"),Item("Super eXtra-Tudo", 0,0,0,0, 0,0,aliado_jogador.status[5]/2, 200, "consumivel"),Item("Super eXtra-Tudo Gigante", 0,0,0,0, 0,0,aliado_jogador.status[5]*2, 500, "consumivel")]
#-- _aprimoramento_ --#
suplemento_alimenticio = [Item("Suplemento Alimenticio (A)", 10,0,0,0, 0,0,0, 5, "consumivel de aprimoramento"),Item("Suplemento Alimenticio (D)", 0,10,0,0, 0,0,0, 5, "consumivel de aprimoramento"),Item("Suplemento Alimenticio (V)", 0,0,5,0, 0,0,0, 5, "consumivel de aprimoramento"),Item("Suplemento Alimenticio (S)", 10,10,5,1, 1,10,0, 5, "consumivel de aprimoramento")]
lata_energetico = [Item("Energetico", 0,0,0,0, 1,50,0, 5, "consumivel de aprimoramento"),Item("Energetico X", 0,0,0,-10, 10,500,0, 5, "consumivel de aprimoramento")]
#-- _roupa_ --#
bermuda_linho = [Item("Bermuda de Linho e Regata ", 0,1,4,0, 0,0,0, 100, "roupa"),Item("Bermuda de Linho e Polo", 0,2,3,2, 0,0,0, 140, "roupa")]
calca_jeans = [Item("Calca Jeans e Regata", 0,4,1,0, 0,0,0, 110, "roupa"),Item("Calca Jeans e Polo",0,6,0,2, 0,0,0, 150, "roupa")]
malha_ninja = Item("Malha Ninja", 5,20,5,1, 0,0,0, 5000, "roupa")
#-- _capa_ --#
jaqueta_imitacao = Item("Jaqueta de Imitacao de Couro", 0,10,0,0, 0,0,0, 150, "capa")
jaqueta_couro = Item("Jaqueta de Couro", 0,100,0,10, 0,0,0, 1000, "capa")
agasalho_la = Item("Agasalho de La", 0,6,0,0, 0,0,0, 100, "capa")
cachecol_la = Item("Cachecol de La", 0,1,0,0, 0,0,0, 30, "capa")
#-- _luva_ --#
luva_luva = [Item("Luvas de La", 0,3,0,0, 0,0,0, 20, "luva"),Item("Luvas de Imitacao de Couro", 3,3,0,0, 0,0,0, 100, "luva"),Item("Luvas de Couro", 8,8,0,0, 0,0,0, 500, "luva"),Item("Luvas de Couro com Spikes de Aluminio", 15,15,0,0, 0,0,0, 700, "luva"),Item("Luvas de Couro com Spikes de Aco", 25,25,0,0, 0,0,0, 1000, "luva"),Item("Luvas de Couro com Spikes de Prata", 25,25,0,5, 0,0,0, 5000, "luva"),Item("Luvas de Couro com Spikes de Ouro", 250,250,0,10, 0,0,0, 10000, "luva"),Item("Luvas de Couro com Spikes de Titanio", 2500,2500,0,20, 0,0,0, 50000, "luva")]
soco_ingles = [Item("Soco-Ingles de PVC", 3,0,0,0, 0,0,0, 50, "luva"),Item("Soco-Ingles de Latao", 10,0,0,0, 0,0,0, 500, "luva"),Item("Soco-Ingles de Aluminio", 25,0,0,0, 0,0,0, 700, "luva"),Item("Soco-Ingles de Aluminio de Aco", 30,0,0,0, 0,0,0, 1000, "luva"),Item("Soco-Ingles de Prata", 35,0,0,5, 0,0,0, 5000, "luva"),Item("Soco-Ingles de Ouro", 350,0,0,10, 0,0,0, 10000, "luva"),Item("Soco-Ingles de Titanio", 3500,0,0,20, 0,0,0, 50000, "luva")]
#-- _anel_ --#
#nome, ataque, defesa, agilidade, sorte, taxarecuperacao, vidamaxima, vidaatual, preco, tipo
anel_magico = [Item("Anel da Forca 1", 10,-2,-2,-2, 0,0,0, 500, "anel"),Item("Anel da Forca 2", 20,-4,-4,-4, 0,0,0, 1000, "anel"),Item("Anel da Forca 2", 40,-8,-8,-8, 0,0,0, 5000, "anel"),Item("Anel da Resistencia 1", -2,10,-2,-2, 0,0,0, 500, "anel"),Item("Anel da Resistencia 2", -4,20,-4,-4, 0,0,0, 1000, "anel"),Item("Anel da Resistencia 2", -8,40,-8,-8, 0,0,0, 5000, "anel"),Item("Anel da Consistencia 1", -2,-2,-2,-2, 0,10,10, 500, "anel"),Item("Anel da Consistencia 2", -4,-4,-4,-4, 0,100,100, 1000, "anel"),Item("Anel da Consistencia 3", -8,-8,-8,-8, 0,1000,1000, 5000, "anel")]
anel_da_imortalidade = Item("Anel da Imortalidade", aliado_jogador.status[0],aliado_jogador.status[1],aliado_jogador.status[2],aliado_jogador.status[3], aliado_jogador.status[4],aliado_jogador.status[5],aliado_jogador.status[6], 100000, "anel")
anel_da_divindade = Item("Anel da Divindade", aliado_jogador.status[0]*2,aliado_jogador.status[1]*2,aliado_jogador.status[2]*2,aliado_jogador.status[3]*2, aliado_jogador.status[4]*2,aliado_jogador.status[5]*2,aliado_jogador.status[6]*2, 100000000, "anel")
#-- _arma_ --#
baralho_as = Item("Ace of Spades", aliado_jogador.status[3]*3,0,0,-5, 0,0,0, 3, "arma")
punhal_envelhecido = Item("Punhal Envelhecido", 10,0,0,3, 0,0,0, 100, "arma")
talheres_prata = Item("Talheres de prata(Garfo e Faca)", 8,0,0,0, 0,0,0, 10, "arma")
guarda_chuva = [Item("Guarda-Chuva Compacto", 5,5,0,0, 0,0,0, 12, "arma"),Item("Guarda-Chuva", 10,10,5,0, 0,0,0, 30, "arma"),Item("Guarda-Chuva Pontudo", 15,10,5,-3, 0,0,0, 30, "arma"),Item("Guarda-Chuva Italiano", 20,20,5,5, 0,0,0, 130, "arma")]
#-- _calcado_ --#
papetes_masculinas = Item("Papetes Masculinas", 0,0,1,0, 0,0,0, 15, "calcado")
sapato_simplorio = Item("Sapato Simplorio", 0,2,1,0, 0,0,0, 50, "calcado")
tenis_calcado = [Item("Tenis Velho", 0,0,2,0, 0,0,0, 10, "calcado"),Item("Tenis Comum", 0,2,2,0, 0,0,0, 90, "calcado"),Item("Tenis de Trilha", 2,8,3,0, 0,0,0, 400, "calcado"),Item("Tenis de Caminhada", 0,3,5,0, 0,0,0, 300, "calcado"),Item("Tenis de Corrida", 0,5,10,0, 0,0,0, 500, "calcado"),Item("Tenis ZX-5000", 10,10,11,5, 0,0,0, 15000, "calcado")]

class Loja(object):
    def __init__(self):
        self.inventario = [],[]
        numero=1
        while numero<31:
            self.inventario[0].append(numero)
            self.inventario[1].append(desequipado[6])
            numero+=1

Venda = Loja()
Reserva_Venda = Loja()

item_adicionado=desequipado[6]
quantidade_adicionada=1
porcentagem_inflacao=1

variavel_cenario = ["nao","nao","nao","nao","nao", "nao","nao","nao","nao","nao", "nao","nao","nao","nao","nao"]
#[0]  olhar cenario primeira vez no seu quarto e reciclada no primeiro andar do seu predio
#[1]  modificar cenario primeira vez no seu quarto
#[2]  cheirar cenario no primeiro andar do seu predio

objeto = ["nao","nao","nao","nao","nao", "nao","nao","nao","nao","nao", "nao","nao","nao","nao","nao"]
#[0]  presente do tutorial e reciclada no bebado do 1o andar
#[1]  porta do quarto 10
#[2]  energetico do bebado (acao revistar)
#[3]  arrombar porta do quarto 10
#[4]  mulher do bebado - talheres de prata

situacao = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0,  0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
#[0]  dois ultimos andares do seu predio
#[1]  quarto 11 do seu predio
#[2]  quarto 24 do seu predio
#[3]  quarto 21 do seu predio
#[4]  quarto 22 do seu predio
#[5]  quarto 30 do seu predio
#[6]  quarto 31 do seu predio
#[7]  quarto 32 do seu predio
#[8]  quarto 33 do seu predio
#[9]  quarto 34 do seu predio
#[10] quarto 20 do seu predio

booleana=[False,False,False,False,False, False,False,False,False,False, False,False,False,False,False, False,False,False,False,False]
#[0]  verifica se pegou o uniforme no seu quarto depois e reciclada para verificar se ja venceu o terceiro andar do seu predio
#[1]  verifica se pegou o soco ingles no seu quarto depois e reciclada para verificar se 
#[2]  verifica se ja zerou o jogo antes
#[3]  verifica no sistema de batalha se usou defesa antes de usar um item
#[4]  verifica no sistema de batalha se usou um item ao abrir a mochila
#[5]  verifica se achou o estudante certo na rua da faculdade

variavel_lugar = "seu quarto"
ponto_de_save = 0

mostrar_save = ''

eegg = 1

acao_do_personagem = "" 
batalha_escapar = ""

teste_de_sorte = 0
calculo_do_dano = 0
calculo_da_fuga = 0
variavel_para_comparar = 0
contador_de_batalha= 0
contador_de_rodadas = 0


#global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas

#--Mudanca de status pela troca de equipamento--#
def statusMudanca(coloca_item, w):
    if (coloca_item==True):
        x=0
        while x<7:
            aliado_jogador.status[x]+=aliado_jogador.equipamento[w].status[x]
            x+=1
    else:
        x=0
        while x<7:
            aliado_jogador.status[x]-=aliado_jogador.equipamento[w].status[x]
            x+=1

def statusEquipamento(coloca_item, w):
    if (coloca_item==True):
        x=0
        while x<6:
            aliado_jogador.status[x]+=aliado_jogador.equipamento[x].status[w]
            x+=1
    else:
        x=0
        while x<6:
            aliado_jogador.status[x]-=aliado_jogador.equipamento[x].status[w]
            x+=1

#--Adicionar Item ao Inventario--#
def adicionaItem():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    variavel_para_comparar=0
    i=0
    while i<=29:
        if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
            variavel_para_comparar+=1
        i+=1
    if(variavel_para_comparar<quantidade_adicionada):
        quantidade_adicionada=variavel_para_comparar
    while (quantidade_adicionada>0):
        i=0
        while i<=29:
            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                aliado_jogador.inventario[1][i]=item_adicionado
                break
            i+=1
        quantidade_adicionada-=1

#--Inventario--#
def inventarioPersonagem():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    os.system('cls')
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                if(i<29):
                    if(aliado_jogador.inventario[1][i+1].tipo!="inventario" or aliado_jogador.inventario[1][i+1].nome!="Nada"):
                        aliado_jogador.inventario[1][i] = aliado_jogador.inventario[1][i+1]
                        aliado_jogador.inventario[1][i+1] = desequipado[6]
                variavel_para_comparar+=1
            i+=1
        print ("\n#"+"-"*77+"#\n Inventario:"+str(variavel_para_comparar).rjust(42-len(str(variavel_para_comparar)))+" espaco(s) livre(s) de 30.\n#"+"-"*77+"#\n"+']]Mochila[[                  |             ]]Equipamentos[['.center(79)+"\n"+'|'.center(79))
        variavel_para_comparar=0
        i=0
        while i<=29:
            if i<6:
                if i==0: letra='A'
                if i==1: letra='B'
                if i==2: letra='C'
                if i==3: letra='D'
                if i==4: letra='E'
                if i==5: letra='F'
                if (aliado_jogador.inventario[1][i].tipo!="inventario" and aliado_jogador.inventario[1][i].nome!="Nada"):
                    print (str(aliado_jogador.inventario[0][i])+" : "+str(aliado_jogador.inventario[1][i].nome)+' '*(36-len(str(aliado_jogador.inventario[1][i].nome))-len(str(aliado_jogador.inventario[0][i])))+'|'+str(aliado_jogador.equipamento[i].nome).rjust(35)+" : "+str(letra)+"\n    ("+str(aliado_jogador.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_jogador.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_jogador.equipamento[i].tipo)))+str(aliado_jogador.equipamento[i].tipo)+")")
                else:
                    print (' '*(45-len(str(aliado_jogador.inventario[1][i].nome))-len(str(aliado_jogador.inventario[0][i])))+'|'+str(aliado_jogador.equipamento[i].nome).rjust(41-len(str(aliado_jogador.inventario[1][i].nome))-len(str(aliado_jogador.inventario[0][i])))+" : "+str(letra)+"\n"+' '*(49-len(str(aliado_jogador.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_jogador.equipamento[i].tipo)))+str(aliado_jogador.equipamento[i].tipo)+")")
            if i==6:print (' '*39+'|'+'-'*39)
            elif i==5: i=5
            elif i<6: print ('|'.center(79))
            if (i>5 and aliado_jogador.inventario[1][i].tipo!="inventario" and aliado_jogador.inventario[1][i].nome!="Nada"):
                if aliado_jogador.inventario[1][i+1].tipo!="inventario" and aliado_jogador.inventario[1][i+1].nome!="Nada":
                    print (str(aliado_jogador.inventario[0][i])+" : "+str(aliado_jogador.inventario[1][i].nome)+' '*(36-len(str(aliado_jogador.inventario[1][i].nome))-len(str(aliado_jogador.inventario[0][i])))+'|'+str(aliado_jogador.inventario[1][i+1].nome).rjust(36-len(str(aliado_jogador.inventario[0][i+1])))+" : "+str(aliado_jogador.inventario[0][i+1])+"\n    ("+str(aliado_jogador.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_jogador.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_jogador.inventario[1][i+1].tipo)))+str(aliado_jogador.inventario[1][i+1].tipo)+")")
                else: print (str(aliado_jogador.inventario[0][i])+" : "+str(aliado_jogador.inventario[1][i].nome)+' '*(36-len(str(aliado_jogador.inventario[1][i].nome))-len(str(aliado_jogador.inventario[0][i])))+'|'+"\n    ("+str(aliado_jogador.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_jogador.inventario[1][i].tipo)))+'|')
                if i/2!=0: print ('|'.center(79))
            if i>5: i+=2
            if i<6: i+=1
        print ("#"+"-"*77+"#\n")
        while 1:
            print("Para analisar um item digite a sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem =="a" or acao_do_personagem =="b" or acao_do_personagem =="c" or acao_do_personagem =="d" or acao_do_personagem =="e" or acao_do_personagem =="f":
                os.system('cls')
                break
            elif acao_do_personagem.isdigit():
                os.system('cls')
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem = acao_do_personagem.lower()
                if acao_do_personagem !="a" or acao_do_personagem !="b" or acao_do_personagem !="c" or acao_do_personagem !="d" or acao_do_personagem !="e" or acao_do_personagem !="f":
                    if(acao_do_personagem=="voltar"):break
                    print("ENTRADA INVALIDA!")
                    time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        if acao_do_personagem =="a":
            if(aliado_jogador.equipamento[0].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[0].nome)+"\nTipo: "+str(aliado_jogador.equipamento[0].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[0].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[0].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[0].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[0].status[3])+"\nVida: "+str(aliado_jogador.equipamento[0].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[0].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,0)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[0]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[0].nome)+".")
                            aliado_jogador.equipamento[0]=desequipado[0]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        elif acao_do_personagem =="b":
            if(aliado_jogador.equipamento[1].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[1].nome)+"\nTipo: "+str(aliado_jogador.equipamento[1].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[1].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[1].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[1].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[1].status[3])+"\nVida: "+str(aliado_jogador.equipamento[1].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[1].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,1)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[1]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[1].nome)+".")
                            aliado_jogador.equipamento[1]=desequipado[1]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        elif acao_do_personagem =="c":
            if(aliado_jogador.equipamento[2].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[2].nome)+"\nTipo: "+str(aliado_jogador.equipamento[2].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[2].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[2].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[2].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[2].status[3])+"\nVida: "+str(aliado_jogador.equipamento[2].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[2].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,2)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[2]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[2].nome)+".")
                            aliado_jogador.equipamento[2]=desequipado[2]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        elif acao_do_personagem =="d":
            if(aliado_jogador.equipamento[3].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[3].nome)+"\nTipo: "+str(aliado_jogador.equipamento[3].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[3].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[3].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[3].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[3].status[3])+"\nVida: "+str(aliado_jogador.equipamento[3].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[3].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,3)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[3]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[3].nome)+".")
                            aliado_jogador.equipamento[3]=desequipado[3]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        elif acao_do_personagem =="e":
            if(aliado_jogador.equipamento[4].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[4].nome)+"\nTipo: "+str(aliado_jogador.equipamento[4].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[4].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[4].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[4].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[4].status[3])+"\nVida: "+str(aliado_jogador.equipamento[4].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[4].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,4)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[4]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[4].nome)+".")
                            aliado_jogador.equipamento[4]=desequipado[4]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        elif acao_do_personagem =="f":
            if(aliado_jogador.equipamento[5].nome!="Nada"):
                print("\nNome: "+str(aliado_jogador.equipamento[5].nome)+"\nTipo: "+str(aliado_jogador.equipamento[5].tipo)+"\nAtaque: "+str(aliado_jogador.equipamento[5].status[0])+"\nDefesa: "+str(aliado_jogador.equipamento[5].status[1])+"\nAgilidade: "+str(aliado_jogador.equipamento[5].status[2])+"\nSorte: "+str(aliado_jogador.equipamento[5].status[3])+"\nVida: "+str(aliado_jogador.equipamento[5].status[5])+"\nReconstituicao: "+str(aliado_jogador.equipamento[5].status[4])+"\n")
                while 1:
                    print ("Deseja desequipar? (sim ou nao)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        break
                    elif(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        variavel_para_comparar=0
                        i=0
                        while i<=29:
                            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                variavel_para_comparar+=1
                            i+=1
                        if(variavel_para_comparar>=1):
                            statusMudanca(False,5)
                            i=0
                            while i<=29:
                                if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                                    aliado_jogador.inventario[1][i]=aliado_jogador.equipamento[5]
                                    break
                                i+=1
                            print ("Voce guardou "+str(aliado_jogador.equipamento[5].nome)+".")
                            aliado_jogador.equipamento[5]=desequipado[5]
                        break
                    else: print ('Entrada invalida.')
            else: print ('Entrada invalida.')
        else:
            i=0
            while i<=29:
                if(i==acao_do_personagem):
                    break
                i+=1
            i=i-1
            if(acao_do_personagem==aliado_jogador.inventario[0][i] and aliado_jogador.inventario[1][i].tipo!="inventario" and aliado_jogador.inventario[1][i].nome!="Nada"):
                if(aliado_jogador.inventario[1][i].tipo=="consumivel de aprimoramento"):
                    print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+ "\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nVida: "+str(aliado_jogador.inventario[1][i].status[5])+"\nAtaque: "+str(aliado_jogador.inventario[1][i].status[0])+"\nDefesa: "+str(aliado_jogador.inventario[1][i].status[1])+"\nAgilidade: "+str(aliado_jogador.inventario[1][i].status[2])+"\nSorte: "+str(aliado_jogador.inventario[1][i].status[3])+"\n")
                    while aliado_jogador.inventario[1][i].tipo!="inventario":
                        print("O que deseja fazer? (usar, descartar ou voltar)")
                        acao_do_personagem=raw_input("-")
                        acao_do_personagem=acao_do_personagem.lower()
                        if(acao_do_personagem=="usar"):
                            aliado_jogador.equipamento[6]=aliado_jogador.inventario[1][i]
                            statusMudanca(True,6)
                            print("\nVoce usou  "+str( aliado_jogador.inventario[1][i].nome)+"!\n")
                            if aliado_jogador.inventario[1][i].status[0]>0: print ('Seu ataque aumentou em '+str(aliado_jogador.inventario[1][i].status[0])+' pontos!')
                            if aliado_jogador.inventario[1][i].status[1]>0: print ('Sua defesa aumentou em '+str(aliado_jogador.inventario[1][i].status[1])+' pontos!')
                            if aliado_jogador.inventario[1][i].status[2]>0: print ('Sua agilidade aumentou em '+str(aliado_jogador.inventario[1][i].status[2])+' pontos!')
                            if aliado_jogador.inventario[1][i].status[3]>0: print ('Sua sorte aumentou em '+str(aliado_jogador.inventario[1][i].status[3])+' pontos!')
                            if aliado_jogador.inventario[1][i].status[5]>0: print ('Sua vida aumentou em '+str(aliado_jogador.inventario[1][i].status[5])+' pontos!')
                            time.sleep(0.5)
                            aliado_jogador.inventario[1][i]=desequipado[6]
                            break
                        else:
                            if(acao_do_personagem=="descartar"):
                                while aliado_jogador.inventario[1][i].tipo!="inventario":
                                    print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                                    acao_do_personagem=raw_input("-")
                                    acao_do_personagem=acao_do_personagem.lower()
                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                        break
                                    else:
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            break
                                        else:
                                            print("\nENTRADA INVALIDA!\n")
                                            time.sleep(0.5)
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    print("\nVoce descartou"+str(aliado_jogador.inventario[1][i].nome)+"!\n")
                                    time.sleep(0.5)
                                    aliado_jogador.inventario[1][i]=desequipado[6]
                                    break
                            else:
                                if(acao_do_personagem=="voltar"):
                                    break
                                else:
                                    print("\nENTRADA INVALIDA!\n")
                                    time.sleep(0.5)
                if(aliado_jogador.inventario[1][i].tipo=="consumivel"):
                    print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+ "\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nVida: "+str(aliado_jogador.inventario[1][i].status[6])+"\n")
                    while 1:
                        print("O que deseja fazer? (usar, descartar ou voltar)")
                        acao_do_personagem=raw_input("-")
                        acao_do_personagem=acao_do_personagem.lower()
                        if(acao_do_personagem=="usar"):
                            print("\nVoce usou "+ str(aliado_jogador.inventario[1][i].nome)+"!\n")
                            if aliado_jogador.status[6]+aliado_jogador.inventario[1][i].status[6]<1.1*aliado_jogador.status[5]:
                                print ('Voce recuperou '+str(aliado_jogador.inventario[1][i].status[6])+' pontos de vida!')
                                time.sleep(0.5)
                            aliado_jogador.status[6]+=aliado_jogador.inventario[1][i].status[6]
                            if (aliado_jogador.status[6]>=1.1*aliado_jogador.status[5]):
                                aliado_jogador.status[6]=aliado_jogador.status[5]*1.1
                            print ('Voce esta com '+aliado_jogador.status[6]+' de '+aliado_jogador.status[5]+' pontos de vida!')
                            time.sleep(0.5)
                            aliado_jogador.inventario[1][i]=desequipado[6]
                            break
                        else:
                            if(acao_do_personagem=="descartar"):
                                while 1:
                                    print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                                    acao_do_personagem=raw_input("-")
                                    acao_do_personagem=acao_do_personagem.lower()
                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                        break
                                    else:
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            break
                                        else:
                                            print("\nENTRADA INVALIDA!\n")
                                            time.sleep(0.5)
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    print("\nVoce descartou"+str(aliado_jogador.inventario[1][i].nome)+"!\n")
                                    time.sleep(0.5)
                                    aliado_jogador.inventario[1][i]=desequipado[6]
                                    break
                            else:
                                if(acao_do_personagem=="voltar"):
                                    break
                                else:
                                    print("\nENTRADA INVALIDA!\n")
                                    time.sleep(0.5)
                if(aliado_jogador.inventario[1][i].tipo!="consumivel de aprimoramento" and aliado_jogador.inventario[1][i].tipo!="consumivel" and aliado_jogador.inventario[1][i].tipo!="inventario"):
                    print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+"\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nAtaque: "+str(aliado_jogador.inventario[1][i].status[0])+"\nDefesa: "+str(aliado_jogador.inventario[1][i].status[1])+"\nAgilidade: "+str(aliado_jogador.inventario[1][i].status[2])+"\nSorte: "+str(aliado_jogador.inventario[1][i].status[3])+"\nVida: "+str(aliado_jogador.inventario[1][i].status[5])+"\nReconstituicao: "+str(aliado_jogador.inventario[1][i].status[4])+"\n")
                    while aliado_jogador.inventario[1][i].tipo!="inventario":
                        print("O que deseja fazer? (equipar, descartar ou voltar)")
                        acao_do_personagem=raw_input("-")
                        acao_do_personagem=acao_do_personagem.lower()
                        if(acao_do_personagem=="descartar"):
                            while 1:
                                print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                                acao_do_personagem=raw_input("-")
                                acao_do_personagem=acao_do_personagem.lower()
                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        break
                                    else:
                                        print("\nENTRADA INVALIDA!\n")
                                        time.sleep(0.5)
                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                print("\nVoce descartou"+str(aliado_jogador.inventario[1][i].nome)+"!\n")
                                time.sleep(0.5)
                                aliado_jogador.inventario[1][i]=desequipado[6]
                                break
                        else:
                            if(acao_do_personagem=="equipar"):#roupa[0], capa[1], luva[2], anel[3], maos[4], calcado[5]
                                if(aliado_jogador.inventario[1][i].tipo=="roupa"):
                                    statusMudanca(False,0)
                                    item_adicionado=aliado_jogador.equipamento[0]#reserva roupa anterior em item_adicionado
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str(aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[0]=aliado_jogador.inventario[1][i]#veste a roupa do inventario
                                    aliado_jogador.inventario[1][i]=item_adicionado#guarda a roupa anterior no mesmo lugar do iventario
                                    statusMudanca(True,0)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="capa"):
                                    statusMudanca(False,1)
                                    item_adicionado=aliado_jogador.equipamento[1]
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str( aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[1]=aliado_jogador.inventario[1][i]
                                    aliado_jogador.inventario[1][i]=item_adicionado
                                    statusMudanca(True,1)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="luva"):
                                    statusMudanca(False,2)
                                    item_adicionado=aliado_jogador.equipamento[2]
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str(aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[2]=aliado_jogador.inventario[1][i]
                                    aliado_jogador.inventario[1][i]=item_adicionado
                                    statusMudanca(True,2)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="anel"):
                                    statusMudanca(False,3)
                                    item_adicionado=aliado_jogador.equipamento[3]
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str(aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[3]=aliado_jogador.inventario[1][i]
                                    aliado_jogador.inventario[1][i]=item_adicionado
                                    statusMudanca(True,3)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="arma"):
                                    statusMudanca(False,4)
                                    item_adicionado=aliado_jogador.equipamento[4]
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str(aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[4]=aliado_jogador.inventario[1][i]
                                    aliado_jogador.inventario[1][i]=item_adicionado
                                    statusMudanca(True,4)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="calcado"):
                                    statusMudanca(False,5)
                                    item_adicionado=aliado_jogador.equipamento[5]
                                    print("Voce guardou "+str(item_adicionado.nome)+" e equipou "+str(aliado_jogador.inventario[1][i].nome)+"!")
                                    time.sleep(1)
                                    aliado_jogador.equipamento[5]=aliado_jogador.inventario[1][i]
                                    aliado_jogador.inventario[1][i]=item_adicionado
                                    statusMudanca(True,5)
                                    break
                                if(aliado_jogador.inventario[1][i].tipo=="consumivel" or aliado_jogador.inventario[1][i].tipo=="consumivel de aprimoramento"):
                                    print("voce nao pode equipar!")
                                    time.sleep(0.5)
                            else:
                                if(acao_do_personagem=="voltar"):
                                    break
                                else:
                                    print("\nENTRADA INVLIDA!\n")
                                    time.sleep(0.5)
        if acao_do_personagem!="voltar":
            time.sleep(0.5)
        os.system('cls')

#--Fichas do Sistema de Troca--#
def fichaTroca(jogador, reserva, garota, headbanger):
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    if jogador == True : print ("\n#"+"-"*77+"#\n "+str(aliado_jogador.identificacao)+" ) Nome: "+str(aliado_jogador.nome)+"\nVida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n")
    if aliado_jogador.identificacao!=1 and aliado_reserva.disponivel == True and reserva == True :
        print ("\n#"+"-"*77+"#\n "+str(aliado_reserva.identificacao)+" ) Nome: "+str(aliado_reserva.nome)+"\nVida: "+str(aliado_reserva.status[6])+" de "+str(aliado_reserva.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_reserva.status[6]))-len(str(aliado_reserva.status[5])))+str(aliado_reserva.status[4])+"\n Ataque: "+str(aliado_reserva.status[0])+"Agilidade: ".rjust(42-len(str(aliado_reserva.status[0])))+str(aliado_reserva.status[2])+"\n Defesa: "+str(aliado_reserva.status[1])+"Sorte: ".rjust(38-len(str(aliado_reserva.status[1])))+str(aliado_reserva.status[3])+"\n Capa: "+str(aliado_reserva.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_reserva.equipamento[1].nome)))+str(aliado_reserva.equipamento[2].nome)+"\n Roupa: "+str(aliado_reserva.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_reserva.equipamento[0].nome)))+str(aliado_reserva.equipamento[3].nome)+"\n Calcado: "+str(aliado_reserva.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_reserva.equipamento[5].nome)))+str(aliado_reserva.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_reserva.dinheiro)+" Reais\n")
        time.sleep(0.15)
    if aliado_jogador.identificacao!=2 and aliado_garota.disponivel == True and garota == True :
        print ("\n#"+"-"*77+"#\n "+str(aliado_garota.identificacao)+" ) Nome: "+str(aliado_garota.nome)+"\nVida: "+str(aliado_garota.status[6])+" de "+str(aliado_garota.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_garota.status[6]))-len(str(aliado_garota.status[5])))+str(aliado_garota.status[4])+"\n Ataque: "+str(aliado_garota.status[0])+"Agilidade: ".rjust(42-len(str(aliado_garota.status[0])))+str(aliado_garota.status[2])+"\n Defesa: "+str(aliado_garota.status[1])+"Sorte: ".rjust(38-len(str(aliado_garota.status[1])))+str(aliado_garota.status[3])+"\n Capa: "+str(aliado_garota.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_garota.equipamento[1].nome)))+str(aliado_garota.equipamento[2].nome)+"\n Roupa: "+str(aliado_garota.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_garota.equipamento[0].nome)))+str(aliado_garota.equipamento[3].nome)+"\n Calcado: "+str(aliado_garota.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_garota.equipamento[5].nome)))+str(aliado_garota.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_garota.dinheiro)+" Reais\n")
        time.sleep(0.15)
    if aliado_jogador.identificacao!=3 and aliado_headbanger.disponivel == True and headbanger == True :
        print ("\n#"+"-"*77+"#\n "+str(aliado_headbanger.identificacao)+" ) Nome: "+str(aliado_headbanger.nome)+"\nVida: "+str(aliado_headbanger.status[6])+" de "+str(aliado_headbanger.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_headbanger.status[6]))-len(str(aliado_headbanger.status[5])))+str(aliado_headbanger.status[4])+"\n Ataque: "+str(aliado_headbanger.status[0])+"Agilidade: ".rjust(42-len(str(aliado_headbanger.status[0])))+str(aliado_headbanger.status[2])+"\n Defesa: "+str(aliado_headbanger.status[1])+"Sorte: ".rjust(38-len(str(aliado_headbanger.status[1])))+str(aliado_headbanger.status[3])+"\n Capa: "+str(aliado_headbanger.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_headbanger.equipamento[1].nome)))+str(aliado_headbanger.equipamento[2].nome)+"\n Roupa: "+str(aliado_headbanger.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_headbanger.equipamento[0].nome)))+str(aliado_headbanger.equipamento[3].nome)+"\n Calcado: "+str(aliado_headbanger.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_headbanger.equipamento[5].nome)))+str(aliado_headbanger.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_headbanger.dinheiro)+" Reais\n")
        time.sleep(0.15)
    print ("\n#"+"-"*77+"#\n")

#--Inventario do Sistema de Troca--#
def inventarioTroca(aliado_analisado):
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(aliado_analisado.inventario[1][i].tipo=="inventario" or aliado_analisado.inventario[1][i].nome=="Nada"):
                if(i<29):
                    if(aliado_analisado.inventario[1][i+1].tipo!="inventario" or aliado_analisado.inventario[1][i+1].nome!="Nada"):
                        aliado_analisado.inventario[1][i] = aliado_analisado.inventario[1][i+1]
                        aliado_analisado.inventario[1][i+1] = desequipado[6]
                variavel_para_comparar+=1
            i+=1
        print ("\n#"+"-"*77+"#\n Inventario:"+str(variavel_para_comparar).rjust(42-len(str(variavel_para_comparar)))+" espaco(s) livre(s) de 30.\n#"+"-"*77+"#\n"+']]Mochila[[                  |             ]]Equipamentos[['.center(79)+"\n"+'|'.center(79))
        variavel_para_comparar=0
        i=0
        while i<=29:
            if i<6:
                if i==0: letra='A'
                if i==1: letra='B'
                if i==2: letra='C'
                if i==3: letra='D'
                if i==4: letra='E'
                if i==5: letra='F'
                if (aliado_analisado.inventario[1][i].tipo!="inventario" and aliado_analisado.inventario[1][i].nome!="Nada"):
                    print (str(aliado_analisado.inventario[0][i])+" : "+str(aliado_analisado.inventario[1][i].nome)+' '*(36-len(str(aliado_analisado.inventario[1][i].nome))-len(str(aliado_analisado.inventario[0][i])))+'|'+str(aliado_analisado.equipamento[i].nome).rjust(35)+" : "+str(letra)+"\n    ("+str(aliado_analisado.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_analisado.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_analisado.equipamento[i].tipo)))+str(aliado_analisado.equipamento[i].tipo)+")")
                else:
                    print (' '*(45-len(str(aliado_analisado.inventario[1][i].nome))-len(str(aliado_analisado.inventario[0][i])))+'|'+str(aliado_analisado.equipamento[i].nome).rjust(41-len(str(aliado_analisado.inventario[1][i].nome))-len(str(aliado_analisado.inventario[0][i])))+" : "+str(letra)+"\n"+' '*(49-len(str(aliado_analisado.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_analisado.equipamento[i].tipo)))+str(aliado_analisado.equipamento[i].tipo)+")")
            if i==6:print (' '*39+'|'+'-'*39)
            elif i==5: i=5
            elif i<6: print ('|'.center(79))
            if (i>5 and aliado_analisado.inventario[1][i].tipo!="inventario" and aliado_analisado.inventario[1][i].nome!="Nada"):
                if aliado_analisado.inventario[1][i+1].tipo!="inventario" and aliado_analisado.inventario[1][i+1].nome!="Nada":
                    print (str(aliado_analisado.inventario[0][i])+" : "+str(aliado_analisado.inventario[1][i].nome)+' '*(36-len(str(aliado_analisado.inventario[1][i].nome))-len(str(aliado_analisado.inventario[0][i])))+'|'+str(aliado_analisado.inventario[1][i+1].nome).rjust(36-len(str(aliado_analisado.inventario[0][i+1])))+" : "+str(aliado_analisado.inventario[0][i+1])+"\n    ("+str(aliado_analisado.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_analisado.inventario[1][i].tipo)))+'|'+"(".rjust(34-len(str(aliado_analisado.inventario[1][i+1].tipo)))+str(aliado_analisado.inventario[1][i+1].tipo)+")")
                else: print (str(aliado_analisado.inventario[0][i])+" : "+str(aliado_analisado.inventario[1][i].nome)+' '*(36-len(str(aliado_analisado.inventario[1][i].nome))-len(str(aliado_analisado.inventario[0][i])))+'|'+"\n    ("+str(aliado_analisado.inventario[1][i].tipo)+")"+' '*(33-len(str(aliado_analisado.inventario[1][i].tipo)))+'|')
                if i/2!=0: print ('|'.center(79))
            if i>5: i+=2
            if i<6: i+=1
        print ("#"+"-"*77+"#\n")
        while 1:
            print("Para analisar um item digite a sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isdigit():
                os.system('cls')
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem = acao_do_personagem.lower()
                if acao_do_personagem !="a" or acao_do_personagem !="b" or acao_do_personagem !="c" or acao_do_personagem !="d" or acao_do_personagem !="e" or acao_do_personagem !="f":
                    if(acao_do_personagem=="voltar"):break
                    print("ENTRADA INVALIDA!")
                    time.sleep(0.5)
                else: print ('Desequipe sozinho antes de trocar.')
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==aliado_analisado.inventario[0][i] and aliado_analisado.inventario[1][i].tipo!="inventario" and aliado_analisado.inventario[1][i].nome!="Nada"):
            if aliado_analisado.identificacao == aliado_jogador.identificacao : fichaTroca(False,True,True,True)
            if aliado_analisado.identificacao == aliado_reserva.identificacao : fichaTroca(True,False,True,True)
            if aliado_analisado.identificacao == aliado_garota.identificacao : fichaTroca(True,True,False,True)
            if aliado_analisado.identificacao == aliado_headbanger.identificacao : fichaTroca(True,True,True,False)
            while 1:
                print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                acao_do_personagem = raw_input('-')
                if acao_do_personagem.isdigit():
                    acao_do_personagem=int(acao_do_personagem)
                    if  aliado_analisado.identificacao==acao_do_personagem: print ('Nao se escolha! \nSe nao quer entregar para ninguem, simplesmente digite voltar!')
                    else: break
                else:
                    if(acao_do_personagem=="voltar"):break
                    print("ENTRADA INVALIDA!")
                    time.sleep(0.5)
            if(acao_do_personagem=="voltar"):break
            if acao_do_personagem==aliado_jogador.identificacao and aliado_jogador.disponivel==True:
                item_adicionado=aliado_analisado.inventario[1][i]
                variavel_para_comparar=0
                e=0
                while e<=29:
                    if(aliado_jogador.inventario[1][e].tipo=="inventario" or aliado_jogador.inventario[1][e].nome=="Nada"):
                        variavel_para_comparar+=1
                    e+=1
                if(variavel_para_comparar<1):
                    print ('Inventario LOTADO!')
                    time.sleep(1)
                else:
                    e=0
                    while e<=29:
                        if(aliado_jogador.inventario[1][e].tipo=="inventario" or aliado_jogador.inventario[1][e].nome=="Nada"):
                            aliado_jogador.inventario[1][e]=item_adicionado
                            aliado_analisado.inventario[1][i]=desequipado[6]
                            print (str(aliado_analisado.nome)+' transferiu '+item_adicionado+' para '+str(aliado_jogador.nome)+'.')
                            break
                        e+=1
            elif acao_do_personagem==aliado_reserva.identificacao and aliado_reserva.disponivel==True:
                item_adicionado=aliado_analisado.inventario[1][i]
                variavel_para_comparar=0
                e=0
                while e<=29:
                    if(aliado_reserva.inventario[1][e].tipo=="inventario" or aliado_reserva.inventario[1][e].nome=="Nada"):
                        variavel_para_comparar+=1
                    e+=1
                if(variavel_para_comparar<1):
                    print ('Inventario LOTADO!')
                    time.sleep(1)
                else:
                    e=0
                    while e<=29:
                        if(aliado_reserva.inventario[1][e].tipo=="inventario" or aliado_reserva.inventario[1][e].nome=="Nada"):
                            aliado_reserva.inventario[1][e]=item_adicionado
                            aliado_analisado.inventario[1][i]=desequipado[6]
                            print (str(aliado_analisado.nome)+' transferiu '+item_adicionado+' para '+str(aliado_reserva.nome)+'.')
                            break
                        e+=1
            elif acao_do_personagem==aliado_garota.identificacao and aliado_garota.disponivel==True:
                item_adicionado=aliado_analisado.inventario[1][i]
                variavel_para_comparar=0
                e=0
                while e<=29:
                    if(aliado_garota.inventario[1][e].tipo=="inventario" or aliado_garota.inventario[1][e].nome=="Nada"):
                        variavel_para_comparar+=1
                    e+=1
                if(variavel_para_comparar<1):
                    print ('Inventario LOTADO!')
                    time.sleep(1)
                else:
                    e=0
                    while e<=29:
                        if(aliado_garota.inventario[1][e].tipo=="inventario" or aliado_garota.inventario[1][e].nome=="Nada"):
                            aliado_garota.inventario[1][e]=item_adicionado
                            aliado_analisado.inventario[1][i]=desequipado[6]
                            print (str(aliado_analisado.nome)+' transferiu '+item_adicionado+' para '+str(aliado_garota.nome)+'.')
                            break
                        e+=1
            elif acao_do_personagem==aliado_headbanger.identificacao and aliado_headbanger.disponivel==True:
                item_adicionado=aliado_analisado.inventario[1][i]
                variavel_para_comparar=0
                e=0
                while e<=29:
                    if(aliado_headbanger.inventario[1][e].tipo=="inventario" or aliado_headbanger.inventario[1][e].nome=="Nada"):
                        variavel_para_comparar+=1
                    e+=1
                if(variavel_para_comparar<1):
                    print ('Inventario LOTADO!')
                    time.sleep(1)
                else:
                    e=0
                    while e<=29:
                        if(aliado_headbanger.inventario[1][e].tipo=="inventario" or aliado_headbanger.inventario[1][e].nome=="Nada"):
                            aliado_headbanger.inventario[1][e]=item_adicionado
                            aliado_analisado.inventario[1][i]=desequipado[6]
                            print (str(aliado_analisado.nome)+' transferiu '+item_adicionado+' para '+str(aliado_headbanger.nome)+'.')
                            break
                        e+=1
            else: print ('Entrada invalida!')

#--Sistema de Troca de Personagem--#
def trocaPersonagem():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        fichaTroca(True,True,True,True)
        while 1:
            print("Para analisar um personagem digite o numero da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isdigit():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVALIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        if acao_do_personagem==aliado_jogador.identificacao:
            print ("O que deseja fazer? (substituir, transferir dinheiro ou transferir item)")
            if acao_do_personagem=="substituir":
                fichaTroca(False,True,True,True)
                while 1:
                    print ('Com quem quer jogar? (digite o numero da posicao ou "voltar")')
                    acao_do_personagem = raw_input('-')
                    if acao_do_personagem.isdigit():
                        acao_do_personagem=int(acao_do_personagem)
                        break
                    else:
                        if(acao_do_personagem=="voltar"):break
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)
                if(acao_do_personagem=="voltar"):break
                if acao_do_personagem==aliado_reserva.identificacao and aliado_reserva.disponivel == True:
                    if aliado_jogador.identificacao==2:
                        aliado_garota=aliado_jogador
                        aliado_jogador=aliado_reserva
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                    if aliado_jogador.identificacao==3:
                        aliado_headbanger=aliado_jogador
                        aliado_jogador=aliado_reserva
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                elif acao_do_personagem==aliado_garota.identificacao and aliado_garota.disponivel == True:
                    if aliado_jogador.identificacao==1:
                        aliado_reserva=aliado_jogador
                        aliado_jogador=aliado_garota
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                    if aliado_jogador.identificacao==3:
                        aliado_headbanger=aliado_jogador
                        aliado_jogador=aliado_garota
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                elif acao_do_personagem==aliado_headbanger.identificacao and aliado_headbanger.disponivel == True:
                    if aliado_jogador.identificacao==1:
                        aliado_reserva=aliado_jogador
                        aliado_jogador=aliado_headbanger
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                    if aliado_jogador.identificacao==2:
                        aliado_garota=aliado_jogador
                        aliado_jogador=aliado_headbanger
                        print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                else:print ('Entrada invalida!')
            elif acao_do_personagem=="transferir dinheiro":
                fichaTroca(False,True,True,True)
                while 1:
                    print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                    acao_do_personagem = raw_input('-')
                    if acao_do_personagem.isdigit():
                        acao_do_personagem=int(acao_do_personagem)
                        break
                    else:
                        if(acao_do_personagem=="voltar"):break
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)
                if(acao_do_personagem=="voltar"):break
                if acao_do_personagem==aliado_reserva.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_jogador.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_jogador.dinheiro-=acao_do_personagem
                    aliado_reserva.dinheiro+=acao_do_personagem
                    print (str(aliado_jogador.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_reserva.nome)+'.')
                elif acao_do_personagem==aliado_garota.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_jogador.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_jogador.dinheiro-=acao_do_personagem
                    aliado_garota.dinheiro+=acao_do_personagem
                    print (str(aliado_jogador.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_garota.nome)+'.')
                elif acao_do_personagem==aliado_headbanger.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_jogador.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_jogador.dinheiro-=acao_do_personagem
                    aliado_headbanger.dinheiro+=acao_do_personagem
                    print (str(aliado_jogador.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_headbanger.nome)+'.')
            elif acao_do_personagem=="transferir item": inventarioTroca(aliado_jogador)
        elif acao_do_personagem==aliado_reserva.identificacao and alidado_reserva.disponivel==True:
            print ("O que deseja fazer? (substituir, transferir dinheiro ou transferir item)")
            if acao_do_personagem=="substituir":
                if aliado_jogador.identificacao==2:
                    aliado_garota=aliado_jogador
                    aliado_jogador=aliado_reserva
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                if aliado_jogador.identificacao==3:
                    aliado_headbanger=aliado_jogador
                    aliado_jogador=aliado_reserva
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
            elif acao_do_personagem=="transferir dinheiro":
                fichaTroca(True,False,True,True)
                while 1:
                    print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                    acao_do_personagem = raw_input('-')
                    if acao_do_personagem.isdigit():
                        acao_do_personagem=int(acao_do_personagem)
                        break
                    else:
                        if(acao_do_personagem=="voltar"):break
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)
                if(acao_do_personagem=="voltar"):break
                if acao_do_personagem==aliado_jogador.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_reserva.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_reserva.dinheiro-=acao_do_personagem
                    aliado_jogador.dinheiro+=acao_do_personagem
                    print (str(aliado_reserva.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_jogador.nome)+'.')
                elif acao_do_personagem==aliado_garota.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_reserva.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_reserva.dinheiro-=acao_do_personagem
                    aliado_garota.dinheiro+=acao_do_personagem
                    print (str(aliado_reserva.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_garota.nome)+'.')
                elif acao_do_personagem==aliado_headbanger.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_reserva.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_reserva.dinheiro-=acao_do_personagem
                    aliado_headbanger.dinheiro+=acao_do_personagem
                    print (str(aliado_reserva.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_headbanger.nome)+'.')
            elif acao_do_personagem=="transferir item":
                inventarioTroca(aliado_reserva)
                while 1:
                    variavel_para_comparar=0
                    i=0
                    while i<=29:
                        if(aliado_reserva.inventario[1][i].tipo=="inventario" or aliado_reserva.inventario[1][i].nome=="Nada"):
                            variavel_para_comparar+=1
                        i+=1
                    print("Mochila:        "+str(variavel_para_comparar)+" espaco(s) livre(s) de 30.\n")
                    variavel_para_comparar=0
                    time.sleep(0.5)
                    i=0
                    while i<=29:
                        if (aliado_reserva.inventario[1][i].tipo!="inventario" and aliado_reserva.inventario[1][i].nome!="Nada"):
                            print(str(aliado_reserva.inventario[0][i])+" : "+str(aliado_reserva.inventario[1][i].nome)+"\n     ("+str(aliado_reserva.inventario[1][i].tipo)+")\n")
                        i+=1
                    while 1:
                        print("Para analisar um item digite o numero da sua posicao!\nPara voltar ao jogo digite voltar.")
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    i=0
                    while i<=29:
                        if(i==acao_do_personagem):
                            break
                        i+=1
                    i=i-1
                    if(acao_do_personagem==aliado_reserva.inventario[0][i] and aliado_reserva.inventario[1][i].tipo!="inventario" and aliado_reserva.inventario[1][i].nome!="Nada"):
                        fichaTroca(True,False,True,True)
                        while 1:
                            print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                            acao_do_personagem = raw_input('-')
                            if acao_do_personagem.isdigit():
                                acao_do_personagem=int(acao_do_personagem)
                                break
                            else:
                                if(acao_do_personagem=="voltar"):break
                                print("ENTRADA INVALIDA!")
                                time.sleep(0.5)
                        if(acao_do_personagem=="voltar"):break
                        if acao_do_personagem==aliado_jogador.identificacao:
                            item_adicionado=aliado_reserva.inventario[1][i]
                            variavel_para_comparar=0
                            e=0
                            while e<=29:
                                if(aliado_jogador.inventario[1][e].tipo=="inventario" or aliado_jogador.inventario[1][e].nome=="Nada"):
                                    variavel_para_comparar+=1
                                e+=1
                            if(variavel_para_comparar<1):
                                print ('Inventario LOTADO!')
                                time.sleep(1)
                            else:
                                e=0
                                while e<=29:
                                    if(aliado_jogador.inventario[1][e].tipo=="inventario" or aliado_jogador.inventario[1][e].nome=="Nada"):
                                        aliado_jogador.inventario[1][e]=item_adicionado
                                        aliado_reserva.inventario[1][i]=desequipado[6]
                                        print (str(aliado_reserva.nome)+' transferiu '+item_adicionado+' para '+str(aliado_jogador.nome)+'.')
                                        break
                                    e+=1
                        elif acao_do_personagem==aliado_garota.identificacao:
                            item_adicionado=aliado_reserva.inventario[1][i]
                            variavel_para_comparar=0
                            e=0
                            while e<=29:
                                if(aliado_garota.inventario[1][e].tipo=="inventario" or aliado_garota.inventario[1][e].nome=="Nada"):
                                    variavel_para_comparar+=1
                                e+=1
                            if(variavel_para_comparar<1):
                                print ('Inventario LOTADO!')
                                time.sleep(1)
                            else:
                                e=0
                                while e<=29:
                                    if(aliado_garota.inventario[1][e].tipo=="inventario" or aliado_garota.inventario[1][e].nome=="Nada"):
                                        aliado_garota.inventario[1][e]=item_adicionado
                                        aliado_reserva.inventario[1][i]=desequipado[6]
                                        print (str(aliado_reserva.nome)+' transferiu '+item_adicionado+' para '+str(aliado_garota.nome)+'.')
                                        break
                                    e+=1
                        elif acao_do_personagem==aliado_headbanger.identificacao:
                            item_adicionado=aliado_reserva.inventario[1][i]
                            variavel_para_comparar=0
                            e=0
                            while e<=29:
                                if(aliado_headbanger.inventario[1][e].tipo=="inventario" or aliado_headbanger.inventario[1][e].nome=="Nada"):
                                    variavel_para_comparar+=1
                                e+=1
                            if(variavel_para_comparar<1):
                                print ('Inventario LOTADO!')
                                time.sleep(1)
                            else:
                                e=0
                                while e<=29:
                                    if(aliado_headbanger.inventario[1][e].tipo=="inventario" or aliado_headbanger.inventario[1][e].nome=="Nada"):
                                        aliado_headbanger.inventario[1][e]=item_adicionado
                                        aliado_reserva.inventario[1][i]=desequipado[6]
                                        print (str(aliado_reserva.nome)+' transferiu '+item_adicionado+' para '+str(aliado_headbanger.nome)+'.')
                                        break
                                    e+=1
                        else: print ('Entrada invalida!')
        elif acao_do_personagem==aliado_garota.identificacao:
            print ("O que deseja fazer? (substituir, transferir dinheiro ou transferir item)")
            if acao_do_personagem=="substituir":
                if aliado_jogador.identificacao==1:
                    aliado_reserva=aliado_jogador
                    aliado_jogador=aliado_garota
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                if aliado_jogador.identificacao==3:
                    aliado_headbanger=aliado_jogador
                    aliado_jogador=aliado_garota
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
            elif acao_do_personagem=="transferir dinheiro":
                fichaTroca(True,True,False,True)
                while 1:
                    print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                    acao_do_personagem = raw_input('-')
                    if acao_do_personagem.isdigit():
                        acao_do_personagem=int(acao_do_personagem)
                        break
                    else:
                        if(acao_do_personagem=="voltar"):break
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)
                if(acao_do_personagem=="voltar"):break
                if acao_do_personagem==aliado_jogador.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_garota.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_garota.dinheiro-=acao_do_personagem
                    aliado_jogador.dinheiro+=acao_do_personagem
                    print (str(aliado_garota.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_jogador.nome)+'.')
                elif acao_do_personagem==aliado_reserva.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_garota.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_garota.dinheiro-=acao_do_personagem
                    aliado_reserva.dinheiro+=acao_do_personagem
                    print (str(aliado_garota.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_reserva.nome)+'.')
                elif acao_do_personagem==aliado_headbanger.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_garota.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_garota.dinheiro-=acao_do_personagem
                    aliado_headbanger.dinheiro+=acao_do_personagem
                    print (str(aliado_garota.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_headbanger.nome)+'.')
            elif acao_do_personagem=="transferir item": inventarioTroca(aliado_garota)
        elif acao_do_personagem==aliado_headbanger.identificacao:
            print ("O que deseja fazer? (substituir, transferir dinheiro ou transferir item)")
            if acao_do_personagem=="substituir":
                if aliado_jogador.identificacao==1:
                    aliado_reserva=aliado_jogador
                    aliado_jogador=aliado_headbanger
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
                if aliado_jogador.identificacao==2:
                    aliado_garota=aliado_jogador
                    aliado_jogador=aliado_headbanger
                    print ('Agora voce esta jogando como '+str(aliado_jogador.nome)+'!')
            elif acao_do_personagem=="transferir dinheiro":
                fichaTroca(True,True,True,False)
                while 1:
                    print ('Para quem vai entregar? (digite o numero da posicao ou "voltar")')
                    acao_do_personagem = raw_input('-')
                    if acao_do_personagem.isdigit():
                        acao_do_personagem=int(acao_do_personagem)
                        break
                    else:
                        if(acao_do_personagem=="voltar"):break
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)
                if(acao_do_personagem=="voltar"):break
                if acao_do_personagem==aliado_jogador.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_headbanger.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_headbanger.dinheiro-=acao_do_personagem
                    aliado_jogador.dinheiro+=acao_do_personagem
                    print (str(aliado_headbanger.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_jogador.nome)+'.')
                elif acao_do_personagem==aliado_reserva.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_headbanger.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_headbanger.dinheiro-=acao_do_personagem
                    aliado_reserva.dinheiro+=acao_do_personagem
                    print (str(aliado_headbanger.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_reserva.nome)+'.')
                elif acao_do_personagem==aliado_garota.identificacao:
                    while 1:
                        print ('Quanto? (digite um valor ou "voltar")')
                        acao_do_personagem = raw_input('-')
                        if acao_do_personagem.isdigit():
                            acao_do_personagem=int(acao_do_personagem)
                            if acao_do_personagem>aliado_headbanger.dinheiro:
                                print ('Voce nao tem todo esse dinheiro!')
                            elif acao_do_personagem<=0:
                                print ('Voce so pode entregar valores acima de zero.')
                            else:
                                break
                        else:
                            if(acao_do_personagem=="voltar"):break
                            print("ENTRADA INVALIDA!")
                            time.sleep(0.5)
                    if(acao_do_personagem=="voltar"):break
                    aliado_headbanger.dinheiro-=acao_do_personagem
                    aliado_garota.dinheiro+=acao_do_personagem
                    print (str(aliado_headbanger.nome)+' transferiu '+acao_do_personagem+' Reais para '+str(aliado_garota.nome)+'.')
            elif acao_do_personagem=="transferir item": inventarioTroca(aliado_headbanger)
        else: print ('Entrada invalida!')

#--Loja: Vender--#
def lojaVender():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("Mochila:        "+str(variavel_para_comparar)+" espacos livres.\n")
        variavel_para_comparar=0
        time.sleep(0.5)
        i=0
        while i<=29:
            if (aliado_jogador.inventario[1][i].tipo!="inventario" and aliado_jogador.inventario[1][i].nome!="Nada"):
                print(str(aliado_jogador.inventario[0][i])+" : "+str(aliado_jogador.inventario[1][i].nome)+"\n     ("+str(aliado_jogador.inventario[1][i].tipo)+")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o numero da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isdigit():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVALIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==aliado_jogador.inventario[0][i] and aliado_jogador.inventario[1][i].tipo!="inventario" and aliado_jogador.inventario[1][i].nome!="Nada"):
            if(aliado_jogador.inventario[1][i][5]=="consumivel de aprimoramento"):
                print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+ "\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nVida: "+str(aliado_jogador.inventario[1][i].status[5])+"\nAtaque: "+str(aliado_jogador.inventario[1][i].status[0])+"\nDefesa: "+str(aliado_jogador.inventario[1][i].status[1])+"\nAgilidade: "+str(aliado_jogador.inventario[1][i].status[2])+"\nSorte: "+str(aliado_jogador.inventario[1][i].status[3])+"\n")
            if(aliado_jogador.inventario[1][i][5]=="consumivel"):
                print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+ "\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nVida: "+str(aliado_jogador.inventario[1][i].status[6])+"\n")
            if(aliado_jogador.inventario[1][i].tipo!="consumivel de aprimoramento" and aliado_jogador.inventario[1][i].tipo!="consumivel" and aliado_jogador.inventario[1][i].tipo!="inventario"):
                print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+"\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nAtaque: "+str(aliado_jogador.inventario[1][i].status[0])+"\nDefesa: "+str(aliado_jogador.inventario[1][i].status[1])+"\nAgilidade: "+str(aliado_jogador.inventario[1][i].status[2])+"\nSorte: "+str(aliado_jogador.inventario[1][i].status[3])+"\nVida: "+str(aliado_jogador.inventario[1][i].status[5])+"\nReconstituicao: "+str(aliado_jogador.inventario[1][i].status[4])+"\n")
        while 1:
            print("Posso comprar por "+str(aliado_jogador.inventario[1][i].preco*porcentagem_inflacao)+"Reais.")
            time.sleep(0.5)
            print("Vai querer vender?(sim ou nao)")
            acao_do_personagem=raw_input("-")
            acao_do_personagem=acao_do_personagem.lower()
            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                break
            else:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    aliado_jogador.dinheiro += aliado_jogador.inventario[1][i].preco*porcentagem_inflacao
                    aliado_jogador.inventario[1][i]=desequipado[6]
                    print("Obrigado!")
                    time.sleep(0.5)
                    break
                else:
                    print("ENTRADA INVALIDA!")
                    time.sleep(0.5)

#--Loja: Comprar--#
def lojaComprar():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("                      "+str(variavel_para_comparar)+" espaco(s) livre(s) de 30.\n")
        variavel_para_comparar=0
        print("Produtos a venda:\n")
        time.sleep(0.5)
        i=0
        while i<=29:
            if (Venda.inventario[1][i].tipo!="inventario"):
                print(str(Venda.inventario[0][i])+" : "+str(Venda.inventario[1][i].nome)+"\n     ("+str(Venda.inventario[1][i].tipo)+")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o numero da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isdigit():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVALIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==Venda.inventario[0][i] and Venda.inventario[1][i].tipo!="inventario"):
            if(Venda.inventario[1][i][5]=="consumivel de aprimoramento"):
                print("\nNome: "+str(Venda.inventario[1][i].nome)+ "\nTipo: "+str(Venda.inventario[1][i].tipo)+"\nVida: "+str(Venda.inventario[1][i].status[5])+"\nAtaque: "+str(Venda.inventario[1][i].status[0])+"\nDefesa: "+str(Venda.inventario[1][i].status[1])+"\nAgilidade: "+str(Venda.inventario[1][i].status[2])+"\nSorte: "+str(Venda.inventario[1][i].status[3])+"\n")
            if(Venda.inventario[1][i][5]=="consumivel"):
                print("\nNome: "+str(Venda.inventario[1][i].nome)+ "\nTipo: "+str(Venda.inventario[1][i].tipo)+"\nVida: "+str(Venda.inventario[1][i].status[6])+"\n")
            if(Venda.inventario[1][i].tipo!="consumivel de aprimoramento" and Venda.inventario[1][i].tipo!="consumivel" and Venda.inventario[1][i].tipo!="inventario"):
                print("\nNome: "+str(Venda.inventario[1][i].nome)+"\nTipo: "+str(Venda.inventario[1][i].tipo)+"\nAtaque: "+str(Venda.inventario[1][i].status[0])+"\nDefesa: "+str(Venda.inventario[1][i].status[1])+"\nAgilidade: "+str(Venda.inventario[1][i].status[2])+"\nSorte: "+str(Venda.inventario[1][i].status[3])+"\nVida: "+str(Venda.inventario[1][i].status[5])+"\nReconstituicao: "+str(Venda.inventario[1][i].status[4])+"\n")
            item_adicionado=Venda.inventario[1][i]
            while 1:
                print("Deseja comprar quantos?(digite uma quantidade ou voltar)")
                acao_do_personagem = raw_input('-')
                if acao_do_personagem.isdigit():
                    acao_do_personagem=int(acao_do_personagem)
                    variavel_para_comparar=0
                    i=0
                    while i<=29:
                        if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                            variavel_para_comparar+=1
                        i+=1
                    if(acao_do_personagem>variavel_para_comparar):
                        print("Voce nao pode comprar essa quantidade, pois so tem"+str(variavel_para_comparar)+"espacos livres na mochila!")
                        variavel_para_comparar=0
                    else:
                        quantidade_adicionada=acao_do_personagem
                        break
                else:
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem=="voltar"):break
                    print("ENTRADA INVALIDA!")
                    time.sleep(0.5)
            if(acao_do_personagem=="voltar"):break
            while 1:
                print("Ficou "+str(item_adicionado.preco*quantidade_adicionada*porcentagem_inflacao)+" Reais.")
                print("Vai comprar mesmo?(sim ou nao)")
                acao_do_personagem=raw_input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                    break
                else:
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        if(aliado_jogador.dinheiro >= item_adicionado.preco*quantidade_adicionada*porcentagem_inflacao):
                            aliado_jogador.dinheiro -= item_adicionado.preco*quantidade_adicionada*porcentagem_inflacao
                            adicionaItem()
                            print("Obrigado!")
                            time.sleep(0.5)
                            break
                        else:
                            print("Voce nao tem grana pra pagar!")
                            time.sleep(0.5)
                            break
                    else:
                        print("ENTRADA INVALIDA!")
                        time.sleep(0.5)

#--Save--#
def save():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
    print('\nDeseja salvar seu progresso?("sim" ou "nao")\n')
    time.sleep(0.5)
    while 1:
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
            print("\nDeseja salvar em qual espaco?\n")
            time.sleep(0.5)
            arq = open('\espaco_save00.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  0:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save01.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  1:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save02.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  2:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save03.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  3:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save04.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  4:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save05.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  5:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save06.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  6:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save07.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  7:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save08.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  8:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            arq = open('\espaco_save09.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  9:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
            arq.close
            while 1:
                print("\n(Digite um numero entre 0 e 9)")
                acao_do_personagem=raw_input("-")
                if(acao_do_personagem=="0"):
                    arq = open('\espaco_save00.py', 'wb')
                    break
                else:
                    if(acao_do_personagem=="1"):
                        arq = open('\espaco_save01.py', 'wb')
                        break
                    else:
                        if(acao_do_personagem=="2"):
                            arq = open('\espaco_save02.py', 'wb')
                            break
                        else:
                            if(acao_do_personagem=="3"):
                                arq = open('\espaco_save03.py', 'wb')
                                break
                            else:
                                if(acao_do_personagem=="4"):
                                    arq = open('\espaco_save04.py', 'wb')
                                    break
                                else:
                                    if(acao_do_personagem=="5"):
                                        arq = open('\espaco_save05.py', 'wb')
                                        break
                                    else:
                                        if(acao_do_personagem=="6"):
                                            arq = open('\espaco_save06.py', 'wb')
                                            break
                                        else:
                                            if(acao_do_personagem=="7"):
                                                arq = open('\espaco_save07.py', 'wb')
                                                break
                                            else:
                                                if(acao_do_personagem=="8"):
                                                    arq = open('\espaco_save08.py', 'wb')
                                                    break
                                                else:
                                                    if(acao_do_personagem=="9"):
                                                        arq = open('\espaco_save09.py', 'wb')
                                                        break
                                                    else:
                                                        print("Entrada invalida!\n")
                                                        time.sleep(0.5)
            #recomendo voce usar um for aqui :) - Lucas Sabiao
            mostrar_save = [aliado_jogador.nome,aliado_jogador.status[5],variavel_lugar,aliado_jogador.status[0],aliado_jogador.status[1],aliado_jogador.status[2],aliado_jogador.status[3]]
            pickle.dump(mostrar_save, arq)
            pickle.dump(variavel_cenario, arq)
            pickle.dump(objeto, arq)
            pickle.dump(situacao, arq)
            pickle.dump(booleana, arq)
            pickle.dump(variavel_lugar, arq)
            pickle.dump(ponto_de_save, arq)
            pickle.dump(aliado_jogador, arq)
            pickle.dump(aliado_reserva, arq)
            pickle.dump(aliado_headbanger, arq)
            pickle.dump(aliado_garota, arq)
            arq.close
            print("\nPronto!\n")
            time.sleep(1)
            break
        else:
            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                break
            else:
                print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                time.sleep(0.5)

#--Inventario do Sistema de Batalha--#
def inventarioBatalha():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    os.system('cls')
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(aliado_jogador.inventario[1][i].tipo=="inventario" or aliado_jogador.inventario[1][i].nome=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("Mochila:        "+str(variavel_para_comparar)+" espaco(s) livre(s) de 30.\n")
        variavel_para_comparar=0
        time.sleep(0.5)
        i=0
        while i<=29:
            if (aliado_jogador.inventario[1][i].tipo=="consumivel" and aliado_jogador.inventario[1][i].nome!="Nada"):
                print (str(aliado_jogador.inventario[0][i])+" : "+str(aliado_jogador.inventario[1][i].nome)+"\n")
            i+=1
        while 1:
            print ("Para analisar um item digite o numero da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isdigit():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVALIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==aliado_jogador.inventario[0][i] and aliado_jogador.inventario[1][i].nome!="Nada" and aliado_jogador.inventario[1][i].tipo=="consumivel"):
            print("\nNome: "+str(aliado_jogador.inventario[1][i].nome)+ "\nTipo: "+str(aliado_jogador.inventario[1][i].tipo)+"\nVida: "+str(aliado_jogador.inventario[1][i].status[6])+"\n")
            while 1:
                print("O que deseja fazer? (usar ou voltar)")
                acao_do_personagem=raw_input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="usar"):
                    print("\nVoce usou "+ str(aliado_jogador.inventario[1][i].nome)+"!\n")
                    if aliado_jogador.status[6]+aliado_jogador.inventario[1][i].status[6]<1.1*aliado_jogador.status[5]:
                        print ('Voce recuperou '+str(aliado_jogador.inventario[1][i].status[6])+' pontos de vida!')
                        time.sleep(0.5)
                    aliado_jogador.status[6]+=aliado_jogador.inventario[1][i].status[6]
                    if (aliado_jogador.status[6]>=1.1*aliado_jogador.status[5]):
                        aliado_jogador.status[6]=aliado_jogador.status[5]*1.1
                    print ('Voce esta com '+aliado_jogador.status[6]+' de '+aliado_jogador.status[5]+' pontos de vida!')
                    time.sleep(0.5)
                    aliado_jogador.inventario[1][i]=desequipado[6]
                    booleana[4]=True
                    break
                elif(acao_do_personagem=="voltar"):
                    os.system('cls')
                    break
                else:
                    print("\nENTRADA INVALIDA!\n")
                    time.sleep(0.5)
        else:
            print ("\nENTRADA INVALIDA!\n")
            time.sleep(0.5)


#--Sistema de batalha--#
def batalha(entrada_inimigo_batalha):
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    adversario_inimigo=entrada_inimigo_batalha
    adversario_inimigo.status=entrada_inimigo_batalha.status
    raw_input('|>')
    os.system("cls")
    print ("\n\n\n\n\n\n\n\n"+"Batalha!!!".center(79)+"\n"+"E hora da briga, estudante!!!".center(79))
    time.sleep(3)
    os.system("cls")
    contador_de_rodadas=1
    while(adversario_inimigo.status[6]>0):
        booleana[3]=False
        if(aliado_jogador.status[6]<=0):break
        if aliado_jogador.status[6] < aliado_jogador.status[5]:
            print ('\nVoce se recuperou em '+str(aliado_jogador.status[4])+" pontos de vida.\n")
        if adversario_inimigo.status[6] < adversario_inimigo.status[5]:
            print ('\nO oponente se recuperou em '+str(adversario_inimigo.status[4])+" pontos de vida.\n")
        if contador_de_rodadas!=1: raw_input('|>')
        aliado_jogador.status[6]+=aliado_jogador.status[4]
        if aliado_jogador.status[6] > aliado_jogador.status[5]: aliado_jogador.status[6]=aliado_jogador.status[5]
        if aliado_jogador.status[6] <=0 : aliado_jogador.status[6]=1
        adversario_inimigo.status[6]+=adversario_inimigo.status[4]
        if adversario_inimigo.status[6] > adversario_inimigo.status[5]: adversario_inimigo.status[6]=adversario_inimigo.status[5]
        if adversario_inimigo.status[6] <=0 : adversario_inimigo.status[6]=1
        os.system("cls")
        print("\n]]"+ "="*75+"[[\n"+"\t\t\t   Inicio da rodada numero "+str(contador_de_rodadas)+"\n]]"+"="*75+"[[\n")
        if(aliado_jogador.status[6]<10):
            if(contador_de_rodadas==1):
                print("\nVoce entrou na batalha quase sem forcas vitais!")
                time.sleep(1)
                print("Seu ultimo recurso e a tensao!\n")
                time.sleep(1)
            else:
                if(contador_de_batalha==0):
                    print("\nVoce esta com a vida muito proxima a zero!")
                    time.sleep(1)
                    print("Seu ultimo recurso e a tensao!\n")
                    time.sleep(1)
            if(contador_de_batalha>0):       
                print("\nVoce aguentou mais uma rodada com a vida proxima a zero!")
                time.sleep(1)
                print("Voce extendeu o limite do seu folego e agora o limite dos seus pontos de vida subiu!\n")
                time.sleep(2)
                aliado_jogador.status[5]+=+contador_de_batalha
            contador_de_batalha+=1
        else:
            if(aliado_jogador.status[6]<=aliado_jogador.status[5]*0.05):
                teste_de_sorte=random.randrange(150)
                if(teste_de_sorte<=10+aliado_jogador.status[3]):
                    print("\nVoce esta dando o seu melhor para aguentar, isso esta melhorando o seu folego!")
                    time.sleep(1)
                    print("O limite dos seus pontos de vida aumentou!\n")
                    time.sleep(2)
                    aliado_jogador.status[5]+=int((random.randrange(aliado_jogador.status[5]))/20)+1
        while 1:
            if adversario_inimigo.status[6]<=0.05*adversario_inimigo.status[5]: barra_inimigo = "[-----------------------------!]"
            elif adversario_inimigo.status[6]<=adversario_inimigo.status[5]: barra_inimigo = "["+"-"*int(30-(adversario_inimigo.status[6]*30/adversario_inimigo.status[5]))+"|"*int(adversario_inimigo.status[6]*30/adversario_inimigo.status[5])+"]"
            else: barra_inimigo = "[!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]"
            if aliado_jogador.status[6]<=0.05*aliado_jogador.status[5]: barra_jogador = "[!-----------------------------]"
            elif aliado_jogador.status[6]<=aliado_jogador.status[5]: barra_jogador = "["+"|"*int(aliado_jogador.status[6]*30/aliado_jogador.status[5])+"-"*int(30-(aliado_jogador.status[6]*30/aliado_jogador.status[5]))+"]"
            else: barra_jogador = "[!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!]"
            print ("\n#"+"-"*77+"#\n"+'|'.center(79)+'\n'+str(aliado_jogador.nome)+' '*(39-len(str(aliado_jogador.nome)))+'|'+str(adversario_inimigo.nome).rjust(78-len(aliado_jogador.nome)-(39-len(str(aliado_jogador.nome))))+"\n"+str(barra_jogador)+' '*(39-len(str(barra_jogador)))+'|'+str(barra_inimigo).rjust(39)+"\n"+str(aliado_jogador.status[6])+' /'+str(aliado_jogador.status[5])+' '*(37-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+'|'+str(adversario_inimigo.status[6]).rjust(79-(39+len(str(adversario_inimigo.status[5]))+len(str(aliado_jogador.status[5]))))+' /'+str(adversario_inimigo.status[5])+"\n"+'|'.center(79)+"\n#"+"-"*77+"#\nO que voce fara agora, "+str(aliado_jogador.nome)+"?\nAtacar, defender, ver mochila, ver ficha do personagem ou fugir?")
            time.sleep(0.15)
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            os.system("cls")
            if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
                print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
                raw_input('|>')
                os.system('cls')
            elif (acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                inventarioBatalha()
                os.system('cls')
                if booleana[4] == True: break
            elif (acao_do_personagem != "atacar" and acao_do_personagem != "defender" and acao_do_personagem != "fugir" and acao_do_personagem!="f" and acao_do_personagem!="fugri" and acao_do_personagem!="fguir" and acao_do_personagem!="fugeir" and acao_do_personagem!="furig" and acao_do_personagem!="fuer" and acao_do_personagem!="ffugri" and acao_do_personagem!="gfuir" and acao_do_personagem!="fiur" and acao_do_personagem!="fugi" and acao_do_personagem!="fugr" and acao_do_personagem!="fug" and acao_do_personagem!="fgir" and acao_do_personagem!="fir" and acao_do_personagem!="fgr" and acao_do_personagem!="ugir" and acao_do_personagem!="gir" and acao_do_personagem!="figr" and acao_do_personagem!="fu" and acao_do_personagem != "d" and acao_do_personagem != "defende" and acao_do_personagem != "defern" and acao_do_personagem != "defenrede" and acao_do_personagem != "ddefender" and acao_do_personagem != "defenrd" and acao_do_personagem != "deffender" and acao_do_personagem != "defendder" and acao_do_personagem != "ddeffender" and acao_do_personagem != "defnder" and acao_do_personagem != "defndr" and acao_do_personagem != "dfnder" and acao_do_personagem != "dfendr" and acao_do_personagem != "defnde" and acao_do_personagem != "defnd" and acao_do_personagem != "dfede" and acao_do_personagem != "def" and acao_do_personagem!="a" and acao_do_personagem!="at" and acao_do_personagem!="ata" and acao_do_personagem!="atac" and acao_do_personagem!="ataca" and acao_do_personagem!="atcar" and acao_do_personagem!="tacar" and acao_do_personagem!="aacar" and acao_do_personagem!="ataar" and acao_do_personagem!="atacr" and acao_do_personagem!="acar" and acao_do_personagem!="aaar" and acao_do_personagem!="aacr" and acao_do_personagem!="aaca" and acao_do_personagem!="atar" and acao_do_personagem!="atcr" and acao_do_personagem!="atca" and acao_do_personagem!="ata" and acao_do_personagem!="ataa" and acao_do_personagem!="atara" and acao_do_personagem!="stssr" and acao_do_personagem!="atavar" and acao_do_personagem!="atahvea" and acao_do_personagem!="atrex" and acao_do_personagem!="atasfa" and acao_do_personagem!="atacart" and acao_do_personagem!="taacar" and acao_do_personagem!="tacaar" and acao_do_personagem!="tacara" and acao_do_personagem!="aactar" and acao_do_personagem!="aacatr" and acao_do_personagem!="aacart" and acao_do_personagem!="aatcar" and acao_do_personagem!="cataar" and acao_do_personagem!="taaacar" and acao_do_personagem!="catar" and acao_do_personagem!="rataca" and acao_do_personagem!="atraca" and acao_do_personagem!="atracar"):
                print("\nComando invalido!\n")
                raw_input('|>')
            else: break
        contador_de_rodadas=contador_de_rodadas+1
        if (acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
            if booleana[3]==False : print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(evasiva)"+"(ofensiva)".rjust(69))
            else : print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(parcialmente defensiva)"+"(ofensiva)".rjust(69))
            time.sleep(2)
            escrever(0.025,"\nO inimigo atacou enquanto voce usava o item...\n")
            time.sleep(0.5)
            teste_de_sorte=random.randrange(10)+calculo_da_fuga
            if(teste_de_sorte>8):
                escrever(0.025,'\nVoce esquivou de qualquer manobra ofensiva do oponente!\n')
                time.sleep(0.5)
            else:
                if(teste_de_sorte>5):
                    escrever(0.025,'\nVoce nao conseguiu se esquivar')
                    time.slpeep(0.5)
                    escrever(0.025,', \nmas pode se defender!\n')
                    time.sleep(0.5)
                    if booleana[3]==False : calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-2*aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                    else : calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-3*aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                    if (calculo_do_dano<0):
                        escrever(0.025,'\nSua defesa foi formidavel!')
                        time.sleep(0.5)
                        escrever(0.025,'Voce barrou o ataque naturalmente e conseguiu afastar o inimigo!\n')
                        time.sleep(0.5)
                    else:
                        if(calculo_do_dano==0):
                            print("\nPor muito pouco voce conseguiu barrar todo o ataque inimigo!\n")
                            time.sleep(2)
                        else:
                            print("\nMesmo assim, o impacto dos golpes do inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                            time.sleep(3)
                            aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
                else:
                    if(teste_de_sorte>2):
                        print('\nVoce nao conseguiu uma brecha para se esquivar ou se defender...\n')
                        time.sleep(2)
                        if booleana[3]==False : calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                        else: calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-2*aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                        if (calculo_do_dano>0):
                            print("\nVoce foi atacado diretamente, sofrendo "+str(calculo_do_dano)+" pontos de dano!\n")
                            time.sleep(3)
                            aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                        else:
                            print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                            time.sleep(3)
                    else:
                        print('\nO golpe do oponente foi critico!\n')
                        time.sleep(2)
                        if booleana[3]==False : calculo_do_dano = 2*adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                        else: calculo_do_dano = 2*adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-2*aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                        if (calculo_do_dano>0):
                            if booleana[3]==True : print("\nO inimigo aproveitou a sua defesa precária e te atacou violentamente, \ncausando "+str(calculo_do_dano)+" pontos de dano.\n")
                            else : print("\nO inimigo aproveitou a oportunidade e te atacou violentamente, \ncausando "+str(calculo_do_dano)+" pontos de dano.\n")
                            time.sleep(3)
                            aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            teste_de_sorte=random.randrange(300)
                            if(teste_de_sorte<=30+aliado_jogador.status[3]):
                                print("\nVoce aumentou seu folego enquanto tentava aguentar os golpes que voce levou em cheio!")
                                time.sleep(2)
                                print("O limite dos seus pontos de vida cresceu!")
                                time.sleep(2)
                                aliado_jogador.status[5]=aliado_jogador.status[5]+int((random.randrange(aliado_jogador.status[5]))/10)+3
                        else:
                            print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                            time.sleep(3)
        elif(acao_do_personagem == "defender" or acao_do_personagem == "d" or acao_do_personagem == "defende" or acao_do_personagem == "defern" or acao_do_personagem == "defenrede" or acao_do_personagem == "ddefender" or acao_do_personagem == "defenrd" or acao_do_personagem == "deffender" or acao_do_personagem == "defendder" or acao_do_personagem == "ddeffender" or acao_do_personagem == "defnder" or acao_do_personagem == "defndr" or acao_do_personagem == "dfnder" or acao_do_personagem == "dfendr" or acao_do_personagem == "defnde" or acao_do_personagem == "defnd" or acao_do_personagem == "dfede" or acao_do_personagem == "def"): #defesa(2personagem_jogador[2]) vs ataque(adversario_inimigo.status[0])
            booleana[3]=True
            print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(defensiva)"+"(ofensiva)".rjust(69))
            time.sleep(2)
            teste_de_sorte = random.randrange(50)
            if (teste_de_sorte<=10+aliado_jogador.status[3]-adversario_inimigo.status[3]):#S_defesa(3personagem_jogador[2]) vs ataque(adversario_inimigo.status[0])
                print("\nSua postura de defesa te favoreceu!\n")
                time.sleep(2)
                teste_de_sorte = random.randrange(40)
                if (teste_de_sorte<=10+adversario_inimigo.status[3]-aliado_jogador.status[3]):#S_defesa(3personagem_jogador[2]) vs S_ataque(2adversario_inimigo.status[0])
                    print("\n... Mas o ataque do inimigo foi critico!\n")
                    calculo_do_dano = (2*adversario_inimigo.status[0])+int((random.randrange(adversario_inimigo.status[0]))*0.35)-(3*aliado_jogador.status[1])-int((random.randrange(aliado_jogador.status[1]))*0.35)
                    if (calculo_do_dano < 0):#S_defesa(3aliado_jogador.status[1]) CONTRA-ATACA S_ataque(2adversario_inimigo.status[0])
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+int(((random.randrange(aliado_jogador.status[0]))/2)*0.35)
                        print("\nNao importa, sua defesa e incrivel!")
                        time.sleep(2)
                        print("Alem de defender voce conseguiu contra-atacar, \ncausando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                        time.sleep(3)
                        teste_de_sorte = random.randrange(5)#aumento de defesa
                        if(teste_de_sorte<=1):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                variavel_para_comparar=aliado_jogador.status[1]
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+1
                                statusEquipamento(True,1)
                                if (variavel_para_comparar < aliado_jogador.status[1]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                if (variavel_para_comparar > aliado_jogador.status[1]):
                                    aliado_jogador.status[1]=variavel_para_comparar
                        elif(teste_de_sorte>=4):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte<=20+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+2
                                statusEquipamento(True,1)
                        elif(teste_de_sorte==3):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte<=10+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+3
                                statusEquipamento(True,1)
                        elif(teste_de_sorte==2):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte==10+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/24)+4
                                statusEquipamento(True,1)
                        adversario_inimigo.status[6]-=calculo_do_dano
                    else:
                        if (calculo_do_dano == 0):#S_defesa(3aliado_jogador.status[1]) ANULA S_ataque(2adversario_inimigo.status[0])
                            print("\nDefesa e ataque se anulam! A tensao aumenta!\n")
                            time.sleep(2)
                        else:
                            time.sleep(2)
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30+aliado_jogador.status[2]+aliado_jogador.status[3]-adversario_inimigo.status[2]-adversario_inimigo.status[4]):
                                print ("\nApesar de vantajosa, a sua defesa nao pareceu ser o suficiente,")
                                time.sleep(0.5)
                                print ('mas voce conseguiu esquivar de todos os ataques,')
                                time.sleep(0.5)
                                print ('o inimigo nem pode tocar em voce!')
                                time.sleep(0.5)
                            else:#S_defesa(3personagem_jogador[2]) APANHA DO S_ataque(2adversario_inimigo.status[0])
                                print("\nVoce sofreu "+str(calculo_do_dano)+" pontos de dano...\n")
                                time.sleep(2)
                                aliado_jogador.status[6] = aliado_jogador.status[6] - calculo_do_dano
                else:#S_defesa(3aliado_jogador.status[1]) vs ataque(adversario_inimigo.status[0])
                    calculo_do_dano = (adversario_inimigo.status[0])+int((random.randrange(adversario_inimigo.status[0]))*0.35)-(3*aliado_jogador.status[1])-int((random.randrange(aliado_jogador.status[1]))*0.35)
                    if (calculo_do_dano<0):#S_defesa(3personagem_jogador[2]) CONTRA-ATACA ataque(adversario_inimigo.status[0])
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+int(((random.randrange(aliado_jogador.status[0]))/2)*0.35)
                        print("\nSua defesa foi tao grande que, alem de bloquear o ataque, \nvoce conseguiu contra-atacar, causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                        time.sleep(2)
                        adversario_inimigo.status[6]-=calculo_do_dano
                    else:
                        if (calculo_do_dano ==0):#S_defesa(3personagem_jogador[2]) ANULA ataque(adversario_inimigo.status[0])
                            print("\nSua defesa foi completa!\n")
                            time.sleep(2)
                        else:#S_defesa(3personagem_jogador[2]) APANHA DO ataque(adversario_inimigo.status[0])
                            print("\nVoce sofreu miseros "+str(calculo_do_dano)+" pontos de dano.\n")
                            time.sleep(2)
                            aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
            else:
                teste_de_sorte = random.randrange(40)
                if(teste_de_sorte<=10-aliado_jogador.status[3]+adversario_inimigo.status[3]):#defesa(2personagem_jogador[2]) vs S_ataque(2adversario_inimigo.status[0])
                    calculo_do_dano = 2*adversario_inimigo.status[0]+int((random.randrange(adversario_inimigo.status[0]))*0.35)-int((1.5)*aliado_jogador.status[1])-int((random.randrange(aliado_jogador.status[1]))*0.35)
                    if (calculo_do_dano<0):
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+int(((random.randrange(aliado_jogador.status[0]))/2)*0.35)
                        print("\nSua defesa e simplesmente  I M E N S A !")
                        time.sleep(2)
                        print("O inimigo avancou furiosamente mas voce o lancou para tras \ne contra-atacou causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                        time.sleep(3)
                        teste_de_sorte = random.randrange(6)#aumento de defesa
                        if(teste_de_sorte<=1):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                variavel_para_comparar=aliado_jogador.status[1]
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+1
                                statusEquipamento(True,1)
                                if (variavel_para_comparar < aliado_jogador.status[1]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                if (variavel_para_comparar > aliado_jogador.status[1]):
                                    aliado_jogador.status[1]=variavel_para_comparar
                        if(teste_de_sorte==2):
                            teste_de_sorte = random.randrange(200)
                            if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+2
                                statusEquipamento(True,1)
                        if(teste_de_sorte==3):
                            teste_de_sorte = random.randrange(200)
                            if (teste_de_sorte<=20+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+3
                                statusEquipamento(True,1)
                        if(teste_de_sorte==4):
                            teste_de_sorte = random.randrange(300)
                            if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/24)+4
                                statusEquipamento(True,1)
                        if(teste_de_sorte>=5):
                            teste_de_sorte = random.randrange(100)
                            if (teste_de_sorte<=10+aliado_jogador.status[3]):
                                variavel_para_comparar=aliado_jogador.status[1]
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+int((random.randrange(aliado_jogador.status[0]))/24)+1
                                statusEquipamento(True,1)
                                if (variavel_para_comparar < aliado_jogador.status[1]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                if (variavel_para_comparar > aliado_jogador.status[1]):
                                    aliado_jogador.status[1]=variavel_para_comparar
                        adversario_inimigo.status[6]-=calculo_do_dano
                    else:
                        if(calculo_do_dano==0):
                            print("\nVoce surpreendeu o inimigo que estava confiante,")
                            time.sleep(2)
                            print("suas forcas se anularam numa estrondosa colisao!\n")
                            time.sleep(2)
                            teste_de_sorte=random.randrange(300)
                            if(teste_de_sorte<=10+aliado_jogador.status[3]):
                                print("\nA liberacao de energia durante a colisao despertou novos limites para sua forca e agora esta mais forte!")
                                time.sleep(3)
                                print("TODOS os seus pontos subiram!\n")
                                time.sleep(3)
                                statusEquipamento(False,0)
                                statusEquipamento(False,1)
                                statusEquipamento(False,5)
                                aliado_jogador.status[5]=aliado_jogador.status[5]+int((random.randrange(aliado_jogador.status[5]))/12)+4
                                aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/12)+3
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+2
                                statusEquipamento(True,0)
                                statusEquipamento(True,1)
                                statusEquipamento(True,5)
                                aliado_jogador.status[2]+=1
                                aliado_jogador.status[3]+=1
                                aliado_jogador.status[4]+=1
                        else:
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30+aliado_jogador.status[2]+aliado_jogador.status[3]-adversario_inimigo.status[2]-adversario_inimigo.status[3]):
                                print ("\nApesar da pressao do ataque inimigo,")
                                time.sleep(0.5)
                                print ('voce conseguiu esquivar de todos os ataques,')
                                time.sleep(0.5)
                                print ('o inimigo nem pode tocar em voce!')
                                time.sleep(0.5)
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
                else:#defesa(2aliado_jogador.status[1]) vs ataque(adversario_inimigo.status[0])
                    calculo_do_dano = adversario_inimigo.status[0]+int((random.randrange(adversario_inimigo.status[0]))*0.35)-2*aliado_jogador.status[1]-int((random.randrange(aliado_jogador.status[1]))*0.35)
                    if (calculo_do_dano<0):
                        calculo_do_dano = calculo_do_dano*(-1)+int(((random.randrange(aliado_jogador.status[0]))/2)*0.35)
                        print("\nSua defesa E ENORME!")
                        time.sleep(2)
                        print("Voce barrou o ataque naturalmente e contra-atacou, \ncausando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                        time.sleep(3)
                        teste_de_sorte = random.randrange(5)#aumento de defesa
                        if(teste_de_sorte<=1):
                            teste_de_sorte = random.randrange(200)
                            if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                variavel_para_comparar=aliado_jogador.status[1]
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+1
                                statusEquipamento(True,1)
                                if (variavel_para_comparar < aliado_jogador.status[1]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                if (variavel_para_comparar > aliado_jogador.status[1]):
                                    aliado_jogador.status[1]=variavel_para_comparar
                        elif(teste_de_sorte>=4):
                            teste_de_sorte = random.randrange(300)
                            if (teste_de_sorte<=60+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+2
                                statusEquipamento(True,1)
                        elif(teste_de_sorte==3):
                            teste_de_sorte = random.randrange(400)
                            if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/12)+3
                                statusEquipamento(True,1)
                        elif(teste_de_sorte==2):
                            teste_de_sorte = random.randrange(300)
                            if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                time.sleep(2)
                                print("Seus pontos de defesa subiram!\n")
                                time.sleep(2)
                                statusEquipamento(False,1)
                                aliado_jogador.status[1]=aliado_jogador.status[1]+int((random.randrange(aliado_jogador.status[1]))/24)+4
                                statusEquipamento(True,1)
                        adversario_inimigo.status[6]-=calculo_do_dano
                    else:
                        if(calculo_do_dano==0):
                            print("\nVoce barrou o ataque do inimigo!\n")
                            time.sleep(2)
                        else:
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30+aliado_jogador.status[2]+aliado_jogador.status[3]-adversario_inimigo.status[2]-adversario_inimigo.status[3]):
                                print("\nVoce conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em voce!")
                                time.sleep(1.5)
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(3)
                                aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
        else:
            if (acao_do_personagem=="atacar" or acao_do_personagem=="a" or acao_do_personagem=="at" or acao_do_personagem=="ata" or acao_do_personagem=="atac" or acao_do_personagem=="ataca" or acao_do_personagem=="atcar" or acao_do_personagem=="tacar" or acao_do_personagem=="aacar" or acao_do_personagem=="ataar" or acao_do_personagem=="atacr" or acao_do_personagem=="acar" or acao_do_personagem=="aaar" or acao_do_personagem=="aacr" or acao_do_personagem=="aaca" or acao_do_personagem=="atar" or acao_do_personagem=="atcr" or acao_do_personagem=="atca" or acao_do_personagem=="ata" or acao_do_personagem=="ataa" or acao_do_personagem=="atara" or acao_do_personagem=="stssr" or acao_do_personagem=="atavar" or acao_do_personagem=="atahvea" or acao_do_personagem=="atrex" or acao_do_personagem=="atasfa" or acao_do_personagem=="atacart" or acao_do_personagem=="taacar" or acao_do_personagem=="tacaar" or acao_do_personagem=="tacara" or acao_do_personagem=="aactar" or acao_do_personagem=="aacatr" or acao_do_personagem=="aacart" or acao_do_personagem=="aatcar" or acao_do_personagem=="cataar" or acao_do_personagem=="taaacar" or acao_do_personagem=="catar" or acao_do_personagem=="rataca" or acao_do_personagem=="atraca" or acao_do_personagem=="atracar"):
                teste_de_sorte=random.randrange(2)
                if (teste_de_sorte==1):#ataque(aliado_jogador.status[0]) vs defesa(2adversario_inimigo.status[1])
                    print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(ofensiva)"+"(defensiva)".rjust(69))
                    time.sleep(2)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+aliado_jogador.status[3]-adversario_inimigo.status[3]):#S_ataque(2aliado_jogador.status[0]) vs defesa(2adversario_inimigo.status[1])
                        print("\nSeu ataque foi critico!!!\n")
                        time.sleep(2)
                        teste_de_sorte=random.randrange(50)
                        if (teste_de_sorte<=10+adversario_inimigo.status[3]-aliado_jogador.status[3]):#S_ataque(2aliado_jogador.status[0]) vs S_defesa(3adversario_inimigo.status[1])
                            print("\nApesar do seu critico, voce e pressionado pela postura de defesa do seu inimigo!\n")
                            time.sleep(3)
                            calculo_do_dano=2*aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))*0.35)-3*adversario_inimigo.status[1]-int((random.randrange(adversario_inimigo.status[1]))*0.35)
                            if (calculo_do_dano<0):#S_ataque(2aliado_jogador.status[0]) APANHA DE S_defesa(3adversario_inimigo.status[1])
                                calculo_do_dano = calculo_do_dano*(-1)+int((random.randrange(adversario_inimigo.status[0]))*0.35)
                                print("\nPor mais que tente, voce nao consegue atravessar a defesa do seu inimigo!")
                                time.sleep(2)
                                print("Alem de te bloquear, ele te contra-atacou, causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
                                teste_de_sorte=random.randrange(200)
                                if(teste_de_sorte<=40+aliado_jogador.status[3]):
                                    print("\nVoce tentou ao maximo ultrapassar a defesa do seu inimigo, exigiu muito dos seus musculos que se fortaleceram!\n")
                                    time.sleep(3)
                                    print("\nSeus pontos de ataque subiram!\n")
                                    time.sleep(2)
                                    statusEquipamento(False,0)
                                    aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+4
                                    statusEquipamento(True,0)
                            else:
                                if (calculo_do_dano==0):#S_ataque(2aliado_jogador.status[0]) ANULA S_defesa(3adversario_inimigo.status[1])
                                    print("\nA disputa de forcas e intensa, voce e seu inimigo deram o melhor de si, mas nenhum dos dois se sobrepos!\n")
                                    time.sleep(3)
                                else:#S_ataque(2aliado_jogador.status[0]) ATACA S_defesa(3adversario_inimigo.status[1])
                                    teste_de_sorte = random.randrange(300)
                                    if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                        print ('\nSua forca parece ser mais do que o bastante, mas foi irrelevante,')
                                        time.sleep(0.5)
                                        print ('seu oponente conseguiu esquivar de todos os seus ataques...')
                                        time.sleep(0.5)
                                        print ('Voce nem pode tocar no inimigo!')
                                        time.sleep(0.5)
                                    else:
                                        print("\nSeu ataque foi explosivo!")
                                        time.sleep(2)
                                        print("Nem o melhor da defesa do seu inimigo foi capaz de conter sua ira!")
                                        time.sleep(2)
                                        print("Voce causou "+str(calculo_do_dano)+" pontos de dano ao seu inimigo!\n")
                                        time.sleep(2)
                                        adversario_inimigo.status[6]-=calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte==10+aliado_jogador.status[3]):
                                            print("\nA explosao de energia dos seus musculos os expandiu definitivamente!\n")
                                            time.sleep(2)
                                            print("\nSeus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+(random.randrange(aliado_jogador.status[0]))+3
                                            statusEquipamento(True,0)
                        else:#S_ataque(2aliado_jogador.status[0]) vs defesa(2adversario_inimigo.status[1])
                            calculo_do_dano = 2*aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))*0.35)-2*adversario_inimigo.status[1]-int((random.randrange(adversario_inimigo.status[1]))*0.35)
                            if(calculo_do_dano<0):#S_ataque(2aliado_jogador.status[0]) APANHA DE defesa(2adversario_inimigo.status[1])
                                calculo_do_dano=calculo_do_dano*(-1)+int((random.randrange(adversario_inimigo.status[0]))*0.35)
                                print("\nVoce deu o seu maximo, mas mesmo assim nem se equiparou as habilidades de auto-defesa do seu inimigo!")
                                time.sleep(3)
                                print("Sem fazer muito esforco ele se defendeu e contra-atacou, te causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(3)
                                aliado_jogador.status[6] = aliado_jogador.status[6] - calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#S_ataque(2aliado_jogador.status[0]) ANULA defesa(2adversario_inimigo.status[1])
                                    print("\nVoce assustou o inimigo por um instante, mas - por muito pouco - ele conseguiu barrar todos os seus movimentos ofensivos...\n")
                                    time.sleep(3)
                                else:
                                    teste_de_sorte=random.randrange(50)
                                    if(teste_de_sorte<=10+aliado_jogador.status[3]):#XS_ataque(3aliado_jogador.status[0]) vs defesa(adversario_inimigo.status[1])
                                        print("\nVoce rompeu a defesa do seu inimigo, causando "+str(calculo_do_dano)+" pontos de dano!")
                                        time.sleep(3)
                                        print("\nSuper Critico!!!\n")
                                        time.sleep(4)
                                        print("Voce iniciou um ataque em frenesi!!!\n")
                                        time.sleep(2)
                                        adversario_inimigo.status[6]-=calculo_do_dano
                                        teste_de_sorte=random.randrange(9)+5
                                        while(teste_de_sorte>0):#XS_ataque(3aliado_jogador.status[0]) ATACA defesa(adversario_inimigo.status[1])
                                            calculo_do_dano=2*(random.randrange(aliado_jogador.status[0]))-(random.randrange(adversario_inimigo.status[1]))
                                            while(calculo_do_dano<=0):
                                                calculo_do_dano=(random.randrange(aliado_jogador.status[0])+3)-(random.randrange(adversario_inimigo.status[1]))
                                            print(str(calculo_do_dano)+" pontos de dano!\n")
                                            time.sleep(0.25)
                                            adversario_inimigo.status[6]-=calculo_do_dano
                                            teste_de_sorte=teste_de_sorte-1
                                        print("\nVoce desferiu toda sua furia no inimigo!\n")
                                        time.sleep(2)
                                        teste_de_sorte=random.randrange(3)
                                        if(teste_de_sorte<=1):
                                            teste_de_sorte=random.randrange(50)
                                            if(teste_de_sorte<=5+aliado_jogador.status[3]):
                                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                                statusEquipamento(False,0)
                                                aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                                statusEquipamento(True,0)
                                        if(teste_de_sorte>=2):
                                            teste_de_sorte=random.randrange(50)
                                            if(teste_de_sorte<=5+aliado_jogador.status[3]):
                                                print("\nVoce ultrapassou o seu limite e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                                statusEquipamento(False,0)
                                                aliado_jogador.status[0]=aliado_jogador.status[0]++int((random.randrange(aliado_jogador.status[0]))/3)+4
                                                statusEquipamento(True,0)
                                    else:#S_ataque(2aliado_jogador.status[0]) ATACA defesa(2adversario_inimigo.status[1])
                                        teste_de_sorte = random.randrange(300)
                                        if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                            print ('\nMas seu surto de poder foi irrelevante,')
                                            time.sleep(0.5)
                                            print ('seu oponente conseguiu esquivar de todos os seus ataques...')
                                            time.sleep(0.5)
                                            print ('Voce nem pode tocar no inimigo!')
                                            time.sleep(0.5)
                                        else:
                                            print("\nSeu ataque de golpes duplos pressionaram a defesa do seu inimigo, \ncausando "+str(calculo_do_dano)+" pontos de dano!\n")
                                            time.sleep(3)
                                            teste_de_sorte=random.randrange(200)
                                            if(teste_de_sorte<=25+aliado_jogador.status[3]):
                                                print("\nVoce aprimorou o ritmo dos seus ataques e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                                statusEquipamento(False,0)
                                                aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+2
                                                statusEquipamento(True,0)
                                            adversario_inimigo.status[6]-=calculo_do_dano
                    else:#ataque(aliado_jogador.status[0])
                        teste_de_sorte=random.randrange(50)
                        if(teste_de_sorte<=10+adversario_inimigo.status[3]-aliado_jogador.status[3]):#ataque(aliado_jogador.status[0]) vs S_defesa(3adversario_inimigo.status[1])
                            print("\nA postura de defesa do seu inimigo te colocou numa situacao dificil!\n")
                            time.sleep(2)
                            calculo_do_dano=aliado_jogador.status[0]+int(random.randrange(aliado_jogador.status[0])*0.35)-3*adversario_inimigo.status[1]-int(random.randrange(adversario_inimigo.status[1])*0.35)
                            if(calculo_do_dano<0):#ataque(aliado_jogador.status[0]) APANHA DE S_defesa(3adversario_inimigo.status[1])
                                calculo_do_dano=calculo_do_dano*(-1)+int((random.randrange(adversario_inimigo.status[0]))*0.35)
                                print("\nE muito dificil passar por tamanha defesa, seu ataque foi infimo, \nalem de ser inutilizado, voce sofreu represalia...")
                                time.sleep(3)
                                print("Seu inimigo contra-atacou, causando "+str(calculo_do_dano)+" pontos de dano.\n")
                                time.sleep(2)
                                teste_de_sorte=random.randrange(100)
                                if(teste_de_sorte<=15+aliado_jogador.status[3]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de ataque subiram!\n")
                                    time.sleep(2)
                                    statusEquipamento(False,0)
                                    aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                    statusEquipamento(True,0)
                                aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#ataque(aliado_jogador.status[0]) ANULA S_defesa(3adversario_inimigo.status[1])
                                    print("\nO inimigo mal consegue reter seus golpes, mas o suficiente para para-lo.")
                                    time.sleep(2)
                                    print("Ao mesmo tempo sua forca foi o bastante para evitar um contra-ataque!\n")
                                    time.sleep(2)
                                else:#ataque(aliado_jogador.status[0]) ATACA S_defesa(3adversario_inimigo.status[1])
                                    teste_de_sorte = random.randrange(300)
                                    if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                        print ('\nMesmo assim voce pressionou o seu oponente,')
                                        time.sleep(0.5)
                                        print ('que foi obrigado a esquivar de todos os seus ataques...')
                                        time.sleep(0.5)
                                        print ('Voce nem pode tocar no inimigo!')
                                        time.sleep(0.5)
                                    else:                                    
                                        print("\nDepois de alguns golpes, voce tornou insignificante a vantagem defensiva do seu inimigo, \ncausando humilhantes, "+str(calculo_do_dano)+" pontos de dano a ele!\n")
                                        time.sleep(4)
                                        teste_de_sorte=random.randrange(200)
                                        if(teste_de_sorte<=20+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                            statusEquipamento(True,0)
                                        adversario_inimigo.status[6]-=calculo_do_dano
                        else:#ataque(aliado_jogador.status[0]) vs defesa(2adversario_inimigo.status[1])
                            calculo_do_dano = aliado_jogador.status[0]+int(random.randrange(aliado_jogador.status[0])*0.35)-2*adversario_inimigo.status[1]-int(random.randrange(adversario_inimigo.status[1])*0.35)
                            if(calculo_do_dano<0):#ataque(aliado_jogador.status[0]) APANHA DE defesa(2adversario_inimigo.status[1])
                                calculo_do_dano=calculo_do_dano*(-1)+int((random.randrange(adversario_inimigo.status[0]))*0.35)
                                print("\nO inimigo se defendeu e contra-atacou, te causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                teste_de_sorte=random.randrange(80)
                                if(teste_de_sorte<=8+aliado_jogador.status[3]):
                                    print("\nVoce descobriu mais sobre a sua forca durante a disputa e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de ataque subiram!\n")
                                    time.sleep(2)
                                    statusEquipamento(False,0)
                                    aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                    statusEquipamento(True,0)
                                aliado_jogador.status[6] = aliado_jogador.status[6] - calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#ataque(aliado_jogador.status[0]) ANULA defesa(2adversario_inimigo.status[1])
                                    print("\nSeu oponente defendeu todos os seus golpes, \nmas voce nao deu brecha para que ele avancasse!\n")
                                    time.sleep(2)
                                    teste_de_sorte=random.randrange(200)
                                    if(teste_de_sorte<=25+aliado_jogador.status[3]):
                                        print("\nO trabalho que seu inimigo te deu rendeu frutos!")
                                        time.sleep(2)
                                        print("Voce descobriu mais sobre as taticas de luta dele e esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de ataque subiram!\n")
                                        time.sleep(2)
                                        statusEquipamento(False,0)
                                        aliado_jogador.status[0]=aliado_jogador.status[0]+(random.randrange(aliado_jogador.status[0]))+(random.randrange(aliado_jogador.status[3]))+2
                                        statusEquipamento(True,0)
                                else:#ataque(aliado_jogador.status[0]) ATACA defesa(2adversario_inimigo.status[1])
                                    teste_de_sorte = random.randrange(300)
                                    if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                        print("\nSeu oponente conseguiu esquivar\n de todos os seus ataques, \nvoce nem pode tocar no inimigo!")
                                        time.sleep(1.5)
                                    else:
                                        print("\nVoce acertou o inimigo durante a disputa de forcas, causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(2)
                                        adversario_inimigo.status[6]-=calculo_do_dano
                else:#ataque(aliado_jogador.status[0]) vs ataque(adversario_inimigo.status[0])
                    print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(ofensiva)"+"(ofensiva)".rjust(69))
                    time.sleep(2)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+aliado_jogador.status[3]-adversario_inimigo.status[3]):#S_ataque(2aliado_jogador.status[0]) vs ataque(adversario_inimigo.status[0])
                        print("\nSeu ataque foi critico!!!\n")
                        time.sleep(2)
                        teste_de_sorte=random.randrange(40)
                        if (teste_de_sorte<=10-aliado_jogador.status[3]+adversario_inimigo.status[3]):#S_ataque(2aliado_jogador.status[0]) vs S_ataque(2adversario_inimigo.status[0])
                            print("\nMas o ataque do oponente tambem foi critico!!!\n")
                            time.sleep(2)
                            print("\nVoces entraram na briga pra valer!")
                            time.sleep(1)
                            print("Avancaram de punhos cerrados, trocando golpes com as defesas abertas!\n")
                            time.sleep(2)
                            calculo_do_dano=2*aliado_jogador.status[0]+random.randrange(aliado_jogador.status[0])-adversario_inimigo.status[1]-random.randrange(adversario_inimigo.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nSeu oponente desviou dos seus golpes!")
                                    time.sleep(1)
                                else:
                                    print("\nVoce causou significativos "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                                    time.sleep(2)
                                    adversario_inimigo.status[6]-=calculo_do_dano
                                    teste_de_sorte=random.randrange(100)
                                    if(teste_de_sorte<=10+aliado_jogador.status[3]):
                                        print("\nSeus pontos de ataque subiram enquanto voce forcava os seus musculos!\n")
                                        time.sleep(2)
                                        statusEquipamento(False,0)
                                        aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                        statusEquipamento(True,0)
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo\nfoi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=2*adversario_inimigo.status[0]+random.randrange(adversario_inimigo.status[0])-aliado_jogador.status[1]-random.randrange(aliado_jogador.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nE voce esquivou dos ataques dele!")
                                    time.sleep(1)
                                else:
                                    print("\nEnquanto o oponente te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao\nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
                        else:#S_ataque(2aliado_jogador.status[0]) vs ataque(adversario_inimigo.status[0])
                            print("\nVoce avancou violentamente sobre o inimigo, pressionando-o sem compaixao!")
                            time.sleep(3)
                            print("Apesar de forcar um leve recuo do inimigo, voce nao deixou de levar uns bons \ngolpes!\n")
                            time.sleep(3)
                            calculo_do_dano=2*aliado_jogador.status[0]+random.randrange(aliado_jogador.status[0])-adversario_inimigo.status[1]-random.randrange(adversario_inimigo.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nSeu oponente desviou dos seus golpes!")
                                    time.sleep(1)
                                else:
                                    print("\nVoce golpeou o inimigo ate lhe causar "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    teste_de_sorte = random.randrange(5)#aumento de ataque
                                    if(teste_de_sorte<=1):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=45+aliado_jogador.status[3]):
                                            variavel_para_comparar=aliado_jogador.status[0]
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+1
                                            statusEquipamento(True,0)
                                            if (variavel_para_comparar < aliado_jogador.status[0]):
                                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                            if (variavel_para_comparar > aliado_jogador.status[0]):
                                                aliado_jogador.status[0]=variavel_para_comparar
                                    elif(teste_de_sorte>=4):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(True,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+2
                                            statusEquipamento(False,0)
                                    elif(teste_de_sorte==3):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=20+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                            statusEquipamento(True,0)
                                    elif(teste_de_sorte==2):
                                        teste_de_sorte = random.randrange(300)
                                        if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+4
                                            statusEquipamento(True,0)
                                    adversario_inimigo.status[6]-=calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo \nfoi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=adversario_inimigo.status[0]+random.randrange(adversario_inimigo.status[0])-aliado_jogador.status[1]-random.randrange(aliado_jogador.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nE voce esquivou dos ataques dele!")
                                    time.sleep(1)
                                else:
                                    print("\nJa o inimigo causou apenas "+str(calculo_do_dano)+" pontos de dano a voce!\n")
                                    time.sleep(2)
                                    aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir nao ataque do oponente.\n")
                                time.sleep(3)
                    else:#ataque(aliado_jogador.status[0]) vs ataque(adversario_inimigo.status[0])
                        teste_de_sorte=random.randrange(40)
                        if(teste_de_sorte==10+adversario_inimigo.status[3]-aliado_jogador.status[3]): #ataque(aliado_jogador.status[0]) vs S_ataque(2adversario_inimigo.status[0])
                            print("\nO ataque do oponente foi critico!...\n")
                            time.sleep(2)
                            print("\nVoce foi pressionado enquanto trocavam golpes, \nos socos e chutes do seu oponente te acertaram em pontos menos resistentes do \nseu corpo, que estavam desprotegidos!")
                            time.sleep(4)
                            print("Mesmo assim voce manteve um bom ritmo de ataque!\n")
                            time.sleep(2)
                            calculo_do_dano=aliado_jogador.status[0]+random.randrange(aliado_jogador.status[0])-adversario_inimigo.status[1]-random.randrange(adversario_inimigo.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nSeu oponente desviou dos seus golpes!")
                                    time.sleep(1)
                                else:
                                    print("\nVoce infringiu "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                                    time.sleep(2)
                                    teste_de_sorte = random.randrange(5)#aumento de ataque
                                    if(teste_de_sorte<=1):
                                        teste_de_sorte = random.randrange(100)
                                        if (teste_de_sorte<=15+aliado_jogador.status[3]):
                                            variavel_para_comparar=aliado_jogador.status[0]
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+1
                                            statusEquipamento(True,0)
                                            if (variavel_para_comparar < aliado_jogador.status[0]):
                                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                            if (variavel_para_comparar > aliado_jogador.status[0]):
                                                aliado_jogador.status[0]=variavel_para_comparar
                                    elif(teste_de_sorte>=4):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+2
                                            statusEquipamento(True,0)
                                    elif(teste_de_sorte==3):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=20+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                            statusEquipamento(True,0)
                                    elif(teste_de_sorte==2):
                                        teste_de_sorte = random.randrange(300)
                                        if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+4
                                            statusEquipamento(True,0)
                                    adversario_inimigo.status[6]-=calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo \nfoi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=2*adversario_inimigo.status[0]+random.randrange(adversario_inimigo.status[0])-aliado_jogador.status[1]-random.randrange(aliado_jogador.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nE voce esquivou dos ataques dele!")
                                    time.sleep(1)
                                else:
                                    print("\nEnquanto o seu inimigo te agrediu violentamente, \ncausando "+str(calculo_do_dano)+" pontos de dano a voce!\n")
                                    time.sleep(2)
                                    aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
                        else:#ataque(aliado_jogador.status[0]) vs ataque(adversario_inimigo.status[0])
                            print("\nVoces se atacaram num ritmo leve, parecem estar testando um ao outro,\nficou claro que nenhum dos dois mostrou tudo o que e capaz.\n")
                            time.sleep(4)
                            calculo_do_dano=aliado_jogador.status[0]+random.randrange(aliado_jogador.status[0])-adversario_inimigo.status[1]-random.randrange(adversario_inimigo.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nSeu oponente desviou dos seus golpes!")
                                    time.sleep(1)
                                else:
                                    print("\nVoce feriu seu oponente em "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    teste_de_sorte = random.randrange(5)#aumento de ataque
                                    if(teste_de_sorte<=1):
                                        teste_de_sorte = random.randrange(100)
                                        if (teste_de_sorte<=15+aliado_jogador.status[3]):
                                            variavel_para_comparar=aliado_jogador.status[0]
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+1
                                            statusEquipamento(True,0)
                                            if (variavel_para_comparar < aliado_jogador.status[0]):
                                                print("\nVoce testou o seu limite e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                            if (variavel_para_comparar > aliado_jogador.status[0]):
                                                aliado_jogador.status[0]=variavel_para_comparar
                                    elif(teste_de_sorte>=4):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=40+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+2
                                            statusEquipamento(True,0)
                                    elif(teste_de_sorte==3):
                                        teste_de_sorte = random.randrange(200)
                                        if (teste_de_sorte<=20+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+3
                                            statusEquipamento(True,0)
                                    elif(teste_de_sorte==2):
                                        teste_de_sorte = random.randrange(300)
                                        if (teste_de_sorte<=30+aliado_jogador.status[3]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            statusEquipamento(False,0)
                                            aliado_jogador.status[0]=aliado_jogador.status[0]+int((random.randrange(aliado_jogador.status[0]))/6)+4
                                            statusEquipamento(True,0)
                                    adversario_inimigo.status[6]-=calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo \nfoi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=adversario_inimigo.status[0]+random.randrange(adversario_inimigo.status[0])-aliado_jogador.status[1]-random.randrange(aliado_jogador.status[1])
                            if(calculo_do_dano>0):
                                teste_de_sorte = random.randrange(300)
                                if(teste_de_sorte<=30-aliado_jogador.status[2]-aliado_jogador.status[3]+adversario_inimigo.status[2]+adversario_inimigo.status[3]):
                                    print("\nE voce esquivou dos ataques dele!")
                                    time.sleep(1)
                                else:
                                    print("\nSeu inimigo te golpeou causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
            else:
                if(acao_do_personagem=="fugir" or acao_do_personagem=="f" or acao_do_personagem=="fugri" or acao_do_personagem=="fguir" or acao_do_personagem=="fugeir" or acao_do_personagem=="furig" or acao_do_personagem=="fuer" or acao_do_personagem=="ffugri" or acao_do_personagem=="gfuir" or acao_do_personagem=="fiur" or acao_do_personagem=="fugi" or acao_do_personagem=="fugr" or acao_do_personagem=="fug" or acao_do_personagem=="fgir" or acao_do_personagem=="fir" or acao_do_personagem=="fgr" or acao_do_personagem=="ugir" or acao_do_personagem=="gir" or acao_do_personagem=="figr" or acao_do_personagem=="fu"):
                    print ("\n"+"Postura de Batalha:".center(79)+"\n\n"+str(aliado_jogador.nome)+str(adversario_inimigo.nome).rjust(79-len(aliado_jogador.nome))+"\n\n(fugitiva)"+"(ofensiva)".rjust(69))
                    time.sleep(2)
                    print("\nVoce tenta aumentar o ritmo de esquiva...\n")
                    time.sleep(2)
                    teste_de_sorte=random.randrange(10)+calculo_da_fuga
                    if(teste_de_sorte==10):
                        print('\nVoce esquivou de qualquer manobra ofensiva do oponente e conseguiu uma brecha para fugir!\n')
                        time.sleep(3)
                        print('\nDeseja fugir da luta?("sim" ou "nao")\n')
                        time.sleep(1)
                        batalha_escapar=""
                        while 1:
                            batalha_escapar = raw_input('-')
                            batalha_escapar = batalha_escapar.lower()
                            if(batalha_escapar== "nao" or batalha_escapar=="n" or batalha_escapar=="ao" or batalha_escapar=="no" or batalha_escapar=="na" or batalha_escapar== "naao" or batalha_escapar=="naoo" or batalha_escapar=="aoo" or batalha_escapar=="noo" or batalha_escapar=="naa" or batalha_escapar== "noop" or batalha_escapar=="a" or batalha_escapar=="mao" or batalha_escapar=="nso" or batalha_escapar=="ns" or batalha_escapar== "nnao" or batalha_escapar=="nn" or batalha_escapar=="aao" or batalha_escapar=="nno" or batalha_escapar=="nna"): break
                            if(batalha_escapar=="sim" or batalha_escapar=="s" or batalha_escapar=="si" or batalha_escapar=="sm" or batalha_escapar=="im" or batalha_escapar=="ssim"): break
                            else: print('\nEntrada invalida! Digite "sim" ou "nao".\n')
                        if(batalha_escapar=="sim" or batalha_escapar=="s" or batalha_escapar=="si" or batalha_escapar=="sm" or batalha_escapar=="im" or batalha_escapar=="ssim"):
                            batalha_escapar="sim"
                            break
                    else:
                        if(teste_de_sorte>8):
                            print('\nVoce esquivou de qualquer manobra ofensiva do oponente, mas nao conseguiu uma brecha para fugir...\n')
                            time.sleep(3)
                        else:
                            if(teste_de_sorte>5):
                                print('\nVoce nao conseguiu uma brecha para fugir, nem pode se esquivar, \nmas pode se defender!\n')
                                time.sleep(3)
                                calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-2*aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                                if (calculo_do_dano<0):
                                    print('\nSua defesa E ENORME!')
                                    time.sleep(2)
                                    print('Voce barrou o ataque naturalmente e conseguiu afastar o inimigo, \ncriando uma brecha para fugir!\n')
                                    time.sleep(3)
                                    print('\nDeseja fugir da luta?("sim" ou "nao")\n')
                                    time.sleep(1)
                                    batalha_escapar=""
                                    while 1:
                                        batalha_escapar = raw_input('-')
                                        batalha_escapar = batalha_escapar.lower()
                                        if(batalha_escapar== "nao" or batalha_escapar=="n" or batalha_escapar=="ao" or batalha_escapar=="no" or batalha_escapar=="na" or batalha_escapar== "naao" or batalha_escapar=="naoo" or batalha_escapar=="aoo" or batalha_escapar=="noo" or batalha_escapar=="naa" or batalha_escapar== "noop" or batalha_escapar=="a" or batalha_escapar=="mao" or batalha_escapar=="nso" or batalha_escapar=="ns" or batalha_escapar== "nnao" or batalha_escapar=="nn" or batalha_escapar=="aao" or batalha_escapar=="nno" or batalha_escapar=="nna"): break
                                        if(batalha_escapar=="sim" or batalha_escapar=="s" or batalha_escapar=="si" or batalha_escapar=="sm" or batalha_escapar=="im" or batalha_escapar=="ssim"): break
                                        else: print('\nEntrada invalida! Digite "sim" ou "nao".\n')
                                    if(batalha_escapar=="sim" or batalha_escapar=="s" or batalha_escapar=="si" or batalha_escapar=="sm" or batalha_escapar=="im" or batalha_escapar=="ssim"):
                                        batalha_escapar="sim"
                                        break
                                else:
                                    if(calculo_do_dano==0):
                                        print("\nVoce barrou o ataque do inimigo!\n")
                                        time.sleep(2)
                                    else:
                                        print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(3)
                                        aliado_jogador.status[6] = aliado_jogador.status[6]-calculo_do_dano
                            else:
                                if(teste_de_sorte>2):
                                    print('\nVoce nao conseguiu uma brecha para fugir, se esquivar ou se defender...\n')
                                    time.sleep(2)
                                    calculo_do_dano = adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                                    if (calculo_do_dano>0):
                                        print("\nVoce foi atacado diretamente, sofrendo "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(3)
                                        aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                                    else:
                                        print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(3)
                                else:
                                    print('\nVoce tropecou ao tentar fugir!\n')
                                    time.sleep(2)
                                    print('\nO golpe do oponente foi critico!\n')
                                    time.sleep(2)
                                    calculo_do_dano = 2*adversario_inimigo.status[0]+(random.randrange(adversario_inimigo.status[0]))-aliado_jogador.status[1]-(random.randrange(aliado_jogador.status[1]))
                                    if (calculo_do_dano>0):
                                        print("\nO inimigo aproveitou a abertura na sua defesa e te atacou violentamente, \ncausando "+str(calculo_do_dano)+" pontos de dano.\n")
                                        time.sleep(3)
                                        aliado_jogador.status[6]=aliado_jogador.status[6]-calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte<=20+aliado_jogador.status[3]):
                                            print("\nVoce aumentou seu folego enquanto tentava escapar dos golpes que voce levou em cheio!")
                                            time.sleep(2)
                                            print("O limite dos seus pontos de vida cresceu!")
                                            time.sleep(2)
                                            statusEquipamento(False,5)
                                            aliado_jogador.status[5]=aliado_jogador.status[5]+int((random.randrange(aliado_jogador.status[5]))/6)+3
                                            statusEquipamento(True,5)
                                    else:
                                        print("\nMesmo sem se defender, sua constituicao \nfoi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(3)
                    calculo_da_fuga=calculo_da_fuga+((aliado_jogador.status[2]-adversario_inimigo.status[2])*0.10)+((aliado_jogador.status[3]-adversario_inimigo.status[3])*0.10)
                    if(batalha_escapar =="sim"):
                        break
        print ("\n")
    batalha_escapar="nao"
    variavel_para_comparar = 0
    contador_de_batalha = 0
    contador_de_rodadas = 1
    raw_input("|>")
    os.system("cls")
    print ("\n"+"Fim da Batalha!".center(79)+"\n")
    time.sleep(2)
    if(adversario_inimigo.status[6]<=0):
        inimigo_derrotado = str(adversario_inimigo.nome)+" foi derrotado(a)!"
        print ("\n"+inimigo_derrotado.center(79)+"\n")
    else:
        if(aliado_jogador.status[6]<=0):
            print ("\n"+"Voce foi derrotado.".center(79)+"\n")
        else:
            if(batalha_escapar =="sim"):
                print ("\n"+"Voce conseguiu escapar!".center(79)+"\n")
                batalha_escapar="escapou"
    raw_input("|>")
    os.system("cls")

#--Ruas Perigosas--#
def ruasPerigosas(distancia_restante,periculosidade_ruas):
    caminhada_perigosa=0
    if(ponto_de_save==3):
        print ('Sao 10 ruas perigosas de distancia ate a faculdade')
        time.sleep(3)
    while 0<distancia_restante:
        if caminhada_perigosa>0: print ('Voce seguiu para a proxima rua! Faltam '+str(distancia_restante)+'!')
        raw_input('|>')
        os.system('cls')
        teste_de_sorte=random.randrange(100)
        if distancia_restante<=2 and caminhada_perigosa>4 :periculosidade_ruas-=2
        if periculosidade_ruas<3 :
            if(teste_de_sorte<10): batalha(estudante[0])
            elif(teste_de_sorte<20): batalha(arruaceiro_oponente[0])
            elif(teste_de_sorte<30): batalha(estudante_brigento[1])
            elif(teste_de_sorte<40): batalha(arruaceiro_oponente[1])
            elif(teste_de_sorte<50): batalha(estudante_brigento[2])
            elif(teste_de_sorte<60): batalha(arruaceiro_oponente[2])
            elif(teste_de_sorte<70): batalha(estudante_brigento[3])
            elif(teste_de_sorte<80): batalha(arruaceiro_oponente[3])
            elif(teste_de_sorte<90): batalha(estudante_brigento[4])
            elif(teste_de_sorte<100): batalha(arruaceiro_oponente[4])
        elif periculosidade_ruas<5 :
            if(teste_de_sorte<10): batalha(arruaceiro_oponente[0])
            elif(teste_de_sorte<20): batalha(arruaceiro_oponente[1])
            elif(teste_de_sorte<30): batalha(arruaceiro_oponente[2])
            elif(teste_de_sorte<40): batalha(arruaceiro_oponente[3])
            elif(teste_de_sorte<50): batalha(arruaceiro_oponente[3])
            elif(teste_de_sorte<60): batalha(arruaceiro_oponente[4])
            elif(teste_de_sorte<70): batalha(arruaceiro_oponente[5])
            elif(teste_de_sorte<80): batalha(estudante_brigento[1])
            elif(teste_de_sorte<90): batalha(estudante_brigento[2])
            elif(teste_de_sorte<100): batalha(estudante_brigento[3])
        elif periculosidade_ruas<7 :
            if(teste_de_sorte<10): batalha(arruaceiro_oponente[1])
            elif(teste_de_sorte<20): batalha(arruaceiro_oponente[2])
            elif(teste_de_sorte<30): batalha(arruaceiro_oponente[3])
            elif(teste_de_sorte<40): batalha(arruaceiro_oponente[4])
            elif(teste_de_sorte<50): batalha(arruaceiro_oponente[4])
            elif(teste_de_sorte<60): batalha(arruaceiro_oponente[5])
            elif(teste_de_sorte<70): batalha(arruaceiro_oponente[5])
            elif(teste_de_sorte<80): batalha(arruaceiro_oponente[6])
            elif(teste_de_sorte<90): batalha(arruaceiro_oponente[6])
            elif(teste_de_sorte<100): batalha(arruaceiro_oponente[7])
        elif periculosidade_ruas<9 :
            if(teste_de_sorte<10): batalha(arruaceiro_oponente[4])
            elif(teste_de_sorte<20): batalha(arruaceiro_oponente[5])
            elif(teste_de_sorte<30): batalha(arruaceiro_oponente[5])
            elif(teste_de_sorte<40): batalha(arruaceiro_oponente[6])
            elif(teste_de_sorte<50): batalha(arruaceiro_oponente[6])
            elif(teste_de_sorte<60): batalha(arruaceiro_oponente[7])
            elif(teste_de_sorte<70): batalha(arruaceiro_oponente[7])
            elif(teste_de_sorte<80): batalha(arruaceiro_oponente[8])
            elif(teste_de_sorte<90): batalha(arruaceiro_oponente[8])
            elif(teste_de_sorte<100): batalha(estudante_brigento[5])
        teste_de_sorte=random.randrange(200)
        if(teste_de_sorte<100+aliado_jogador.status[3]):
            print ('O seu oponente deixou cair dinheiro no chao durante a luta!')
            time.sleep(2)
            aliado_jogador.dinheiro+=adversario_inimigo.dinheiro*0.15
            print ('Voce juntou '+str(adversario_inimigo.dinheiro*0.15)+' Reais do chao!')
            raw_input('|>')
            os.system('cls')
        if(aliado_jogador.furtar>0): aliado_jogador.dinheiro += adversario_inimigo.dinheiro*0.05*aliado_jogador.furtar*aliado_jogador.status[3]
        distancia_restante-=1
        periculosidade_ruas+=1
        caminhada_perigosa+=1
    

#--Matar alguem--#
def matarAlguem():
    raw_input("Voce entrou em conflito com a sua consciencia(Aperte ENTER)")
    raw_input("Voce o matou!")
    raw_input("                                         Voce o matou!")
    raw_input("Seu assassino!")
    raw_input("                                Voce o matou!")
    raw_input("             Voce o matou!")
    raw_input("                                    Seu assassino!")
    raw_input("Voce o matou!")
    raw_input("                          Voce o matou!")
    raw_input("     Voce o matou!")
    raw_input("                 Voce o matou!")
    raw_input("Voce o matou!")
    raw_input("                                Seu monstro!")
    raw_input("                                      Seu monstro!")
    raw_input("          Voce o matou!")
    raw_input("     Voce o matou!")
    raw_input("                     Seu monstro!")
    raw_input("                                Voce o matou!")
    raw_input("                    Voce o matou!")
    raw_input("                                         Voce o matou!")
    raw_input("      Voce o matou!")
    raw_input("                                Seu monstro!")
    raw_input("Voce o matou!")
    raw_input("            Voce o matou!")
    raw_input("Seu monstro!")
    raw_input("                                   Voce o matou!")
    raw_input("                          Voce o matou!")
    raw_input("        Voce o matou!")
    raw_input("                               Seu assassino!")
    raw_input("               Voce o matou!")
    raw_input("Seu assassino!")
    raw_input("         Voce o matou!")
    raw_input("                               Seu assassino!")
    raw_input("                  Voce o matou!")
    raw_input("Seu assassino!")
    raw_input("                                         Voce o matou!")
    raw_input("                                Voce o matou!")
    raw_input("          Voce o matou!")
    raw_input("     ")
    print("     Ele...")
    time.sleep(2)
    print("     Ele era um ser vivo...")
    time.sleep(2)
    print("     Ele era um ser humano...")
    time.sleep(2)
    print("                   E voce o matou!")
    time.sleep(2)
    escrever(0.05,"Por hora seu conflito consciencial cessou...",1)

#--Seu predio: Quarto Andar--#
def seuPredioQuartoAndar():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    variavel_lugar = "seu predio, 4o andar"
    booleana[0]= False
    if(situacao[0]<5):
        print("Voce foi abordado novamente pelo morador do quarto 44...")
        time.sleep(2)
        print(" - Nos sabemos que voce nao venceu nem do 3o andar, se nao e capaz disso,\nnao e capaz de nos vencer!")
        time.sleep(2)
        print("Ele te empurrou escada abaixo... Voce perdeu 5 pontos de vida durante a queda!")
        time.sleep(2)
        aliado_jogador.status[6]=aliado_jogador.status[6]-5
        if(aliado_jogador.status[6]<=0):
            aliado_jogador.status[6]=1
    while 1:
        if(situacao[0]<5):
            print("Agora voce esta no terceiro andar.")
            time.sleep(2)
            break
        print("\n#"+"-"*30+"#\n\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#"+ "-"*30+"#\n")
        print("\nE agora, "+str(aliado_jogador.nome)+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(40, 41, 42, 43 ou 44)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="40" and acao_do_personagem!="41" and acao_do_personagem!="42" and acao_do_personagem!="43" and acao_do_personagem!="44"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                print("Voce desceu para o terceiro andar.")
                time.sleep(2)
                break
            else:
                if(acao_do_personagem=="40"):
                    if(situacao[0]>6):
                        print("Voce ja lutou aqui!")
                        time.sleep(2)
                    else:
                        print(' - Aqui no 4o andar moram os mais fortes, mas ha muita diferenca entre nos!')
                        time.sleep(2)
                        print(' - Por isso ha uma ordem para nos enfrentar, comecando por mim!')
                        time.sleep(2)
                        print(' - Como nao pegamos leve, nos apresentamos um "cartao de visita" ao oponente, para ele saber se e capaz de sobreviver.')
                        time.sleep(2)
                        print(" - Aqui esta o meu: ")
                        time.sleep(1)
                        print("\n"+str(adversario_inimigo.nome)+": "+str(adversario_inimigo.status[5])+"pontos de vida.\nAtaque : "+str(adversario_inimigo.status[0])+".     Defesa : "+str(adversario_inimigo.status[1])+".\n")
                        time.sleep(2)
                        print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                        time.sleep(1)
                        while 1:
                            acao_do_personagem = raw_input("-")
                            acao_do_personagem = acao_do_personagem.lower()
                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                break
                            else:
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    batalha(estudante_brigento[5])
                                    if(aliado_jogador.status[6]<=0):break
                                    if(adversario_inimigo.status[6]>0):
                                        while (adversario_inimigo.status[6]>0):
                                            print(" - O que foi, desistiu?(sim ou nao)")
                                            time.sleep(1)
                                            while 1:
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem = acao_do_personagem.lower()
                                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                    print(" - Entao vamos voltar a lutar!")
                                                    time.sleep(2)
                                                    batalha(estudante_brigento[5])
                                                else:
                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                        print(" - Tem certeza?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                        time.sleep(1)
                                                        acao_do_personagem=raw_input("-")
                                                        acao_do_personagem=acao_do_personagem.lower()
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - Muito obrigado pela colaboracao financeira! Ate outro dia, talvez...")
                                                            time.sleep(2)
                                                            aliado_jogador.dinheiro=aliado_jogador.dinheiro/2
                                                            break
                                                        else:
                                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                print(" - Entao vamos voltar a lutar!")
                                                                time.sleep(2)
                                                                batalha(estudante_brigento[5])
                                                            else:
                                                                print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                time.sleep(1)
                                                    else:
                                                        print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                        time.sleep(1)
                                        if(aliado_jogador.status[6]<=0):break
                                        else:
                                            print(" - Parabens! Voce e realmente forte!")
                                            time.sleep(2)
                                            situacao[0]=situacao[0]+1
                                            break
                                    else:
                                        print(" - Parabens! Voce e realmente forte!")
                                        time.sleep(2)
                                        situacao[0]=situacao[0]+1
                                        break
                                else:
                                    print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                    time.sleep(1)
                else:
                    if(acao_do_personagem=="41"):
                        if(situacao[0]==7):
                            print(' - SERA que voce esta PRONTO para brigar comigo, fracote??? Hahahahaha!')
                            time.sleep(2)
                            print(" - Aqui esta o meu cartao: ")
                            time.sleep(1)
                            print("\n"+str(adversario_inimigo.nome)+": "+str(adversario_inimigo.status[5])+"pontos de vida.\nAtaque : "+str(adversario_inimigo.status[0])+".     Defesa : "+str(adversario_inimigo.status[1])+".\n")
                            time.sleep(2)
                            print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                            time.sleep(1)
                            while 1:
                                acao_do_personagem = raw_input("-")
                                acao_do_personagem = acao_do_personagem.lower()
                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        batalha(estudante_brigento[6])
                                        if(aliado_jogador.status[6]<=0):break
                                        if(adversario_inimigo.status[6]>0):
                                            while (adversario_inimigo.status[6]>0):
                                                print(" - O que ha? Vai cair fora mesmo???(sim ou nao)")
                                                time.sleep(1)
                                                while 1:
                                                    acao_do_personagem = raw_input("-")
                                                    acao_do_personagem = acao_do_personagem.lower()
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        print(" - Entao cai dentro!!!")
                                                        time.sleep(2)
                                                        batalha(estudante_brigento[6])
                                                    else:
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - E serio?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                            time.sleep(1)
                                                            acao_do_personagem=raw_input("-")
                                                            acao_do_personagem=acao_do_personagem.lower()
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                print(" - Hahaha! Voce nao e o primeiro que sai do desafio! Por que voce acha que tem um premio?")
                                                                time.sleep(1)
                                                                print(" - Voce pode tentar de novo se quiser compensar a perda! HAHAHAHAHA!")
                                                                time.sleep(1)
                                                                aliado_jogador.dinheiro=aliado_jogador.dinheiro/2
                                                                break
                                                            else:
                                                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                    print(" - Entao cai dentro!!!")
                                                                    time.sleep(2)
                                                                    batalha(estudante_brigento[6])
                                                                else:
                                                                    print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                    time.sleep(1)
                                                        else:
                                                            print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                            time.sleep(1)
                                            if(aliado_jogador.status[6]<=0):break
                                            else:
                                                print(" - CARAMBA! E nao e que voce estava pronto mesmo?! Hahahaha... Tudo bem perder as vezes...")
                                                time.sleep(2)
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print(" - CARAMBA! E nao e que voce estava pronto mesmo?! Hahahaha... Tudo bem perder as vezes...")
                                            time.sleep(2)
                                            situacao[0]=situacao[0]+1
                                            break
                                    else:
                                        print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                        time.sleep(1)
                        else:
                            if(situacao[0]>7):
                                print("Voce ja lutou aqui!")
                                time.sleep(2)
                            else:
                                print(" - Voce nao pode me desafiar enquanto nao vencer do briguento do quarto 40")
                                time.sleep(2)
                    else:
                        if(acao_do_personagem=="42"):
                            if(situacao[0]==8):
                                print(' - Humhumhumhum... Voce vai perder...')
                                time.sleep(2)
                                print(" - Veja: ")
                                time.sleep(1)
                                print("\n"+str(adversario_inimigo.nome)+": "+str(adversario_inimigo.status[5])+"pontos de vida.\nAtaque : "+str(adversario_inimigo.status[0])+".     Defesa : "+str(adversario_inimigo.status[1])+".\n")
                                time.sleep(2)
                                print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                time.sleep(1)
                                while 1:
                                    acao_do_personagem = raw_input("-")
                                    acao_do_personagem = acao_do_personagem.lower()
                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                        break
                                    else:
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            batalha(estudante_brigento[7])
                                            if(aliado_jogador.status[6]<=0):break
                                            if(adversario_inimigo.status[6]>0):
                                                while (adversario_inimigo.status[6]>0):
                                                    print(" - Voce vai fugir?(sim ou nao) Humhumhumhum...")
                                                    time.sleep(1)
                                                    while 1:
                                                        acao_do_personagem = raw_input("-")
                                                        acao_do_personagem = acao_do_personagem.lower()
                                                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                            print(" - Venha!!!")
                                                            time.sleep(2)
                                                            batalha(estudante_brigento[7])
                                                        else:
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                print(" - Voce vai mesmo?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                                time.sleep(1)
                                                                acao_do_personagem=raw_input("-")
                                                                acao_do_personagem=acao_do_personagem.lower()
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    print(" - Humhumhumhum... Fraco! Eu sempre soube que voce era fraco!")
                                                                    time.sleep(1)
                                                                    print(" - Volte quando voce deixar de ser fraco! FWUAHAHAHAHAHAHAHA!!! NUNCAAA!!!")
                                                                    time.sleep(1)
                                                                    aliado_jogador.dinheiro=aliado_jogador.dinheiro/2
                                                                    break
                                                                else:
                                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                        print(" - Venha!!!")
                                                                        time.sleep(2)
                                                                        batalha(estudante_brigento[7])
                                                                    else:
                                                                        print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                        time.sleep(1)
                                                            else:
                                                                print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                time.sleep(1)
                                                if(aliado_jogador.status[6]<=0):break
                                                else:
                                                    print(" - COMO?! COMO?! Voce trapaceou! EU SEI!!! Mas tudo bem, voce nao conseguira vencer o proximo, nem trapaceando MUITO!")
                                                    situacao[0]=situacao[0]+1
                                                    break
                                            else:
                                                print(" - COMO?! COMO?! Voce trapaceou! EU SEI!!! Mas tudo bem, voce nao conseguira vencer o proximo, nem trapaceando MUITO!")
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                            time.sleep(1)
                            else:
                                if(situacao[0]>8):
                                    print("Voce ja lutou aqui!")
                                    time.sleep(2)
                                else:
                                    print("Voce nao pode me desafiar enquanto nao vencer do briguento do quarto 41")
                                    time.sleep(2)
                        else:
                            if(acao_do_personagem=="43"):
                                if(situacao[0]==9):
                                    print(' - Sua presenca e insignificante.')
                                    time.sleep(2)
                                    print(" - Mas vou te dar a honra de apreciar o meu cartao: ")
                                    time.sleep(1)
                                    print("\n"+str(adversario_inimigo.nome)+": "+str(adversario_inimigo.status[5])+"pontos de vida.\nAtaque : "+str(adversario_inimigo.status[0])+".     Defesa : "+str(adversario_inimigo.status[1])+".\n")
                                    time.sleep(2)
                                    print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                    time.sleep(1)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                            break
                                        else:
                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                batalha(estudante_brigento[8])
                                                if(aliado_jogador.status[6]<=0):break
                                                if(adversario_inimigo.status[6]>0):
                                                    while (adversario_inimigo.status[6]>0):
                                                        print(" - ... Fugindo?(sim ou nao)")
                                                        time.sleep(1)
                                                        while 1:
                                                            acao_do_personagem = raw_input("-")
                                                            acao_do_personagem = acao_do_personagem.lower()
                                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                print(" - Voce vai MORRER!!!")
                                                                time.sleep(2)
                                                                batalha(estudante_brigento[8])
                                                            else:
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    print(" - Vai fugir mesmo, lixo?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                                    time.sleep(1)
                                                                    acao_do_personagem=raw_input("-")
                                                                    acao_do_personagem=acao_do_personagem.lower()
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - Sao os lixos como voce que pagaram o premio que NUNCA SERA SEU!")
                                                                        time.sleep(1)
                                                                        print(" - Volte quando quiser apanhar mais!")
                                                                        time.sleep(1)
                                                                        aliado_jogador.dinheiro=aliado_jogador.dinheiro/2
                                                                        break
                                                                    else:
                                                                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                            print(" - Voce vai MORRER!!!")
                                                                            time.sleep(2)
                                                                            batalha(estudante_brigento[8])
                                                                        else:
                                                                            print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                            time.sleep(1)
                                                                else:
                                                                    print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                    time.sleep(1)
                                                    if(aliado_jogador.status[6]<=0):break
                                                    else:
                                                        print(" - Desgracado... Voce e forte demais...")
                                                        time.sleep(2)
                                                        situacao[0]=situacao[0]+1
                                                        break
                                                else:
                                                    print(" - Desgracado... Voce e forte demais...")
                                                    time.sleep(2)
                                                    situacao[0]=situacao[0]+1
                                                    break
                                            else:
                                                print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                time.sleep(1)
                                else:
                                    if(situacao[0]>9):
                                        print("Voce ja lutou aqui!")
                                        time.sleep(2)
                                    else:
                                        print("Voce nao pode me desafiar enquanto nao vencer do briguento do quarto 42")
                                        time.sleep(2)
                            else:
                                if(acao_do_personagem=="44"):
                                    if(situacao[0]==10):
                                        print(' - Me perdoe pelo comportamento daqueles dois... Nenhum deles tem a cabeca no lugar.')
                                        time.sleep(2)
                                        print(" - Mesmo assim, e raro alguem passar do quarto 40, e rarissimo alguem chegar ate mim.")
                                        time.sleep(2)
                                        print(" - Voce e um briguento e tanto!")
                                        time.sleep(2)
                                        print(" - Vamos logo ao que interessa: ")
                                        time.sleep(1)
                                        print("\n"+str(adversario_inimigo.nome)+": "+str(adversario_inimigo.status[5])+"pontos de vida.\nAtaque : "+str(adversario_inimigo.status[0])+".     Defesa : "+str(adversario_inimigo.status[1])+".\n")
                                        time.sleep(2)
                                        print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                        time.sleep(1)
                                        while 1:
                                            acao_do_personagem = raw_input("-")
                                            acao_do_personagem = acao_do_personagem.lower()
                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                break
                                            else:
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    batalha(estudante_brigento[9])
                                                    if(aliado_jogador.status[6]<=0):break
                                                    if(adversario_inimigo.status[6]>0):
                                                        while (adversario_inimigo.status[6]>0):
                                                            print(" - ... Vai abandonar a nossa luta?(sim ou nao)")
                                                            time.sleep(1)
                                                            while 1:
                                                                acao_do_personagem = raw_input("-")
                                                                acao_do_personagem = acao_do_personagem.lower()
                                                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                    print(" - Desde o inicio, eu sabia que voce nao era qualquer um!")
                                                                    time.sleep(2)
                                                                    batalha(estudante_brigento[9])
                                                                else:
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - Certeza, vai abandonar a ultima luta?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                                        time.sleep(1)
                                                                        acao_do_personagem=raw_input("-")
                                                                        acao_do_personagem=acao_do_personagem.lower()
                                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                            print(" - Recupere-se e treine mais!")
                                                                            time.sleep(1)
                                                                            print(" - Estarei esperando o seu retorno!")
                                                                            time.sleep(1)
                                                                            aliado_jogador.dinheiro=aliado_jogador.dinheiro/2
                                                                            break
                                                                        else:
                                                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                                print(" - Ainda bem, nao quero deixar a nossa luta para depois!!!")
                                                                                time.sleep(2)
                                                                                batalha(estudante_brigento[9])
                                                                            else:
                                                                                print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                                time.sleep(1)
                                                                    else:
                                                                        print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                                                        time.sleep(1)
                                                        if(aliado_jogador.status[6]<=0):break
                                                        else:
                                                            print(" - Incrivel... Voce e um genio das batalhas! E realmente digno do premio!")
                                                            time.sleep(2)
                                                            print(" - Aqui esta: uma Malha Ninja!")
                                                            time.sleep(1)
                                                            print("Voce guardou a Malha Ninja na sua Mochila!")
                                                            time.sleep(2)
                                                            quantidade_adicionada=1
                                                            item_adicionado=malha_ninja
                                                            adicionaItem()
                                                            situacao[0]=situacao[0]+1
                                                            break
                                                    else:
                                                        print(" - Incrivel... Voce e um genio das batalhas! E realmente digno do premio!")
                                                        time.sleep(2)
                                                        print(" - Aqui esta: uma Malha Ninja!")
                                                        time.sleep(1)
                                                        print("Voce guardou a Malha Ninja na sua Mochila!")
                                                        time.sleep(2)
                                                        quantidade_adicionada=1
                                                        item_adicionado=malha_ninja
                                                        adicionaItem()
                                                        situacao[0]=situacao[0]+1
                                                        break
                                                else:
                                                    print('ENTRADA INVALIDA! Digite "sim" ou "nao".\n')
                                    else:
                                        if(situacao[0]>10):
                                            print("Voce ja lutou aqui!")
                                            time.sleep(2)
                                        else:
                                            print(" - Voce nao pode me desafiar enquanto nao vencer do briguento do quarto 43")
                                            time.sleep(2)
                                else:
                                    if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                        save()
                                    else:
                                        if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                            inventarioPersonagem()
                                        else:
                                            print('\nEntrada Invalida!\n')
                                            time.sleep(1)
        if(aliado_jogador.status[6]<=0):break

#--Seu predio: Terceiro Andar--#
def seuPredioTerceiroAndar(): #iemanjá
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    if booleana[0]==True:
        os.system('cls')
        escrever(0.02,"Agora que voce venceu todos os lutadores do 3o andar voce subiu ao 4o.\n",1)
        raw_input('|>')
        os.system('cls')
        seuPredioQuartoAndar()
    if(variavel_lugar == "seu predio, 4o andarb"):
        seuPredioQuartoAndar()
    if(aliado_jogador.status[6]>0):
        variavel_lugar = "seu predio, 3o andar"
        if(situacao[0]==0):
            escrever(0.02,"Voce e abordado pelo morador do quarto 44...\n",1)
            escrever(0.02," - E ai, voce e o morador do 13 ne?...\n",1)
            escrever(0.3,"...\n")
            escrever(0.02," - Voce e um pouco azarado, rapaz!")
            escrever(0.2," ... ")
            escrever(0.02,"Ou sortudo, depende do seu ponto de vista.\n",1)
            escrever(0.3,"...\n")
            escrever(0.02," - Okay, vou te explicar...\n",1)
            escrever(0.02," - Voce sabe que nos dois ultimos andares desse predio, o terceiro e o quarto,\nso tem quartos de estudantes briguentos, e nos estamos desafiando outros\narruaceiros a lutarem conosco!\n",1)
            escrever(0.3,"...\n")
            escrever(0.02," - Claro, se voce vencer de todos nos, sera recompensado!\n",1)
            escrever(0.02," - Va em frente, visite um dos quartos para lutar com um de nos!\n",1)
            escrever(0.02," - Eu estarei la em cima, no meu quarto, te esperando.\n",1.5)
            escrever(0.03,"\nEle subiu as escadas...\n")
            escrever(0.3,"...\n")
            situacao[0]+=1
        elif(situacao[0]==1): escrever(0.02,"Voce ainda nao venceu nenhuma luta do desafio dos estudantes briguentos!\n",1)
        elif(situacao[0]==2): escrever(0.02,"Voce ja venceu 1 luta do desafio dos estudantes briguentos!\n",1)
        elif(situacao[0]>=3 and situacao[0]<6): escrever(0.02,"Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!\n",1)
        elif(situacao[0]<11):
            escrever(0.02,"Voce ja venceu todas as lutas do terceiro andar, \nentao voce continuou subindo para o 4o andar.\n",1)
            seuPredioQuartoAndar()
            variavel_lugar = "seu predio, 3o andar"
        else:
            escrever(0.02,"Voce ja venceu o desafio dos estudantes briguentos do seu predio!\n")
    raw_input('|>')
    os.system('cls')
    while 1:
        if(aliado_jogador.status[6]<=0):break
        if(situacao[0]>=11):#?
            variavel_lugar = "seu predio, 2o andar"
            break
        else:
            if(situacao[0]>6):#?
                escrever(0.02,"Como voce ja venceu as lutas aqui, voce continuou descendo...")
                time.sleep(1)
                print("Voce desceu para o segundo andar.")
                time.sleep(1)
                variavel_lugar = "seu predio, 2o andar"
                break
        print("\n#"+"-"*30+"#\n\nLista de Acoes\n\nCenario: "+str( variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos: 30, 31, 32, 33 e 34\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#"+"-"*30+"#\n")
        print("\nE agora, "+str(aliado_jogador.nome)+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(30, 31, 32, 33 ou 34)\n")
            time.sleep(1)
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="30" and acao_do_personagem!="31" and acao_do_personagem!="32" and acao_do_personagem!="33" and acao_do_personagem!="34"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                print("Voce subiu para o quarto andar, la voce encontrou mais cinco quartos de portas abertas.")
                time.sleep(1)
                seuPredioQuartoAndar()
            else:
                if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                    print("Voce desceu para o segundo andar.")
                    time.sleep(1)
                    break
                else:
                    if(acao_do_personagem=="30"):
                        if(situacao[5] == 0):
                            print("Eu sou o seu oponente! Venca todos deste andar para subir!")
                            time.sleep(2)
                            batalha(estudante_brigento[0])
                            if(aliado_jogador.status[6]<=0):
                                aliado_jogador.status[6]=1
                                print(" - Voce e fraco, se fosse uma luta no andar de cima voce teria morrido!")
                                time.sleep(1)
                                print(" - Va cuidar desses seus ferimentos e volte para lutar mais!")
                                time.sleep(1)
                            else:
                                if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                    while (adversario_inimigo.status[6]>0):
                                        print(" - Voce nao pode fugir das lutas, e uma regra para continuar no desafio e ganhar o premio!")
                                        time.sleep(2)
                                        batalha(estudante_brigento[0])
                                        if(aliado_jogador.status[6]<=0):
                                            aliado_jogador.status[6]=1
                                            print(" - Voce e fraco, se fosse uma luta no andar de cima voce teria morrido!")
                                            time.sleep(1)
                                            print(" - Va cuidar desses seus ferimentos e volte para lutar mais!")
                                            time.sleep(1)
                                            break
                                        else:
                                            print(" - Isso ai! Voce me venceu!")
                                            time.sleep(2)
                                            situacao[0]=situacao[0]+1
                                            situacao[5]=1
                                            if(situacao[0]==6):
                                                booleana[0]= True
                                            else:
                                                if(situacao[0]==2):
                                                    print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                    time.sleep(2)
                                                else:
                                                    if(situacao[0]>=3 and situacao[0]<6):
                                                        print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                        time.sleep(2)
                                            break
                                else:
                                    print(" - Isso ai! Voce me venceu!")
                                    time.sleep(2)
                                    situacao[0]=situacao[0]+1
                                    situacao[5]=1
                                    if(situacao[0]==6):
                                        booleana[0]= True
                                    else:
                                        if(situacao[0]==2):
                                            print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                            time.sleep(2)
                                        else:
                                            if(situacao[0]>=3 and situacao[0]<6):
                                                print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                time.sleep(2)
                        else:
                            print("Voce ja lutou aqui!")
                            time.sleep(2)
                    else:
                        if(acao_do_personagem=="31"):
                            if(situacao[6] == 0):
                                print(" - Voce e o desafiante??? Parece um fracote!")
                                time.sleep(2)
                                batalha(estudante_brigento[1])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    print(" - Voce e mesmo um fracote!")
                                    time.sleep(1)
                                    print(" - Va se curar para continuar tentando subir para o quarto andar!")
                                    time.sleep(1)
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            print(" - Volte aqui seu fracote! Nao seja um covarde! Voce nao pode fugir de TODAS as lutas!")
                                            time.sleep(2)
                                            batalha(estudante_brigento[1])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                print(" - Voce e mesmo um fracote!")
                                                time.sleep(1)
                                                print(" - Va se curar para continuar tentando subir para o quarto andar!")
                                                time.sleep(1)
                                                break
                                            else:
                                                print(" - Nao vacile com os caras la do quarto andar, eles nao pegam leve!")
                                                time.sleep(2)
                                                situacao[0]=situacao[0]+1
                                                situacao[6]=1
                                                if(situacao[0]==6):
                                                    booleana[0]= True
                                                else:
                                                    if(situacao[0]==2):
                                                        print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                        time.sleep(2)
                                                    else:
                                                        if(situacao[0]>=3 and situacao[0]<6):
                                                            print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                            time.sleep(2)
                                                break
                                    else:
                                        print(" - Nao vacile com os caras la do quarto andar, eles nao pegam leve!")
                                        time.sleep(2)
                                        situacao[0]=situacao[0]+1
                                        situacao[6]=1
                                        if(situacao[0]==6):
                                            booleana[0]= True
                                        else:
                                            if(situacao[0]==2):
                                                print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                time.sleep(2)
                                            else:
                                                if(situacao[0]>=3 and situacao[0]<6):
                                                    print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                    time.sleep(2)
                            else:
                                print("Voce ja lutou aqui!")
                                time.sleep(2)
                        else:
                            if(acao_do_personagem=="32"):
                                if(situacao[7]==0):
                                    print(" - Cai dentro, rapa!")
                                    time.sleep(2)
                                    batalha(estudante_brigento[2])
                                    if(aliado_jogador.status[6]<=0):
                                        aliado_jogador.status[6]=1
                                        print(" - Moleque criado a leite com pera!")
                                        time.sleep(1)
                                        print(" - La em cima ninguem vai te dar essa colher de cha que eu to te dando!")
                                        time.sleep(1)
                                    else:
                                        if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                            while (adversario_inimigo.status[6]>0):
                                                print(" - Ramelao, nao foge da luta, nao!")
                                                time.sleep(2)
                                                batalha(estudante_brigento[2])
                                                if(aliado_jogador.status[6]<=0):
                                                    aliado_jogador.status[6]=1
                                                    print(" - Moleque criado a leite com pera!")
                                                    time.sleep(1)
                                                    print(" - La em cima ninguem vai te dar essa colher de cha que eu to te dando!")
                                                    time.sleep(1)
                                                    break
                                                else:
                                                    print(" - Nada mal, quem sabe voce consegue o premio! Nunca se sabe... ")
                                                    time.sleep(2)
                                                    situacao[0]=situacao[0]+1
                                                    situacao[7]=1
                                                    if(situacao[0]==6):
                                                        booleana[0]= True
                                                    else:
                                                        if(situacao[0]==2):
                                                            print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                            time.sleep(2)
                                                        else:
                                                            if(situacao[0]>=3 and situacao[0]<6):
                                                                print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                                time.sleep(2)
                                                    break
                                        else:
                                            print(" - Nada mal, quem sabe voce consegue o premio! Nunca se sabe... ")
                                            time.sleep(2)
                                            situacao[0]=situacao[0]+1
                                            situacao[7]=1
                                            if(situacao[0]==6):
                                                booleana[0]= True
                                            else:
                                                if(situacao[0]==2):
                                                    print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                    time.sleep(2)
                                                else:
                                                    if(situacao[0]>=3 and situacao[0]<6):
                                                        print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                        time.sleep(2)
                                else:
                                    print("Voce ja lutou aqui!")
                                    time.sleep(2)
                            else:
                                if(acao_do_personagem=="33"):
                                    if(situacao[8]==0):
                                        print(" - OOo, CIDADAO!")
                                        time.sleep(2)
                                        batalha(estudante_brigento[3])
                                        if(aliado_jogador.status[6]<=0):
                                            aliado_jogador.status[6]=1
                                            print(" - Olha la, o cara nao aguenta e depois vai chorando pra casa!")
                                            time.sleep(1)
                                            print(" - Se voce continuar tropecando assim, cedo ou tarde o mundo vai te atropela!")
                                            time.sleep(1)
                                        else:
                                            if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                                while (adversario_inimigo.status[6]>0):
                                                    print(" - Ta na hora de acordar pra vida, cidadao!")
                                                    time.sleep(2)
                                                    batalha(estudante_brigento[3])
                                                    if(aliado_jogador.status[6]<=0):
                                                        aliado_jogador.status[6]=1
                                                        print(" - Olha la, o cara nao aguenta e depois vai chorando pra casa!")
                                                        time.sleep(1)
                                                        print(" - Se voce continuar tropecando assim, cedo ou tarde o mundo vai te atropela!")
                                                        time.sleep(1)
                                                        break
                                                    else:
                                                        print(" - ACORDA CARA! Voce nao e mais nenhum menininho bobinho, nao! ")
                                                        time.sleep(2)
                                                        situacao[0]=situacao[0]+1
                                                        situacao[8]=1
                                                        if(situacao[0]==6):
                                                            booleana[0]= True
                                                        else:
                                                            if(situacao[0]==2):
                                                                print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                                time.sleep(2)
                                                            else:
                                                                if(situacao[0]>=3 and situacao[0]<6):
                                                                    print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                                    time.sleep(2)
                                                        break
                                            else:
                                                print(" - ACORDA CARA! Voce nao e mais nenhum menininho bobinho, nao! ")
                                                time.sleep(2)
                                                situacao[0]=situacao[0]+1
                                                situacao[8]=1
                                                if(situacao[0]==6):
                                                    booleana[0]= True
                                                else:
                                                    if(situacao[0]==2):
                                                        print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                        time.sleep(2)
                                                    else:
                                                        if(situacao[0]>=3 and situacao[0]<6):
                                                            print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                            time.sleep(2)
                                    else:
                                        print("Voce ja lutou aqui!")
                                        time.sleep(2)
                                else:
                                    if(acao_do_personagem=="34"):
                                        if(situacao[9]==0):
                                            print(" - Qual e, velho? O negocio e descer o murro de ferro na cara do inimigo!")
                                            time.sleep(2)
                                            batalha(estudante_brigento[4])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                print(" - Voce nao tem um sangue fervente o suficiente para derreter o metal!")
                                                time.sleep(1)
                                                print(" - Voce precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                time.sleep(1)
                                            else:
                                                if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                                    while (adversario_inimigo.status[6]>0):
                                                        print(" - As mentiras ja sao antigas demais, mas voce nao quer saber!\nCorrer e uma futilidade!")
                                                        time.sleep(2)
                                                        batalha(estudante_brigento[4])
                                                        if(aliado_jogador.status[6]<=0):
                                                            aliado_jogador.status[6]=1
                                                            print(" - Voce nao tem um sangue fervente o suficiente para derreter o metal!")
                                                            time.sleep(2)
                                                            print(" - Voce precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                            time.sleep(2)
                                                            break
                                                        else:
                                                            print(" - A verdade e mais dura que o aco! Mas a visao nunca morre!")
                                                            time.sleep(2)
                                                            situacao[0]=situacao[0]+1
                                                            situacao[9]=1
                                                            if(situacao[0]==6):
                                                                booleana[0]= True
                                                            else:
                                                                if(situacao[0]==2):
                                                                    print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                                    time.sleep(2)
                                                                else:
                                                                    if(situacao[0]>=3 and situacao[0]<6):
                                                                        print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                                        time.sleep(2)
                                                            break
                                                else:
                                                    print(" - A verdade e mais dura que o aco! Mas a visao nunca morre!")
                                                    time.sleep(2)
                                                    situacao[0]=situacao[0]+1
                                                    situacao[9]=1
                                                    if(situacao[0]==6):
                                                        booleana[0]= True
                                                    else:
                                                        if(situacao[0]==2):
                                                            print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                                                            time.sleep(2)
                                                        else:
                                                            if(situacao[0]>=3 and situacao[0]<6):
                                                                print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                                                                time.sleep(2)
                                        else: print("Voce ja lutou aqui!")
                                    else:
                                        if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                            save()
                                        else:
                                            if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                inventarioPersonagem()
                                            else: print('Entrada Invalida!')

#--Seu predio: Segundo Andar--#
def seuPredioSegundoAndar():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    if(variavel_lugar == "seu predio, 3o andarb" or variavel_lugar == "seu predio, 4o andarb"):
        seuPredioTerceiroAndar()
    variavel_lugar = "seu predio, 2o andar"
    while 1:
        if(aliado_jogador.status[6]<=0):break
        print("\n#"+"-"*30+"#\n\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos\n")
        if(situacao[2]==1):
            print("\narrombar o quarto 24")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n\n#"+"-"*30+"#\n\nE agora, "+str(aliado_jogador.nome)+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(20, 21, 22, 23 ou 24)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="20" and acao_do_personagem!="21" and acao_do_personagem!="22" and acao_do_personagem!="23" and acao_do_personagem!="24"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                escrever(0.02,"Voce subiu para o terceiro andar,",0.5)
                escrever(0.02,"la voce encontrou cinco quartos\ncom as portas abertas e outra escada ascendente.\n",1)
                seuPredioTerceiroAndar()
                if(aliado_jogador.status[6]<=0):break
            else:
                if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                    escrever(0.02,"Voce desceu para o primeiro andar, o andar do seu quarto.\n",1)
                    break
                else:
                    if(acao_do_personagem=="20"):
                        if(situacao[3]==10):
                            escrever(0.02,"Voce ja pegou tudo o que tinha para pegar aqui.\n",0.5)
                        else:
                            escrever(0.02,"Voce bate na porta e percebe, pelo barulho do trepidar da macaneta, \nque ela esta destrancada...\n",2)
                            escrever(0.02,"Abrir a porta?")
                            print(" (sim ou nao)")
                            while 1:
                                acao_do_personagem = raw_input("-")
                                acao_do_personagem = acao_do_personagem.lower()
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    escrever(0.04,"Voce entrou, nao havia ninguem...\n",1)
                                    escrever(0.02,"Ao revistar o quarto voce encontrou 10 Reais!\n")
                                    aliado_jogador.dinheiro=aliado_jogador.dinheiro+10
                                    situacao[10]=1
                                    break
                                else:
                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                        escrever(0.02,"Voce ignorou o quarto...\n",1)
                                        time.sleep(0.75)
                                        break
                                    else: print('ENTRADA INVALIDA!')
                    else:
                        if(acao_do_personagem=="21"):
                            if(situacao[3]==7):
                                escrever(0.02,"Voce bate na porta...\n",0.5)
                                escrever(0.08," - Ola! ",0.1)
                                escrever(0.02,"- diz o avo do garoto ",0.1)
                                escrever(0.06,"- Muito obrigado por treinar o meu neto,\nagora ele nao precisa se esconder mais dos trombadinhas da faculdade.\n")
                            if(situacao[3]==6):
                                escrever(0.02," - Obrigado por me treinar, senhor.\n",2)
                                batalha(garoto_oponente[5])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    escrever(0.02," - Me supere. Estarei te esperando.\n")
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            escrever(0.02," - Nao abandone nossa luta!\n")
                                            batalha(garoto_oponente[5])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                escrever(0.02," - Me supere. Estarei te esperando.\n")
                                            else:
                                                if(adversario_inimigo.status[6]<=0):
                                                    escrever(0.02," - Obrigado, mesmo!\n")
                                                    situacao[3]=7
                                    else:
                                        if(adversario_inimigo.status[6]<=0):
                                            escrever(0.02," - Obrigado, mesmo!\n")
                                            situacao[3]=7
                            if(situacao[3]==5):
                                escrever(0.02," - Estou empolgado! Nao aguentava mais esperar pela nossa luta!\n")
                                batalha(garoto_oponente[4])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    escrever(0.02," - Quando voce estiver pronto para uma revanche, me procure novamente.\n")
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            escrever(0.02," - A nossa luta nao acabou ainda!\n")
                                            batalha(garoto_oponente[4])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                escrever(0.02," - Quando voce estiver pronto para uma revanche, me procure novamente.\n")
                                            else:
                                                if(adversario_inimigo.status[6]<=0):
                                                    escrever(0.02," - Incrivel, voce sempre me surpreende! Se prepare, da proxima vez estarei ainda mais forte!\n")
                                                    situacao[3]=6
                                    else:
                                        if(adversario_inimigo.status[6]<=0):
                                            escrever(0.02," - Incrivel, voce sempre me surpreende! Se prepare, da proxima vez estarei ainda mais forte!\n")
                                            situacao[3]=6
                            if(situacao[3]==4):
                                escrever(0.02," - Dessa vez nao vou perder tao facil!\n")
                                batalha(garoto_oponente[3])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    escrever(0.02," - Estou te levando a serio, nao vou perder mais!\n - Estarei te esperando para uma revanche.\n")
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            escrever(0.02," - Honre a nossa luta ate o fim!\n")
                                            batalha(garoto_oponente[3])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                escrever(0.02," - Estou te levando a serio, nao vou perder mais!\n - Estarei te esperando para uma revanche.\n")
                                            else:
                                                if(adversario_inimigo.status[6]<=0):
                                                    escrever(0.02," - Voce e mesmo forte! \nTreinarei mais e estarei te esperando para o nosso proximo confronto!\n")
                                                    situacao[3]=5
                                    else:
                                        if(adversario_inimigo.status[6]<=0):
                                            escrever(0.02," - Voce e mesmo forte! \nTreinarei mais e estarei te esperando para o nosso proximo confronto!\n")
                                            situacao[3]=5
                            if(situacao[3]==3):
                                escrever(0.02," - Eu estava te esperando, panaca!\n")
                                batalha(garoto_oponente[2])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    escrever(0.02," - Nao aguenta o tranco, nao? Hahaha!\n - Volte qualquer hora para apanhar mais!\n")
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            escrever(0.02," - Volte aqui seu panaca!\n")
                                            batalha(garoto_oponente[2])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                escrever(0.02," - Nao aguenta o tranco, nao? Hahaha!\n - Volte qualquer hora para apanhar mais!\n")
                                            else:
                                                if(adversario_inimigo.status[6]<=0):
                                                    escrever(0.02," - Voce e mesmo forte! Continuarei treinando e esperarei o nosso proximo confronto!\n")
                                                    situacao[3]=4
                                    else:
                                        if(adversario_inimigo.status[6]<=0):
                                            escrever(0.02," - Voce e mesmo forte! Continuarei treinando e esperarei o nosso proximo confronto!\n")
                                            situacao[3]=4
                            if(situacao[3]==2):
                                escrever(0.02," - Meu avo disse que voce viria... - disse o garoto baixinho - Vamos logo ao que interessa!\n")
                                batalha(garoto_oponente[1])
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                    escrever(0.02," - Voce nao e tao forte quanto meu avo falou.\n")
                                    situacao[3]=3
                                else:
                                    if(adversario_inimigo.status[6]>0 and aliado_jogador.status[6]>1):
                                        while (adversario_inimigo.status[6]>0):
                                            escrever(0.02," - Meu avo disse para nao parar de lutar ate eu nao aguentar mais!\n")
                                            batalha(garoto_oponente[1])
                                            if(aliado_jogador.status[6]<=0):
                                                aliado_jogador.status[6]=1
                                                escrever(0.02," - Voce nao e tao forte quanto meu avo falou.\n")
                                                situacao[3]=3
                                            else:
                                                if(adversario_inimigo.status[6]<=0):
                                                    escrever(0.02," - Voce e muito forte!!! \nVou treinar e estarei te esperando para uma proxima luta!\n")
                                                    situacao[3]=3
                                    else:
                                        if(adversario_inimigo.status[6]<=0):
                                            escrever(0.02," - Voce e muito forte!!! \nVou treinar e estarei te esperando para uma proxima luta!\n")
                                            situacao[3]=3
                            if(situacao[3]==1):
                                escrever(0.02,"A porta esta trancada.\n")
                            if(situacao[3]==0):
                                escrever(0.04,"Voce bateu na porta...\n",0.5)
                                escrever(0.03,"Um senhor baixo e fracote abriu a porta... Ele parecia muito com um frango\n",0.5)
                                escrever(0.02," - O que que voce quer?!\n")
                                escrever(0.08,"...\n",0.1)
                                escrever(0.02," - Saia daqui entao!\n")
                                batalha(senhor_doente)
                                if(aliado_jogador.status[6]<=0):break
                                if(adversario_inimigo.status[6]>0):
                                    escrever(0.03,"Depois de se afastar o senhor comecou a gritar...\n",0.1)
                                    escrever(0.02,"Com a mao no peito, ele comecou a tossir...\n",0.1)
                                    escrever(0.1," - Ahhhh... ",0.1)
                                    escrever(0.02,"- gemeu o senhor que caia lentamente.\n",0.1)
                                    escrever(0.01," - O QUE VOCE FEZ COM MEU AVO?! ",0.1)
                                    escrever(0.03,"- era a voz de um menino vindo la de dentro do quarto.\n")
                                    escrever(0.02,"O menino pegou o senhor nos bracos antes que tombasse \ne apertou algumas vezes uma bombinha para asma na boca dele...\n",0.5)
                                    escrever(0.01," - VOCE VAI PAGAR CARO!\n")
                                    batalha(garoto_oponente[0])
                                    if(aliado_jogador.status[6]<=0):break
                                    if(adversario_inimigo.status[6]>0):
                                        escrever(0.02," - SAIA JA DAQUI!\n",0.5)
                                        escrever(0.02,"Em seguida ele fechou e trancou a porta.\n")
                                        situacao[3]==1
                                    else:
                                        escrever(0.02,"O garoto caiu no chao dentro da casa e comecou a chorar.\n - SAIA DAQUI ANTES QUE EU CHAME A POLICIA! - disse o senhor que ja estava um pouco melhor...\nEm seguida ele fechou e trancou a porta.\n")
                                        situacao[3]=1
                                else:
                                    escrever(0.04,"O senhor caiu no chao com uma mao no peito...\n",0.5)
                                    escrever(0.02,"Ele tentava gritar algo enquanto estendia a outra mao...\n",0.5)
                                    escrever(0.03,"Mas nao conseguia dizer nada, estava tendo crise de asma...\n",0.5)
                                    escrever(0.02,"Sua mao apontava para um lugar dentro da casa...\nVai ajudar o idoso?")
                                    print(" (sim ou nao)")
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            escrever(0.009,"Voce entrou na casa, pegou a bombinha em cima da mesa \ne a apertou na boca do velho...\n",1)
                                            escrever(0.1," - Ah... Ah... ",0.5)
                                            escrever(0.02,"- o senhor tentava recuperar o ar ",0.5)
                                            escrever(0.08,"- Voce nao e um mau rapaz \nno fim das contas...\n",0.1)
                                            escrever(0.02,"...\n",0.5)
                                            escrever(0.06," - Voce gosta de lutar, nao e garoto? Eu brigava muito quando era mais jovem...\n",0.1)
                                            escrever(0.02,"...\n",0.5)
                                            escrever(0.04," - Nem sempre os punhos sao o bastante...\n",0.1)
                                            escrever(0.02,"...\n",0.5)
                                            escrever(0.03," - Nao falo do coracao na luta, isso voce ja tem, falo de armas...\n",0.5)
                                            escrever(0.02," - Tome... Eu usava este punhal no meu tempo... Agora e seu.\n")
                                            item_adicionado=punhal_envelhecido
                                            quantidade_adicionada=1
                                            adicionaItem()
                                            escrever(0.02,"Voce guardou o Punhal Envelhecido na mala!\n",1)
                                            escrever(0.02," - Se nao for pedir demais, venha sempre que puder para treinar o meu neto...\n",0.5)
                                            escrever(0.02,"Ele ainda e muito fraco e eu nao tenho mais o mesmo vigor de antes...\n",0.5)
                                            escrever(0.02," - Nao me entenda mal, nao e uma troca de favores... \nE um pedido de um velho que nao consegue ajudar seu neto.\n")
                                            situacao[3]=2
                                            break
                                        else:
                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                escrever(0.01," - O QUE VOCE FEZ COM MEU AVO?! ",0.1)
                                                escrever(0.03,"- era a voz de um menino vindo la de dentro do quarto.\n")
                                                escrever(0.02,"O menino pegou o senhor nos bracos antes que tombasse \ne apertou algumas vezes uma bombinha para asma na boca dele...\n",0.5)
                                                escrever(0.01," - VOCE VAI PAGAR CARO!\n")
                                                batalha(garoto_oponente[0])
                                                if(aliado_jogador.status[6]<=0):break
                                                if(adversario_inimigo.status[6]>0):
                                                    escrever(0.02," - SAIA JA DAQUI!\n",0.5)
                                                    escrever(0.02,"Em seguida ele fechou e trancou a porta.\n")
                                                    situacao[3]=1
                                                else:
                                                    escrever(0.02,"O garoto caiu no chao dentro da casa e comecou a chorar.\n - SAIA DAQUI ANTES QUE EU CHAME A POLICIA! - disse o senhor que ja estava um pouco melhor...\nEm seguida ele fechou e trancou a porta.\n")
                                                    situacao[3]=1
                                                break
                                            else: print('ENTRADA INVALIDA!')
                        else:
                            if(acao_do_personagem=="22"):
                                if(situacao[4]==4):
                                    escrever(0.02,"Voce bateu na porta... ",0.5)
                                    escrever(0.02,"Ninguem te atendeu.\n")
                                if(situacao[4]==3):
                                    escrever(0.02," - E ai, rapaz!")
                                    escrever(0.05," . . . ")
                                    teste_de_sorte = random.randrange(3)
                                    if(teste_de_sorte==1):
                                        escrever(0.02,"Voce chegou em boa hora! \nEntre e coma um pedaco de pizza comigo!\n",1)
                                        escrever(0.02,"Voce ganhou um pedaco de pizza!\n",1)
                                        item_adicionado=pedaco_pizza[0]
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        escrever(0.02," - Ate outra hora, vizinho!\n")
                                    else:
                                        escrever(0.02,"Estou sem pizza agora, talvez mais tarde...\n")
                                if(situacao[4]==2):
                                    escrever(0.01," - O que voce quer aqui?\n",0.5)
                                    escrever(0.02,"Voce vai dizer a ele que comeu a sua pizza?")
                                    print(" (sim ou nao)")
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            escrever(0.05," - ...",0.1)
                                            escrever(0.05," VOCE...\n",0.1)
                                            escrever(0.02," - Voce e muito cara de pau mesmo, mas adimiro a sua sinceridade.\n",0.2)
                                            escrever(0.02," - Eu sempre como pizza, quando voce quiser passe aqui para pegar um pedaco.")
                                            situacao[4]=3
                                            break
                                        else:
                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                escrever(0.05," - ...",0.1)
                                                escrever(0.01," Me deixe em paz!\n")
                                                situacao[4]=4
                                                break
                                            else: print('Entrada invalida!')
                                if(situacao[4]==1):
                                    escrever(0.03,"Voce bateu na porta do quarto, que agora esta fechado.\n",0.1)
                                    escrever(0.02,"Voce escuta passos rapidos e violentos vindo a porta...\n")
                                    escrever(0.01," - EU TO MUITO PUTO! ",0.1)
                                    escrever(0.03,"- diz o estudante que abriu violentamente a porta ",0.1)
                                    escrever(0.01,"- ENTRARAM E COMERAM A MINHA PIZZA!\n")
                                    escrever(0.05,"..\n.",0.1)
                                    escrever(0.03," - Ah esquece... Nem deve ter sido voce...\n")
                                    situacao[4]=2
                                if(situacao[4]==0):
                                    escrever(0.02,"O quarto esta aberto, voce entra e ve um estudante vagabundo dormindo num sofa com uma pizza no colo.\n",0.1)
                                    escrever(0.02,"E ai, vai pegar essa pizza?")
                                    print(" (sim ou nao)")
                                    time.sleep(0.5)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            escrever(0.02,"Voce guardou a pizza inteira na mochila!\n")
                                            item_adicionado=pizza_inteira[0]
                                            quantidade_adicionada=1
                                            adicionaItem()
                                            situacao[4]=1
                                            break
                                        else:
                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                escrever(0.02,"Voce deixou a pizza para depois!\n")
                                                break
                                            else: print('Entrada invalida!')
                            else:
                                if(acao_do_personagem=="23"):
                                   escrever(0.02,"Voce ve um quarto aberto, sujo e vazio...\n",0.3)
                                   escrever(0.02,"Parece abandonado por um bom tempo... Ja tem fauna e flora proria!\n")
                                else:
                                    if(acao_do_personagem=="24"):
                                        if(situacao[2]==0):
                                            escrever(0.03,"Voce encara um individuo de aparencia extravagante e vulgar encostado no batente da porta...\n")
                                            escrever(0.01," - Quale merh-mao? Ta querenu treta?\n")
                                            batalha(mane_bone)
                                            if(aliado_jogador.status[6]<=0):break
                                            if(adversario_inimigo.status[6]>0):
                                                escrever(0.02,"Ele corre atras de voce e te da um chute no joelho!\n",1)
                                                escrever(0.009,"!!!\n",0.5)
                                                escrever(0.02,"Voce perdeu 30 pontos de vida!\n",0.5)
                                                escrever(0.01," - Fica diboa rapah!\n")
                                                aliado_jogador.status[6]=aliado_jogador.status[6]-30
                                                if(aliado_jogador.status[6]<=0):aliado_jogador.status[6]=1
                                                escrever(0.03,"Ele voltou ao batente da porta do quarto e agora esta te encarando...\n",1)
                                                escrever(0.09,"Voce me envergonha.\n")
                                            else:
                                                escrever(0.009," - Que isso maluco?!",0.1)
                                                escrever(0.009," Que isso?!\n")
                                                escrever(0.02,"Ele entrou cambaleando para o quarto dele e se trancou!\n")
                                                situacao[2]=1
                                        if(situacao[2]==1): escrever(0.02,"O quarto esta trancado...")
                                        if(situacao[2]==2):
                                            escrever(0.03,"Voce ve uma porta quebrada ao meio, caida, mas presa apenas pela dobradica inferior, \na superior segurava apenas um pedaco de madeira desprendido da porta.\n",1)
                                            escrever(0.04,"Dentro voce ve muito sangue pelo quarto, os poucos moveis quebrados, \n",0.5)
                                            escrever(0.02,"mas nada de valor...",0.1)
                                            matarAlguem()
                                        if(situacao[2]==3):
                                            escrever(0.03,"Voce ve uma porta quebrada ao meio, caida, mas presa apenas pela dobradica inferior, \na superior segurava apenas um pedaco de madeira desprendido da porta.\n",1)
                                            escrever(0.04,"Tambem escuta, vindo la de dentro, solucos em sussurros e sussurros em solucos...\n",0.5)
                                            escrever(0.02,"Melhor nao entrar... Nao ha nada de mais la dentro.")
                                    else:
                                        if(acao_do_personagem=="arrombar a porta do quarto 24" or acao_do_personagem=="arrombar o quarto 24" or acao_do_personagem=="arrombar" or acao_do_personagem=="arrombar a porta" or acao_do_personagem=="entrar no quarto 24"):
                                            if(situacao[2]==1):
                                                escrever(0.007,"Voce pisoteou a porta e entrou no quarto!",0.5)
                                                escrever(0.08," - Nao,",0.5)
                                                escrever(0.02," por favor nao!...",0.5)
                                                while 1:
                                                    if(situacao[2]==2): break
                                                    if(situacao[2]==3): break
                                                    escrever(0.03,"Melhor nao continuar...")
                                                    print(" (sim ou nao)")
                                                    acao_do_personagem=raw_input("-")
                                                    acao_do_personagem=acao_do_personagem.lower()
                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                        while 2:
                                                            escrever(0.02,"Eu insisto... ",0.1)
                                                            escrever(0.02,"E melhor parar... ",0.1)
                                                            escrever(0.02,"Voce esta de cabeca quente...")
                                                            print(" (sim ou nao)")
                                                            acao_do_personagem=raw_input("-")
                                                            acao_do_personagem=acao_do_personagem.lower()
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                raw_input("(Aperte ENTER)")
                                                                raw_input("!!!!!!!!!!!!")
                                                                escrever(0.01," - NAO,",0.1)
                                                                escrever(0.02," NAO!\n")
                                                                raw_input("(Continue golpeando com o ENTER)")
                                                                raw_input("!!!!!!!!!!!!")
                                                                raw_input("!!!!!!!!....")
                                                                raw_input("!!!!........")
                                                                raw_input("....!!!!....")
                                                                raw_input("........!!!!")
                                                                raw_input("!!!!....!!!!")
                                                                escrever(0.02," - N",0.5)
                                                                escrever(0.05,"-NA",0.1)
                                                                escrever(0.1,"o..o!\n")
                                                                raw_input("(Ja nao ha mais motivos para golpear...)")
                                                                escrever(0.03,"Seus punhos vermelhos tremem...\n",0.5)
                                                                escrever(0.01,"Voce o espancou ate a morte...\n",0.1)
                                                                escrever(0.5,"...\n")
                                                                matarAlguem()
                                                                situacao[2]=2
                                                                break
                                                            else:
                                                                if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                    escrever(0.03,"Voce respirou fundo, abaixou os punhos e se retirou do quarto...",0.1)
                                                                    escrever(0.02,"Voce superou seus instintos e respeitou seus principios...",0.1)
                                                                    escrever(0.02,"Ao recuperar seu folego, seus pontos de vida aumentaram.")
                                                                    time.sleep(1)
                                                                    aliado_jogador.status[5]=aliado_jogador.status[5]+50
                                                                    aliado_jogador.status[6]=aliado_jogador.status[5]
                                                                    situacao[2]=3
                                                                    break
                                                                else: print("Entrada invalida... A situacao e tensa, mantenha a seriedade e responda corretamente.")
                                                        break
                                                    else:
                                                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                            escrever(0.03,"Voce respirou fundo, abaixou os punhos e se retirou do quarto...",0.1)
                                                            escrever(0.02,"Voce superou seus instintos e respeitou seus principios...",0.1)
                                                            escrever(0.02,"Ao recuperar seu folego, seus pontos de vida aumentaram.")
                                                            time.sleep(1)
                                                            aliado_jogador.status[5]=aliado_jogador.status[5]+100
                                                            aliado_jogador.status[6]=aliado_jogador.status[5]
                                                            situacao[2]=3
                                                            break
                                                        else: print("Entrada invalida... A situacao e tensa, mantenha a seriedade e responda corretamente.")
                                            if(situacao[2]==2):
                                                matarAlguem()
                                            if(situacao[2]==3): print("Voce ja fez o bastante por aqui... Melhor se afastar.")
                                        elif(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"): save()
                                        elif(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"): inventarioPersonagem()
                                        else: print('Entrada Invalida!')

#--Seu predio: Primeiro Andar--#
def seuPredioPrimeiroAndar():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    if(variavel_lugar == "seu predio, 2o andarb" or variavel_lugar == "seu predio, 3o andarb" or variavel_lugar == "seu predio, 4o andarb"):
        seuPredioSegundoAndar()
    if(aliado_jogador.status[6]>0):
        variavel_lugar = "seu predio, 1o andar"
        escrever(0.02,"\nAgora voce esta no corredor do primeiro andar do seu predio.\n\n")
    while 1:
        raw_input('|>')
        os.system('cls')
        print("\n#"+"-"*30+"#\n"+"\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\nolhar\n")
        if (variavel_cenario[0] == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            if (variavel_cenario[2] == "sim" and objeto[0] == "nao"):
                print(" olhar o bebado\n")
        if(objeto[1] == "sim" and objeto[3]!='sim'):
            print("\narrombar o quarto 10\n")
        if (objeto[0] == "1"):
            print("\nacordar o bebado\n\nrevistar o bebado\n")
        if (objeto[0] == "2"):
            print("\nmover o bebado\n")
        if (objeto[0] == "3"):
            print("\natacar o bebado\n")
        if (objeto[0] == "sim"):
            print("\nabrir a porta dos fundos\n")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n\nO que voce fara agora, "+str(aliado_jogador.nome)+"?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(aliado_jogador.status[6]<=0):break
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(10, 11, 12 ou 14)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="10" and acao_do_personagem!="11" and acao_do_personagem!="12" and acao_do_personagem!="13" and acao_do_personagem!="14"):
                acao_do_personagem="entrada invalida!"
        if(acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem == "olhar" or acao_do_personagem == "ver" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha" or acao_do_personagem == "olhar quarto" or acao_do_personagem == "olha quarto" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha o quarto" or acao_do_personagem == "ve" or acao_do_personagem == "ve"):
                escrever(0.015,"\nVoce ve um corredor estreito com 5 portas, o seu e os outros quartos desse \nandar do predio.\nNum dos lados desse corredor ha uma janela quebrada,\n",1)
                if (objeto[0]=="sim" or objeto[0]=="pegou o dinheiro"):
                    escrever(0.025,"mas no outro se encontra a porta dos fundos.\n")
                elif (variavel_cenario[2] == "1" or variavel_cenario[2] == "sim"):
                    escrever(0.025,"mas no outro se encontra um bebado caido no chao, imundo e cercado de vomito,\nencostado na porta dos fundos, impedindo o acesso.\n")
                else:
                    escrever(0.025,"mas no outro se encontra, encostado na porta dos fundos e caido no chao \ncoberto por cacos de vidro, um homem sujo, \ncercado por algum liquido que parece laranja...\n")
                    variavel_cenario[0] = "sim"
                escrever(0.015,"\nE ao longo do corredor, em frente aos quartos ha um par de escadas azul-pastel \num pouco alaranjada ao redor das ferrugens.\nA mais proxima sobe e a colada a parede desce.\n\n")
            else:
                if(acao_do_personagem=="cheirar" or acao_do_personagem=="cherar" or acao_do_personagem=="dar um tapa" or acao_do_personagem=="cheira" or acao_do_personagem=="chera"):
                    if(variavel_cenario[2]=="nao"):
                        variavel_cenario[2]="sim"
                    escrever(0.02,"\nVoce sente um cheiro forte de alcool e vomito\n\n")
                else:
                    if(acao_do_personagem=="10"):
                        if(objeto[3]=="sim"):
                            escrever(0.02,"\nVoce ve uma porta arrombada... \nNao ha mais nada de interessante dentro do quarto.\n\n")
                        else:
                            escrever(0.02,"\nVoce bateu na porta, mas ninguem atendeu... \nEla parece facil de ser arrombada...\n\n")
                            objeto[1]="sim"
                    else:
                        if(acao_do_personagem=="11"):
                            if(situacao[1]==0):
                                escrever(0.025,"\nQuando voce bateu, a porta se abriu no primeiro toque \npor nao ter uma fechadura...\nVoce ve, dentro da casa, uma mulher alta de ombros largos, BEM LARGOS, \nmusculosa e com o maxilar largo...\n",0.5)
                                escrever(0.04,"Ela estava apenas de toalha...\n\n")
                                escrever(0.01," - MAS QUE ATREVIMENTO! SUMA DAQUI! ",0.5)
                                escrever(0.025,"- diz a mulher enquanto te epurra com a \nporta que e fechada violentamente.\n\n",0.5)
                                escrever(0.015,"Voce perdeu 5 pontos de vida ao cair no corredor...\n\n")
                                aliado_jogador.status[6]=aliado_jogador.status[6]-5
                                if(aliado_jogador.status[6]<=0):
                                    aliado_jogador.status[6]=1
                                situacao[1]=1
                            else:
                                if(situacao[1]==1):
                                    escrever(0.04,"\nVoce empurrou a porta sem fechadura, mas moradora que ainda estava te toalha, \nfuriosamente fechou a porta gritando, antes que voce pudesse terminar de abrir!\n\n",0.5)
                                    escrever(0.015,"Voce perdeu 5 pontos de vida ao cair no corredor...\n\n")
                                    aliado_jogador.status[6]=aliado_jogador.status[6]-5
                                    if(aliado_jogador.status[6]<=0):
                                        aliado_jogador.status[6]=1
                                    situacao[1]=2
                                else:
                                    if(situacao[1]==2):
                                        escrever(0.04,"\nVoce abriu a porta e levou um soco na cara, \ncaindo em seguida no chao do corredor.\n",0.5)
                                        escrever(0.025,"Voce perdeu 10 pontos de vida...\n\n")
                                        aliado_jogador.status[6]=aliado_jogador.status[6]-10
                                        if(aliado_jogador.status[6]<=0):
                                            aliado_jogador.status[6]=1
                                        situacao[1]=3
                                    else:
                                        if(situacao[1]==3):
                                            escrever(0.04,"\nVoce abriu a porta e viu a mulher de toalha extremamente furiosa \ncom os ombros levemente curvados, deixando a mostra seus bracos musculosos e gigantescos.\n\n",0.5)
                                            escrever(0.015," - VOCE VAI APANHAR MUITO AGORA!\n")
                                            batalha(mulher_toalha)
                                            if(aliado_jogador.status[6]<=0):break
                                            if(adversario_inimigo.status[6]>0):
                                                escrever(0.02,"\n - E NAO VOLTE MAIS AQUI!\n")
                                            else:
                                                escrever(0.03,"\nA mulher caiu inconsciente no chao...\n")
                                                escrever(0.02,"Dentro da casa voce encontrou 100 reais e um suplemento alimenticio\nVoce guardou ambos na mochila!\n\n")
                                                aliado_jogador.dinheiro=aliado_jogador.dinheiro+100
                                                quantidade_adicionada=1
                                                item_adicionado=suplemento_alimenticio[0]
                                                adicionaItem()
                                                situacao[1]=4
                                        else:
                                            if(situacao[1]==4):
                                                escrever(0.02,"\nVoce entra no quarto, encontra a mulher que voce derrotou caida no chao \ne mais nada alem dos moveis velhos dela.\n\n")
                        else:
                            if(acao_do_personagem=="12"):
                                escrever(0.02,"\nVoce bateu na porta...\n - Ja vai! - exclama uma senhora de dentro da casa.\n\n")
                                escrever(1,"...\n\n")
                                escrever(0.1," - Ola, meu jovem!")
                                escrever(0.08," Por que voce nao entra e prova um pouco \ndo bolo que eu acabei de fazer?\n\n")
                                while 1:
                                    escrever(0.02,"Vai entrar e comer um pedaco de bolo?")
                                    print(" (sim ou nao)")
                                    acao_do_personagem=raw_input('-')
                                    acao_do_personagem=acao_do_personagem.lower()
                                    os.system('cls')
                                    if "n" in acao_do_personagem and not "s" in acao_do_personagem:
                                        escrever(0.02,"Voce recusou o convite...")
                                        escrever(0.08," "*15+"\n - Volte quando estiver com fome, meu jovem!")
                                        break
                                    if "s" in acao_do_personagem and not "n" in acao_do_personagem:
                                        print("\n           (  (\n    ( (     )  )\n     ) )            ) )\n        _.-------._( (\n     .-` %*%*%*%*% `-.\n     |`-._________.-`|\n     |~ `~~~~~~~~~`.:|\n     | ~`~~~~~~~~~`.:|\n  _..|. `~~~~~~~~~`.:|.._\n.`    `-.________..-`    `.\n `-.___________________.-`\n     `----------------`\n")
                                        escrever(0.25,"............".center(79)+"\n\n")
                                        os.system('cls')
                                        escrever(0.02,"\n"+"Voce recurperou TODOS os seus pontos de vida!".center(79)+"\n")
                                        aliado_jogador.status[6]=aliado_jogador.status[5]
                                        break
                                    else:print("Entrada Invalida!")
                            else:
                                if(acao_do_personagem=="14"):
                                    if(objeto[4]=="sim"):
                                        escrever(0.02,"\nSuma daqui seu idiota... Deixe-a em paz...\n")
                                    else:
                                        if(objeto[0]=="sim" or objeto[0]=="pegou o dinheiro"):
                                            escrever(0.02,"\nVoce bateu na porta... E escuta passos se aproximarem de dentro...\n\n")
                                            escrever(0.035," - O que voce quer? -")
                                            escrever(0.02,"questionou a mulher que abrira a porta aos prantos\n")
                                            escrever(0.5,"...")
                                            escrever(0.03,"Ela observa o corpo do marido no chao do corredor...\n\n")
                                            escrever(0.02," - F",0.5)
                                            escrever(0.02,"-F")
                                            escrever(0.009,"oi voce?!...\n\n")
                                            escrever(0.5,"...\n\n")
                                            escrever(0.02," - VOCE VAI PAGAR CARO POR MATAR MEU MARIDO!\n")
                                            batalha(mulher_prantos)
                                            if(aliado_jogador.status[6]<=0):break
                                            if(adversario_inimigo.status[6]>0):
                                                escrever(0.02,"\n - CHEGA!\n")
                                                escrever(0.06," - Voce matou meu marido...\n")
                                                escrever(0.015," - Como voce teve a pachorra de me procurar?!\n")
                                                escrever(0.02,"Ela fechou a porta chorando.\n")
                                            else:
                                                escrever(0.02,"\nA mulher caiu inconsciente no chao...\nDentro da casa voce encontrou um par de talheres de prata...\nVoce os guardou na mochila...")
                                                escrever(1,"...")
                                                escrever(0.05,"Seu idiota...\n")
                                                quantidade_adicionada=1
                                                item_adicionado=talheres_prata
                                                adicionaItem()
                                                objeto[4]="sim"
                                        else:
                                            escrever(0.02,"\nVoce bateu na porta...\n",1)
                                            escrever(0.02," - JA DISSE PARA VOCE IR EMBORA SEU BEBADO! - ",0.1)
                                            escrever(0.03,"grita uma mulher de dentro.\n",0.1)
                                            escrever(0.02," - NINGUEM TE MERECE COMO MARIDO!\n")
                                else:
                                    if(acao_do_personagem=="13"):
                                        escrever(0.02,"\nVoce e bobo?\n")
                                        escrever(0.02,"Esse e o seu quarto!\n",0.5)
                                        escrever(0.02,"Voce esta atrasado demais para voltar!\n")
                                    else:
                                        if(acao_do_personagem=="arrombar a porta do quarto 10" or acao_do_personagem=="arrombar 10" or acao_do_personagem=="arrombar quarto 10" or acao_do_personagem=="arrombar o quarto 10" or acao_do_personagem=="arrombar" or acao_do_personagem=="arrombar a porta" or acao_do_personagem=="quarto 10" or acao_do_personagem=="entrar no quarto 10"):
                                            if(objeto[3]=="sim"):
                                                escrever(0.02,"\nVoce ja arrombou essa porta... \nNao ha mais nada de interessante dentro do quarto.\n")
                                            else:
                                                escrever(0.02,"\nVoce entrou no quarto e encontrou uma Jaqueta de Couro!\n",1)
                                                escrever(0.02,"Voce a guardou na mochila!\n")
                                                item_adicionado=jaqueta_imitacao
                                                quantidade_adicionada=1
                                                adicionaItem()
                                                objeto[3]="sim"
                                        else:
                                            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                                                escrever(0.02,"\nVoce subiu para o segundo andar, \nla voce encontrou mais cinco quartos e outra escada ascendente.\n",1)
                                                seuPredioSegundoAndar()
                                                if(aliado_jogador.status[6]<=0):break
                                            else:
                                                if(acao_do_personagem=="olhar o bebado"  or acao_do_personagem=="bebado"  or acao_do_personagem=="bebado" or acao_do_personagem=="olhar bebado" or acao_do_personagem=="olha o bebado" or acao_do_personagem=="olha bebado" or acao_do_personagem=="olhar o bebado" or acao_do_personagem=="olhar bebado" or acao_do_personagem=="olha o bebado" or acao_do_personagem=="olha bebado"):
                                                    if objeto[0]!="pegou o dinheiro" and objeto[0]!='sim':
                                                        objeto[0]="1"
                                                        escrever(0.02,"\nVoce ve um homem de 40 anos, coberto por cacos de vidro, bebida e vomito, \ndormindo no chao.\n")
                                                    else: print ('\nVoce ve um bebado morto.\n')
                                                else:
                                                    if(acao_do_personagem=="revistar o bebado" or acao_do_personagem=="revistar bebado" or acao_do_personagem=="revistar" or acao_do_personagem=="revista bebado" or acao_do_personagem=="revista o bebado" or acao_do_personagem=="revistar o bebado" or acao_do_personagem=="revistar bebado" or acao_do_personagem=="revistar" or acao_do_personagem=="revista bebado" or acao_do_personagem=="revista o bebado"):
                                                        if(objeto[2]=="nao"):
                                                            escrever(0.02,"\nVoce achou um energetico e o guardou na mochila!\n")
                                                            item_adicionado=lata_energetico[0]
                                                            quantidade_adicionada=1
                                                            adicionaItem()
                                                            objeto[2]="sim"
                                                        else:
                                                            escrever(0.02,"\nVoce nao encontrou mais nada...\n")
                                                    else:
                                                        if(acao_do_personagem=="acordar o bebado" or acao_do_personagem=="acordar" or acao_do_personagem=="acordar bebado" or acao_do_personagem=="acorda o bebado" or acao_do_personagem=="acorda bebado" or acao_do_personagem=="acordar o bebado" or acao_do_personagem=="acordar bebado" or acao_do_personagem=="acorda o bebado" or acao_do_personagem=="acorda bebado"):
                                                            if objeto[0]!="pegou o dinheiro" and objeto[0]!='sim':
                                                                objeto[0]="2"
                                                            escrever(0.02,"\nVoce tenta acordar o bebado,",0.5)
                                                            escrever(0.02," mas nao consegue...\n")
                                                        else:
                                                            if(acao_do_personagem=="mover o bebado" or acao_do_personagem=="mover bebado" or acao_do_personagem=="move o bebado" or acao_do_personagem=="move bebado" or acao_do_personagem=="mover o bebado" or acao_do_personagem=="mover bebado" or acao_do_personagem=="move o bebado" or acao_do_personagem=="move bebado" or acao_do_personagem=="mover" or acao_do_personagem=="move"):
                                                                if objeto[0]!="pegou o dinheiro" and objeto[0]!='sim':
                                                                    objeto[0]="3"
                                                                    escrever(0.035,"\nVoce pensa em mover o bebado...\n",0.5)
                                                                    escrever(0.02,"Mas o cheiro e a sujeira fazem voce vomitar em cima dele!\n",1)
                                                                    escrever(1,"...\n",1)
                                                                    escrever(0.02,"Ele continua dormindo...\n")
                                                                else: escrever(0.02,'\nAO MENOS RESPEITE OS QUE ESTAO MORTOS!\nDeixe-o descansar em paz...\n')
                                                            else:
                                                                if(acao_do_personagem=="atacar o bebado" or acao_do_personagem=="atacar bebado" or acao_do_personagem=="ataca o bebado" or acao_do_personagem=="ataca bebado" or acao_do_personagem=="atacar o bebado" or acao_do_personagem=="atacar bebado" or acao_do_personagem=="ataca o bebado" or acao_do_personagem=="ataca bebado" or acao_do_personagem=="atacar" or acao_do_personagem=="ataca"):
                                                                    if objeto[0]!="pegou o dinheiro" and objeto[0]!="sim":
                                                                        escrever(0.02,"\nVoce chuta varias vezes o bebado violentamente!\n")
                                                                        raw_input("(Aperte Enter)")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("(Pronto, voce chutou o suficiente!)")
                                                                        escrever(0.02," - P",0.1)
                                                                        escrever(0.02,"-PARA!",0.1)
                                                                        escrever(0.009," PARA! PARA! -")
                                                                        escrever(0.03," berra o bebado que acabou de acordar.",1)
                                                                        escrever(0.02,"Ele se levanta e te empurra ganhando distancia.",1)
                                                                        escrever(0.3,"...")
                                                                        escrever(0.009," - Ss",0.1)
                                                                        escrever(0.02,"seu muleque i-",0.5)
                                                                        escrever(0.03,"ins",0.3)
                                                                        escrever(0.008,"strosmestido!...",1)
                                                                        escrever(0.02," *hic*\n",0.5)
                                                                        batalha(bebado_inimigo)
                                                                        if(aliado_jogador.status[6]<=0):break
                                                                        if(adversario_inimigo.status[6]>0):
                                                                            escrever(0.02,"\nVoce escapa da briga, mas em seguida o bebado tosse sangue e cai no chao...\n")
                                                                        else:
                                                                            escrever(0.03,"\nO bebado coberto de bebida, vomito e sangue, cai de costas no chao,\nsendo empalado pelos diversos cacos de vidro...\n",0.5)
                                                                            escrever(0.04,"O sangue dele escorre pelo corredor ate os seus pes...\n",1)
                                                                            escrever(0.03,"Voce se afasta e vira o rosto fechando os olhos e abaixando os punhos...\n",2)
                                                                            escrever(0.015,"Agora, desencostado da porta dos fundos, o bebado ja nao e mais um impecilio...\n")
                                                                        objeto[0]="sim"
                                                                    else: escrever(0.02,'\nEle ja esta morto!\n')
                                                                else:
                                                                    if(acao_do_personagem=="abrir a porta dos fundos" or acao_do_personagem=="abrir porta dos fundos" or acao_do_personagem=="abrir porta do fundos" or acao_do_personagem=="abrir porta dos fundo" or acao_do_personagem=="abrir" or acao_do_personagem=="abrir porta do fundo" or acao_do_personagem=="abrir a porta" or acao_do_personagem=="abrir porta"):
                                                                        if(objeto[0]=="sim"):
                                                                            escrever(0.02,"\nVoce abre a porta... ",1)
                                                                            escrever(0.02,"E um armario de limpeza.\nEm meio as vassouras, rodos e outras coisas, voce encontra uma mala...\n",2)
                                                                            escrever(0.02,"Voce abre a mala e encontra, entre os materiais de escritorio, 10 Reais!\n")
                                                                            escrever(1,"...\n")
                                                                            escrever(0.02,"Voce tambem achou um lapis apontado e o guardou na mochila!\n")
                                                                            item_adicionado=equipamento_inicial[2]
                                                                            quantidade_adicionada=1
                                                                            adicionaItem()
                                                                            objeto[0]="pegou o dinheiro"
                                                                            aliado_jogador.dinheiro=aliado_jogador.dinheiro+10
                                                                        else:
                                                                            if(objeto[0]=="pegou o dinheiro"):
                                                                                escrever(0.02,"\nVoce ve materiais de limpesa e uma mala aberta.\n")
                                                                            else:
                                                                                escrever(0.01,"\nNao da para abrir!\n")
                                                                    else:
                                                                        if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                                                                            if(ponto_de_save==1):
                                                                                while 1:
                                                                                    escrever(0.03,"\nDo lado de fora ha um oponente MUITO forte.\nTem certeza que esta pronto para sair?")
                                                                                    print(" (sim ou nao)")
                                                                                    acao_do_personagem=raw_input("-")
                                                                                    acao_do_personagem=acao_do_personagem.lower()
                                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                                        acao_do_personagem="sim"
                                                                                        break
                                                                                    else:
                                                                                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                                            escrever(0.02,"\nVoce decidiu nao sair do predio.\n")
                                                                                            break
                                                                                        else:
                                                                                            print("Entrada invalida!")
                                                                                if(acao_do_personagem=="sim"):
                                                                                    escrever(0.02,"\nVoce desceu as escadas e saiu do predio...\n")
                                                                                    break
                                                                            else:
                                                                                escrever(0.02,"\nVoce desceu as escadas e saiu do predio...\n")
                                                                                variavel_lugar = "sua rua"
                                                                                suaRua()
                                                                                break
                                                                        else:
                                                                            if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                                                                save()
                                                                            else:
                                                                                if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                                                    inventarioPersonagem()
                                                                                else:
                                                                                    print('\nEntrada Invalida!\n')

#--Sua Rua--#
def suaRua():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        if(aliado_jogador.status[6]<=0):break
        print("\n#", "-"*30,"#\n", "\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\nolhar\n")
        print("\nentrar na loja\n\nentrar na pizzaria\n")
        print("\nentrar no predio\n\nver ficha do personagem\nver mochila\n\npegar onibus\nir a pe\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        print("\nQual sera a sua atitude, "+str(aliado_jogador.nome)+"?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                save()
            else:
                if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                    inventarioPersonagem()
                else:
                    if(acao_do_personagem=="entrar na loja" or acao_do_personagem=="loja" or acao_do_personagem=="entrar loja" or acao_do_personagem=="entrar a loja" or acao_do_personagem=="entra na loja" or acao_do_personagem=="lloja" or acao_do_personagem=="entra loja" or acao_do_personagem=="entra a loja" or acao_do_personagem=="etrar na loja" or acao_do_personagem=="lojja" or acao_do_personagem=="etrar loja" or acao_do_personagem=="etrar a loja" or acao_do_personagem=="etra na loja" or acao_do_personagem=="llojja" or acao_do_personagem=="etra loja" or acao_do_personagem=="etra a loja"):
                        while 2:
                            print("\nVai comprar, vender ou sair?")
                            acao_do_personagem=raw_input("-")
                            acao_do_personagem=acao_do_personagem.lower()
                            if(acao_do_personagem=="comprar"):
                                porcentagem_inflacao=1
                                Venda.inventario[1][0]=bermuda_linho[0]
                                Venda.inventario[1][1]=bermuda_linho[1]
                                Venda.inventario[1][2]=calca_jeans[0]
                                Venda.inventario[1][3]=calca_jeans[1]
                                Venda.inventario[1][4]=luva_luva[0]
                                Venda.inventario[1][5]=luva_luva[1]
                                Venda.inventario[1][6]=papetes_masculinas
                                Venda.inventario[1][7]=tenis_calcado[0]
                                Venda.inventario[1][8]=equipamento_inicial[4]
                                Venda.inventario[1][9]=sapato_simplorio
                                Venda.inventario[1][10]=tenis_calcado[1]
                                lojaComprar()
                                Venda=Reserva_Venda
                            else:
                                if(acao_do_personagem=="vender"):
                                    porcentagem_inflacao=0.5
                                    lojaVender()
                                else:
                                    if(acao_do_personagem=="sair"):
                                        print("\nVoce saiu da loja.\n")
                                        time.sleep(1)
                                        break
                                    else:
                                        print('\nEntrada Invalida!\n')
                                        time.sleep(0.5)
                    else:
                        if(acao_do_personagem=="entrar na pizzaria" or acao_do_personagem=="pizzaria" or acao_do_personagem=="entrar pizzaria" or acao_do_personagem=="entrar a pizzaria" or acao_do_personagem=="entrar na pizaria" or acao_do_personagem=="pizaria" or acao_do_personagem=="entrar pizaria" or acao_do_personagem=="entrar a pizaria" or acao_do_personagem=="entrar na pizza" or acao_do_personagem=="pizza" or acao_do_personagem=="entrar pizza" or acao_do_personagem=="entrar a pizza" or acao_do_personagem=="entrar na piza" or acao_do_personagem=="piza" or acao_do_personagem=="entrar piza" or acao_do_personagem=="entrar a piza" or acao_do_personagem=="entra na pizzaria" or acao_do_personagem=="comer pizzaria" or acao_do_personagem=="entra pizzaria" or acao_do_personagem=="entra a pizzaria" or acao_do_personagem=="entra na pizaria" or acao_do_personagem=="comer pizaria" or acao_do_personagem=="entra pizaria" or acao_do_personagem=="entra a pizaria" or acao_do_personagem=="entra na pizza" or acao_do_personagem=="comer pizza" or acao_do_personagem=="entra pizza" or acao_do_personagem=="entra a pizza" or acao_do_personagem=="entra na piza" or acao_do_personagem=="comer piza" or acao_do_personagem=="entra piza" or acao_do_personagem=="entra a piza" or acao_do_personagem=="etrar na pizzaria" or acao_do_personagem=="ppizzaria" or acao_do_personagem=="etrar pizzaria" or acao_do_personagem=="etrar a pizzaria" or acao_do_personagem=="etrar na pizaria" or acao_do_personagem=="ppizaria" or acao_do_personagem=="etrar pizaria" or acao_do_personagem=="etrar a pizaria" or acao_do_personagem=="etrar na pizza" or acao_do_personagem=="ppizza" or acao_do_personagem=="etrar pizza" or acao_do_personagem=="etrar a pizza" or acao_do_personagem=="etrar na piza" or acao_do_personagem=="ppiza" or acao_do_personagem=="etrar piza" or acao_do_personagem=="etrar a piza" or acao_do_personagem=="etra na pizzaria" or acao_do_personagem=="come pizzaria" or acao_do_personagem=="etra pizzaria" or acao_do_personagem=="etra a pizzaria" or acao_do_personagem=="etra na pizaria" or acao_do_personagem=="come pizaria" or acao_do_personagem=="etra pizaria" or acao_do_personagem=="etra a pizaria" or acao_do_personagem=="etra na pizza" or acao_do_personagem=="come pizza" or acao_do_personagem=="etra pizza" or acao_do_personagem=="etra a pizza" or acao_do_personagem=="etra na piza" or acao_do_personagem=="come piza" or acao_do_personagem=="etra piza" or acao_do_personagem=="etra a piza"):
                            porcentagem_inflacao=1.5
                            Venda.inventario[1][2]=pizza_inteira[0]
                            Venda.inventario[1][1]=pedaco_pizza[0]
                            Venda.inventario[1][0]=talheres_prata
                            lojaComprar()
                            Venda=Reserva_Venda
                            print("\nVoce saiu da pizzaria.\n")
                            time.sleep(1)
                            break
                        else:
                            if(acao_do_personagem=="entrar no predio" or acao_do_personagem=="predio" or acao_do_personagem=="entrar predio" or acao_do_personagem=="entrar o predio" or acao_do_personagem=="entra no predio" or acao_do_personagem=="ppredio" or acao_do_personagem=="entra predio" or acao_do_personagem=="entra o predio" or acao_do_personagem=="etrar no predio" or acao_do_personagem=="predio" or acao_do_personagem=="etrar predio" or acao_do_personagem=="etrar o predio" or acao_do_personagem=="etra no predio" or acao_do_personagem=="entrar no predio" or acao_do_personagem=="etra predio" or acao_do_personagem=="etra o predio"):
                                variavel_lugar = "seu predio, 1o andar"
                                seuPredioPrimeiroAndar()
                            else:
                                if acao_do_personagem == "olhar" or acao_do_personagem=="olh" or acao_do_personagem == "ver" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha" or acao_do_personagem == "olhar quarto" or acao_do_personagem == "olha quarto" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha o quarto" or acao_do_personagem == "ve" or acao_do_personagem == "ve" :
                                    print("Voce ve uma rua com uma pizzaria de familia, \numa loja e predios de classe baixa,")
                                    time.sleep(2)
                                    print("poucas pessoas passando com cara de cansadas,")
                                    time.sleep(2)
                                    print("mas voce nao consegue ver o horizonte,")
                                    time.sleep(2)
                                    print("ja que os predios da rua sao altos e proximos demais uns dos outros.")
                                    time.sleep(2)
                                    print("Numa das duas esquinas ha um ponto de onibus, mas ambas terminam \ndobrando, limitando mais ainda o horizonte. ")
                                    time.sleep(3)
                                    print ("...")
                                    time.sleep(1.5)
                                    print ("Da a sensacao de morar numa caixa de sapatos suja!")
                                    time.sleep(2)
                                else:
                                    if acao_do_personagem=="pegar onibus" or acao_do_personagem=="onibus" or acao_do_personagem=="ir onibus" or acao_do_personagem=="ir de onibus" :
                                        print ('A passagem custa 5 Reais.')
                                        time.sleep(1.5)
                                        if aliado_jogador.dinheiro>=5:
                                            while 5:
                                                print ('Voce ira de onibus? (sim ou nao)')
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem=acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    if(ponto_de_save==3):
                                                        for i in range(3):
                                                            print ('.',)
                                                            time.sleep(2)
                                                        print (' O onibus chegou!!!')
                                                        time.sleep(2)
                                                        break
                                                else:
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        break
                                                    else:
                                                        print ('Nao entendi...')
                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"): break
                                    else:
                                        if acao_do_personagem=='ir a pe' or acao_do_personagem=='ir pe' or acao_do_personagem=='ir andando' or acao_do_personagem=='sair' or acao_do_personagem=='ir pra escola' or acao_do_personagem=='ir a escola' or acao_do_personagem=='ir para a escola' or acao_do_personagem=='ir a aula' or acao_do_personagem=='ir para a aula' or acao_do_personagem=='ir pra aula' or acao_do_personagem=='ir pra fatec' or acao_do_personagem=='ir para a fatec' or acao_do_personagem=='ir a fatec' or acao_do_personagem=='fatec' or acao_do_personagem=='ir pra facul' or acao_do_personagem=='ir para a faculdade' or acao_do_personagem=='ir pra faculdade' or acao_do_personagem=='ir a faculdade' or acao_do_personagem=='ir para faculdade' or acao_do_personagem=='pe' or acao_do_personagem=='ir para a proxima rua' or acao_do_personagem=='andando' or acao_do_personagem=='ir caminhando' or acao_do_personagem=='caminhando':
                                            while 9:
                                                print ('Voce ira a pe? (sim ou nao)')
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem=acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    if(ponto_de_save==3):
                                                        ruasPerigosas(10,1)
                                                        break
                                                else:
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        break
                                                    else:
                                                        print ('Nao entendi...')
                                        else:
                                            print('\nEntrada Invalida!\n')
                                            time.sleep(0.5)


#--Sua Faculdade--#
def suaFaculdade():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas


#--Rua da Faculdade--#
def ruaFaculdade():
    global narrador_inimigo, bebado_inimigo, mulher_prantos, mulher_toalha, mane_bone, senhor_doente, garoto_oponente, gangue_comparsa, arruaceiro_oponente, estudante_brigento, aliado_headbanger,Venda, Reserva_Venda,porcentagem_inflacao,bermuda_linho,calca_jeans,desequipado,pedaco_pizza, pizza_inteira,bolo_chocolate,equipamento_inicial,malha_ninja,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,soco_ingles,luva_luva,anel_magico,anel_da_imortalidade,anel_da_divindade,papetes_masculinas,tenis_calcado,sapato_simplorio,item_adicionado,quantidade_adicionada,variavel_cenario,objeto,situacao,booleana,variavel_lugar,ponto_de_save,mostrar_save, aliado_jogador,aliado_reserva, aliado_garota,adversario_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas
    while 1:
        if(aliado_jogador.status[6]<=0):break
        print("\n#", "-"*30,"#\n", "\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\nbrigar\n")
        print("\nentrar na lanchonete\n")
        if ponto_de_save==4: print("\nver ficha do personagem\nver mochila\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        else: print("\nentrar na faculdade\n\nver ficha do personagem\nver mochila\n\npegar onibus\nir a pe\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        print("\n"+str(aliado_jogador.nome)+", o que pretende fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        os.system("cls")
        if(acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
            raw_input('|>')
            os.system('cls')
        else:
            if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                save()
            else:
                if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                    inventarioPersonagem()
                else:
                    if "fac" in acao_do_personagem or "fatec" in acao_do_personagem or "universidade" in acao_do_personagem:
                        variavel_lugar = "sua faculdade"
                        suaFaculdade()
                    else:
                        if "lanch" in acao_do_personagem or "boteco" in acao_do_personagem or "bar" in acao_do_personagem or "lanx" in acao_do_personagem or "vida" in acao_do_personagem or "recup" in acao_do_personagem or "saud" in acao_do_personagem or "piz" in acao_do_personagem or "com" in acao_do_personagem or "cantina" in acao_do_personagem:
                            porcentagem_inflacao=1.5
                            L=0
                            while L<6:
                                Venda.inventario[1][L]=lanches_cantina[L]
                                L+=1
                            lojaComprar()
                            Venda=Reserva_Venda
                            print("\nVoce saiu da lanchonete.\n")
                            time.sleep(1)
                            break
                        else:
                            if "bri" in acao_do_personagem or "brg" in acao_do_personagem or "lut" in acao_do_personagem or "bgar" in acao_do_personagem or "bate" in acao_do_personagem or "invest" in acao_do_personagem:
                                teste_de_sorte=random.randrange(100)
                                if(teste_de_sorte<5): batalha(estudante_brigento[1])
                                elif(teste_de_sorte<10): batalha(estudante_brigento[2])
                                elif(teste_de_sorte<15): batalha(estudante_brigento[3])
                                elif(teste_de_sorte<20): batalha(estudante_brigento[4])
                                elif(teste_de_sorte<25):
                                    batalha(estudante_brigento[5])
                                    if booleana[5] == False:
                                        if(aliado_jogador.status[6]<=0):break
                                        print ('Depois de derrubar o oponente, voce o interrogou...')
                                        time.sleep(2)
                                        print (' - Provavelmente e um dos servicos do Olhos de Sangue...\n...')
                                        time.sleep(1)
                                        print (' - Voce parece muito com ele! Muito mesmo!\n...?')
                                        time.sleep(1)
                                        print (' - Fico grato por voce nao ser ele! ... Nao quero mais falar disso!\n!!!')
                                        time.sleep(1)
                                        print (' - Por que os estudante estao agressivos??? Voce é mesmo um alienado!\nForam os bandidos eles estao nos obrigando a fazer servicos!\n...')
                                        time.sleep(1.5)
                                        print (' - ... Do contrario eles nos matam!\n...')
                                        time.sleep(1.5)
                                        print (' - Me deixe ir antes que eles percebam, por favor!')
                                        time.sleep(1)
                                        booleana[5] = True
                                        print ('Voce tem toda a informacao que poderia conseguir aqui!\nProcurar mais dentro da faculdade parece uma boa ideia...')
                                        break
                                elif(teste_de_sorte<30): batalha(arruaceiro_oponente[1])
                                elif(teste_de_sorte<35): batalha(arruaceiro_oponente[2])
                                elif(teste_de_sorte<40): batalha(arruaceiro_oponente[3])
                                elif(teste_de_sorte<45): batalha(arruaceiro_oponente[3])
                                elif(teste_de_sorte<50): batalha(arruaceiro_oponente[4])
                                elif(teste_de_sorte<55): batalha(arruaceiro_oponente[4])
                                elif(teste_de_sorte<60): batalha(arruaceiro_oponente[5])
                                elif(teste_de_sorte<70): batalha(arruaceiro_oponente[5])
                                elif(teste_de_sorte<80): batalha(arruaceiro_oponente[6])
                                elif(teste_de_sorte<90): batalha(arruaceiro_oponente[7])
                                elif(teste_de_sorte<100): batalha(estudante_brigento[8])
                                if(aliado_jogador.status[6]<=0):break
                                if booleana[5] == False:
                                    print ('Depois de derrubar o oponente, voce o interrogou...')
                                    time.sleep(2)
                                    teste_de_sorte=random.randrange(100)
                                    if teste_de_sorte<20: print(' - Pare! Nao sei de nada disso!')
                                    elif teste_de_sorte<40: print(' - Esquema? Eu realmente nao sei!')
                                    elif teste_de_sorte<60: print(' - Bandidos?! Cara nao quero saber disso!')
                                    elif teste_de_sorte<80: print(' - Por favor, me deixe em paz, eu nao sei!')
                                    elif teste_de_sorte<100: print(' - Nao me interessa seus assuntos, suma!')
                            else:
                                if acao_do_personagem=="pegar onibus" or acao_do_personagem=="onibus" or acao_do_personagem=="ir onibus" or acao_do_personagem=="ir de onibus" :
                                    if ponto_de_save==4: print ('Voce nao pode voltar, investigue mais por aqui!')
                                    else:
                                        print ('A passagem custa 5 Reais.')
                                        time.sleep(1.5)
                                        if aliado_jogador.dinheiro>=5:
                                            while 5:
                                                print ('Voce ira de onibus? (sim ou nao)')
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem=acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    break#evento de viagem
                                                else:
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        break
                                                    else:
                                                        print ('Nao entendi...')
                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"): break
                                else:
                                    if acao_do_personagem=='ir a pe' or acao_do_personagem=='ir pe' or acao_do_personagem=='ir andando' or acao_do_personagem=='sair' or acao_do_personagem=='ir pra escola' or acao_do_personagem=='ir a escola' or acao_do_personagem=='ir para a escola' or acao_do_personagem=='ir a aula' or acao_do_personagem=='ir para a aula' or acao_do_personagem=='ir pra aula' or acao_do_personagem=='ir pra fatec' or acao_do_personagem=='ir para a fatec' or acao_do_personagem=='ir a fatec' or acao_do_personagem=='fatec' or acao_do_personagem=='ir pra facul' or acao_do_personagem=='ir para a faculdade' or acao_do_personagem=='ir pra faculdade' or acao_do_personagem=='ir a faculdade' or acao_do_personagem=='ir para faculdade' or acao_do_personagem=='pe' or acao_do_personagem=='ir para a proxima rua' or acao_do_personagem=='andando' or acao_do_personagem=='ir caminhando' or acao_do_personagem=='caminhando':
                                        if ponto_de_save==4: print ('Voce nao pode voltar, investigue mais por aqui!')
                                        else:
                                            while 9:
                                                print ('Voce ira a pe? (sim ou nao)')
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem=acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    if(ponto_de_save==3):
                                                        ruasPerigosas(10,1)
                                                        break
                                                else:
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        break
                                                    else:
                                                        print ('Nao entendi...')
                                    else:
                                        print('\nEntrada Invalida!\n')
    


#####################----------------------------__BRIGA DE ESTUDANTE__----------------------------#####################
while 1:
    while (aliado_jogador.status[6]>0):
        print('''   _________________________________________________________________________  
 |\ _______________________________________________________________________ /|
 | |                                                                       | | 
 | |  ===================================================================  | |
 | |  = * = * = * = * = * = * = * = * *=* * = * = * = * = * = * = * = * =  | |
 | |  = = =================== : --------------- : =================== = =  | | 
 | |  = * - - - - - - - - - - : =============== : - - - - - - - - - - * =  | | 
 | |  = = = - === - ======================================= - === - = = =  | |
 | |  = * ==== - ================== ** = ** ================== - ==== * =  | | 
 | |  = = -==-==-==-==-==-===                     ===-==-==-==-==-==- = =  | | 
 | |  = * ==-==-==-==-==-===       B R I G A       ===-==-==-==-==-== * =  | | 
 | |  = = -==-==-==-==-==-=           D E           =-==-==-==-==-==- = =  | | 
 | |  = * ==-==-==-==-==-===   E S T U D A N T E   ===-==-==-==-==-== * =  | |
 | |  = = -==-==-==-==-==-===                     ===-==-==-==-==-==- = =  | | 
 | |  = * ==== - ================== ** = ** ================== - ==== * =  | | 
 | |  = = = - === - ======================================= - === - = = =  | |
 | |  = * - - - - - - - - - - : =============== : - - - - - - - - - - * =  | | 
 | |  = = =================== : --------------- : =================== = =  | | 
 | |  = * = * = * = * = * = * = * = * =*= * = * = * = * = * = * = * = * =  | |
 | |  ================================ por: Fernando Luiz Neme Chibli ===  | | 
 | |_______________________________________________________________________| | 
 |/_________________________________________________________________________\|
''')
        while 1:
            print('Digite "comecar", "continuar" ou "criar/zerar saves":')
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem =="comecar" or acao_do_personagem == "mecar" or acao_do_personagem == "come" or acao_do_personagem =="iniciar" or acao_do_personagem =="inicia" or acao_do_personagem =="inici" or acao_do_personagem =="inicio" or acao_do_personagem =="inicio" or acao_do_personagem =="new game" or acao_do_personagem =="start new game" or acao_do_personagem =="start" or acao_do_personagem =="start game" or acao_do_personagem =="comecar" or acao_do_personagem =="comeca" or acao_do_personagem =="comeca" or acao_do_personagem =="com" or acao_do_personagem =="cmecar" or acao_do_personagem =="cmecar" or acao_do_personagem =="comcar" or acao_do_personagem =="comcar" or acao_do_personagem =="comear" or acao_do_personagem =="comer" or acao_do_personagem =="cocar" or acao_do_personagem =="ccar" or acao_do_personagem =="cmcr" or acao_do_personagem =="cmecr" or acao_do_personagem =="cocar" or acao_do_personagem =="ccar" or acao_do_personagem =="cmcr" or acao_do_personagem =="cmecr" or acao_do_personagem =="cumessa" or acao_do_personagem =="comessa" or acao_do_personagem =="comessar"): break
            else:
                os.system("cls")
                if (acao_do_personagem == "continuar" or acao_do_personagem == "ccontinuar" or acao_do_personagem == "continuarr" or acao_do_personagem == "conntinuar" or acao_do_personagem == "conttinuar" or acao_do_personagem == "continnuar" or acao_do_personagem == "ccontinuarr" or acao_do_personagem == "cconntinuar" or acao_do_personagem == "cconttinuar" or acao_do_personagem == "ccontinnuar" or acao_do_personagem == "cconnttinuar" or acao_do_personagem == "cconntinnuar" or acao_do_personagem == "cconntinuarr" or acao_do_personagem == "continuart" or acao_do_personagem == "cconttinnuar" or acao_do_personagem == "cconttinuarr" or acao_do_personagem == "cconnttinnuarr" or acao_do_personagem == "cntnr" or acao_do_personagem == "contnr" or acao_do_personagem == "continr" or acao_do_personagem == "continur" or acao_do_personagem == "cntinuar" or acao_do_personagem == "cntnuar" or acao_do_personagem == "cntnar" or acao_do_personagem == "cntinur" or acao_do_personagem == "cntinr" or acao_do_personagem == "cntinar" or acao_do_personagem == "contnur" or acao_do_personagem == "ontinuar" or acao_do_personagem == "cotinuar" or acao_do_personagem == "coninuar" or acao_do_personagem == "contiuar" or acao_do_personagem == "coinar" or acao_do_personagem == "continua" or acao_do_personagem == "cntn" or acao_do_personagem == "contn" or acao_do_personagem == "contin" or acao_do_personagem == "continu" or acao_do_personagem == "cntinua" or acao_do_personagem == "cntnua" or acao_do_personagem == "cntna" or acao_do_personagem == "cntinu" or acao_do_personagem == "cntin" or acao_do_personagem == "cntina" or acao_do_personagem == "contnu" or acao_do_personagem == "ontinua" or acao_do_personagem == "cotinua" or acao_do_personagem == "coninua" or acao_do_personagem == "contiua" or acao_do_personagem == "coina" or acao_do_personagem == "con" or acao_do_personagem == "cont" or acao_do_personagem == "conti" or acao_do_personagem == "ccontin" or acao_do_personagem == "ccontinu"):
                    print("\nDeseja continuar o jogo guardado em qual espaco?\n")
                    time.sleep(1)
                    arq = open('\espaco_save00.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  0:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save01.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  1:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save02.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  2:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save03.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  3:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save04.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  4:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save05.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  5:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save06.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  6:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save07.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  7:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save08.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  8:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    arq = open('\espaco_save09.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  9:     Lugar: "+str(mostrar_save[2])+"\n          Nome: "+str(mostrar_save[0])+"  Vida: "+str(mostrar_save[1])+"\n          Ataque: "+str(mostrar_save[3])+"  Defesa: "+str(mostrar_save[4])+"  Agilidade: "+str(mostrar_save[5])+"  Sorte: "+str(mostrar_save[6]))
                    arq.close
                    while 1:
                        print("\n(Digite um numero entre 0 e 9)")
                        acao_do_personagem=raw_input("-")
                        if(acao_do_personagem=="0"):
                            arq = open('\espaco_save00.py', 'rb')
                            break
                        else:
                            if(acao_do_personagem=="1"):
                                arq = open('\espaco_save01.py', 'rb')
                                break
                            else:
                                if(acao_do_personagem=="2"):
                                    arq = open('\espaco_save02.py', 'rb')
                                    break
                                else:
                                    if(acao_do_personagem=="3"):
                                        arq = open('\espaco_save03.py', 'rb')
                                        break
                                    else:
                                        if(acao_do_personagem=="4"):
                                            arq = open('\espaco_save04.py', 'rb')
                                            break
                                        else:
                                            if(acao_do_personagem=="5"):
                                                arq = open('\espaco_save05.py', 'rb')
                                                break
                                            else:
                                                if(acao_do_personagem=="6"):
                                                    arq = open('\espaco_save06.py', 'rb')
                                                    break
                                                else:
                                                    if(acao_do_personagem=="7"):
                                                        arq = open('\espaco_save07.py', 'rb')
                                                        break
                                                    else:
                                                        if(acao_do_personagem=="8"):
                                                            arq = open('\espaco_save08.py', 'rb')
                                                            break
                                                        else:
                                                            if(acao_do_personagem=="9"):
                                                                arq = open('\espaco_save09.py', 'rb')
                                                                break
                                                            else:
                                                                escrever(0,"Entrada invalida!\n",0.5)
                    mostrar_save = pickle.load(arq)
                    variavel_cenario = pickle.load(arq)
                    objeto = pickle.load(arq)
                    situacao = pickle.load(arq)
                    booleana = pickle.load(arq)
                    variavel_lugar = pickle.load(arq)
                    ponto_de_save = pickle.load(arq)
                    aliado_jogador = pickle.load(arq)
                    aliado_reserva = pickle.load(arq)
                    aliado_headbanger = pickle.load(arq)
                    aliado_garota = pickle.load(arq)
                    arq.close
                    if(ponto_de_save>0):
                        escrever(0.02,"\nCarregado!\n",1)
                        print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
                        raw_input('|>')
                        os.system('cls')
                    else:
                        escrever(0,"\nERRO: Voce nao possui dados salvos.\n",0.5)
                    break
                else:
                    os.system("cls")
                    if(acao_do_personagem=="limpar" or acao_do_personagem=="zerar" or acao_do_personagem=="limpar saves" or acao_do_personagem=="criar saves" or acao_do_personagem=="zerar saves" or acao_do_personagem=="resetar saves" or acao_do_personagem=="resetar" or acao_do_personagem=="criar/zerar saves"):
                        mostrar_save = [aliado_jogador.nome,aliado_jogador.status[5],variavel_lugar,aliado_jogador.status[0],aliado_jogador.status[1],aliado_jogador.status[2],aliado_jogador.status[3]]
                        i=0
                        while 1:
                            if(i==0):
                                arq = open('\espaco_save00.py', 'wb')
                            if(i==1):
                                arq = open('\espaco_save01.py', 'wb')
                            if(i==2):
                                arq = open('\espaco_save02.py', 'wb')
                            if(i==3):
                                arq = open('\espaco_save03.py', 'wb')
                            if(i==4):
                                arq = open('\espaco_save04.py', 'wb')
                            if(i==5):
                                arq = open('\espaco_save05.py', 'wb')
                            if(i==6):
                                arq = open('\espaco_save06.py', 'wb')
                            if(i==7):
                                arq = open('\espaco_save07.py', 'wb')
                            if(i==8):
                                arq = open('\espaco_save08.py', 'wb')
                            if(i==9):
                                arq = open('\espaco_save09.py', 'wb')
                            if(i==10):
                                arq = open('\espaco_save09.py', 'wb')
                                pickle.dump(mostrar_save, arq)
                                pickle.dump(variavel_cenario, arq)
                                pickle.dump(objeto, arq)
                                pickle.dump(situacao, arq)
                                pickle.dump(booleana, arq)
                                pickle.dump(variavel_lugar, arq)
                                pickle.dump(ponto_de_save, arq)
                                pickle.dump(aliado_jogador, arq)
                                pickle.dump(aliado_reserva, arq)
                                pickle.dump(aliado_headbanger, arq)
                                pickle.dump(aliado_garota, arq)
                                arq.close
                                break
                            pickle.dump(mostrar_save, arq)
                            pickle.dump(variavel_cenario, arq)
                            pickle.dump(objeto, arq)
                            pickle.dump(situacao, arq)
                            pickle.dump(booleana, arq)
                            pickle.dump(variavel_lugar, arq)
                            pickle.dump(ponto_de_save, arq)
                            pickle.dump(aliado_jogador, arq)
                            pickle.dump(aliado_reserva, arq)
                            pickle.dump(aliado_headbanger, arq)
                            pickle.dump(aliado_garota, arq)
                            arq.close
                            escrever(0.02,"Save "+str(i)+" foi criado!\n",0.5)
                            i=i+1
                        if(i==10):break
                    else:
                        print('Entrada invalida!\n')

#-- Primeira parte... TUTORIAL--#
        if(ponto_de_save==0):
            os.system("cls")
            escrever(0.02,"\nIniciando novo jogo...\n",1)
            escrever(0.02,"\nVoce e um homem...",0.5)
            escrever(0.02," Qual e o seu nome?",0.5)
            print(" (maximo 25 caracteres)")
            while 1:
                aliado_jogador.nome = raw_input("-")
                aliado_jogador.nome = aliado_jogador.nome.capitalize()
                if len(str(aliado_jogador.nome))>25: print ('Entrada invalida: digite um nome com 25 caracteres ou menos!')
                elif len(str(aliado_jogador.nome))<1: print ('Entrada invalida: digite um nome com ao menos um caracter!')
                elif '\n' in aliado_jogador.nome: print ('Entrada invalida: nomes nao podem ter quebra de linha.')
                else: break
            while 1:
                escrever(0.02,"\nSeu nome e "+str(aliado_jogador.nome)+ "?\n")
                while 2:
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        break
                    else:
                        if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                            escrever(0.01,"\nEntao qual e o seu nome?\n")
                            while 1:
                                aliado_jogador.nome = raw_input("-")
                                if len(str(aliado_jogador.nome))>25: print ('Entrada invalida: digite um nome com 25 caracteres ou menos!')
                                elif len(str(aliado_jogador.nome))<1: print ('Entrada invalida: digite um nome com ao menos um caracter!')
                                elif '\n' in aliado_jogador.nome: print ('Entrada invalida: nomes nao podem ter quebra de linha.')
                                else: break
                            break
                        else:
                            print('\nEntrada invalida!\n')
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    break
            escrever(0.02,"Muito prazer, "+str(aliado_jogador.nome)+'.\n',2)
            escrever(0.02,'Nos ja nos conhecemos?')
            print (' (digite "nao" para ver o tutorial)')
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            while 1:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    escrever(0.02,'Nao me lembro de voce...',1)
                    escrever(0.02,' Tem certeza de que nos conhecemos???\n')
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):break
                elif(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):break
                else:
                    print('Entrada invalida!')
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
            while 1:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    break
                else:
                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                        os.system("cls")
                        escrever(0.02,'\nPermita-me, entao, me apresentar...\n',0.5)
                        escrever(0.03,'\nSou o narrador da nossa historia,',0.5)
                        escrever(0.03,' vou apenas te guiar de acordo com as suas \ndecisoes...\n',0.5)
                        escrever(0.01,'Entao saiba que nao vou facilitar as coisas para voce!\n',0.5)
                        escrever(0.03,'Porem minha funcao e te guiar,',0.2)
                        escrever(0.02,' ser os seus olhos,',0.2)
                        escrever(0.02,' ouvidos,',0.2)
                        escrever(0.02,' maos e nariz.\n',0.5)
                        escrever(0.02,'\nToda vez te mostrarei uma lista para voce nao se sentir tao deslocado.\n',0.5)
                        escrever(0.02,'Claro, voce pode tentar outras coisas,')
                        escrever(0.07,' mas eu dito as regras aqui.\n',0.5)
                        escrever(0.02,'\nVoce so recebera minha atencao quando eu pedir e\npercebera isso quando ver um hifen apos a minha pergunta.\n',1)
                        escrever(0.02,'\nFui claro?')
                        print(' (sim ou nao)')
                        acao_do_personagem = raw_input("-")
                        acao_do_personagem = acao_do_personagem.lower()
                        while 1:
                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                break
                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                escrever(0.04,'Voce e bobo??\n')
                            else:
                                print('Entrada invalida!')
                            acao_do_personagem = raw_input("-")
                            acao_do_personagem = acao_do_personagem.lower()
                        os.system("cls")
                        escrever(0.02,'\nBom menino!\n',0.5)
                        escrever(0.02,'\nPor vezes a tela se apaga, por isso preste bastante atencao no que voce le.\n',1)
                        escrever(0.02,'\nFalando nisso, ha o "|>"',1.3)
                        escrever(0.02,', que pedira a sua anuencia para apagar a tela.\n',0.2)
                        escrever(0.02,'\nE so mais uma coisa...',0.5)
                        escrever(0.02,' Fique atento as mudancas que causar durante o jogo!\n',1)
                        escrever(0.02,'\nAcho que ja e o bastante para comecarmos, mas posso repetir se voce quiser...\n',1)
                        escrever(0.02,'\nVoce entendeu tudo o que eu disse?')
                        print(' (sim ou nao)')
                        objeto[0]="ganha presente"
                    else:
                        print('Entrada invalida!')
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        acao_do_personagem="sim"
            os.system("cls")
            if(objeto[0]=="ganha presente"):
                escrever(0.02,"\nOtimo, "+str(aliado_jogador.nome)+".\n",1)
                escrever(0.02,"Acho que comecamos com o pe direito! Fico feliz que voce tenha me escutado \ncomo um bom garoto!\nPor isso deixei um presente para voce no seu guarda-roupas, tenho certeza que \nvoce ficara feliz.\n")
            else:
                escrever(0.03,"\nEu realmente nao me lembro de voce...",1)
                escrever(0.02,"\nEntao nao espere que eu te trate como um conhecido!\n")

#####################----------------------------__INICIO DO JOGO__----------------------------#####################
            raw_input("|>")
            item_adicionado=pedaco_pizza[0]
            quantidade_adicionada=1
            adicionaItem()
            os.system("cls")
            escrever(0.02,"\nAcabou de amanhecer,",0.5)
            escrever(0.02," seu quarto esta desarrumado,",0.5)
            escrever(0.02," voce ainda esta de pijama\n",0.5)
            escrever(0.02,"e atrasado para a aula",0.5)
            escrever(0.05," - nao que voce se importe muito com isso.\n")
            while 1:
                raw_input("|>")
                os.system("cls")
                print("\n#"+ "-"*30+"#\n\nLista de Acoes\n\nCenario: "+str(variavel_lugar)+"\n\nVoce pode:\n\nolhar\narrumar o quarto\nvestir\n")
                if (variavel_cenario[0] == "sim"): print("olhar as gavetas\nolhar o guarda-roupas\nolhar a estante\n\nolhar pela janela")
                print("\nver ficha do personagem\nver mochila\nsair do quarto\n")
                if(eegg > 1 and eegg<6): print("Voce nao deve:\nolhar a janela\n")
                print("#"+ "-"*30+"#\n\nE agora, "+str(aliado_jogador.nome)+", o que voce vai fazer?")
                acao_do_personagem = raw_input("-")
                acao_do_personagem = acao_do_personagem.lower()
                os.system("cls")
                if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
                    print ("\n#"+"-"*77+"#\n"+"\n Nome: "+str(aliado_jogador.nome)+"\n Vida: "+str(aliado_jogador.status[6])+" de "+str(aliado_jogador.status[5])+" Reconstituicao: ".rjust(45-len(str(aliado_jogador.status[6]))-len(str(aliado_jogador.status[5])))+str(aliado_jogador.status[4])+"\n Ataque: "+str(aliado_jogador.status[0])+"Agilidade: ".rjust(42-len(str(aliado_jogador.status[0])))+str(aliado_jogador.status[2])+"\n Defesa: "+str(aliado_jogador.status[1])+"Sorte: ".rjust(38-len(str(aliado_jogador.status[1])))+str(aliado_jogador.status[3])+"\n Capa: "+str(aliado_jogador.equipamento[1].nome)+"Luvas: ".rjust(40-len(str(aliado_jogador.equipamento[1].nome)))+str(aliado_jogador.equipamento[2].nome)+"\n Roupa: "+str(aliado_jogador.equipamento[0].nome)+"Anel: ".rjust(38-len(str(aliado_jogador.equipamento[0].nome)))+str(aliado_jogador.equipamento[3].nome)+"\n Calcado: "+str(aliado_jogador.equipamento[5].nome)+"Arma: ".rjust(36-len(str(aliado_jogador.equipamento[5].nome)))+str(aliado_jogador.equipamento[4].nome)+"\n Dinheiro: "+str(aliado_jogador.dinheiro)+" Reais\n"+"\n#"+"-"*77+"#\n")
                else:
                    if (acao_do_personagem== "vetir" or acao_do_personagem=="vest" or acao_do_personagem=="vesti" or acao_do_personagem=="veti" or acao_do_personagem=="estir" or acao_do_personagem=="esti" or acao_do_personagem=="etir" or acao_do_personagem == "vestir" or acao_do_personagem == "vesir" or acao_do_personagem == "vestir uniforme" or acao_do_personagem == "vestir o uniforme" or acao_do_personagem == "vestir o uniforme estudantil" or acao_do_personagem == "vestir uniforme estudantil" or acao_do_personagem == "se vestir" or acao_do_personagem == "se vestir para a aula" or acao_do_personagem == "se vestir pra aula" or acao_do_personagem == "vestir para a aula" or acao_do_personagem == "me arrumar" or acao_do_personagem == "tomar banho" or acao_do_personagem == "ir ao banheiro" or acao_do_personagem == "cagar" or acao_do_personagem == "mijar" or acao_do_personagem == "fazer xixi" or acao_do_personagem == "trocar de roupa" or acao_do_personagem == "me trocar" or acao_do_personagem == "trocar"):
                        if (booleana[0] == False):
                            escrever(0.01,"\nVoce colocou a mao embaixo do seu travesseiro e achou seu uniforme.\n",0.5)
                            escrever(0.02,"Voce guardou o Uniforme Estudantil na sua mochila!\n")
                            item_adicionado=equipamento_inicial[1]
                            quantidade_adicionada=1
                            adicionaItem()
                            booleana[0] = True
                        else:
                            print("\nVoce ja pegou seu uniforme!\nPara o equipar, verifique sua mochila.")
                    else:
                        if (acao_do_personagem == "arrumar o quarto" or acao_do_personagem == "arrumar" or acao_do_personagem == "arrumar quarto" or acao_do_personagem == "arruma" or acao_do_personagem == "arruma o quarto" or acao_do_personagem == "arruma quarto" or acao_do_personagem == "quarto"):
                            if (variavel_cenario[1] == "nao"):
                                escrever(0.02,"\nVoce achou 15 Reais enquanto arrumava o seu quarto!\n")
                                aliado_jogador.dinheiro = +15
                                variavel_cenario[1] = "sim"
                            else:
                                escrever(0.01,"\nVoce ja arrumou o seu quarto!\n")
                        else:
                            if (acao_do_personagem == "olhar" or acao_do_personagem=="olh" or acao_do_personagem == "ver" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha" or acao_do_personagem == "olhar quarto" or acao_do_personagem == "olha quarto" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha o quarto" or acao_do_personagem == "ve" or acao_do_personagem == "ve"):
                                if (variavel_cenario[1] == "nao"):
                                    escrever(0.02,"\nVoce nao consegue ver nada alem de bagunca,",1)
                                    escrever(0.08," MUITA BAGUNCA!!!\n")
                                else:
                                    escrever(0.02,"\nVoce ve um quarto arrumado, com um guarda-roupas, uma estante de livros, uma \nmesa de escritorio com gavetas e uma janela.\n")
                                    variavel_cenario[0] = "sim"
                            else:
                                if (acao_do_personagem == "olhar as gavetas" or acao_do_personagem == "olhar gavetas" or acao_do_personagem == "olha a gaveta" or acao_do_personagem == "olhar a gaveta" or acao_do_personagem == "olhar gaveta" or acao_do_personagem == "olhar as gaveta" or acao_do_personagem == "olha as gavetas" or acao_do_personagem == "olha gaveta" or acao_do_personagem == "olha as gaveta" or acao_do_personagem == "olha a gavetas" or acao_do_personagem == "ver as gavetas" or acao_do_personagem == "ver a gaveta" or acao_do_personagem == "ver as gaveta" or acao_do_personagem == "ver a gavetas" or acao_do_personagem=="gaveta" or acao_do_personagem=="gavetas"):
                                    if (booleana[1] == True): escrever(0.01,"\nVoce olhou novamente as gavetas, mas nao encontrou nada interessante.\nPara ver o que voce ja encontrou, verifique sua mochila.\n")
                                    else:
                                        escrever(0.01,"\nVoce achou um Soco-Ingles enquanto olhava as gavetas!\n",0.5)
                                        item_adicionado=soco_ingles[0]
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        escrever(0.02,"Voce o guardou na mochila!\n")
                                        booleana[1]=True
                                else:
                                    if (acao_do_personagem == "olhar o guarda-roupas" or acao_do_personagem =="olhar o guarda" or acao_do_personagem =="olhar o garda" or acao_do_personagem == "guarda" or acao_do_personagem=="roupa" or acao_do_personagem == "olha o guarda-roupas" or acao_do_personagem == "olha o guarda-roupa" or acao_do_personagem == "olhar o guarda-roupa" or acao_do_personagem == "olhar guarda-roupas" or acao_do_personagem == "olha guarda-roupas" or acao_do_personagem == "olha guarda-roupa" or acao_do_personagem == "olhar guarda-roupa" or acao_do_personagem == "olhar o guarda roupas" or acao_do_personagem == "olha o guarda roupas" or acao_do_personagem == "olha o guarda roupa" or acao_do_personagem == "olhar o guarda roupa" or acao_do_personagem == "olhar guarda roupas" or acao_do_personagem == "olha guarda roupas" or acao_do_personagem == "olha guarda roupa" or acao_do_personagem == "olhar guarda roupa" or acao_do_personagem == "olhar o guardaroupas" or acao_do_personagem == "olha o guardaroupas" or acao_do_personagem == "olha o guardaroupa" or acao_do_personagem == "olhar o guardaroupa" or acao_do_personagem == "olhar guardaroupas" or acao_do_personagem == "olha guardaroupas" or acao_do_personagem == "olha guardaroupa" or acao_do_personagem == "olhar guardaroupa" or acao_do_personagem == "olhar o guardarroupas" or acao_do_personagem == "olha o guardarroupas" or acao_do_personagem == "olha o guardarroupa" or acao_do_personagem == "olhar o guardarroupa" or acao_do_personagem == "olhar guardarroupas" or acao_do_personagem == "olha guardarroupas" or acao_do_personagem == "olha guardarroupa" or acao_do_personagem == "olhar guardarroupa" or acao_do_personagem == "guarda-roupa" or acao_do_personagem == "guarda-roupas" or acao_do_personagem == "guarda roupa" or acao_do_personagem == "guarda roupas" or acao_do_personagem == "guardaroupa" or acao_do_personagem == "guardaroupas" or acao_do_personagem == "guardarroupa" or acao_do_personagem == "guardarroupas" or acao_do_personagem == "olhar o armario" or acao_do_personagem == "olhar o armario" or acao_do_personagem == "olhar armario" or acao_do_personagem == "olhar armario" or acao_do_personagem == "olha o armario" or acao_do_personagem == "olha o armario" or acao_do_personagem == "olha armario" or acao_do_personagem == "olha armario" or acao_do_personagem == "armario" or acao_do_personagem == "armario" or acao_do_personagem == "sair do armario" or acao_do_personagem == "vestir smoking" or acao_do_personagem == "ver armario" or acao_do_personagem == "ver o armario" or acao_do_personagem == "ver armario" or acao_do_personagem == "ver o armario" or acao_do_personagem == "ver o guarda-roupas" or acao_do_personagem == "ver o guardarroupas" or acao_do_personagem == "ver o guarda roupas" or acao_do_personagem == "ver o guardaroupas" or acao_do_personagem == "ver o guarda-roupa" or acao_do_personagem == "ver o guardarroupa" or acao_do_personagem == "ver o guarda roupa" or acao_do_personagem == "ver o guardaroupa" or acao_do_personagem == "ver guarda-roupas" or acao_do_personagem == "ver guardarroupas" or acao_do_personagem == "ver guarda roupas" or acao_do_personagem == "ver guardaroupas" or acao_do_personagem == "ver guarda-roupa" or acao_do_personagem == "ver guardarroupa" or acao_do_personagem == "ver guarda roupa" or acao_do_personagem == "ver guardaroupa"):
                                        if(objeto[0]=="ganha presente"):
                                            escrever(0.02,"\nVoce encontrou uma bela caixa de presente. \nVai abrir?")
                                            print(" (sim ou nao)")
                                            while 1:
                                                acao_do_personagem = raw_input("-")
                                                acao_do_personagem = acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    escrever(0.03,"Voce desembalou o presente e...",2)
                                                    escrever(0.01," Encontrou um par de Papetes Masculinas!\n",0.5)
                                                    escrever(0.02,"Voce guardou as Papetes Masculinas na sua mochila!\n")
                                                    item_adicionado=papetes_masculinas
                                                    quantidade_adicionada=1
                                                    adicionaItem()
                                                    objeto[0] = "nao"
                                                    break
                                                else:
                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                        break
                                                    else:
                                                        print('Entrada Invalida!')
                                        else:
                                            escrever(0.02,"\nVoce nao ve muitas roupas...",0.5)
                                            escrever(0.02," Voce e muito pobre, arrume um emprego!\n")
                                    else:
                                        if (acao_do_personagem == "olhar a janela"):###__EASTER-EGG
                                            if (eegg == 1):
                                                escrever(0.02,"\nVoce ve...",2)
                                                escrever(0.02," Uma janela, sua anta!\n",0.5)
                                                escrever(0,"... Hunf...\n",0.5)
                                                escrever(0.02,"Volte para as aulas de ortografia!\n")
                                                escrever(0.1,"...\n")
                                                escrever(0.01,"O que? Voce acha que eu fui muito grosso?\n")
                                                escrever(0.04,"Okay, "+str(aliado_jogador.nome)+", vamos la...\n")
                                                escrever(0.04,"Ha uma diferenca muito grande entre olhar A janela e olhar PELA janela!\n",1)
                                                print("Tente mais uma vez, sua anta!\n")
                                                eegg = 2
                                            else:
                                                if (eegg == 2):
                                                    escrever(0.02,"\nDigitando errado MAIS UMA VEZ?!\n")
                                                    escrever(0.02,"Okay, "+str(aliado_jogador.nome)+", voce ja esta passando dos limites da burrice...\n")
                                                    eegg = 3
                                                else:
                                                    if (eegg == 3):
                                                        escrever(0.02,"\nVoce encara a janela...",1)
                                                        escrever(0.02," Voce parece um retardado fazendo isso...\n")
                                                        eegg = 4
                                                    else:
                                                        if (eegg == 4):
                                                            escrever(0.03,'\nEnquanto voce encarava a janela um pombo pousou nela...\n'+' '*30+'\nEle olhou bem no fundo dos seus olhos e disse',0.5)
                                                            escrever(0.04,' "Voce e um idiota."...    \n')
                                                            escrever(0.03,'Nao, ele nao disse isso... Na verdade fui eu quem disse isso,',0.5)
                                                            escrever(0.02,' seu idiota.\n')
                                                            eegg = 5
                                                        else:
                                                            if (eegg == 5):
                                                                escrever(0.01,"\nJa chega! Voce esgotou minha paciencia!\n")
                                                                batalha(narrador_inimigo)
                                                                if(aliado_jogador.status[6]<=0):break
                                                                if(adversario_inimigo.status[6]>0):
                                                                    escrever(0.02,"\nVou te deixar em paz por agora, \nmas tente voltar a me irritar para ver o que te acontece!\n")
                                                                else:
                                                                    escrever(0.04,"\nAaaah!",1)
                                                                    escrever(0.02," Eu deveria ter me feito mais forte para essa luta...\n",1)
                                                                    escrever(0.02,"Okay, voce venceu... Mas pare de me irritar!\n")
                                                                    eegg = 6
                                                            else:
                                                                if (eegg == 6):
                                                                    escrever(0.01,"\n...\n")
                                                                    eegg = 7
                                                                else:
                                                                    escrever(0.005,"\nVoce ve uma janela que abre horizontalmente para as duas direcoes,\nsendo que o vidro da janela esquerda esta rachado por, \nprovavelmente, um apedrejamento.\nOs batentes sao de madeira antiga, deteriorada pela acao de cupins.\n")
                                        else:
                                            if (acao_do_personagem == "olhar pela janela" or acao_do_personagem == "olha pela janela" or acao_do_personagem == "janela" or acao_do_personagem ==  "olhar janela" or acao_do_personagem == "olha janela" or acao_do_personagem=="ver janela" or acao_do_personagem=="ver a janela"):
                                                escrever(0.03,"\nVoce ve uma rua com predios de classe baixa,\npoucas pessoas passando com cara de cansadas,\nmas voce nao consegue ver o horizonte,\nja que voce mora no primeiro andar e os predios do outro\nlado da rua sao altos e proximos demais uns dos outros.\n",2)
                                                escrever(0.005,"\nVoce percebe um sujeito te encarando do outro lado da rua...\n",1.5)
                                                escrever(0.04,"\nEle esta em pe e encostado na grade cinza, empoeirada e enferrujada\ndo predio da frente um pouco a esquerda da porta dessa grade,\nde modo a ficar de frente para a porta do seu predio.\n",2)
                                                escrever(0.03,"\nSua face cheia de raiva expressa com rigidez a sua intencao,\nsua jeans e velha, sua camisa e rasgada de forma a parecer uma regata,\nenquanto seus bracos cruzados parecem prontos para uma briga!\n")
                                            else:
                                                if (acao_do_personagem == "olhar a estante" or acao_do_personagem =="ohar a estante" or acao_do_personagem =="ohar estante" or acao_do_personagem == "olhar estante" or acao_do_personagem == "olha a estante" or acao_do_personagem == "olha estante" or acao_do_personagem == "estante" or acao_do_personagem == "ver a estante" or acao_do_personagem == "ver estante" or acao_do_personagem == "ver a estante" or acao_do_personagem == "ver estante" or acao_do_personagem =="olahr a estante"):
                                                    escrever(0.015,"\nVoce ve livros e apostilas rabiscadas na capa e a maioria rasgadas no canto \ndos furos das espirais... Nada muito interessante...\n",2)
                                                    escrever(0.03,"Mas voce ve um pedaco de papel vermelho colocado entre as paginas de um \ndos livros...\nLer o bilhete??")
                                                    print(" (sim ou nao)")
                                                    while 1:
                                                        acao_do_personagem=raw_input("-")
                                                        acao_do_personagem=acao_do_personagem.lower()
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            escrever(0.03,'\n "       Voce pode digitar seus comandos de outras formas, como por exemplo,\n'+"\nao inves de digitar 'ver mochila' voce pode simplesmente digitar 'mala'!\n"+'\nTente sempre digitar da forma mais simples, isso facilitara muito o seu jogo!\n\nNao custa nada tentar! ;)\n\n                               assinado: Programador "\n')
                                                            break
                                                        else:
                                                            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                print("Voce ignorou o bilhete.\n")
                                                                break
                                                            else:
                                                                print('Entrada invalida!')
                                                else:
                                                    if (acao_do_personagem == "destruir o universo"): #Easter-Egg para o Yuri
                                                        print ("\n"+"Adeus...".center(79)+"\n")
                                                        aliado_jogador.status[0]=77777
                                                        aliado_jogador.status[1]=77777
                                                        aliado_jogador.status[2]=777
                                                        aliado_jogador.status[3]=777
                                                        aliado_jogador.status[4]=777
                                                        aliado_jogador.status[5]=7777777
                                                        aliado_jogador.status[6]=7777777
                                                        time.sleep(5)
                                                        os.system('cls')
                                                        while 1:
                                                            acao_do_personagem = raw_input("")
                                                            acao_do_personagem = acao_do_personagem.lower()
                                                            if(acao_do_personagem=="reconstruir o universo" or acao_do_personagem == "reconstruir universo" or acao_do_personagem == "construir o universo" or acao_do_personagem == "criar um novo universo" or acao_do_personagem == "construir um universo" or acao_do_personagem == "criar o universo"):
                                                                break
                                                            os.system('cls')
                                                        os.system('cls')
                                                        print("\n"+"Ola!".center(79)+"\n")
                                                    else:
                                                        if(acao_do_personagem=="sair do quarto" or acao_do_personagem=="sair" or acao_do_personagem=="ir para a aula" or acao_do_personagem=="ir pra aula" or acao_do_personagem=="ir para aula" or acao_do_personagem=="ir a aula" or acao_do_personagem=="ir a aula" or acao_do_personagem=="sair quarto"):
                                                            while 1:
                                                                escrever(0.02,"Se sair voce nao podera voltar.\nTem certeza que deseja sair?")
                                                                print(" (sim ou nao)")
                                                                acao_do_personagem=raw_input("-")
                                                                acao_do_personagem=acao_do_personagem.lower()
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    acao_do_personagem="sim"
                                                                    break
                                                                else:
                                                                    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                                                                        print("Voce decidiu nao sair do quarto.")
                                                                        break
                                                                    else:
                                                                        print("Entrada invalida!")
                                                            if(acao_do_personagem=="sim"):
                                                                break
                                                        else:
                                                            if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                                inventarioPersonagem()
                                                            else:
                                                                print('Entrada Invalida!')
            if(aliado_jogador.status[6]<=0):break
            ponto_de_save = 1
            variavel_cenario[1] = "nao"
            variavel_cenario[0] = "nao"
            booleana[0] = False
            escrever(0.02,"Voce saiu do seu quarto.",2)
            os.system('cls')
            save()

##########--------------------------------------------------FIM DA PRIMEIRA PARTE--------------------------------------------------##########
        if(ponto_de_save==1):
            if(variavel_lugar == "seu predio, 1o andar" or variavel_lugar == "seu predio, 2o andar" or variavel_lugar == "seu predio, 3o andar" or variavel_lugar == "seu predio, 4o andar"):
                if(variavel_lugar == "seu predio, 1o andar"):
                    variavel_lugar = "seu predio, 1o andarb"
                if(variavel_lugar == "seu predio, 2o andar"):
                    variavel_lugar = "seu predio, 2o andarb"
                if(variavel_lugar == "seu predio, 3o andar"):
                    variavel_lugar = "seu predio, 3o andarb"
                if(variavel_lugar == "seu predio, 4o andar"):
                    variavel_lugar = "seu predio, 4o andarb"
                seuPredioPrimeiroAndar()
            else:
                os.system("cls")
                escrever(0.02,"\nVoce continua atrasado para a aula - nao que voce deva se importar \nmuito com isso.\n",1)
                os.system("cls")
                variavel_lugar = "seu predio, 1o andar"
                seuPredioPrimeiroAndar()
            if(aliado_jogador.status[6]<=0):break
            ponto_de_save = 2
            variavel_lugar = "em frente ao seu predio"
            save()


##########--------------------------------------------------FIM DA SEGUNDA PARTE--------------------------------------------------##########
        if(ponto_de_save==2):
            raw_input("|>")
            os.system("cls")
            escrever(0.02,"\nAgora voce esta na sua rua.\n\n\n")
            escrever(0.02,"Mas antes que pudesse fazer alguma coisa,\n")
            escrever(0.02,"você foi abordado por um homem aparentemente forte\n")
            escrever(0.04,"vestindo uma jeans velha e uma camisa que foi rasgada de forma a parecer uma regata...\nSeu rosto era magro, de tao afundadas que as bochechas eram, parecia uma caveira,\nsua pele queimada pelo Sol era cheia de manchas, seu cabelo crespo crescia por cima das ventas,\nmas a calvisse da sua fronte se extendia ate a ponta extrema da sua arredondada e fosca cabeca...\n"+" "*5+"\n")
            escrever(0.01," - Cade o dinheiro que voce roubou do nosso esquema?\n"+" "*30+"\n")
            escrever(0.03,"Mas voce REALMENTE nao sabia de esquema algum, quanto menos do dinheiro...\n",1)
            escrever(0.04,"Algo nao parece certo...\n\n",1)
            escrever(0.01," - Nao adianta negar!!! Escolhe, moleque: a grana ou a vida???\n\n")
            escrever(0.05,"...\n"+' '*10+"\n")
            escrever(0.02,"Ele saca uma faca do bolso de tras!\n\n")
            escrever(0.01," - EU VOU TE QUEBRAR ATE VOCE ME DAR O DINHEIRO!!!\n")
            batalha(gangue_comparsa[0])
            if(aliado_jogador.status[6]<=0):
                aliado_jogador.status[6]=1
                escrever(0.025,"Voce caiu no chao...\n",1)
                escrever(0.02,"Ajoelhado na sua barriga e com o antebraco apoiado no seu pescoco\no bandido abriu um largo e amargo sorriso enquanto te fitava com seu olhar insano!\n\n",2)
                escrever(0.01," - HAHAHAHA! Voce vai morrer!\n\n",0.5)
                escrever(0.04,"Voce esta rendido...\n",0.5)
                escrever(0.02,"Com a outra mao ergueu a faca apontada para o seu peito!\n\n")
                escrever(1,"...\n\n",3)
                escrever(0.001,"!!!\n\n",2)
                escrever(0.04,"Enquanto voce estava estirado no chao, o bandido foi violentamente atingido por um soco...\n")
                escrever(0.02,"Voce se levantou rapidamente e pode, entao, observar a sitiuacao...\n")
                escrever(0.05,"Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,\numa calca preta rasgada nos joelhos e um all-star preto,\nalem da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titanio.\n\n",1.5)
                escrever(0.02,"Agora voce esta jogando como o Lutador Headbanger.\n")
                aliado_reserva = aliado_jogador
                aliado_jogador = aliado_headbanger
                batalha(gangue_comparsa[0])
                aliado_jogador = aliado_reserva
                print(" - Pare! Por favor!\n")
                time.sleep(3)
                print("...")
                time.sleep(3)
                print("Antes que voce e o Headbanger pudessem perceber o som da moto, um comparsa o resgatou...")
                time.sleep(3)
                print("O Headbanger se virou e olhou para voce.")
                time.sleep(3)
                print(" - Voce e fraco demais, mas tem muito potencial.")
                time.sleep(3)
                print(" - Nao sei o que voce fez para eles, mas voce parece precisar de ajuda.")
                time.sleep(3)
                print(" - Vou procurar saber o que esta acontecendo... Faca o mesmo, voce tambem!")
                time.sleep(3)
                print(" - Ele sumiu pelos becos da rua...")
                time.sleep(3)
                print("Voce continua sem respostas...")
                time.sleep(3)
                print("Sera que voce encontrara alguma pista na faculdade?")
                time.sleep(5)
            else:
                if(adversario_inimigo.status[6]>0):
                    while(adversario_inimigo.status[6]>0):
                        print("Voce correu um pouco mas ele te alcancou de novo!\n")
                        batalha(gangue_comparsa[0])
                        if(aliado_jogador.status[6]<=0):
                            aliado_jogador.status[6]=1
                            print("Voce caiu no chao...")
                            time.sleep(3)
                            print("Ajoelhado na sua barriga e com o antebraco apoiado no seu pescoco")
                            print("o bandido abriu um largo e amargo sorriso enquanto te fitava com seu olhar insano!")
                            time.sleep(4)
                            print(" - HAHAHAHA! Voce vai morrer!")
                            time.sleep(3)
                            print("Voce esta rendido...")
                            time.sleep(4)
                            print("Com a outra mao ergueu a faca apontada para o seu peito!")
                            time.sleep(3)
                            print("...")
                            time.sleep(5)
                            print("!!!")
                            time.sleep(3)
                            print("O bandido foi violentamente atingido por um soco...")
                            time.sleep(4)
                            print("Voce se levantou rapidamente e pode, entao, observar a sitiuacao...")
                            time.sleep(3)
                            print("Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,")
                            time.sleep(5)
                            print("uma calca preta rasgada nos joelhos e um all-star preto,")
                            time.sleep(5)
                            print("alem da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titanio.")
                            time.sleep(6)
                            aliado_reserva = aliado_jogador
                            aliado_jogador = aliado_headbanger
                            batalha(gangue_comparsa[0])
                            aliado_headbanger = aliado_jogador
                            aliado_jogador = aliado_reserva
                            print(" - Pare! Por favor!\n")
                            time.sleep(3)
                            print("...")
                            time.sleep(3)
                            print("Antes que voce e o Headbanger pudessem perceber o som da moto, um comparsa o resgatou...")
                            time.sleep(3)
                            print("O Headbanger se virou e olhou para voce.")
                            time.sleep(3)
                            print(" - Voce e fraco demais, mas tem muito potencial.")
                            time.sleep(3)
                            print(" - Nao sei o que voce fez para eles, mas voce parece precisar de ajuda.")
                            time.sleep(3)
                            print(" - Vou procurar saber o que esta acontecendo... Faca o mesmo, voce tambem!")
                            time.sleep(3)
                            print(" - Ele sumiu pelos becos da rua...")
                            time.sleep(3)
                            print("Voce continua sem respostas...")
                            time.sleep(3)
                            print("Sera que voce encontrara alguma pista na faculdade?")
                            time.sleep(5)
                        else:
                            print(" - Pare! Por favor!\n")
                            time.sleep(3)
                            print("...")
                            time.sleep(3)
                            print("Antes que voce pudesse perceber o som da moto, um comparsa o resgatou...")
                            time.sleep(3)
                            print("Voce continua sem respostas...")
                            time.sleep(3)
                            print("Sera que voce encontrara alguma pista na faculdade?")
                            time.sleep(5)
                else:
                    print(" - Pare! Por favor!\n")
                    time.sleep(3)
                    print("...")
                    time.sleep(3)
                    print("Voce escuta um som de moto ao fundo...")
                    time.sleep(3)
                    print("Um comparsa motoqueiro tentou te atropelar, mas voce conseguiu executar uma evasao rolando para a calcada!")
                    time.sleep(3)
                    print(" - Agora voce vai entregar o dinheiro, ou nao vai?! - inqueriu, o motoqueiro montado em sua Twister 250.")
                    time.sleep(3)
                    batalha(gangue_comparsa[1])
                    if(aliado_jogador.status[6]<=0): break
                    if(adversario_inimigo.status[6]>0):
                        print("Correndo entre uns becos da sua rua, voce conseguiu se esconder...")
                        time.sleep(2)
                        print("...")
                        time.sleep(2)
                        print("...")
                        time.sleep(2)
                        print("Voce conseguiu despita-los...")
                        time.sleep(2)
                    else:
                        print("Voce derrotou os dois!")
                        time.sleep(2)
                        print("Eles estao desmaiados na rua...")
                        time.sleep(2)
                        print("Mas antes que voce pudesse pensar em algo, o barrulho de varias sirenes te alertou!")
                        time.sleep(2)
                        print("Voce se escondeu em um dos becos, mas pode assistir os policiais prendendo os dois bandidos...")
                        time.sleep(2)
                        print("Voce conseguiu se manter escondido ate a cena esfriar, mas continua sem respostas...")
                        time.sleep(2)
            ponto_de_save = 3
            variavel_lugar = "sua rua"
            save()

##########--------------------------------------------------FIM DA TERCEIRA PARTE--------------------------------------------------##########
        if(ponto_de_save==3):
            if(variavel_lugar == "seu predio, 1o andar" or variavel_lugar == "seu predio, 2o andar" or variavel_lugar == "seu predio, 3o andar" or variavel_lugar == "seu predio, 4o andar"):
                if(variavel_lugar == "seu predio, 1o andar"):
                    variavel_lugar = "seu predio, 1o andarb"
                if(variavel_lugar == "seu predio, 2o andar"):
                    variavel_lugar = "seu predio, 2o andarb"
                if(variavel_lugar == "seu predio, 3o andar"):
                    variavel_lugar = "seu predio, 3o andarb"
                if(variavel_lugar == "seu predio, 4o andar"):
                    variavel_lugar = "seu predio, 4o andarb"
                seuPredioPrimeiroAndar()
                variavel_lugar = "sua rua"
            else:
                raw_input("|>")
                os.system("cls")
                print("Voce esta na sua rua, por agora tudo esta calmo....")
                suaRua()
            if(aliado_jogador.status[6]<=0):break
            ponto_de_save = 4
            variavel_lugar="rua da faculdade"
            save()

##########--------------------------------------------------FIM DA QUARTA PARTE--------------------------------------------------##########
        if(ponto_de_save==4):
            variavel_lugar="rua da faculdade"
            print ('Voce finalmente chegou na rua faculdade! \nMas algo parece estranho por aqui, \nmuitos estudantes e arruaceiros estao brigando!')
            ruaFaculdade()
            if(aliado_jogador.status[6]<=0):break
            ponto_de_save = 5
            save()

##########--------------------------------------------------FIM DA QUINTA PARTE--------------------------------------------------##########
        if(ponto_de_save==5):
            print ('Voce entrou na faculdade',)
            timesleep(2)
            for nicacao in range(3):
                print ('.',)
                timesleep(0.5)
            print ('\n!!!!!!')
            print ('Uma garota saltou acertando um soco na sua cara!!!')
            ponto_de_save = 6
            save()
            
##########--------------------------------------------------FIM DO JOGO--------------------------------------------------##########
        break
    if(aliado_jogador.status[6]>0):
        print("\nParabens, "+str(aliado_jogador.nome)+"!!! Voce terminou o jogo!!!")
        if(booleana[2]==False):
            item_adicionado=anel_da_imortalidade
            quantidade_adicionada=1
            adicionaItem()
            print("Voce ganhou um Anel da Imortalidade!")
            ponto_de_save=0
            save()
        else:
            item_adicionado=anel_da_divindade
            quantidade_adicionada=1
            adicionaItem()
            print("Voce ganhou um Anel da Divindade!")
            ponto_de_save=0
            save()
    print("\nVoce deseja jogar novamente, "+str(aliado_jogador.nome)+'?("sim" ou "nao")\n')
    while 1:
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
            raw_input("\nReiniciando...(APERTE ENTER)\n")
            if (aliado_jogador.status[6] <= 0):
                print("Voce morreu, "+ aliado_jogador.nome+ "...\nO jogo acabou para voce...")
                
                aliado_jogador = Personagem("NULO", 10,8,1,1, 0,100,100, 0, 1, equipamento_inicial[0], desequipado_capa, desequipado[2], desequipado[3], desequipado[4], equipamento_inicial[3])
                aliado_reserva = aliado_jogador
                aliado_headbanger = Personagem("Lutador Headbanger", 1200,800,50,50, 100,100000,100000, 0, 3, desequipado[0], desequipado[1], desequipado[2], desequipado[3], desequipado[4], desequipado[5])
                aliado_garota = Personagem("Garota", 25,20,1,1, 0,300,300, 25, 2, equipamento_inicial[1], desequipado[1], desequipado[2], desequipado[3], equipamento_inicial[2], equipamento_inicial[4])

                item_adicionado=desequipado[6]
                quantidade_adicionada=1
                porcentagem_inflacao=1

                variavel_cenario = ["nao" ,"nao" ,"nao"]
                objeto = ["nao", "nao", "nao", "nao", "nao"]
                situacao = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
                booleana = [False, False, False]

                variavel_lugar = "seu quarto"
                ponto_de_save = 0

                mostrar_save = ''

                eegg = 1
            break
        else:
            if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
                break
            else:
                print('\nEntrada invalida!(digite "sim" ou "nao)\n')
    if(acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="ao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem== "naao" or acao_do_personagem=="naoo" or acao_do_personagem=="aoo" or acao_do_personagem=="noo" or acao_do_personagem=="naa" or acao_do_personagem== "noop" or acao_do_personagem=="a" or acao_do_personagem=="mao" or acao_do_personagem=="nso" or acao_do_personagem=="ns" or acao_do_personagem== "nnao" or acao_do_personagem=="nn" or acao_do_personagem=="aao" or acao_do_personagem=="nno" or acao_do_personagem=="nna"):
        break
    
exit()
