# -*- coding: cp1252 -*-
#--Import--#
#use o python 2.7.4 que e coisa de macho!!!!!!11!!!!!1!!onze!!!! - Lucas Sabiao
import random
import ConfigParser
import pickle
import time

#ASSISTA DEVIL SURVIVOR 2

#"Nome"[0], atq[1], def[2], agi[3], luk[4], vidamaxima[5], vidaatual[6], dinheiro[7]
personagem_jogador = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
personagem_reserva = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
personagem_inimigo = [ "Inimigo", 10, 8, 1, 1, 100, 100]

#["Nome"[0], atq[1], def[2], agi[3], luk[4], tipo[5], preco[6], recupera[7]

desequipado_roupa = ["Nada", 0, 0, 0, 0, "roupa", 0, 0]
desequipado_capa = ["Nada", 0, 0, 0, 0, "capa", 0, 0]
desequipado_luva = ["Nada", 0, 0, 0, 0, "luva", 0, 0]
desequipado_anel = ["Nada", 0, 0, 0, 0, "anel", 0, 0]
desequipado_maos = ["Nada", 0, 0, 0, 0, "armamento", 0, 0]
desequipado_calcado = ["Nada", 0, 0, 0, 0, "calcados", 0, 0]
espaco_vazio = ["Vazio", 0, 0, 0, 0, "inventario", 0, 0]

pedaco_pizza = ["Pedaco de Pizza", 0, 0, 0, 0, "consumivel", 5, 50]
bolo_chocolate = ["Bolo de Chocolate", 0, 0, 0, 0, "consumivel", 100, personagem_jogador[5]]

pijama_inicial = ["Pijama", 0, 0, 0, 5, "roupa", 5, 0]
uniforme_estudantil = ["Uniforme Estudantil",0,1,0,0,"roupa",5,0]
bermuda_linho_regata = ["Bermuda de Linho e Regata ",0,1,4,0,"roupa",100,0]
bermuda_linho_polo = ["Bermuda de Linho e Polo",0,2,3,2,"roupa",140,0]
calca_jeans_regata = ["Calca Jeans e Regata",0,4,1,0,"roupa",110,0]
calca_jeans_polo = ["Calca Jeans e Polo",0,6,0,2,"roupa",150,0]
malha_ninja = ["Malha Ninja", 5, 20, 5, 1, "roupa", 5000, 0]

lapis_apontado = ["Lapis Apontado", 3,0,0,1,"armamento",2,0]
punhal_envelhecido = ["Punhal Envelhecido", 10, 0,0,3,"armamento",300,0]
talheres_prata = ["Talheres de prata(Garfo e Faca)", 8, 0,0,0,"armamento",10,0]

jaqueta_imitacao = ["Jaqueta de Imitacao de Couro", 0, 20, 0, 0,"capa",150,0]
jaqueta_couro = ["Jaqueta de Couro", 0, 200, 0, 10,"capa",2000,0]
agasalho_la = ["Agasalho de La", 0, 6, 0, 0,"capa",100,0]

suplemento_alimenticio = ["Suplemento Alimenticio", 10, 0, 0, 0, "consumivel de aprimoramento",5, 0]
lata_energetico = ["Energetico", 0, 0, 0, 0, "consumivel de aprimoramento",5, 50]

luva_la = ["Luvas de La", 0, 3, 0, 0, "luva", 20, 0]
luva_imitacao = ["Luvas de Imitacao de Couro", 3, 3, 0, 0, "luva", 100, 0]
soco_pvc = ["Soco-Ingles de PVC", 3, 0, 0, 0, "luva", 50, 0]
luva_couro = ["Luvas de Couro", 8, 8, 0, 0, "luva", 500, 0]
soco_latao = ["Soco-Ingles de Latao", 10, 0, 0, 0, "luva", 500, 0]
luva_spikes_alu = ["Luvas de Couro com Spikes de Aluminio", 15, 15, 0, 0, "luva", 700, 0]
soco_alu = ["Soco-Ingles de Aluminio", 25, 0, 0, 0, "luva", 700, 0]
luva_spikes_aco = ["Luvas de Couro com Spikes de Aco", 25, 25, 0, 0, "luva", 1000, 0]
soco_aco = ["Soco-Ingles de Aluminio de Aco", 30, 0, 0, 0, "luva", 1000, 0]
luva_spikes_ag = ["Luvas de Couro com Spikes de Prata", 25, 25, 0, 5, "luva", 5000, 0]
soco_ag = ["Soco-Ingles de Prata", 35, 0, 0, 5, "luva", 5000, 0]
luva_spikes_au = ["Luvas de Couro com Spikes de Ouro", 250, 250, 0, 10, "luva", 10000, 0]
soco_au = ["Soco-Ingles de Ouro", 350, 0, 0, 10, "luva", 10000, 0]
luva_spikes_titanio = ["Luvas de Couro com Spikes de Titanio", 2500, 2500, 0, 20, "luva", 50000, 0]
soco_titanio = ["Soco-Ingles de Titanio", 3500, 0, 0, 20, "luva", 50000, 0]

anel_forca1 = ["Anel da Forca 1", 10, -2, -2, -2, "anel", 500, 0]
anel_resistencia1 = ["Anel da Resistencia 1", -2, 10, -2, -2, "anel", 500, 0]
anel_forca2 = ["Anel da Forca 2", 20, -4, -4, -4, "anel", 1000, 0]
anel_resistencia2 = ["Anel da Resistencia 2", -4, 20, -4, -4, "anel", 1000, 0]
anel_forca3 = ["Anel da Forca 2", 40, -8, -8, -8, "anel", 5000, 0]
anel_resistencia3 = ["Anel da Resistencia 2", -8, 40, -8, -8, "anel", 5000, 0]

anel_consistencia1 = ["Anel da Consistencia 1", -2, -2, -2, -2, "anel", 500, 10]
anel_consistencia2 = ["Anel da Consistencia 2", -4, -4, -4, -4, "anel", 1000, 100]
anel_consistencia3 = ["Anel da Consistencia 3", -8, -8, -8, -8, "anel", 5000, 1000]

anel_da_imortalidade = ["Anel da Imortalidade", personagem_jogador[1], personagem_jogador[2], personagem_jogador[3], personagem_jogador[4], "anel", 100000, personagem_jogador[5]]
anel_da_divindade = ["Anel da Divindade", personagem_jogador[1]*2, personagem_jogador[2]*2, personagem_jogador[3]*2, personagem_jogador[4]*2, "anel", 100000000, personagem_jogador[5]*2]

chinelo_inicial = ["Chinelos", 0, 0, 0, -5, "calcados", 5, 0]
papetes_masculinas = ["Papetes Masculinas", 0, 0, 1, 0, "calcados", 15, 0]
tenis_velho = ["Tenis Velho", 0, 0, 2, 0, "calcados", 10, 0]
tenis_simplorio = ["Tenis Simplorio", 0, 1, 2, 0, "calcados", 50, 0]
sapato_simplorio = ["Sapato Simplorio", 0, 2, 1, 0, "calcados", 50, 0]
tenis_comum = ["Tenis Comum", 0, 2, 2, 0, "calcados", 90, 0]
tenis_trilha = ["Tenis de Trilha", 2, 8, 3, 0, "calcados", 400, 0]
tenis_caminhada = ["Tenis de Caminhada", 0, 3, 5, 0, "calcados", 300, 0]
tenis_corrida = ["Tenis de Corrida", 0, 5, 10, 0, "calcados", 500, 0]
tenis_ZX5000 = ["Tenis ZX-5000", 10, 10, 11, 5, "calcados", 15000, 0]

item_adicionado=espaco_vazio
quantidade_adicionada=1
porcentagem_inflacao=1

equipado_roupa = pijama_inicial
equipado_capa = desequipado_capa
equipado_luva = desequipado_luva
equipado_anel = desequipado_anel
equipado_maos = desequipado_maos
equipado_calcado = chinelo_inicial

variavel_cenario = ["nao" ,"nao" ,"nao"]
#[0]  olhar cenario primeira vez no seu quarto e reciclada no primeiro andar do seu predio
#[1]  modificar cenario primeira vez no seu quarto
#[2]  cheirar cenario no primeiro andar do seu predio

objeto = ["nao", "nao", "nao", "nao", "nao"]
#[0]  presente do tutorial e reciclada no bebado do 1ºandar
#[1]  porta do quarto 10
#[2]  energetico do bebado (acao revistar)
#[3]  arrombar porta do quarto 10
#[4]  mulher do bebado - talheres de prata

situacao = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
#[0]  dois últimos andares do seu predio
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

temporario = [False, False, False]
#[0]  verifica se pegou o uniforme no seu quarto depois e reciclada para verificar se ja venceu o terceiro andar do seu predio
#[1]  verifica se pegou o soco ingles no seu quarto depois e reciclada para verificar se 
#[2]  verifica se ja zerou o jogo antes

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


#global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda

mala = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio]
loja_venda = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio]
inventario_reserva = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio]

#--Sistema de Troca de Personagem--#

#--Adicionar Item ao Inventario--#
def adicionaItem():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    variavel_para_comparar=0
    i=0
    while i<=29:
        if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
            variavel_para_comparar+=1
        i+=1
    if(variavel_para_comparar<quantidade_adicionada):
        quantidade_adicionada=variavel_para_comparar
    while (quantidade_adicionada>0):
        i=0
        while i<=29:
            if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
                mala[1][i]=item_adicionado
                break
            i+=1
        quantidade_adicionada-=1

#--Inventario--#
def inventarioPersonagem():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("Mochila:        "+str(variavel_para_comparar)+" espacos livres.\n")
        variavel_para_comparar=0
        time.sleep(0.5)
        i=0
        while i<=29:
            if (mala[1][i]!=espaco_vazio and mala[1][i][0]!="Nada"):
                print(str(mala[0][i])+" : "+str(mala[1][i][0])+"\n     ("+str(mala[1][i][5])+")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o número da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isnumeric():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVÁLIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==mala[0][i] and mala[1][i]!=espaco_vazio and mala[1][i][0]!="Nada"):
            if(mala[1][i][5]=="consumivel de aprimoramento"):
                print("\nNome:"+str(mala[1][i][0])+ "\nTipo:"+str(mala[1][i][5])+"\nVida:"+str(mala[1][i][7])+"\nAtaque:"+str(mala[1][i][1])+"\nDefesa:"+str(mala[1][i][2])+"\nAgilidade:"+str(mala[1][i][3])+"\nSorte:"+str(mala[1][i][4])+"\n")
                while 1:
                    print("O que deseja fazer? (usar, descartar ou voltar)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem=="usar"):
                        personagem_jogador[5]=personagem_jogador[5]+mala[1][i][7]
                        personagem_jogador[6]=personagem_jogador[5]
                        personagem_jogador[1]=personagem_jogador[1]+mala[1][i][1]
                        personagem_jogador[2]=personagem_jogador[2]+mala[1][i][2]
                        personagem_jogador[3]=personagem_jogador[3]+mala[1][i][3]
                        personagem_jogador[4]=personagem_jogador[4]+mala[1][i][4]
                        print("\nVoce usou"+str( mala[1][i][0])+"!\n")
                        time.sleep(0.5)
                        mala[1][i]=espaco_vazio
                        break
                    else:
                        if(acao_do_personagem=="descartar"):
                            while 1:
                                print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                                acao_do_personagem=raw_input("-")
                                acao_do_personagem=acao_do_personagem.lower()
                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        break
                                    else:
                                        print("\nENTRADA INVÁLIDA!\n")
                                        time.sleep(0.5)
                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                print("\nVoce descartou"+str(mala[1][i][0])+"!\n")
                                time.sleep(0.5)
                                mala[1][i]=espaco_vazio
                                break
                        else:
                            if(acao_do_personagem=="voltar"):
                                break
                            else:
                                print("\nENTRADA INVÁLIDA!\n")
                                time.sleep(0.5)
            if(mala[1][i][5]=="consumivel"):
                print("\nNome: "+str(mala[1][i][0])+ "\nTipo:"+str(mala[1][i][5])+"\nVida:"+str(mala[1][i][7])+"\n")
                while 1:
                    print("O que deseja fazer? (usar, descartar ou voltar)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem=="usar"):
                        personagem_jogador[6]=personagem_jogador[6]+mala[1][i][7]
                        if (personagem_jogador[6]>=(personagem_jogador[5]+0.1*personagem_jogador[6])):
                            personagem_jogador[6]=personagem_jogador[5]+0.1
                        print("\nVoce usou"+ str(mala[1][i][0])+"!\n")
                        time.sleep(0.5)
                        mala[1][i]=espaco_vazio
                        break
                    else:
                        if(acao_do_personagem=="descartar"):
                            while 1:
                                print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                                acao_do_personagem=raw_input("-")
                                acao_do_personagem=acao_do_personagem.lower()
                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        break
                                    else:
                                        print("\nENTRADA INVÁLIDA!\n")
                                        time.sleep(0.5)
                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                print("\nVoce descartou"+str(mala[1][i][0])+"!\n")
                                time.sleep(0.5)
                                mala[1][i]=espaco_vazio
                                break
                        else:
                            if(acao_do_personagem=="voltar"):
                                break
                            else:
                                print("\nENTRADA INVÁLIDA!\n")
                                time.sleep(0.5)
            if(mala[1][i][5]!="consumivel de aprimoramento" and mala[1][i][5]!="consumivel"):
                print("\nNome:"+str(mala[1][i][0])+"\nTipo:"+str(mala[1][i][5])+"\nAtaque:"+str(mala[1][i][1])+"\nDefesa:"+str(mala[1][i][2])+"\nAgilidade:"+str(mala[1][i][3])+"\nSorte:"+str(mala[1][i][4])+"\n")
                while 1:
                    print("O que deseja fazer? (equipar, descartar ou voltar)")
                    acao_do_personagem=raw_input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem=="descartar"):
                        while 1:
                            print("\nTem certeza que deseja descartar? (sim ou nao)\n")
                            acao_do_personagem=raw_input("-")
                            acao_do_personagem=acao_do_personagem.lower()
                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                break
                            else:
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    break
                                else:
                                    print("\nENTRADA INVÁLIDA!\n")
                                    time.sleep(0.5)
                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                            print("\nVoce descartou"+str(mala[1][i][0])+"!\n")
                            time.sleep(0.5)
                            mala[1][i]=espaco_vazio
                            break
                    else:
                        if(acao_do_personagem=="equipar"):
                            if(mala[1][i][5]=="roupa"):
                                personagem_jogador[1] = personagem_jogador[1] - equipado_roupa[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_roupa[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_roupa[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_roupa[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_roupa[7]
                                item_adicionado=equipado_roupa
                                print("Voce guardou "+str(item_adicionado[0])+" e equipou "+str(mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_roupa=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_roupa[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_roupa[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_roupa[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_roupa[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_roupa[7]
                                break
                            if(mala[1][i][5]=="capa"):                            
                                personagem_jogador[1] = personagem_jogador[1] - equipado_capa[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_capa[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_capa[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_capa[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_capa[7]
                                item_adicionado=equipado_capa
                                print("Voce guardou "+str(item_adicionado[0])+" e equipou "+str( mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_capa=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_capa[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_capa[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_capa[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_capa[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_capa[7]
                                break
                            if(mala[1][i][5]=="luva"):
                                personagem_jogador[1] = personagem_jogador[1] - equipado_luva[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_luva[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_luva[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_luva[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_luva[7]
                                item_adicionado=equipado_luva
                                print("Voce guardou "+str(item_adicionado[0])+" e equipou "+str(mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_luva=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_luva[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_luva[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_luva[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_luva[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_luva[7]
                                break
                            if(mala[1][i][5]=="anel"):
                                personagem_jogador[1] = personagem_jogador[1] - equipado_anel[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_anel[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_anel[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_anel[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_anel[7]
                                item_adicionado=equipado_anel
                                print("Voce guardou "+str(item_adicionado[0])+" e equipou "+str(mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_anel=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_anel[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_anel[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_anel[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_anel[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_anel[7]
                                break
                            if(mala[1][i][5]=="armamento"):
                                personagem_jogador[1] = personagem_jogador[1] - equipado_maos[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_maos[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_maos[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_maos[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_maos[7]
                                item_adicionado=equipado_maos
                                print("Voce guardou "+str(item_adicionado[0])+" e equipou "+str(mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_maos=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_maos[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_maos[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_maos[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_maos[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_maos[7]
                                break
                            if(mala[1][i][5]=="calcados"):
                                personagem_jogador[1] = personagem_jogador[1] - equipado_calcado[1]
                                personagem_jogador[2] = personagem_jogador[2] - equipado_calcado[2]
                                personagem_jogador[3] = personagem_jogador[3] - equipado_calcado[3]
                                personagem_jogador[4] = personagem_jogador[4] - equipado_calcado[4]
                                personagem_jogador[5] = personagem_jogador[5] - equipado_calcado[7]
                                item_adicionado=equipado_calcado
                                print("Voce guardou "+str(tem_adicionado[0])+" e equipou "+str(mala[1][i][0])+"!")
                                time.sleep(1)
                                equipado_calcado=mala[1][i]
                                mala[1][i]=item_adicionado
                                personagem_jogador[1] = personagem_jogador[1] + equipado_calcado[1]
                                personagem_jogador[2] = personagem_jogador[2] + equipado_calcado[2]
                                personagem_jogador[3] = personagem_jogador[3] + equipado_calcado[3]
                                personagem_jogador[4] = personagem_jogador[4] + equipado_calcado[4]
                                personagem_jogador[5] = personagem_jogador[5] + equipado_calcado[7]
                                break
                            if(mala[1][i][5]=="consumivel" or mala[1][i][5]=="consumivel de aprimoramento"):
                                print("voce nao pode equipar!")
                                time.sleep(0.5)
                        else:
                            if(acao_do_personagem=="voltar"):
                                break
                            else:
                                print("\nENTRADA INVLIDA!\n")
                                time.sleep(0.5)

#--Loja: Vender--#
def lojaVender():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("Mochila:        "+str(variavel_para_comparar)+" espacos livres.\n")
        variavel_para_comparar=0
        time.sleep(0.5)
        i=0
        while i<=29:
            if (mala[1][i]!=espaco_vazio and mala[1][i][0]!="Nada"):
                print(str(mala[0][i])+" : "+str(mala[1][i][0])+"\n     ("+str(mala[1][i][5])+")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o número da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isnumeric():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVÁLIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==mala[0][i] and mala[1][i]!=espaco_vazio and mala[1][i][0]!="Nada"):
            if(mala[1][i][5]=="consumivel de aprimoramento"):
                print("\nNome:"+str(mala[1][i][0])+ "\nTipo:"+str(mala[1][i][5])+"\nVida:"+str(mala[1][i][7])+"\nAtaque:"+str(mala[1][i][1])+"\nDefesa:"+str(mala[1][i][2])+"\nAgilidade:"+str(mala[1][i][3])+"\nSorte:"+str(mala[1][i][4])+"\n")
        if(mala[1][i][5]=="consumivel"):
            print("\nNome:"+str(mala[1][i][0])+ "\nTipo:"+str(mala[1][i][5])+"\nVida:"+str(mala[1][i][7])+"\n")
        if(mala[1][i][5]!="consumivel de aprimoramento" and mala[1][i][6]!="consumivel"):
            print("\nNome:"+str(mala[1][i][0])+"\nTipo:"+str(mala[1][i][5])+"\nAtaque:"+str(mala[1][i][1])+"\nDefesa:"+str(mala[1][i][2])+"\nAgilidade:"+str(mala[1][i][3])+"\nSorte:"+str(mala[1][i][4])+"\n")
        while 1:
            print("Posso comprar por "+str(mala[1][i][6]*0.5)+"Reais.")
            time.sleep(0.5)
            print("Vai querer vender?(sim ou nao)")
            acao_do_personagem=raw_input("-")
            acao_do_personagem=acao_do_personagem.lower()
            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                break
            else:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    personagem_jogador[7] = personagem_jogador[7] + mala[1][i][6]*porcentagem_inflacao
                    mala[1][i]=espaco_vazio
                    print("Obrigado!")
                    time.sleep(0.5)
                    break
                else:
                    print("ENTRADA INVÁLIDA!")
                    time.sleep(0.5)

#--Loja: Comprar--#
def lojaComprar():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 1:
        variavel_para_comparar=0
        i=0
        while i<=29:
            if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
                variavel_para_comparar+=1
            i+=1
        print("                      "+str(variavel_para_comparar)+" espacos livres na mochila.\n")
        variavel_para_comparar=0
        print("Produtos a venda:\n")
        time.sleep(0.5)
        i=0
        while i<=29:
            if (loja_venda[1][i]!=espaco_vazio):
                print(str(loja_venda[0][i])+" : "+str(loja_venda[1][i][0])+"\n     ("+str(loja_venda[1][i][5])+")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o número da sua posicao!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = raw_input('-')
            if acao_do_personagem.isnumeric():
                acao_do_personagem=int(acao_do_personagem)
                break
            else:
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="voltar"):break
                print("ENTRADA INVÁLIDA!")
                time.sleep(0.5)
        if(acao_do_personagem=="voltar"):break
        i=0
        while i<=29:
            if(i==acao_do_personagem):
                break
            i+=1
        i=i-1
        if(acao_do_personagem==loja_venda[0][i] and loja_venda[1][i]!=espaco_vazio):
            if(loja_venda[1][i][6]=="consumivel de aprimoramento"):
#'''Foi exatamente aqui que eu parei!
#    continue trocando virgulas por + nos prints e colocando str(objeto) em todas as variaveis que estiverem dentro dos prints
#     por exemplo str(loja_venda[1][i][6])    '''
                print("\nNome:"+str(loja_venda[1][i][0])+ "\nTipo:"+str(loja_venda[1][i][5])+"\nVida:"+str(loja_venda[1][i][7])+"\nAtaque:"+str(loja_venda[1][i][1])+"\nDefesa:"+str(loja_venda[1][i][2])+"\nAgilidade:"+str(loja_venda[1][i][3])+"\nSorte:"+str(loja_venda[1][i][4])+"\n")
            if(loja_venda[1][i][6]=="consumivel"):
                print("\nNome:"+str(loja_venda[1][i][0])+"\nTipo:"+str(loja_venda[1][i][5])+"\nVida:"+str(loja_venda[1][i][7])+"\n")
            if(loja_venda[1][i][6]!="consumivel de aprimoramento" and loja_venda[1][i][6]!="consumivel"):
                print("\nNome:"+str(loja_venda[1][i][0])+"\nTipo:"+str(loja_venda[1][i][5])+"\nAtaque:"+str(loja_venda[1][i][1])+"\nDefesa:"+str(loja_venda[1][i][2])+"\nAgilidade:"+str(loja_venda[1][i][3])+"\nSorte:"+str(loja_venda[1][i][4]+)"\n")
            item_adicionado=loja_venda[1][i]
            while 1:
                print("Deseja comprar quantos?(digite uma quantidade ou voltar)")
                acao_do_personagem = raw_input('-')
                if acao_do_personagem.isnumeric():
                    acao_do_personagem=int(acao_do_personagem)
                    variavel_para_comparar=0
                    i=0
                    while i<=29:
                        if(mala[1][i]==espaco_vazio or mala[1][i][0]=="Nada"):
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
                    print("ENTRADA INVÁLIDA!")
                    time.sleep(0.5)
            if(acao_do_personagem=="voltar"):break
            while 1:
                print("Ficou "+str(item_adicionado[6]*quantidade_adicionada)+"Reais.")
                print("Vai comprar mesmo?(sim ou nao)")
                acao_do_personagem=raw_input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                    break
                else:
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        if(personagem_jogador[7] >= item_adicionado[6]*quantidade_adicionada*porcentagem_inflacao):
                            personagem_jogador[7] = personagem_jogador[7] - item_adicionado[6]*quantidade_adicionada*porcentagem_inflacao
                            adicionaItem()
                            print("Obrigado!")
                            time.sleep(0.5)
                            break
                        else:
                            print("Voce nao tem grana pra pagar!")
                            time.sleep(0.5)
                            break
                    else:
                        print("ENTRADA INVÁLIDA!")
                        time.sleep(0.5)

#--Ficha do Personagem--#
def ficha_personagem():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    print("\n#"+"-"*30+"#\n"+"\nNome:"+str(personagem_jogador[0]))
    time.sleep(0.23)
    print("\nVida:"+str(personagem_jogador[6])+"de"+str(personagem_jogador[5]))
    time.sleep(0.23)
    print("\nAtaque:"+str(personagem_jogador[1])+"\nDefesa:"+str(personagem_jogador[2])+"\nAgilidade:"+str(personagem_jogador[3])+"\nSorte:"+str(personagem_jogador[4]))
    time.sleep(0.23)
    print("\nCapa:"+str(equipado_capa[0])+"\nRoupa:"+str(equipado_roupa[0])+"\nCalcados:"+str(equipado_calcado[0]))
    time.sleep(0.23)
    print("\nLuvas:"+str(equipado_luva[0])+"\nAnel:"+str(equipado_anel[0])+"\nArmamento:"+str(equipado_maos[0]))
    time.sleep(0.23)
    print("\nDinheiro:"+str(personagem_jogador[7])+"Reais\n")
    time.sleep(0.23)
    print("\n#"+"-"*30+"#\n")
    time.sleep(0.23)

#--Save--#
def save():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    ficha_personagem()
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
            print("\nEspaco  0:     Lugar:"+str(mostrar_save[5])+"\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str(mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save01.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  1:     Lugar:"+str(mostrar_save[5])+"\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str(mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save02.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  2:     Lugar:"+str(mostrar_save[5])+"\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save03.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  3:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save04.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  4:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save05.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  5:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save06.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  6:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save07.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  7:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save08.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  8:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            arq = open('\espaco_save09.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaco  9:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11]))
            arq.close
            while 1:
                print("\n(Digite um número entre 0 e 9)")
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
            mostrar_save = ("  Nome:"+str( personagem_jogador[0])+ "  Vida:"+str( personagem_jogador[5])+"  Lugar:"+str( variavel_lugar)+ "  Ataque:"+str( personagem_jogador[1])+ "  Defesa:"+str( personagem_jogador[2])+"  Agilidade:"+str( personagem_jogador[3]))
            pickle.dump(mostrar_save, arq)
            pickle.dump(equipado_roupa, arq)
            pickle.dump(equipado_capa, arq)
            pickle.dump(equipado_luva, arq)
            pickle.dump(equipado_anel, arq)
            pickle.dump(equipado_maos, arq)
            pickle.dump(equipado_calcado, arq)
            pickle.dump(variavel_cenario, arq)
            pickle.dump(objeto, arq)
            pickle.dump(situacao, arq)
            pickle.dump(temporario, arq)
            pickle.dump(variavel_lugar, arq)
            pickle.dump(ponto_de_save, arq)
            pickle.dump(personagem_jogador, arq)
            pickle.dump(personagem_reserva, arq)
            pickle.dump(personagem_inimigo, arq)
            pickle.dump(mala, arq)
            arq.close
            print("\nPronto!\n")
            break
        else:
            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                break
            else:
                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                time.sleep(0.5)

#--Sistema de batalha--#
def batalha():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    print("\nBatalha!!!\nÉ hora da briga!!!\n")
    time.sleep(4)
    contador_de_rodadas=1
    while(personagem_inimigo[6]>0):
        if(personagem_jogador[6]<=0):
            break
        print("\n]]"+ "="*30+"[[\n"+"    Inicio da rodada número "+str(contador_de_rodadas)+"\n]]"+"="*30+"[[\n")
        if(personagem_jogador[6]==1):
            if(contador_de_rodadas==1):
                print("\nVoce entrou na batalha com apenas 1 ponto de vida!")
                time.sleep(1)
                print("Seu último recurso e a tensao!\n")
                time.sleep(1)
            else:
                if(contador_de_batalha==0):
                    print("\nVoce esta com apenas 1 ponto de vida!")
                    time.sleep(1)
                    print("Seu último recurso e a tensao!\n")
                    time.sleep(1)
            if(contador_de_batalha>0):       
                print("\nVoce aguentou mais uma rodada com apenas 1 ponto de vida!")
                time.sleep(1)
                print("Voce extendeu o limite do seu fôlego e agora o limite dos seus pontos de vida subiu!\n")
                time.sleep(2)
                personagem_jogador[5]=personagem_jogador[5]+((contador_de_batalha)+(random.randrange(personagem_jogador[2])))
            contador_de_batalha=contador_de_batalha+1
        else:
            if(personagem_jogador[6]<=personagem_jogador[5]*0.05):
                teste_de_sorte=random.randrange(150)
                if(teste_de_sorte<=10+personagem_jogador[4]):
                    print("\nVoce esta dando o seu melhor para aguentar, isso esta melhorando o seu fôlego!")
                    time.sleep(1)
                    print("O limite dos seus pontos de vida aumentou!\n")
                    time.sleep(2)
                    personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[2])+1)
        print("\n#"+"-"*30+"#\n"+"\n\n"+str(personagem_jogador[0])+":\n                    "+str(personagem_jogador[6])+"\n                     de"+str(personagem_jogador[5])+" Pontos de Vida\n\n"+str(personagem_inimigo[0])+":\n                    "+str(personagem_inimigo[6])+"\n                     de"+str(personagem_inimigo[5])+" Pontos de vida\n")
        time.sleep(0.1)
        print("\n#"+"-"*30+"#\nO que voce fara agora, "+str(personagem_jogador[0])+"?\nAtacar, defender ou fugir?")
        time.sleep(0.15)
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        while True:
            if(acao_do_personagem != "atacar" and acao_do_personagem != "defender" and acao_do_personagem != "fugir" and acao_do_personagem!="f" and acao_do_personagem!="fugri" and acao_do_personagem!="fguir" and acao_do_personagem!="fugeir" and acao_do_personagem!="furig" and acao_do_personagem!="fuer" and acao_do_personagem!="ffugri" and acao_do_personagem!="gfuir" and acao_do_personagem!="fiur" and acao_do_personagem!="fugi" and acao_do_personagem!="fugr" and acao_do_personagem!="fug" and acao_do_personagem!="fgir" and acao_do_personagem!="fir" and acao_do_personagem!="fgr" and acao_do_personagem!="ugir" and acao_do_personagem!="gir" and acao_do_personagem!="figr" and acao_do_personagem!="fu" and acao_do_personagem != "d" and acao_do_personagem != "defende" and acao_do_personagem != "defern" and acao_do_personagem != "defenrede" and acao_do_personagem != "ddefender" and acao_do_personagem != "defenrd" and acao_do_personagem != "deffender" and acao_do_personagem != "defendder" and acao_do_personagem != "ddeffender" and acao_do_personagem != "defnder" and acao_do_personagem != "defndr" and acao_do_personagem != "dfnder" and acao_do_personagem != "dfendr" and acao_do_personagem != "defnde" and acao_do_personagem != "defnd" and acao_do_personagem != "dfede" and acao_do_personagem != "def" and acao_do_personagem!="a" and acao_do_personagem!="at" and acao_do_personagem!="ata" and acao_do_personagem!="atac" and acao_do_personagem!="ataca" and acao_do_personagem!="atcar" and acao_do_personagem!="tacar" and acao_do_personagem!="aacar" and acao_do_personagem!="ataar" and acao_do_personagem!="atacr" and acao_do_personagem!="acar" and acao_do_personagem!="aaar" and acao_do_personagem!="aacr" and acao_do_personagem!="aaca" and acao_do_personagem!="atar" and acao_do_personagem!="atcr" and acao_do_personagem!="atca" and acao_do_personagem!="ata" and acao_do_personagem!="ataa" and acao_do_personagem!="atara" and acao_do_personagem!="stssr" and acao_do_personagem!="atavar" and acao_do_personagem!="atahvea" and acao_do_personagem!="atrex" and acao_do_personagem!="atasfa" and acao_do_personagem!="atacart" and acao_do_personagem!="taacar" and acao_do_personagem!="tacaar" and acao_do_personagem!="tacara" and acao_do_personagem!="aactar" and acao_do_personagem!="aacatr" and acao_do_personagem!="aacart" and acao_do_personagem!="aatcar" and acao_do_personagem!="cataar" and acao_do_personagem!="taaacar" and acao_do_personagem!="catar" and acao_do_personagem!="rataca" and acao_do_personagem!="atraca" and acao_do_personagem!="atracar"):
                print("\nComando invalido! Voce so pode atacar, defender ou fugir!\n")
                time.sleep(1)
                acao_do_personagem = raw_input("-")
                acao_do_personagem = acao_do_personagem.lower()
            else: break
        contador_de_rodadas=contador_de_rodadas+1
        if(acao_do_personagem == "defender" or acao_do_personagem == "d" or acao_do_personagem == "defende" or acao_do_personagem == "defern" or acao_do_personagem == "defenrede" or acao_do_personagem == "ddefender" or acao_do_personagem == "defenrd" or acao_do_personagem == "deffender" or acao_do_personagem == "defendder" or acao_do_personagem == "ddeffender" or acao_do_personagem == "defnder" or acao_do_personagem == "defndr" or acao_do_personagem == "dfnder" or acao_do_personagem == "dfendr" or acao_do_personagem == "defnde" or acao_do_personagem == "defnd" or acao_do_personagem == "dfede" or acao_do_personagem == "def"): #defesa(2personagem_jogador[2]) vs ataque(personagem_inimigo[1])
            print("\nPostura de Batalha:\n"+str(personagem_jogador[0])+"\n----------> defensiva\n\n"+str(personagem_inimigo[0])+"\n----------> ofensiva\n\n")
            time.sleep(2)
            teste_de_sorte = random.randrange(50)
            if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_defesa(3personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                print("\nSua postura de defesa te favoreceu!\n")
                time.sleep(2)
                teste_de_sorte = random.randrange(40)
                if (teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#S_defesa(3personagem_jogador[2]) vs S_ataque(2personagem_inimigo[1])
                    print("\n... Mas o ataque do inimigo foi critico!\n")
                    time.sleep(2)
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVoce conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em voce!")
                        time.sleep(2)
                    else:
                        calculo_do_dano = (2*personagem_inimigo[1])+(random.randrange(personagem_inimigo[1]))*(0.2)-(3*personagem_jogador[2])-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano < 0):#S_defesa(3personagem_jogador[2]) CONTRA-ATACA S_ataque(2personagem_inimigo[1])
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nNao importa, sua defesa e incrivel!")
                            time.sleep(2)
                            print("Alem de defender voce conseguiu contra-atacar, causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                            time.sleep(3)
                            teste_de_sorte = random.randrange(5)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variavel_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variavel_para_comparar < personagem_jogador[2]):
                                        print("\nVoce testou o seu limite e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(2)
                                    if (variavel_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variavel_para_comparar
                            if(teste_de_sorte>=4):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            if(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            if(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte==10+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if (calculo_do_dano == 0):#S_defesa(3personagem_jogador[2]) ANULA S_ataque(2personagem_inimigo[1])
                                print("\nDefesa e ataque se anulam! A tensao aumenta!\n")
                                time.sleep(2)
                            else:#S_defesa(3personagem_jogador[2]) APANHA DO S_ataque(2personagem_inimigo[1])
                                print("\nVoce sofreu "+str(calculo_do_dano)+" pontos de dano...\n")
                                time.sleep(2)
                                personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                else:#S_defesa(3personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVoce conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em voce!")
                        time.sleep(2)
                    else:
                        calculo_do_dano = (personagem_inimigo[1])+(random.randrange(personagem_inimigo[1]))*(0.2)-(3*personagem_jogador[2])-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano<0):#S_defesa(3personagem_jogador[2]) CONTRA-ATACA ataque(personagem_inimigo[1])
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nSua defesa foi tao grande que, alem de bloquear o ataque, voce conseguiu contra-atacar, causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                            time.sleep(2)
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if (calculo_do_dano ==0):#S_defesa(3personagem_jogador[2]) ANULA ataque(personagem_inimigo[1])
                                print("\nSua defesa foi completa!\n")
                                time.sleep(2)
                            else:#S_defesa(3personagem_jogador[2]) APANHA DO ataque(personagem_inimigo[1])
                                print("\nVoce sofreu miseros "+str(calculo_do_dano)+" pontos de dano.\n")
                                time.sleep(2)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
            else:
                teste_de_sorte = random.randrange(40)
                if(teste_de_sorte<=10-personagem_jogador[4]+personagem_inimigo[4]):#defesa(2personagem_jogador[2]) vs S_ataque(2personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVoce conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em voce!")
                        time.sleep(2)
                    else:
                        calculo_do_dano = 2*personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))*(0.2)-(1.5)*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano<0):
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nSua defesa e simplesmente  I M E N S A !")
                            time.sleep(2)
                            print("O inimigo avancou furiosamente mas voce o lancou para tras e contra-atacou causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                            time.sleep(3)
                            teste_de_sorte = random.randrange(6)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variavel_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variavel_para_comparar < personagem_jogador[2]):
                                        print("\nVoce testou o seu limite e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(2)
                                    if (variavel_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variavel_para_comparar
                            if(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=40+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            if(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            if(teste_de_sorte==4):
                                teste_de_sorte = random.randrange(300)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            if(teste_de_sorte>=5):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=10+personagem_jogador[4]):
                                    variavel_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+(random.randrange(personagem_jogador[1]))
                                    if (variavel_para_comparar < personagem_jogador[2]):
                                        print("\nVoce testou o seu limite e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(2)
                                    if (variavel_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variavel_para_comparar
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if(calculo_do_dano==0):
                                print("\nVoce surpreendeu o inimigo que estava confiante,")
                                time.sleep(2)
                                print("suas forcas se anularam numa estrondosa colisao!\n")
                                time.sleep(2)
                                teste_de_sorte=random.randrange(300)
                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nA liberacao de energia durante a colisao despertou novos limites para sua forca e agora esta mais forte!")
                                    time.sleep(3)
                                    print("TODOS os seus pontos subiram!\n")
                                    time.sleep(3)
                                    personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[5]))+3
                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                else:#defesa(2personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVoce conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em voce!")
                        time.sleep(2)
                    else:
                        calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-2*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                        if (calculo_do_dano<0):
                            calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(personagem_jogador[1]))/2)
                            print("\nSua defesa É ENORME!")
                            time.sleep(2)
                            print("Voce barrou o ataque naturalmente e contra-atacou, causando "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                            time.sleep(3)
                            teste_de_sorte = random.randrange(5)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variavel_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variavel_para_comparar < personagem_jogador[2]):
                                        print("\nVoce testou o seu limite e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(2)
                                    if (variavel_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variavel_para_comparar
                            elif(teste_de_sorte>=4):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=40+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            elif(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            elif(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(300)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                    time.sleep(2)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(2)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if(calculo_do_dano==0):
                                print("\nVoce barrou o ataque do inimigo!\n")
                                time.sleep(2)
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(3)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
        else:
            if (acao_do_personagem=="atacar" or acao_do_personagem=="a" or acao_do_personagem=="at" or acao_do_personagem=="ata" or acao_do_personagem=="atac" or acao_do_personagem=="ataca" or acao_do_personagem=="atcar" or acao_do_personagem=="tacar" or acao_do_personagem=="aacar" or acao_do_personagem=="ataar" or acao_do_personagem=="atacr" or acao_do_personagem=="acar" or acao_do_personagem=="aaar" or acao_do_personagem=="aacr" or acao_do_personagem=="aaca" or acao_do_personagem=="atar" or acao_do_personagem=="atcr" or acao_do_personagem=="atca" or acao_do_personagem=="ata" or acao_do_personagem=="ataa" or acao_do_personagem=="atara" or acao_do_personagem=="stssr" or acao_do_personagem=="atavar" or acao_do_personagem=="atahvea" or acao_do_personagem=="atrex" or acao_do_personagem=="atasfa" or acao_do_personagem=="atacart" or acao_do_personagem=="taacar" or acao_do_personagem=="tacaar" or acao_do_personagem=="tacara" or acao_do_personagem=="aactar" or acao_do_personagem=="aacatr" or acao_do_personagem=="aacart" or acao_do_personagem=="aatcar" or acao_do_personagem=="cataar" or acao_do_personagem=="taaacar" or acao_do_personagem=="catar" or acao_do_personagem=="rataca" or acao_do_personagem=="atraca" or acao_do_personagem=="atracar"):
                teste_de_sorte=random.randrange(2)
                if (teste_de_sorte==1):#ataque(personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                    print("\nPostura de Batalha:\n"+str(personagem_jogador[0])+"\n----------> ofensiva\n\n"+str(personagem_inimigo[0])+"\n----------> defensiva\n\n")
                    time.sleep(2)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                        print("\nSeu ataque foi critico!!!\n")
                        time.sleep(2)
                        teste_de_sorte=random.randrange(50)
                        if (teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#S_ataque(2personagem_jogador[1]) vs S_defesa(3personagem_inimigo[2])
                            print("\nApesar do seu critico, voce e pressionado pela postura de defesa do seu inimigo!\n")
                            time.sleep(3)
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, voce nem pôde tocar no inimigo!")
                                time.sleep(2)
                            else:
                                calculo_do_dano=2*personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-3*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if (calculo_do_dano<0):#S_ataque(2personagem_jogador[1]) APANHA DE S_defesa(3personagem_inimigo[2])
                                    calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nPor mais que tente, voce nao consegue atravessar a defesa do seu inimigo!")
                                    time.sleep(2)
                                    print("Alem de te bloquear, ele te contra-atacou, causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                                    teste_de_sorte=random.randrange(200)
                                    if(teste_de_sorte<=20+personagem_jogador[4]):
                                        print("\nVoce tentou ao maximo ultrapassar a defesa do seu inimigo, exigiu muito dos seus músculos que se fortaleceram!\n")
                                        time.sleep(3)
                                        print("\nSeus pontos de ataque subiram!\n")
                                        time.sleep(2)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+3
                                else:
                                    if (calculo_do_dano==0):#S_ataque(2personagem_jogador[1]) ANULA S_defesa(3personagem_inimigo[2])
                                        print("\nA disputa de forcas e intensa, voce e seu inimigo deram o melhor de si, mas nenhum dos dois se sobrepôs!\n")
                                        time.sleep(3)
                                    else:#S_ataque(2personagem_jogador[1]) ATACA S_defesa(3personagem_inimigo[2])
                                        print("\nSeu ataque foi explosivo!")
                                        time.sleep(2)
                                        print("Nem o melhor da defesa do seu inimigo foi capaz de conter sua ira!")
                                        time.sleep(2)
                                        print("Voce causou "+str(calculo_do_dano)+" pontos de dano ao seu inimigo!\n")
                                        time.sleep(2)
                                        personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte==10+personagem_jogador[4]):
                                            print("\nA explosao de energia dos seus músculos os expandiu definitivamente!\n")
                                            time.sleep(2)
                                            print("\nSeus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                        else:#S_ataque(2personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, voce nem pôde tocar no inimigo!")
                                time.sleep(2)
                            else:
                                calculo_do_dano = 2*personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-2*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if(calculo_do_dano<0):#S_ataque(2personagem_jogador[1]) APANHA DE defesa(2personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nVoce deu o seu maximo, mas mesmo assim nem se equiparou às habilidades de auto-defesa do seu inimigo!")
                                    time.sleep(3)
                                    print("Sem fazer muito esforco ele se defendeu e contra-atacou, te causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(3)
                                    personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#S_ataque(2personagem_jogador[1]) ANULA defesa(2personagem_inimigo[2])
                                        print("\nVoce assustou o inimigo por um instante, mas - por muito pouco - ele conseguiu barrar todos os seus movimentos ofensivos...\n")
                                        time.sleep(3)
                                    else:
                                        teste_de_sorte=random.randrange(50)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):#XS_ataque(3personagem_jogador[1]) vs defesa(personagem_inimigo[2])
                                            print("\nVoce rompeu a defesa do seu inimigo, causando "+str(calculo_do_dano)+" pontos de dano!")
                                            time.sleep(3)
                                            print("\nSuper Critico!!!\n")
                                            time.sleep(4)
                                            print("Voce iniciou um ataque em frenesi!!!\n")
                                            time.sleep(2)
                                            personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                            teste_de_sorte=random.randrange(9)+1
                                            while(teste_de_sorte>0):#XS_ataque(3personagem_jogador[1]) ATACA defesa(personagem_inimigo[2])
                                                calculo_do_dano=2*(random.randrange(personagem_jogador[1]))-(random.randrange(personagem_inimigo[2]))
                                                while(calculo_do_dano<=0):
                                                    calculo_do_dano=2*(random.randrange(personagem_jogador[1]))-(random.randrange(personagem_inimigo[2]))
                                                print(str(calculo_do_dano)+" pontos de dano!\n")
                                                time.sleep(0.25)
                                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                                teste_de_sorte=teste_de_sorte-1
                                            print("\nVoce desferiu toda sua fúria no inimigo!\n")
                                            time.sleep(2)
                                            teste_de_sorte=random.randrange(3)
                                            if(teste_de_sorte<=1):
                                                teste_de_sorte=random.randrange(100)
                                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                                    print("\nVoce testou o seu limite e agora esta mais forte!")
                                                    time.sleep(2)
                                                    print("Seus pontos de ataque subiram!\n")
                                                    time.sleep(2)
                                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                            if(teste_de_sorte>=2):
                                                teste_de_sorte=random.randrange(100)
                                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                                    print("\nVoce ultrapassou o seu limite e agora esta mais forte!")
                                                    time.sleep(2)
                                                    print("Seus pontos de ataque subiram!\n")
                                                    time.sleep(2)
                                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+3
                                        else:#S_ataque(2personagem_jogador[1]) ATACA defesa(2personagem_inimigo[2])
                                            print("\nSeu ataque de goes duplos pressionaram a defesa do seu inimigo, causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                            time.sleep(3)
                                            teste_de_sorte=random.randrange(200)
                                            if(teste_de_sorte<=20+personagem_jogador[4]):
                                                print("\nVoce aprimorou o ritmo dos seus ataques e agora esta mais forte!")
                                                time.sleep(2)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(2)
                                                personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                            personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                    else:#ataque(personagem_jogador[1])
                        teste_de_sorte=random.randrange(50)
                        if(teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#ataque(personagem_jogador[1]) vs S_defesa(3personagem_inimigo[2])
                            print("\nA postura de defesa do seu inimigo te colocou numa situacao dificil!\n")
                            time.sleep(2)
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, voce nem pôde tocar no inimigo!")
                                time.sleep(2)
                            else:
                                calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-3*personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                                if(calculo_do_dano<0):#ataque(personagem_jogador[1]) APANHA DE S_defesa(3personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nÉ muito dificil passar por tamanha defesa, seu ataque foi infimo, alem de ser inutilizado, voce sofreu represalia...")
                                    time.sleep(3)
                                    print("Seu inimigo contra-atacou, causando "+str(calculo_do_dano)+" pontos de dano.\n")
                                    time.sleep(2)
                                    teste_de_sorte=random.randrange(100)
                                    if(teste_de_sorte<=10+personagem_jogador[4]):
                                        print("\nVoce testou o seu limite e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de ataque subiram!\n")
                                        time.sleep(2)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                    personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#ataque(personagem_jogador[1]) ANULA S_defesa(3personagem_inimigo[2])
                                        print("\nO inimigo mal consegue reter seus golpes, mas o suficiente para para-lo.")
                                        time.sleep(2)
                                        print("Ao mesmo tempo sua forca foi o bastante para evitar um contra-ataque!\n")
                                        time.sleep(2)
                                    else:#ataque(personagem_jogador[1]) ATACA S_defesa(3personagem_inimigo[2])
                                        print("\nDepois de alguns golpes, voce tornou insignificante a vantagem defensiva do seu inimigo, \ncausando humilhantes, "+str(calculo_do_dano)+" pontos de dano a ele!\n")
                                        time.sleep(4)
                                        teste_de_sorte=random.randrange(200)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):
                                            print("\nVoce testou o seu limite e agora esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                        personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                        else:#ataque(personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, voce nem pôde tocar no inimigo!")
                                time.sleep(2)
                            else:
                                calculo_do_dano = personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-2*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if(calculo_do_dano<0):#ataque(personagem_jogador[1]) APANHA DE defesa(2personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nO inimigo se defendeu e contra-atacou, te causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                    time.sleep(2)
                                    teste_de_sorte=random.randrange(100)
                                    if(teste_de_sorte<=10+personagem_jogador[4]):
                                        print("\nVoce descobriu mais sobre a sua forca durante a disputa e agora esta mais forte!")
                                        time.sleep(2)
                                        print("Seus pontos de ataque subiram\n!")
                                        time.sleep(2)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                    personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#ataque(personagem_jogador[1]) ANULA defesa(2personagem_inimigo[2])
                                        print("\nSeu oponente defendeu todos os seus golpes, mas voce nao deu brecha para que ele avancasse!\n")
                                        time.sleep(2)
                                        teste_de_sorte=random.randrange(200)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):
                                            print("\nO trabalho que seu inimigo te deu rendeu frutos!")
                                            time.sleep(2)
                                            print("Voce descobriu mais sobre as taticas de luta dele e esta mais forte!")
                                            time.sleep(2)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(2)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+(random.randrange(personagem_jogador[4]))+1
                                    else:#ataque(personagem_jogador[1]) ATACA defesa(2personagem_inimigo[2])
                                        print("\nVoce acertou o inimigo durante a disputa de forcas, causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(2)
                                        personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                    print("\nPostura de Batalha:\n"+str(personagem_jogador[0])+"\n----------> ofensiva\n\n"+str(personagem_inimigo[0])+"\n----------> ofensiva\n\n")
                    time.sleep(2)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                        print("\nSeu ataque foi critico!!!\n")
                        time.sleep(2)
                        teste_de_sorte=random.randrange(40)
                        if (teste_de_sorte<=10-personagem_jogador[4]+personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs S_ataque(2personagem_inimigo[1])
                            print("\nMas o ataque do oponente tambem foi critico!!!\n")
                            time.sleep(2)
                            print("\nVoces entraram na briga pra valer!")
                            time.sleep(1)
                            print("Avancaram de punhos cerrados, trocando golpes com as defesas abertas!\n")
                            time.sleep(2)
                            calculo_do_dano=2*personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVoce causou significativos "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                                time.sleep(2)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                teste_de_sorte=random.randrange(100)
                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nSeus pontos de ataque subiram enquanto voce forcava os seus músculos!\n")
                                    time.sleep(2)
                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=2*personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nEnquanto o oponente te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
                        else:#S_ataque(2personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                            print("\nVoce avancou violentamente sobre o inimigo, pressionando-o sem compaixao!")
                            time.sleep(3)
                            print("Apesar de forcar um leve recuo do inimigo, voce nao deixou de levar uns bons golpes!\n")
                            time.sleep(3)
                            calculo_do_dano=2*personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVoce golpeou o inimigo ate lhe causar "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nJa o inimigo causou apenas "+str(calculo_do_dano)+" pontos de dano à voce!\n")
                                time.sleep(2)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
                    else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                        teste_de_sorte=random.randrange(40)
                        if(teste_de_sorte==10+personagem_inimigo[4]-personagem_jogador[4]): #ataque(personagem_jogador[1]) vs S_ataque(2personagem_inimigo[1])
                            print("\nO ataque do oponente foi critico!...\n")
                            time.sleep(2)
                            print("\nVoce foi pressionado enquanto trocavam golpes, \nos socos e chutes do seu oponente te acertaram em pontos menos resistentes do seu corpo que estavam desprotegidos!")
                            time.sleep(4)
                            print("Mesmo assim voce manteve um bom ritmo de ataque!\n")
                            time.sleep(2)
                            calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVoce infringiu "+str(calculo_do_dano)+" pontos de dano ao inimigo!\n")
                                time.sleep(2)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=2*personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nEnquanto o seu inimigo te agrediu violentamente, causando "+str(calculo_do_dano)+" pontos de dano à voce!\n")
                                time.sleep(2)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
                        else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                            print("\nVoces se atacaram num ritmo leve, parecem estar testando um ao outro,\n ficou claro que nenhum dos dois mostrou tudo o que e capaz.\n")
                            time.sleep(4)
                            calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVoce feriu seu oponente em "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituicao do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(3)
                            calculo_do_dano=personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nSeu inimigo te golpeou causando "+str(calculo_do_dano)+" pontos de dano!\n")
                                time.sleep(2)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(3)
            else:
                if(acao_do_personagem=="fugir" or acao_do_personagem=="f" or acao_do_personagem=="fugri" or acao_do_personagem=="fguir" or acao_do_personagem=="fugeir" or acao_do_personagem=="furig" or acao_do_personagem=="fuer" or acao_do_personagem=="ffugri" or acao_do_personagem=="gfuir" or acao_do_personagem=="fiur" or acao_do_personagem=="fugi" or acao_do_personagem=="fugr" or acao_do_personagem=="fug" or acao_do_personagem=="fgir" or acao_do_personagem=="fir" or acao_do_personagem=="fgr" or acao_do_personagem=="ugir" or acao_do_personagem=="gir" or acao_do_personagem=="figr" or acao_do_personagem=="fu"):
                    print("\nPostura de Batalha:\n"+str(personagem_jogador[0])+"\n----------> fugitiva\n\n"+str(personagem_inimigo[0])+"\n-----------> ofensiva\n\n")
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
                        while(batalha_escapar != "nao"):
                            batalha_escapar = raw_input('-')
                            batalha_escapar = batalha_escapar.lower()
                            if(batalha_escapar!="nao" and batalha_escapar != "sim"):
                                print('\nEntrada invalida! Digite "sim" ou "nao".\n')
                                time.sleep(1)
                            if(batalha_escapar =="sim"):
                                break
                        if(batalha_escapar =="sim"):
                            break
                    else:
                        if(teste_de_sorte>8):
                            print('\nVoce esquivou de qualquer manobra ofensiva do oponente, mas nao conseguiu uma brecha para fugir...\n')
                            time.sleep(3)
                        else:
                            if(teste_de_sorte>5):
                                print('\nVoce nao conseguiu uma brecha para fugir, nem pode se esquivar, mas pode se defender!\n')
                                time.sleep(3)
                                calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-2*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                if (calculo_do_dano<0):
                                    print('\nSua defesa É ENORME!')
                                    time.sleep(2)
                                    print('Voce barrou o ataque naturalmente e conseguiu afastar o inimigo, criando uma brecha para fugir!\n')
                                    time.sleep(3)
                                    print('\nDeseja fugir da luta?("sim" ou "nao")\n')
                                    time.sleep(1)
                                    batalha_escapar=""
                                    while(batalha_escapar != "nao"):
                                        batalha_escapar = raw_input('-')
                                        batalha_escapar = batalha_escapar.lower()
                                        if(batalha_escapar!="nao" and batalha_escapar != "sim"):
                                            print('\nEntrada invalida! Digite "sim" ou "nao".\n')
                                            time.sleep(1)
                                        if(batalha_escapar =="sim"):
                                            break
                                    if(batalha_escapar =="sim"):
                                        batalha_escapar="sim"
                                        break
                                else:
                                    if(calculo_do_dano==0):
                                        print("\nVoce barrou o ataque do inimigo!\n")
                                        time.sleep(2)
                                    else:
                                        print("\nMesmo se defendendo, o impacto do ataque inimigo te causou "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(3)
                                        personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                            else:
                                if(teste_de_sorte>2):
                                    print('\nVoce nao conseguiu uma brecha para fugir, se esquivar ou se defender...\n')
                                    time.sleep(2)
                                    calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                    if (calculo_do_dano>0):
                                        print("\nVoce foi atacado diretamente, sofrendo "+str(calculo_do_dano)+" pontos de dano!\n")
                                        time.sleep(3)
                                        personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                    else:
                                        print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(3)
                                else:
                                    print('\nVoce tropecou ao tentar fugir!\n')
                                    time.sleep(2)
                                    print('\nO golpe do oponente foi critico!\n')
                                    time.sleep(2)
                                    calculo_do_dano = 2*personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                    if (calculo_do_dano>0):
                                        print("\nO inimigo aproveitou a abertura na sua defesa e te atacou violentamente, causando "+str(calculo_do_dano)+" pontos de dano.\n")
                                        time.sleep(3)
                                        personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte<=20+personagem_jogador[4]):
                                            print("\nVoce aumentou seu folego enquanto tentava escapar dos golpes que voce levou em cheio!")
                                            time.sleep(2)
                                            print("O limite dos seus pontos de vida cresceu!")
                                            time.sleep(2)
                                            personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[5]))+1
                                    else:
                                        print("\nMesmo sem se defender, sua constituicao foi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(3)
                    calculo_da_fuga=calculo_da_fuga+((personagem_jogador[3]-personagem_inimigo[3])*0.10)+((personagem_jogador[4]-personagem_inimigo[4])*0.10)
                    if(batalha_escapar =="sim"):
                        break
    batalha_escapar="nao"
    variavel_para_comparar = 0
    contador_de_batalha = 0
    contador_de_rodadas = 1
    print("\nFim da Batalha!\n")
    time.sleep(2)
    if(personagem_inimigo[6]<=0):
        print("\n"+str(personagem_inimigo[0])+" foi derrotado!\n")
        time.sleep(4)
    else:
        if(personagem_jogador[6]<=0):
            print("\nVoce foi derrotado.\n")
            time.sleep(4)
        else:
            if(batalha_escapar =="sim"):
                print("\nVoce conseguiu escapar!\n")
                time.sleep(3)
                batalha_escapar="escapou"

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

#--Seu predio: Quarto Andar--#
def seuPredioQuartoAndar():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    variavel_lugar = "seu predio, 4º andar"
    temporario[0]= False
    if(situacao[0]<5):
        print("Voce foi abordado novamente pelo morador do quarto 44...")
        time.sleep(2)
        print(" - Nos sabemos que voce nao venceu nem do 3º andar, se nao e capaz disso,\nnao e capaz de nos vencer!")
        time.sleep(2)
        print("Ele te empurrou escada abaixo... Voce perdeu 5 pontos de vida durante a queda!")
        time.sleep(2)
        personagem_jogador[6]=personagem_jogador[6]-5
        if(personagem_jogador[6]<=0):
            personagem_jogador[6]=1
    while 1:
        if(situacao[0]<5):
            print("Agora voce esta no terceiro andar.")
            time.sleep(2)
            break
        print("\n#"+"-"*30+"#\n\nLista de Acões\n\nCenario:"+str(variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#"+ "-"*30+"#\n")
        print("\nE agora, "+str(personagem_jogador[0])+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(40, 41, 42, 43 ou 44)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="40" and acao_do_personagem!="41" and acao_do_personagem!="42" and acao_do_personagem!="43" and acao_do_personagem!="44"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
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
                        print(' - Aqui no 4º andar moram os mais fortes, mas ha muita diferenca entre nos!')
                        time.sleep(2)
                        print(' - Por isso ha uma ordem para nos enfrentar, comecando por mim!')
                        time.sleep(2)
                        print(' - Como nao pegamos leve, nos apresentamos um "cartao de visita" ao oponente, para ele saber se e capaz de sobreviver.')
                        time.sleep(2)
                        personagem_inimigo = [ "Estudante Briguento do Quarto 40", 30, 15, 5, 5, 360, 360]
                        print(" - Aqui esta o meu:")
                        time.sleep(1)
                        print("\n"+str(personagem_inimigo[0])+":"+str(personagem_inimigo[5])+"pontos de vida.\nAtaque : "+str(personagem_inimigo[1])+".     Defesa : "+str(personagem_inimigo[2])+".\n")
                        time.sleep(2)
                        print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                        time.sleep(1)
                        while 1:
                            acao_do_personagem = raw_input("-")
                            acao_do_personagem = acao_do_personagem.lower()
                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                break
                            else:
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    batalha()
                                    if(personagem_jogador[6]<=0):break
                                    if(personagem_inimigo[6]>0):
                                        while (personagem_inimigo[6]>0):
                                            print(" - O que foi, desistiu?(sim ou nao)")
                                            time.sleep(1)
                                            while 1:
                                                acao_do_personagem=raw_input("-")
                                                acao_do_personagem = acao_do_personagem.lower()
                                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                    print(" - Entao vamos voltar a lutar!")
                                                    time.sleep(2)
                                                    batalha()
                                                else:
                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                        print(" - Tem certeza?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                        time.sleep(1)
                                                        acao_do_personagem=raw_input("-")
                                                        acao_do_personagem=acao_do_personagem.lower()
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - Muito obrigado pela colaboracao financeira! Ate outro dia, talvez...")
                                                            time.sleep(2)
                                                            personagem_jogador[7]=personagem_jogador[7]/2
                                                            break
                                                        else:
                                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                print(" - Entao vamos voltar a lutar!")
                                                                time.sleep(2)
                                                                batalha()
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                time.sleep(1)
                                                    else:
                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                        time.sleep(1)
                                        if(personagem_jogador[6]<=0):break
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
                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                    time.sleep(1)
                else:
                    if(acao_do_personagem=="41"):
                        if(situacao[0]==7):
                            print(' - SERÁ que voce esta PRONTO para brigar comigo, fracote??? Hahahahaha!')
                            time.sleep(2)
                            personagem_inimigo = [ "Estudante Briguento do Quarto 41", 50, 30, 10, 10, 550, 550]
                            print(" - Aqui esta o meu cartao:")
                            time.sleep(1)
                            print("\n"+str(personagem_inimigo[0])+":"+str(personagem_inimigo[5])+"pontos de vida.\nAtaque : "+str(personagem_inimigo[1])+".     Defesa : "+str(personagem_inimigo[2])+".\n")
                            time.sleep(2)
                            print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                            time.sleep(1)
                            while 1:
                                acao_do_personagem = raw_input("-")
                                acao_do_personagem = acao_do_personagem.lower()
                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        batalha()
                                        if(personagem_jogador[6]<=0):break
                                        if(personagem_inimigo[6]>0):
                                            while (personagem_inimigo[6]>0):
                                                print(" - O que ha? Vai cair fora mesmo???(sim ou nao)")
                                                time.sleep(1)
                                                while 1:
                                                    acao_do_personagem = raw_input("-")
                                                    acao_do_personagem = acao_do_personagem.lower()
                                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                        print(" - Entao cai dentro!!!")
                                                        time.sleep(2)
                                                        batalha()
                                                    else:
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - É serio?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                            time.sleep(1)
                                                            acao_do_personagem=raw_input("-")
                                                            acao_do_personagem=acao_do_personagem.lower()
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                print(" - Hahaha! Voce nao e o primeiro que sai do desafio! Por que voce acha que tem um premio?")
                                                                time.sleep(1)
                                                                print(" - Voce pode tentar de novo se quiser compensar a perda! HAHAHAHAHA!")
                                                                time.sleep(1)
                                                                personagem_jogador[7]=personagem_jogador[7]/2
                                                                break
                                                            else:
                                                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                    print(" - Entao cai dentro!!!")
                                                                    time.sleep(2)
                                                                    batalha()
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                    time.sleep(1)
                                                        else:
                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                            time.sleep(1)
                                            if(personagem_jogador[6]<=0):break
                                            else:
                                                print(" - CARAMBA! E nao e que voce estava pronto mesmo?! Hahahaha... Tudo bem perder às vezes...")
                                                time.sleep(2)
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print(" - CARAMBA! E nao e que voce estava pronto mesmo?! Hahahaha... Tudo bem perder às vezes...")
                                            time.sleep(2)
                                            situacao[0]=situacao[0]+1
                                            break
                                    else:
                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
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
                                personagem_inimigo = [ "Estudante Briguento do Quarto 42", 90, 70, 15, 15, 790, 790]
                                print(" - Veja:")
                                time.sleep(1)
                                print("\n"+str(personagem_inimigo[0])+":"+str(personagem_inimigo[5])+"pontos de vida.\nAtaque : "+str(personagem_inimigo[1])+".     Defesa : "+str(personagem_inimigo[2])+".\n")
                                time.sleep(2)
                                print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                time.sleep(1)
                                while 1:
                                    acao_do_personagem = raw_input("-")
                                    acao_do_personagem = acao_do_personagem.lower()
                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                        break
                                    else:
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                while (personagem_inimigo[6]>0):
                                                    print(" - Voce vai fugir?(sim ou nao) Humhumhumhum...")
                                                    time.sleep(1)
                                                    while 1:
                                                        acao_do_personagem = raw_input("-")
                                                        acao_do_personagem = acao_do_personagem.lower()
                                                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                            print(" - Venha!!!")
                                                            time.sleep(2)
                                                            batalha()
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
                                                                    personagem_jogador[7]=personagem_jogador[7]/2
                                                                    break
                                                                else:
                                                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                        print(" - Venha!!!")
                                                                        time.sleep(2)
                                                                        batalha()
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                        time.sleep(1)
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                time.sleep(1)
                                                if(personagem_jogador[6]<=0):break
                                                else:
                                                    print(" - COMO?! COMO?! Voce trapaceou! EU SEI!!! Mas tudo bem, voce nao conseguira vencer o proximo, nem trapaceando MUITO!")
                                                    situacao[0]=situacao[0]+1
                                                    break
                                            else:
                                                print(" - COMO?! COMO?! Voce trapaceou! EU SEI!!! Mas tudo bem, voce nao conseguira vencer o proximo, nem trapaceando MUITO!")
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
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
                                    personagem_inimigo = [ "Estudante Briguento do Quarto 43", 180, 100, 20, 20, 1500, 1500]
                                    print(" - Mas vou te dar a honra de apreciar o meu cartao:")
                                    time.sleep(1)
                                    print("\n"+str(personagem_inimigo[0])+":"+str(personagem_inimigo[5])+"pontos de vida.\nAtaque : "+str(personagem_inimigo[1])+".     Defesa : "+str(personagem_inimigo[2])+".\n")
                                    time.sleep(2)
                                    print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                    time.sleep(1)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                            break
                                        else:
                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                batalha()
                                                if(personagem_jogador[6]<=0):break
                                                if(personagem_inimigo[6]>0):
                                                    while (personagem_inimigo[6]>0):
                                                        print(" - ... Fugindo?(sim ou nao)")
                                                        time.sleep(1)
                                                        while 1:
                                                            acao_do_personagem = raw_input("-")
                                                            acao_do_personagem = acao_do_personagem.lower()
                                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                print(" - Voce vai MORRER!!!")
                                                                time.sleep(2)
                                                                batalha()
                                                            else:
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    print(" - Vai fugir mesmo, lixo?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                                    time.sleep(1)
                                                                    acao_do_personagem=raw_input("-")
                                                                    acao_do_personagem=acao_do_personagem.lower()
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - Sao os lixos como voce que pagaram o premio que NUNCA SERÁ SEU!")
                                                                        time.sleep(1)
                                                                        print(" - Volte quando quiser apanhar mais!")
                                                                        time.sleep(1)
                                                                        personagem_jogador[7]=personagem_jogador[7]/2
                                                                        break
                                                                    else:
                                                                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                            print(" - Voce vai MORRER!!!")
                                                                            time.sleep(2)
                                                                            batalha()
                                                                        else:
                                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                            time.sleep(1)
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                    time.sleep(1)
                                                    if(personagem_jogador[6]<=0):break
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
                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
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
                                        print(' - Me perdôe pelo comportamento daqueles dois... Nenhum deles tem a cabeca no lugar.')
                                        time.sleep(2)
                                        print(" - Mesmo assim, e raro alguem passar do quarto 40, e rarissimo alguem chegar ate mim.")
                                        time.sleep(2)
                                        print(" - Voce e um briguento e tanto!")
                                        time.sleep(2)
                                        personagem_inimigo = [ "Estudante Briguento do Quarto 44", 300, 200, 40, 40, 3200, 3200]
                                        print(" - Vamos logo ao que interessa:")
                                        time.sleep(1)
                                        print("\n"+str(personagem_inimigo[0])+":"+str(personagem_inimigo[5])+"pontos de vida.\nAtaque : "+str(personagem_inimigo[1])+".     Defesa : "+str(personagem_inimigo[2])+".\n")
                                        time.sleep(2)
                                        print('\nDeseja prosseguir com a luta?("sim" ou "nao")\n')
                                        time.sleep(1)
                                        while 1:
                                            acao_do_personagem = raw_input("-")
                                            acao_do_personagem = acao_do_personagem.lower()
                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                break
                                            else:
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    batalha()
                                                    if(personagem_jogador[6]<=0):break
                                                    if(personagem_inimigo[6]>0):
                                                        while (personagem_inimigo[6]>0):
                                                            print(" - ... Vai abandonar a nossa luta?(sim ou nao)")
                                                            time.sleep(1)
                                                            while 1:
                                                                acao_do_personagem = raw_input("-")
                                                                acao_do_personagem = acao_do_personagem.lower()
                                                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                    print(" - Desde o inicio, eu sabia que voce nao era qualquer um!")
                                                                    time.sleep(2)
                                                                    batalha()
                                                                else:
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - Certeza, vai abandonar a última luta?(sim ou nao) ... Se voce fugir, deixara METADE DE TODO O SEU DINHEIRO conosco!")
                                                                        time.sleep(1)
                                                                        acao_do_personagem=raw_input("-")
                                                                        acao_do_personagem=acao_do_personagem.lower()
                                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                            print(" - Recupere-se e treine mais!")
                                                                            time.sleep(1)
                                                                            print(" - Estarei esperando o seu retorno!")
                                                                            time.sleep(1)
                                                                            personagem_jogador[7]=personagem_jogador[7]/2
                                                                            break
                                                                        else:
                                                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                                print(" - Ainda bem, nao quero deixar a nossa luta para depois!!!")
                                                                                time.sleep(2)
                                                                                batalha()
                                                                            else:
                                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                                time.sleep(1)
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
                                                                        time.sleep(1)
                                                        if(personagem_jogador[6]<=0):break
                                                        else:
                                                            print(" - Incrivel... Voce e um genio das batalhas! É realmente digno do premio!")
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
                                                        print(" - Incrivel... Voce e um genio das batalhas! É realmente digno do premio!")
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
                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "nao".\n')
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
        if(personagem_jogador[6]<=0):break

#--Seu predio: Terceiro Andar--#
def seuPredioTerceiroAndar():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if temporario[0]==True:
        print("Agora que voce venceu todos os lutadores do 3º andar voce subiu ao 4º.")
        time.sleep(2)
        seuPredioQuartoAndar()
    if(variavel_lugar == "seu predio, 4º andarb"):
        seuPredioQuartoAndar()
    if(personagem_jogador[6]>0):
        variavel_lugar = "seu predio, 3º andar"
        if(situacao[0]==0):
            print("Voce e abordado pelo morador do quarto 44...")
            time.sleep(2)
            print(" - E ai, voce e o morador do 13 ne?...")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print(" - Voce e um pouco azarado, rapaz! ... Ou sortudo, depende do seu ponto de vista.")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print(" - Okay, vou te explicar...")
            time.sleep(2)
            print(" - Voce sabe que nos dois últimos andares desse predio, o terceiro e o quarto,")
            time.sleep(2)
            print("so tem quartos de estudantes briguentos, e nos estamos desafiando outros\n arruaceiros a lutarem conosco!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print(" - Claro, se voce vencer de todos nos, sera recompensado!")
            time.sleep(2)
            print(" - Va em frente, visite um dos quartos para lutar com um de nos!")
            time.sleep(2)
            print(" - Eu estarei la em cima, no meu quarto, te esperando.")
            time.sleep(2)
            print("\nEle subiu as escadas...")
            time.sleep(2)
            print("...")
            time.sleep(1)
            situacao[0]+=1
        else:
            if(situacao[0]==1):
                print("Voce ainda nao venceu nenhuma luta do desafio dos estudantes briguentos!")
                time.sleep(1)
            else:
                if(situacao[0]==2):
                    print("Voce ja venceu 1 luta do desafio dos estudantes briguentos!")
                    time.sleep(1)
                else:
                    if(situacao[0]>=3 and situacao[0]<6):
                        print("Voce ja venceu"+str(situacao[0]-1)+"lutas do desafio dos estudantes briguentos!")
                        time.sleep(1)
                    else:
                        if(situacao[0]<11):
                            print("Voce ja venceu todas as lutas do terceiro andar, \nentao voce continuou subindo para o 4º andar.")
                            time.sleep(1)
                            seuPredioQuartoAndar()
                            variavel_lugar = "seu predio, 3º andar"
                        else:
                            print("Voce ja venceu o desafio dos estudantes briguentos do seu predio!")
                            time.sleep(2)
    while 1:
        if(personagem_jogador[6]<=0):break
        if(situacao[0]>=11):
            variavel_lugar = "seu predio, 2º andar"
            break
        else:
            if(situacao[0]>6):
                print("Como voce ja venceu as lutas aqui, voce continuou descendo...")
                time.sleep(1)
                print("Voce desceu para o segundo andar.")
                time.sleep(1)
                variavel_lugar = "seu predio, 2º andar"
                break
        print("\n#"+"-"*30+"#\n\nLista de Acões\n\nCenario:"+str( variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos: 30, 31, 32, 33 e 34\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#"+"-"*30+"#\n")
        print("\nE agora, "+str(personagem_jogador[0])+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(30, 31, 32, 33 ou 34)\n")
            time.sleep(1)
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="30" and acao_do_personagem!="31" and acao_do_personagem!="32" and acao_do_personagem!="33" and acao_do_personagem!="34"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
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
                            personagem_inimigo = [ "Estudante Briguento do Quarto 30", 5, 12, 2, 2, 110, 110]
                            batalha()
                            if(personagem_jogador[6]<=0):
                                personagem_jogador[6]=1
                                print(" - Voce e fraco, se fosse uma luta no andar de cima voce teria morrido!")
                                time.sleep(1)
                                print(" - Va cuidar desses seus ferimentos e volte para lutar mais!")
                                time.sleep(1)
                            else:
                                if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                    while (personagem_inimigo[6]>0):
                                        print(" - Voce nao pode fugir das lutas, e uma regra para continuar no desafio e ganhar o premio!")
                                        time.sleep(2)
                                        batalha()
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
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
                                                temporario[0]= True
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
                                        temporario[0]= True
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
                                personagem_inimigo = [ "Estudante Briguento do Quarto 31", 13, 4, 5, 1, 130, 130]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Voce e mesmo um fracote!")
                                    time.sleep(1)
                                    print(" - Va se curar para continuar tentando subir para o quarto andar!")
                                    time.sleep(1)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Volte aqui seu fracote! Nao seja um covarde! Voce nao pode fugir de TODAS as lutas!")
                                            time.sleep(2)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
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
                                                    temporario[0]= True
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
                                            temporario[0]= True
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
                                    personagem_inimigo = [ "Estudante Briguento do Quarto 32", 8, 8, 2, 1, 100, 100]
                                    batalha()
                                    if(personagem_jogador[6]<=0):
                                        personagem_jogador[6]=1
                                        print(" - Moleque criado a leite com pera!")
                                        time.sleep(1)
                                        print(" - La em cima ninguem vai te dar essa colher de cha que eu to te dando!")
                                        time.sleep(1)
                                    else:
                                        if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                            while (personagem_inimigo[6]>0):
                                                print(" - Ramelao, nao foge da luta, nao!")
                                                time.sleep(2)
                                                batalha()
                                                if(personagem_jogador[6]<=0):
                                                    personagem_jogador[6]=1
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
                                                        temporario[0]= True
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
                                                temporario[0]= True
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
                                        print(" - ÔÔô, CIDADÃO!")
                                        time.sleep(2)
                                        personagem_inimigo = [ "Estudante Briguento do Quarto 33", 10, 8, 5, 5, 120, 120]
                                        batalha()
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
                                            print(" - Olha la, o cara nao aguenta e depois vai chorando pra casa!")
                                            time.sleep(1)
                                            print(" - Se voce continuar tropecando assim, cedo ou tarde o mundo vai te atropela!")
                                            time.sleep(1)
                                        else:
                                            if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                                while (personagem_inimigo[6]>0):
                                                    print(" - Ta na hora de acordar pra vida, cidadao!")
                                                    time.sleep(2)
                                                    batalha()
                                                    if(personagem_jogador[6]<=0):
                                                        personagem_jogador[6]=1
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
                                                            temporario[0]= True
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
                                                    temporario[0]= True
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
                                            personagem_inimigo = [ "Estudante Briguento do Quarto 34", 20, 20, 6, 6, 66.6, 66.6]
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Voce nao tem um sangue fervente o suficiente para derreter o metal!")
                                                time.sleep(1)
                                                print(" - Voce precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                time.sleep(1)
                                            else:
                                                if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                                    while (personagem_inimigo[6]>0):
                                                        print(" - As mentiras ja sao antigas demais, mas voce nao quer saber!\nCorrer e uma futilidade!")
                                                        time.sleep(2)
                                                        batalha()
                                                        if(personagem_jogador[6]<=0):
                                                            personagem_jogador[6]=1
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
                                                                temporario[0]= True
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
                                                        temporario[0]= True
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
                                            time.sleep(1)
                                    else:
                                        if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                            save()
                                        else:
                                            if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                inventarioPersonagem()
                                            else:
                                                print('\nEntrada Invalida!\n')
                                                time.sleep(1)

#--Seu predio: Segundo Andar--#
def seuPredioSegundoAndar():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if(variavel_lugar == "seu predio, 3º andarb" or variavel_lugar == "seu predio, 4º andarb"):
        seuPredioTerceiroAndar()
    variavel_lugar = "seu predio, 2º andar"
    while 1:
        if(personagem_jogador[6]<=0):break
        print("\n#"+"-"*30+"#\n\nLista de Acões\n\nCenario:"+str(variavel_lugar)+"\n\nVoce pode:\n\nchecar os quartos\n")
        if(situacao[2]==1):
            print("\narrombar o quarto 24")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#"+"-"*30+"#\n")
        print("\nE agora, "+str(personagem_jogador[0])+", o que voce vai fazer?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(20, 21, 22, 23 ou 24)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="20" and acao_do_personagem!="21" and acao_do_personagem!="22" and acao_do_personagem!="23" and acao_do_personagem!="24"):
                acao_do_personagem="entrada invalida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                print("Voce subiu para o terceiro andar,")
                time.sleep(0.5)
                print("la voce encontrou cinco quartos de portas abertas e outra escada ascendente.")
                time.sleep(1)
                seuPredioTerceiroAndar()
                if(personagem_jogador[6]<=0):break
            else:
                if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                    print("Voce desceu para o primeiro andar, o andar do seu quarto.")
                    time.sleep(1)
                    break
                else:
                    if(acao_do_personagem=="20"):
                        if(situacao[3]==10):
                            print("Voce ja pegou tudo o que tinha para pegar aqui.")
                            time.sleep(0.5)
                        else:
                            print("Voce bate na porta e percebe, pelo barulho do trepidar da macaneta, que ela esta destrancada...")
                            time.sleep(2)
                            print("Abrir a porta?(sim ou nao)")
                            while 1:
                                acao_do_personagem = raw_input("-")
                                acao_do_personagem = acao_do_personagem.lower()
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    print("Voce entrou, nao havia ninguem...")
                                    time.sleep(2)
                                    print("Ao revistar o quarto voce encontrou 10 Reais!")
                                    time.sleep(1)
                                    personagem_jogador[7]=personagem_jogador[7]+10
                                    situacao[10]=1
                                    break
                                else:
                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                        print("Voce ignorou o quarto...")
                                        time.sleep(0.75)
                                        break
                                    else:
                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "nao"')
                                        time.sleep(0.5)
                    else:
                        if(acao_do_personagem=="21"):
                            if(situacao[3]==7):
                                print("Voce bate na porta...")
                                time.sleep(0.5)
                                print(" - Ola! - diz o avô do garoto - Muito obrigado por treinar o meu neto,")
                                time.sleep(1)
                                print("agora ele nao precisa se esconder mais dos trombadinhas da escola.")
                                time.sleep(2)
                            if(situacao[3]==6):
                                print(" - Obrigado por me treinar, senhor.")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto, um Homem", 1500, 1000, 50, 50, 20000, 20000]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Me supere. Estarei te esperando.")
                                    time.sleep(1)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Nao abandone nossa luta!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Me supere. Estarei te esperando.")
                                                time.sleep(1)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Obrigado, mesmo!")
                                                    time.sleep(1)
                                                    situacao[3]=7
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Obrigado, mesmo!")
                                            time.sleep(1)
                                            situacao[3]=7
                            if(situacao[3]==5):
                                print(" - Estou empolgado! Nao aguentava mais esperar pela nossa luta!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Forte", 150, 100, 20, 20, 2000, 2000]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Quando voce estiver pronto para uma revanche, me procure novamente.")
                                    time.sleep(1)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - A nossa luta nao acabou ainda!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Quando voce estiver pronto para uma revanche, me procure novamente.")
                                                time.sleep(1)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Incrivel, voce sempre me surpreende! Se prepare, da proxima vez estarei ainda mais forte!")
                                                    time.sleep(1)
                                                    situacao[3]=6
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Incrivel, voce sempre me surpreende! Se prepare, da proxima vez estarei ainda mais forte!")
                                            time.sleep(1)
                                            situacao[3]=6
                            if(situacao[3]==4):
                                print(" - Dessa vez nao vou perder tao facil!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Serio", 30, 25, 10, 5, 200, 200]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Estou te levando a serio, nao vou perder mais!")
                                    time.sleep(0.5)
                                    print(" - Estarei te esperando para uma revanche.")
                                    time.sleep(0.5)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Honre a nossa luta ate o fim!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Estou te levando a serio, nao vou perder mais!")
                                                time.sleep(0.5)
                                                print(" - Estarei te esperando para uma revanche.")
                                                time.sleep(0.5)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Voce e mesmo forte! Treinarei mais e estarei te esperando para o nosso proximo confronto!")
                                                    time.sleep(1)
                                                    situacao[3]=5
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Voce e mesmo forte! Treinarei mais e estarei te esperando para o nosso proximo confronto!")
                                            time.sleep(1)
                                            situacao[3]=5
                            if(situacao[3]==3):
                                print(" - Eu estava te esperando, panaca!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Convencido", 8, 12, 5, 10, 110, 110]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Nao aguenta o tranco, nao? Hahaha!")
                                    time.sleep(0.5)
                                    print(" - Volte qualquer hora para apanhar mais!")
                                    time.sleep(0.5)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Volte aqui seu panaca!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Nao aguenta o tranco, nao? Hahaha!")
                                                time.sleep(0.5)
                                                print(" - Volte qualquer hora para apanhar mais!")
                                                time.sleep(0.5)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Voce e mesmo forte! Continuarei treinando e esperarei o nosso proximo confronto!")
                                                    time.sleep(1)
                                                    situacao[3]=4
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Voce e mesmo forte! Continuarei treinando e esperarei o nosso proximo confronto!")
                                            time.sleep(1)
                                            situacao[3]=4
                            if(situacao[3]==2):
                                print(" - Meu avô disse que voce viria... - disse o garoto baixinho - Vamos logo ao que interessa!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Fracote", 3, 10, 2, 2, 100, 100]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Voce nao e tao forte quanto meu avô falou.")
                                    time.sleep(1)
                                    situacao[3]=3
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Meu avô disse para nao parar de lutar ate eu nao aguentar mais!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Voce nao e tao forte quanto meu avô falou.")
                                                time.sleep(1)
                                                situacao[3]=3
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Voce e muito forte!!! Vou treinar e estarei te esperando para uma proxima luta!")
                                                    time.sleep(1)
                                                    situacao[3]=3
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Voce e muito forte!!! Vou treinar e estarei te esperando para uma proxima luta!")
                                            time.sleep(1)
                                            situacao[3]=3
                            if(situacao[3]==1):
                                print("A porta esta trancada.")
                                time.sleep(1)
                            if(situacao[3]==0):
                                print("Voce bateu na porta...")
                                time.sleep(0.5)
                                print("Um senhor baixo e fracote abriu a porta... Ele parecia muito com um frango")
                                time.sleep(1)
                                print(" - O que que voce quer?!")
                                time.sleep(1)
                                print("...")
                                time.sleep(0.5)
                                print(" - Saia daqui entao!")
                                time.sleep(2)
                                personagem_inimigo = [ "Senhor Doente", 5, 3, -3, 3, 50, 50]
                                batalha()
                                if(personagem_jogador[6]<=0):break
                                if(personagem_inimigo[6]>0):
                                    print("Depois de se afastar o senhor comecou a gritar...")
                                    time.sleep(1)
                                    print("Com a mao no peito, ele comecou a tossir...")
                                    time.sleep(1)
                                    print(" - Ahhhh... - gemiu o senhor que caia lentamente.")
                                    time.sleep(1)
                                    print(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo la de dentro do quarto.")
                                    time.sleep(1)
                                    print("O menino pegou o senhor nos bracos antes que tombasse \ne apertou algumas vezes uma bombinha para asma na boca dele...")
                                    time.sleep(1)
                                    print(" - VOCÊ VAI PAGAR CARO!")
                                    time.sleep(2)
                                    personagem_inimigo = [ "Garoto Perturbado", 2, 10, 1, 1, 100, 100]
                                    batalha()
                                    if(personagem_jogador[6]<=0):break
                                    if(personagem_inimigo[6]>0):
                                        print(" - SAIA JÁ DAQUI!")
                                        time.sleep(0.5)
                                        print("Em seguida ele fechou e trancou a porta.")
                                        time.sleep(0.5)
                                        situacao[3]==1
                                    else:
                                        print("O garoto caiu no chao dentro da casa e comecou a chorar.")
                                        time.sleep(1)
                                        print(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que ja estava um pouco melhor...")
                                        time.sleep(1)
                                        print("Em seguida ele fechou e trancou a porta.")
                                        time.sleep(1)
                                        situacao[3]=1
                                else:
                                    print("O senhor caiu no chao com uma mao no peito...")
                                    time.sleep(1)
                                    print("Ele tentava gritar algo enquanto estendia a outra mao...")
                                    time.sleep(1)
                                    print("Mas nao conseguia dizer nada, estava tendo crise de asma...")
                                    time.sleep(1)
                                    print("Sua mao apontava para um lugar dentro da casa...")
                                    time.sleep(1)
                                    print("Vai ajudar o idoso?\n")
                                    time.sleep(0.5)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            print("Voce entrou na casa, pegou a bombinha em cima da mesa e a apertou na boca no velho...")
                                            time.sleep(1)
                                            print(" - Ah... Ah... - o senhor tentava recuperar o ar - Voce nao e um mau rapaz no fim das contas...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Voce gosta de lutar, nao e garoto? Eu brigava muito quando era mais jovem...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Nem sempre os punhos sao o bastante...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Nao falo do coracao na luta, isso voce ja tem, falo de armas...")
                                            time.sleep(1)
                                            print(" - Tome... Eu usava este punhal no meu tempo... Agora e seu.")
                                            time.sleep(1)
                                            item_adicionado=punhal_envelhecido
                                            quantidade_adicionada=1
                                            adicionaItem()
                                            print("Voce guardou o Punhal Envelhecido na mala!")
                                            time.sleep(1)
                                            print(" - Se nao for pedir demais, venha sempre que puder para treinar o meu neto... \nEle ainda e muito fraco e eu nao tenho mais o mesmo vigor de antes...")
                                            time.sleep(1)
                                            print(" - Nao me entenda mal, nao e uma troca de favores... \nÉ um pedido de um velho que nao consegue ajudar seu neto.")
                                            time.sleep(1)
                                            situacao[3]=2
                                            break
                                        else:
                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                print(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo la de dentro do quarto.")
                                                time.sleep(1)
                                                print("O menino pegou o senhor nos bracos antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
                                                time.sleep(1)
                                                print(" - VOCÊ VAI PAGAR CARO!")
                                                time.sleep(1)
                                                personagem_inimigo = [ "Garoto Irritado", 10, 10, 10, 10, 100, 100]
                                                batalha()
                                                if(personagem_jogador[6]<=0):break
                                                if(personagem_inimigo[6]>0):
                                                    print(" - SAIA JÁ DAQUI!")
                                                    time.sleep(1)
                                                    print("Em seguida ele fechou e trancou a porta.")
                                                    time.sleep(1)
                                                    situacao[3]=1
                                                else:
                                                    print("O garoto caiu no chao dentro da casa e comecou a chorar.")
                                                    time.sleep(1)
                                                    print(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que ja estava um pouco melhor...")
                                                    time.sleep(1)
                                                    print("Em seguida ele fechou e trancou a porta.")
                                                    time.sleep(1)
                                                    situacao[3]=1
                                                break
                                            else:
                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "nao"')
                                                time.sleep(1)
                        else:
                            if(acao_do_personagem=="22"):
                                if(situacao[4]==4):
                                    print("Voce bateu na porta...")
                                    time.sleep(0.5)
                                    print("Ninguem te atendeu.")
                                    time.sleep(0.5)
                                if(situacao[4]==3):
                                    print(" - E ai, rapaz!")
                                    time.sleep(1.5)
                                    teste_de_sorte = random.randrange(3)
                                    if(teste_de_sorte==1):
                                        print(" - Voce chegou em boa hora! Entre e coma um pedaco de pizza comigo!")
                                        time.sleep(1)
                                        print("Voce ganhou um pedaco de pizza!")
                                        time.sleep(1)
                                        item_adicionado=pedaco_pizza
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        print(" - Ate outra hora, vizinho!")
                                        time.sleep(0.5)
                                    else:
                                        print(" - Estou sem pizza agora... Talvez mais tarde...")
                                        time.sleep(1)
                                if(situacao[4]==2):
                                    print(" - O que voce quer aqui?")
                                    time.sleep(1)
                                    print("Voce vai dizer a ele que comeu a sua pizza?(sim ou nao)")
                                    time.sleep(0.5)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            print(" - ...")
                                            time.sleep(1.5)
                                            print(" - VOCÊ...")
                                            time.sleep(1.5)
                                            print(" - Voce e muito cara de pau mesmo, mas adimiro a sua sinceridade.")
                                            time.sleep(1)
                                            print(" - Eu sempre como pizza, quando voce quiser passe aqui para pegar um pedaco.")
                                            time.sleep(1)
                                            situacao[4]=3
                                            break
                                        else:
                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                print(" - ...")
                                                time.sleep(1.5)
                                                print(" - Me deixe em paz!")
                                                time.sleep(1)
                                                situacao[4]=4
                                                break
                                            else:
                                                print('Entrada invalida! Digite "sim" ou "nao".')
                                                time.sleep(0.5)
                                if(situacao[4]==1):
                                    print("Voce bateu na porta do quarto, que agora esta fechado.")
                                    time.sleep(1)
                                    print("Voce escuta passos rapidos e violentos vindo à porta")
                                    time.sleep(1)
                                    print(" - EU TO MUITO PUTO! - diz o estudante que abriu violentamente a porta - ENTRARAM E COMERAM A MINHA PIZZA!")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1.5)
                                    print(" - Ah esquece... Nem deve ter sido voce...")
                                    time.sleep(1)
                                    situacao[4]=2
                                if(situacao[4]==0):
                                    print("O quarto esta aberto, voce entra e ve um estudante vagabundo dormindo num sofa com uma pizza no colo.")
                                    time.sleep(1)
                                    print("E ai, vai pegar essa pizza? (sim ou nao)")
                                    time.sleep(0.5)
                                    while 1:
                                        acao_do_personagem = raw_input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            print("Voce guardou a pizza inteira na mochila!")
                                            time.sleep(1)
                                            item_adicionado=pedaco_pizza
                                            quantidade_adicionada=8
                                            adicionaItem()
                                            situacao[4]=1
                                            break
                                        else:
                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                print("Voce deixou a pizza para depois!")
                                                time.sleep(1)
                                                break
                                            else:
                                                print('Entrada invalida! Digite "sim" ou "nao".')
                                                time.sleep(0.5)
                            else:
                                if(acao_do_personagem=="23"):
                                   print("Voce ve um quarto aberto, sujo e vazio...")
                                   time.sleep(0.5)
                                   print("Parece abandonado por um bom tempo... Ja tem fauna e flora proria!")
                                   time.sleep(1)
                                else:
                                    if(acao_do_personagem=="24"):
                                        if(situacao[2]==0):
                                            print("Voce encara um individuo de aparencia extravagante e vulgar encostado no batente da porta...")
                                            time.sleep(1)
                                            print(" - Quale merh-mao? Ta querenu treta?")
                                            time.sleep(2)
                                            personagem_inimigo = [ "Mane de Bone", 10, 5, 10, 1, 100, 100]
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                print("Ele corre atras de voce e te da um chute no joelho!")
                                                time.sleep(1)
                                                print("!!!")
                                                time.sleep(0.5)
                                                print("Voce perdeu 30 pontos de vida!")
                                                time.sleep(1)
                                                print(" - Fica diboa rapah!")
                                                time.sleep(1)
                                                personagem_jogador[6]=personagem_jogador[6]-30
                                                if(personagem_jogador[6]<=0):personagem_jogador[6]=1
                                                print("Ele voltou ao batente da porta do quarto e agora esta te encarando...")
                                                time.sleep(1)
                                                print("Voce me envergonha.")
                                                time.sleep(1)
                                            else:
                                                print(" - Que isso maluco?! Que isso?!")
                                                time.sleep(1)
                                                print("Ele entrou cambaleando para o quarto dele e se trancou!")
                                                time.sleep(1)
                                                situacao[2]=1
                                        if(situacao[2]==1):
                                            print("O quarto esta trancado...")
                                            time.sleep(1)
                                        if(situacao[2]==2):
                                            print("Voce ve uma porta quebrada ao meio, caida, mas presa apenas pela dobradica inferior, ")
                                            time.sleep(1)
                                            print("a superior segurava apenas um pedaco de madeira desprendido da porta.")
                                            time.sleep(1)
                                            print("Dentro voce ve muito sangue pelo quarto, os poucos moveis quebrados, ")
                                            time.sleep(1)
                                            print("mas nada de valor...")
                                            time.sleep(1)
                                            matarAlguem()
                                        if(situacao[2]==3):
                                            print("Voce ve uma porta quebrada ao meio, caida, mas presa apenas pela dobradica inferior, ")
                                            time.sleep(1)
                                            print("a superior segurava apenas um pedaco de madeira desprendido da porta.")
                                            time.sleep(1)
                                            print("Tambem escuta, vindo la de dentro, solucos em sussurros e sussurros em solucos...")
                                            time.sleep(1)
                                            print("Melhor nao entrar... Nao ha nada de mais la dentro.")
                                            time.sleep(1)
                                    else:
                                        if(acao_do_personagem=="arrombar a porta do quarto 24" or acao_do_personagem=="arrombar o quarto 24" or acao_do_personagem=="arrombar" or acao_do_personagem=="arrombar a porta" or acao_do_personagem=="entrar no quarto 24"):
                                            if(situacao[2]==1):
                                                print("Voce pisoteou a porta e entrou no quarto!")
                                                time.sleep(1)
                                                print(" - Nao, por favor nao!...")
                                                time.sleep(1)
                                                while 1:
                                                    if(situacao[2]==2):
                                                        break
                                                    if(situacao[2]==3):
                                                        break
                                                    print("Melhor nao continuar...(sim ou nao)\n")
                                                    time.sleep(0.5)
                                                    acao_do_personagem=raw_input("-")
                                                    acao_do_personagem=acao_do_personagem.lower()
                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                        while 2:
                                                            print("Eu insisto... É melhor parar... Voce esta de cabeca quente... (sim ou nao)\n")
                                                            time.sleep(0.5)
                                                            acao_do_personagem=raw_input("-")
                                                            acao_do_personagem=acao_do_personagem.lower()
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                raw_input("(Aperte ENTER)")
                                                                raw_input("!!!!!!!!!!!!")
                                                                raw_input(" - NÃO, NÃO!")
                                                                raw_input("!!!!!!!!!!!!")
                                                                raw_input(" - N-NÃo..o!")
                                                                raw_input("!!!!!!!!....")
                                                                raw_input("!!!!........")
                                                                raw_input("....!!!!....")
                                                                raw_input("........!!!!")
                                                                raw_input("!!!!....!!!!")
                                                                print("(Ja nao ha mais motivos para golpear...)")
                                                                time.sleep(1)
                                                                print("Seus punhos vermelhos tremem...")
                                                                time.sleep(1)
                                                                print("Voce o espancou ate a morte...")
                                                                time.sleep(1)
                                                                print("...")
                                                                time.sleep(1)
                                                                matarAlguem()
                                                                situacao[2]=2
                                                                break
                                                            else:
                                                                if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                    print("Voce respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                                    time.sleep(1)
                                                                    print("Voce superou seus instintos e respeitou seus principios...")
                                                                    time.sleep(1)
                                                                    print("Ao recuperar seu fôlego, seus pontos de vida aumentaram.")
                                                                    time.sleep(1)
                                                                    personagem_jogador[5]=personagem_jogador[5]+50
                                                                    personagem_jogador[6]=personagem_jogador[5]
                                                                    situacao[2]=3
                                                                    break
                                                                else:
                                                                    print("Entrada invalida... A situacao e tensa, mantenha a seriedade e responda corretamente.")
                                                                    time.sleep(1)
                                                        break
                                                    else:
                                                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                            print("Voce respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                            time.sleep(1)
                                                            print("Voce superou seus instintos e respeitou seus principios...")
                                                            time.sleep(1)
                                                            print("Ao recuperar seu fôlego, voce recuperou seus pontos de vida.")
                                                            time.sleep(1)
                                                            personagem_jogador[6]=personagem_jogador[5]
                                                            situacao[2]=3
                                                            break
                                                        else:
                                                            print("Entrada invalida... A situacao e tensa, mantenha a seriedade e responda corretamente.")
                                                            time.sleep(1)
                                            if(situacao[2]==2):
                                                matarAlguem()
                                            if(situacao[2]==3):
                                                print("Voce ja fez o bastante por aqui... Melhor se afastar.")
                                                time.sleep(0.5)
                                        else:
                                            if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                                save()
                                            else:
                                                if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                    inventarioPersonagem()
                                                else:
                                                    print('\nEntrada Invalida!\n')
                                                    time.sleep(0.5)

#--Seu predio: Primeiro Andar--#
def seuPredioPrimeiroAndar():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if(variavel_lugar == "seu predio, 2º andarb" or variavel_lugar == "seu predio, 3º andarb" or variavel_lugar == "seu predio, 4º andarb"):
        seuPredioSegundoAndar()
    if(personagem_jogador[6]>0):
        variavel_lugar = "seu predio, 1º andar"
        print("Agora voce esta no corredor do primeiro andar do seu predio.")
        time.sleep(3)
        print("\n#"+"-"*30+"#\n"+"\nLista de Acões\n\nCenario:"+str(variavel_lugar)+"\n\nVoce pode:\nolhar\n")
        time.sleep(1)
        if (variavel_cenario[0] == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            time.sleep(1)
            if (variavel_cenario[2] == "sim" and objeto[0] == "nao"):
                print("olhar o bebado\n")
                time.sleep(1)
        if(objeto[1] == "sim"):
            print("\narrombar o quarto 10\n")
            time.sleep(1)
        if (objeto[0] == "1"):
            print("\nacordar o bebado\n")
            print("\nrevistar o bebado\n")
            time.sleep(1)
        if (objeto[0] == "2"):
            print("\nmover o bebado\n")
            time.sleep(1)
        if (objeto[0] == "3"):
            print("\natacar o bebado\n")
            time.sleep(1)
        if (objeto[0] == "sim"):
            print("\nabrir a porta dos fundos\n")
            time.sleep(1)
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        time.sleep(2)
        print("\nO que voce vai fazer, "+str(personagem_jogador[0])+"?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
    while 1:
        if(personagem_jogador[6]<=0):break
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(10, 11, 12 ou 14)\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="10" and acao_do_personagem!="11" and acao_do_personagem!="12" and acao_do_personagem!="13" and acao_do_personagem!="14"):
                acao_do_personagem="entrada invalida!"
        if(acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(acao_do_personagem == "olhar" or acao_do_personagem == "ver" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha" or acao_do_personagem == "olhar quarto" or acao_do_personagem == "olha quarto" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha o quarto" or acao_do_personagem == "ve" or acao_do_personagem == "ve"):
                if (variavel_cenario[2] == "1" or variavel_cenario[2] == "sim"):
                    print("Voce ve um corredor estreito com 5 portas, o seu e os outros quartos desse andar do predio.")
                    time.sleep(3)
                    print("Num dos lados desse corredor ha uma janela quebrada,")
                    time.sleep(3)
                    print("mas no outro se encontra um bebado caido no chao, imundo e cercado de vômito encostado na porta dos fundos, impedindo o acesso.")
                    time.sleep(3)
                    print("E ao longo do corredor, em frente aos quartos ha um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                    time.sleep(3)
                    print("A mais proxima sobe e a colada à parede desce.")
                    time.sleep(3)
                else:
                    if (objeto[0]=="sim" or objeto[0]=="pegou o dinheiro"):
                        print("Voce ve um corredor estreito com 5 portas, o seu e os outros quartos desse andar do predio.")
                        time.sleep(3)
                        print("Num dos lados desse corredor ha uma janela quebrada, mas no outro se encontra a porta dos fundos.")
                        time.sleep(3)
                        print("Ao longo do corredor, em frente aos quartos ha um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        time.sleep(3)
                        print("A mais proxima sobe e a colada à parede desce.")
                        time.sleep(3)
                    else:
                        print("Voce ve um corredor estreito com 5 portas, o seu e os outros quartos desse andar do predio.")
                        time.sleep(3)
                        print("Num dos lados desse corredor ha uma janela quebrada,")
                        time.sleep(3)
                        print("mas no outro se encontra, encostado na porta dos fundos e caido no chao coberto por cacos de vidro, um homem sujo, \ncercado por algum liquido que parece laranja...")
                        time.sleep(3)
                        print("E ao longo do corredor, em frente aos quartos ha um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        time.sleep(3)
                        print("A mais proxima sobe e a colada à parede desce.")
                        time.sleep(3)
                        variavel_cenario[0] = "sim"
            else:
                if(acao_do_personagem=="cheirar" or acao_do_personagem=="cherar" or acao_do_personagem=="dar um tapa" or acao_do_personagem=="cheira" or acao_do_personagem=="chera"):
                    if(variavel_cenario[2]=="nao"):
                        variavel_cenario[2]="sim"
                    print("Voce sente um cheiro forte de alcool e vômito")
                    time.sleep(3)
                else:
                    if(acao_do_personagem=="10"):
                        if(objeto[3]=="sim"):
                            print("Voce ve uma porta arrombada... Nao ha mais nada de interessante dentro do quarto.")
                            time.sleep(3)
                        else:
                            print("Voce bateu na porta, mas ninguem atendeu... Ela parece facil de ser arrombada...")
                            time.sleep(3)
                            objeto[1]="sim"
                    else:
                        if(acao_do_personagem=="11"):
                            if(situacao[1]==0):
                                print("Quando voce bateu, a porta se abriu no primeiro toque por nao ter uma fechadura...")
                                time.sleep(4)
                                print("Voce ve, dentro da casa, uma mulher alta de ombros largos, BEM LARGOS, musculosa e com o maxilar largo...")
                                time.sleep(4)
                                print("Ela estava apenas de toalha...")
                                time.sleep(2)
                                print(" - MAS QUE ATREVIMENTO! SUMA DAQUI! - diz a mulher enquanto te epurra com a porta que e fechada violentamente.")
                                time.sleep(4)
                                print("Voce perdeu 5 pontos de vida ao cair no corredor...")
                                time.sleep(3)
                                personagem_jogador[6]=personagem_jogador[6]-5
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                situacao[1]=1
                            else:
                                if(situacao[1]==1):
                                    print("Voce empurrou a porta sem fechadura, mas moradora que ainda estava te toalha, \nfuriosamente fechou a porta gritando, antes que voce pudesse terminar de abrir!")
                                    time.sleep(3)
                                    print("Voce perdeu 5 pontos de vida ao cair no corredor...")
                                    time.sleep(3)
                                    personagem_jogador[6]=personagem_jogador[6]-5
                                    if(personagem_jogador[6]<=0):
                                        personagem_jogador[6]=1
                                    situacao[1]=2
                                else:
                                    if(situacao[1]==2):
                                        print("Voce abriu a porta e levou um soco na cara, caindo em seguida no chao do corredor.")
                                        time.sleep(3)
                                        print("Voce perdeu 10 pontos de vida...")
                                        time.sleep(3)
                                        personagem_jogador[6]=personagem_jogador[6]-10
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
                                        situacao[1]=3
                                    else:
                                        if(situacao[1]==3):
                                            print("Voce abriu a porta e viu a mulher de toalha extremamente furiosa com os ombros levemente curvados, \ndeixando à mostra seus bracos musculosos e gigantescos.")
                                            time.sleep(3)
                                            print(" - VOCÊ VAI APANHAR MUITO AGORA!")
                                            time.sleep(3)
                                            personagem_inimigo = [ "Mulher de Toalha", 20, 20, 5, 5, 800, 800]
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                print(" - E NÃO VOLTE MAIS AQUI!")
                                                time.sleep(3)
                                            else:
                                                print("A mulher caiu inconsciente no chao...")
                                                time.sleep(1)
                                                print("Dentro da casa voce encontrou 100 reais e um suplemento alimenticio")
                                                time.sleep(2)
                                                print("Voce guardou ambos na mochila!")
                                                time.sleep(2)
                                                personagem_jogador[7]=personagem_jogador[7]+100
                                                quantidade_adicionada=1
                                                item_adicionado=suplemento_alimenticio
                                                adicionaItem()
                                                situacao[1]=4
                                        else:
                                            if(situacao[1]==4):
                                                print("Voce entra no quarto, encontra a mulher que voce derrotou caida no chao e mais nada alem dos moveis velhos dela.")
                        else:
                            if(acao_do_personagem=="12"):
                                print("Voce bateu na porta...")
                                time.sleep(0.5)
                                print(" - Ja vai! - exclama uma senhora de dentro da casa.")
                                time.sleep(1)
                                print("...")
                                time.sleep(0.5)
                                print(" - Ola, meu jovem! Por que voce nao entra e prova um pouco do bolo que eu acabei de fazer?")
                                time.sleep(1.5)
                                print("...")
                                time.sleep(0.5)
                                print("Voce recurperou TODOS os seus pontos de vida!")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[5]
                            else:
                                if(acao_do_personagem=="14"):
                                    if(objeto[4]=="sim"):
                                        print("Suma daqui seu idiota... Deixe-a em paz...")
                                    else:
                                        if(objeto[0]=="sim" or objeto[0]=="pegou o dinheiro"):
                                            print("Voce bateu na porta...")
                                            time.sleep(1)
                                            print("Voce escuta passos de dentro vindo à porta...")
                                            time.sleep(1)
                                            print(" - O que voce quer? - questionou a mulher que abrira a porta aos prantos")
                                            time.sleep(2)
                                            print("...")
                                            time.sleep(0.5)
                                            print("Ela observa o corpo do marido no chao do corredor...")
                                            time.sleep(1)
                                            print(" - F-Foi voce?!...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.75)
                                            print(" - VOCÊ VAI PAGAR CARO POR MATAR MEU MARIDO!")
                                            time.sleep(1)
                                            personagem_inimigo = [ "Mulher aos Prantos", 20, 20, 10, 10, 900, 200]
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                print(" - CHEGA!")
                                                time.sleep(0.5)
                                                print(" - Voce matou meu marido...")
                                                time.sleep(1)
                                                print(" - Como voce teve a pachorra de me procurar?!")
                                                time.sleep(1)
                                                print("Ela fechou a porta chorando.")
                                                time.sleep(1)
                                            else:
                                                print("A mulher caiu inconsciente no chao...")
                                                time.sleep(2)
                                                print("Dentro da casa voce encontrou um par de talheres de prata...")
                                                time.sleep(2)
                                                print("Voce os guardou na mochila...")
                                                time.sleep(2)
                                                print("...")
                                                time.sleep(2)
                                                print("Seu idiota...")
                                                time.sleep(3)
                                                quantidade_adicionada=1
                                                item_adicionado=talheres_prata
                                                adicionaItem()
                                                objeto[4]="sim"
                                        else:
                                            print("Voce bateu na porta...")
                                            time.sleep(1)
                                            print(" - JÁ DISSE PARA VOCÊ IR EMBORA SEU BÊBADO! - grita uma mulher de dentro da casa - NINGUÉM TE MERECE COMO MARIDO!")
                                            time.sleep(2)
                                else:
                                    if(acao_do_personagem=="13"):
                                        print("Voce e bobo?")
                                        time.sleep(0.5)
                                        print("Esse e o seu quarto!")
                                        time.sleep(0.5)
                                        print("Voce esta atrasado demais para voltar!")
                                        time.sleep(1)
                                    else:
                                        if(acao_do_personagem=="arrombar a porta do quarto 10" or acao_do_personagem=="arrombar 10" or acao_do_personagem=="arrombar quarto 10" or acao_do_personagem=="arrombar o quarto 10" or acao_do_personagem=="arrombar" or acao_do_personagem=="arrombar a porta" or acao_do_personagem=="quarto 10" or acao_do_personagem=="entrar no quarto 10"):
                                            if(objeto[3]=="sim"):
                                                print("Voce ja arrombou essa porta... Nao ha mais nada de interessante dentro do quarto.")
                                                time.sleep(1)
                                            else:
                                                print("Voce entrou no quarto e encontrou uma Jaqueta de Couro!")
                                                time.sleep(1.5)
                                                print("Voce a guardou na mochila!")
                                                time.sleep(1)
                                                item_adicionado=jaqueta_imitacao
                                                quantidade_adicionada=1
                                                adicionaItem()
                                                objeto[3]="sim"
                                        else:
                                            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                                                print("Voce subiu para o segundo andar, la voce encontrou mais cinco quartos e outra escada ascendente.")
                                                time.sleep(1)
                                                seuPredioSegundoAndar()
                                                if(personagem_jogador[6]<=0):break
                                            else:
                                                if(acao_do_personagem=="olhar o bebado"  or acao_do_personagem=="bebado"  or acao_do_personagem=="bebado" or acao_do_personagem=="olhar bebado" or acao_do_personagem=="olha o bebado" or acao_do_personagem=="olha bÊbado" or acao_do_personagem=="olhar o bebado" or acao_do_personagem=="olhar bebado" or acao_do_personagem=="olha o bebado" or acao_do_personagem=="olha bebado"):
                                                    objeto[0]="1"
                                                    print("Voce ve um homem de 40 anos, coberto por cacos de vidro, bebida e vômito, dormindo no chao.")
                                                    time.sleep(1)
                                                else:
                                                    if(acao_do_personagem=="revistar o bebado" or acao_do_personagem=="revistar bebado" or acao_do_personagem=="revistar" or acao_do_personagem=="revista bebado" or acao_do_personagem=="revista o bebado" or acao_do_personagem=="revistar o bebado" or acao_do_personagem=="revistar bebado" or acao_do_personagem=="revistar" or acao_do_personagem=="revista bebado" or acao_do_personagem=="revista o bebado"):
                                                        if(objeto[2]=="nao"):
                                                            print("Voce achou um energetico e o guardou na mochila!")
                                                            time.sleep(1)
                                                            item_adicionado=lata_energetico
                                                            quantidade_adicionada=1
                                                            adicionaItem()
                                                            objeto[2]="sim"
                                                        else:
                                                            print("Voce nao encontrou mais nada...\n")
                                                            time.sleep(2)
                                                    else:
                                                        if(acao_do_personagem=="acordar o bebado" or acao_do_personagem=="acordar" or acao_do_personagem=="acordar bebado" or acao_do_personagem=="acorda o bebado" or acao_do_personagem=="acorda bebado" or acao_do_personagem=="acordar o bebado" or acao_do_personagem=="acordar bebado" or acao_do_personagem=="acorda o bebado" or acao_do_personagem=="acorda bebado"):
                                                            objeto[0]="2"
                                                            print("Voce tenta acordar o bebado, mas nao consegue...")
                                                            time.sleep(1)
                                                        else:
                                                            if(acao_do_personagem=="mover o bebado" or acao_do_personagem=="mover bebado" or acao_do_personagem=="move o bebado" or acao_do_personagem=="move bebado" or acao_do_personagem=="mover o bebado" or acao_do_personagem=="mover bebado" or acao_do_personagem=="move o bebado" or acao_do_personagem=="move bebado" or acao_do_personagem=="mover" or acao_do_personagem=="move"):
                                                                objeto[0]="3"
                                                                print("Voce pensa em mover o bebado...")
                                                                time.sleep(1)
                                                                print("Mas o cheiro e a sujeira fazem voce vomitar em cima dele!")
                                                                time.sleep(2)
                                                                print("...")
                                                                time.sleep(1)
                                                                print("Ele continua dormindo...")
                                                                time.sleep(1)
                                                            else:
                                                                if(acao_do_personagem=="atacar o bebado" or acao_do_personagem=="atacar bebado" or acao_do_personagem=="ataca o bebado" or acao_do_personagem=="ataca bebado" or acao_do_personagem=="atacar o bebado" or acao_do_personagem=="atacar bebado" or acao_do_personagem=="ataca o bebado" or acao_do_personagem=="ataca bebado" or acao_do_personagem=="atacar" or acao_do_personagem=="ataca"):
                                                                    if(objeto[0]!="sim" or objeto[0]!="pegou o dinheiro"):
                                                                        print("Voce chuta varias vezes o bebado violentamente!")
                                                                        time.sleep(0.5)
                                                                        raw_input("(Aperte Enter)")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        raw_input("!!!")
                                                                        print("(Pronto, voce chutou o suficiente!)")
                                                                        time.sleep(0.5)
                                                                        print(" - P-PARA! PARA! PARA! - berra o bebado que acabou de acordar.")
                                                                        time.sleep(1)
                                                                        print("Ele se levanta e te empurra ganhando distancia.")
                                                                        time.sleep(1)
                                                                        print("...")
                                                                        time.sleep(1)
                                                                        print(" - Ssseu muleque i-insstrosmestido!... *hic*\n")
                                                                        time.sleep(2)
                                                                        personagem_inimigo = [ "Bebado", 4, 4, -3, -3, 500, 30]
                                                                        batalha()
                                                                        if(personagem_jogador[6]<=0):break
                                                                        if(personagem_inimigo[6]>0):
                                                                            print("Voce escapa da briga, mas em seguida o bebado tosse sangue e cai no chao...")
                                                                            time.sleep(2)
                                                                        else:
                                                                            print("O bebado coberto de bebida, vômito e sangue, cai de costas no chao,")
                                                                            time.sleep(1)
                                                                            print("sendo empalado pelos diversos cacos de vidro...")
                                                                            time.sleep(1)
                                                                            print("O sangue dele escorre pelo corredor ate os seus pes...")
                                                                            time.sleep(1.5)
                                                                            print("Voce vira o rosto fechando os olhos e abaixando os punhos...")
                                                                            time.sleep(2)
                                                                            print("Agora, desencostado da porta dos fundos, o bebado ja nao e mais um impecilio...")
                                                                            time.sleep(1)
                                                                        objeto[0]="sim"
                                                                else:
                                                                    if(acao_do_personagem=="abrir a porta dos fundos" or acao_do_personagem=="abrir porta dos fundos" or acao_do_personagem=="abrir porta do fundos" or acao_do_personagem=="abrir porta dos fundo" or acao_do_personagem=="abrir" or acao_do_personagem=="abrir porta do fundo" or acao_do_personagem=="abrir a porta" or acao_do_personagem=="abrir porta"):
                                                                        if(objeto[0]=="sim"):
                                                                            print("Voce abre a porta... ")
                                                                            time.sleep(1)
                                                                            print("É um armario de limpeza.")
                                                                            time.sleep(1)
                                                                            print("Em meio às vassouras, rodos e outras coisas, voce encontra uma mala...")
                                                                            time.sleep(2)
                                                                            print("Voce abre a mala, encontra entre os materiais de escritorio e 10 Reais!")
                                                                            time.sleep(1)
                                                                            print("...")
                                                                            time.sleep(2)
                                                                            print("Voce tambem achou um lapis apontado e o guardou na mochila!")
                                                                            time.sleep(1)
                                                                            item_adicionado=lapis_apontado
                                                                            quantidade_adicionada=1
                                                                            adicionaItem()
                                                                            objeto[0]="pegou o dinheiro"
                                                                            personagem_jogador[7]=personagem_jogador[7]+10
                                                                        else:
                                                                            if(objeto[0]=="pegou o dinheiro"):
                                                                                print("Voce ve materiais de limpesa e uma mala aberta.")
                                                                                time.sleep(0.5)
                                                                            else:
                                                                                print("Nao da para abrir!")
                                                                                time.sleep(0.5)
                                                                    else:
                                                                        if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do predio"):
                                                                            if(ponto_de_save==1):
                                                                                while 1:
                                                                                    print("Do lado de fora ha um oponente MUITO forte.")
                                                                                    time.sleep(3)
                                                                                    print("Tem certeza que esta pronto para sair? (sim ou nao)")
                                                                                    acao_do_personagem=raw_input("-")
                                                                                    acao_do_personagem=acao_do_personagem.lower()
                                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                                        acao_do_personagem="sim"
                                                                                        break
                                                                                    else:
                                                                                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                                            print("Voce decidiu nao sair do predio.")
                                                                                            time.sleep(0.5)
                                                                                            break
                                                                                        else:
                                                                                            print("Entrada invalida!")
                                                                                            time.sleep(0.5)
                                                                                if(acao_do_personagem=="sim"):
                                                                                    print("Voce desceu as escadas e saiu do predio...")
                                                                                    time.sleep(0.5)
                                                                                    break
                                                                            else:
                                                                                print("Voce desceu as escadas e saiu do predio...")
                                                                                time.sleep(0.5)
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
                                                                                    time.sleep(0.5)
        print("\n#"+"-"*30+"#\n"+"\nLista de Acões\n\nCenario:"+str(variavel_lugar)+"\n\nVoce pode:\nolhar\n")
        if (variavel_cenario[0] == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            if (variavel_cenario[2] == "sim" and objeto[0] == "nao"):
                print("olhar o bebado\n")
        if(objeto[1] == "sim"):
            print("\narrombar o quarto 10\n")
        if (objeto[0] == "1"):
            print("\nacordar o bebado\n")
            print("\nrevistar o bebado\n")
        if (objeto[0] == "2"):
            print("\nmover o bebado\n")
        if (objeto[0] == "3"):
            print("\natacar o bebado\n")
        if (objeto[0] == "sim"):
            print("\nabrir a porta dos fundos\n")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        print("\nO que voce fara agora, "+str(personagem_jogador[0])+"?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()

#--Sua Rua--#
def suaRua():
    global inventario_reserva,porcentagem_inflacao,bermuda_linho_regata,bermuda_linho_polo,calca_jeans_regata,calca_jeans_polo,desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 1:
        if(personagem_jogador[6]<=0):break
        print("\n#", "-"*30,"#\n", "\nLista de Acões\n\nCenario:"+str(variavel_lugar)+"\n\nVoce pode:\nolhar\n")
        print("\nentrar na loja\n\nentrar na pizzaria\n")
        print("\nentrar no predio\n\nver ficha do personagem\nver mochila\n\npegar ônibus\nir à pe\n\nsalvar o jogo\n"+"\n#"+"-"*30+"#\n")
        print("\nQual sera a sua atitude, "+str(personagem_jogador[0])+"?\n")
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
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
                                loja_venda[1][0]=bermuda_linho_regata
                                loja_venda[1][1]=bermuda_linho_polo
                                loja_venda[1][2]=calca_jeans_regata
                                loja_venda[1][3]=calca_jeans_polo
                                loja_venda[1][4]=luva_la
                                loja_venda[1][5]=luva_imitacao
                                loja_venda[1][6]=papetes_masculinas
                                loja_venda[1][7]=tenis_velho
                                loja_venda[1][8]=tenis_simplorio
                                loja_venda[1][9]=sapato_simplorio
                                loja_venda[1][10]=tenis_comum
                                lojaComprar()
                                loja_venda=inventario_reserva
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
                            inventario_reserva=loja_venda
                            loja_venda[1][1]=pedaco_pizza
                            loja_venda[1][0]=talheres_prata
                            lojaComprar()
                            loja_venda=inventario_reserva
                            print("\nVoce saiu da pizzaria.\n")
                            time.sleep(1)
                            break
                        else:
                            if(acao_do_personagem=="entrar no predio" or acao_do_personagem=="predio" or acao_do_personagem=="entrar predio" or acao_do_personagem=="entrar o predio" or acao_do_personagem=="entra no predio" or acao_do_personagem=="ppredio" or acao_do_personagem=="entra predio" or acao_do_personagem=="entra o predio" or acao_do_personagem=="etrar no predio" or acao_do_personagem=="predio" or acao_do_personagem=="etrar predio" or acao_do_personagem=="etrar o predio" or acao_do_personagem=="etra no predio" or acao_do_personagem=="entrar no predio" or acao_do_personagem=="etra predio" or acao_do_personagem=="etra o predio"):
                                variavel_lugar = "seu predio, 1º andar"
                                seuPredioPrimeiroAndar()
                            else:
                                print('\nEntrada Invalida!\n')
                                time.sleep(0.5)
        

        


#####################----------------------------__BRIGA DE ESTUDANTE__----------------------------#####################
while 1:
    while (personagem_jogador[6]>0):
        print('''
   _________________________________________________________________________  
 |\ _______________________________________________________________________ /| 
 | |                                                                       | | 
 | | * =* =* =* =* =* =* = : --------------------- : = *= *= *= *= *= *= * | | 
 | | ===================== : - - - - - - - - - - - : ===================== | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================================================================== | |
 | | ==-==-==-==-==-==-=                               =-==-==-==-==-==-== | | 
 | | =-==-==-==-==-==-==      Briga de Estudante       ==-==-==-==-==-==-= | | 
 | | ==-==-==-==-==-==-= por:Fernando Luiz Neme Chibli =-==-==-==-==-==-== | |
 | | =-==-==-==-==-==-==                               ==-==-==-==-==-==-= | | 
 | | ==============================         ============================== | | 
 | | *=*=*=*=*=*=*=*=*=*=*=*=*=    [comecar]    =*=*=*=*=*=*=*=*=*=*=*=*=* | | 
 | | ======================**=**=            =**=**======================= | | 
 | | *=*=*=*=*=*=*=*=*=*=*=*=*=   [continuar]   =*=*=*=*=*=*=*=*=*=*=*=*=* | |
 | | ======================**=**=            =**=**======================= | | 
 | | *=*=*=*=*=*=*=*=*=*=*=   [criar/zerar saves]   =*=*=*=*=*=*=*=*=*=*=* | | 
 | | =============================           ============================= | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | |
 | | ===================== : - - - - - - - - - - - : ===================== | | 
 | | * =* =* =* =* =* =* = : --------------------- : = *= *= *= *= *= *= * | |
 | |_______________________________________________________________________| | 
 |/_________________________________________________________________________\|

 Digite "comecar", "continuar" ou "criar/zerar saves":''')
        while 1:
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem =="comecar" or acao_do_personagem == "mecar" or acao_do_personagem == "come" or acao_do_personagem =="iniciar" or acao_do_personagem =="inicia" or acao_do_personagem =="inici" or acao_do_personagem =="inicio" or acao_do_personagem =="inicio" or acao_do_personagem =="new game" or acao_do_personagem =="start new game" or acao_do_personagem =="start" or acao_do_personagem =="start game" or acao_do_personagem =="comecar" or acao_do_personagem =="comeca" or acao_do_personagem =="comeca" or acao_do_personagem =="com" or acao_do_personagem =="cmecar" or acao_do_personagem =="cmecar" or acao_do_personagem =="comcar" or acao_do_personagem =="comcar" or acao_do_personagem =="comear" or acao_do_personagem =="comer" or acao_do_personagem =="cocar" or acao_do_personagem =="ccar" or acao_do_personagem =="cmcr" or acao_do_personagem =="cmecr" or acao_do_personagem =="cocar" or acao_do_personagem =="ccar" or acao_do_personagem =="cmcr" or acao_do_personagem =="cmecr" or acao_do_personagem =="cumessa" or acao_do_personagem =="comessa" or acao_do_personagem =="comessar"):
                break
            else:
                if (acao_do_personagem == "continuar" or acao_do_personagem == "ccontinuar" or acao_do_personagem == "continuarr" or acao_do_personagem == "conntinuar" or acao_do_personagem == "conttinuar" or acao_do_personagem == "continnuar" or acao_do_personagem == "ccontinuarr" or acao_do_personagem == "cconntinuar" or acao_do_personagem == "cconttinuar" or acao_do_personagem == "ccontinnuar" or acao_do_personagem == "cconnttinuar" or acao_do_personagem == "cconntinnuar" or acao_do_personagem == "cconntinuarr" or acao_do_personagem == "continuart" or acao_do_personagem == "cconttinnuar" or acao_do_personagem == "cconttinuarr" or acao_do_personagem == "cconnttinnuarr" or acao_do_personagem == "cntnr" or acao_do_personagem == "contnr" or acao_do_personagem == "continr" or acao_do_personagem == "continur" or acao_do_personagem == "cntinuar" or acao_do_personagem == "cntnuar" or acao_do_personagem == "cntnar" or acao_do_personagem == "cntinur" or acao_do_personagem == "cntinr" or acao_do_personagem == "cntinar" or acao_do_personagem == "contnur" or acao_do_personagem == "ontinuar" or acao_do_personagem == "cotinuar" or acao_do_personagem == "coninuar" or acao_do_personagem == "contiuar" or acao_do_personagem == "coinar" or acao_do_personagem == "continua" or acao_do_personagem == "cntn" or acao_do_personagem == "contn" or acao_do_personagem == "contin" or acao_do_personagem == "continu" or acao_do_personagem == "cntinua" or acao_do_personagem == "cntnua" or acao_do_personagem == "cntna" or acao_do_personagem == "cntinu" or acao_do_personagem == "cntin" or acao_do_personagem == "cntina" or acao_do_personagem == "contnu" or acao_do_personagem == "ontinua" or acao_do_personagem == "cotinua" or acao_do_personagem == "coninua" or acao_do_personagem == "contiua" or acao_do_personagem == "coina" or acao_do_personagem == "con" or acao_do_personagem == "cont" or acao_do_personagem == "conti" or acao_do_personagem == "ccontin" or acao_do_personagem == "ccontinu"):
                    print("\nDeseja continuar o jogo guardado em qual espaco?\n")
                    time.sleep(1)
                    arq = open('\espaco_save00.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  0:     Lugar:"+str(mostrar_save[5])+"\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save01.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  1:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save02.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  2:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save03.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  3:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save04.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  4:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save05.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  5:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save06.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  6:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save07.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  7:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save08.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  8:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    arq = open('\espaco_save09.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaco  9:     Lugar:"+str(mostrar_save[5])+ "\n          Nome:"+str(mostrar_save[1])+"  Vida:"+str( mostrar_save[3])+"\n          Ataque:"+str(mostrar_save[7])+"  Defesa:"+str(mostrar_save[9])+"  Agilidade:"+str(mostrar_save[11])
                    arq.close
                    while 1:
                        print("\n(Digite um número entre 0 e 9)")
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
                                                                print("Entrada invalida!\n")
                                                                time.sleep(0.5)
                    mostrar_save = pickle.load(arq)
                    equipado_roupa = pickle.load(arq)
                    equipado_capa = pickle.load(arq)
                    equipado_luva = pickle.load(arq)
                    equipado_anel = pickle.load(arq)
                    equipado_maos = pickle.load(arq)
                    equipado_calcado = pickle.load(arq)
                    variavel_cenario = pickle.load(arq)
                    objeto = pickle.load(arq)
                    situacao = pickle.load(arq)
                    temporario = pickle.load(arq)
                    variavel_lugar = pickle.load(arq)
                    ponto_de_save = pickle.load(arq)
                    personagem_jogador = pickle.load(arq)
                    personagem_reserva = pickle.load(arq)
                    personagem_inimigo = pickle.load(arq)
                    mala = pickle.load(arq)
                    arq.close
                    if(ponto_de_save>0):
                        print("\nCarregado!\n")
                        time.sleep(0.5)
                        ficha_personagem()
                    else:
                        print("\nERRO: Voce nao possui dados salvos.\n")
                        time.sleep(0.5)
                    break
                else:
                    if(acao_do_personagem=="limpar" or acao_do_personagem=="zerar" or acao_do_personagem=="limpar saves" or acao_do_personagem=="criar saves" or acao_do_personagem=="zerar saves" or acao_do_personagem=="resetar saves" or acao_do_personagem=="resetar" or acao_do_personagem=="criar/zerar saves"):
                        mostrar_save = ("  Nome:"+str( personagem_jogador[0])+ "  Vida:"+str( personagem_jogador[5])+"  Lugar:"+str( variavel_lugar)+ "  Ataque:"+str( personagem_jogador[1])+ "  Defesa:"+str( personagem_jogador[2])+"  Agilidade:"+str( personagem_jogador[3]))
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
                                pickle.dump(equipado_roupa, arq)
                                pickle.dump(equipado_capa, arq)
                                pickle.dump(equipado_luva, arq)
                                pickle.dump(equipado_anel, arq)
                                pickle.dump(equipado_maos, arq)
                                pickle.dump(equipado_calcado, arq)
                                pickle.dump(variavel_cenario, arq)
                                pickle.dump(objeto, arq)
                                pickle.dump(situacao, arq)
                                pickle.dump(temporario, arq)
                                pickle.dump(variavel_lugar, arq)
                                pickle.dump(ponto_de_save, arq)
                                pickle.dump(personagem_jogador, arq)
                                pickle.dump(personagem_reserva, arq)
                                pickle.dump(personagem_inimigo, arq)
                                pickle.dump(mala, arq)
                                arq.close
                                break
                            pickle.dump(mostrar_save, arq)
                            pickle.dump(equipado_roupa, arq)
                            pickle.dump(equipado_capa, arq)
                            pickle.dump(equipado_luva, arq)
                            pickle.dump(equipado_anel, arq)
                            pickle.dump(equipado_maos, arq)
                            pickle.dump(equipado_calcado, arq)
                            pickle.dump(variavel_cenario, arq)
                            pickle.dump(objeto, arq)
                            pickle.dump(situacao, arq)
                            pickle.dump(temporario, arq)
                            pickle.dump(variavel_lugar, arq)
                            pickle.dump(ponto_de_save, arq)
                            pickle.dump(personagem_jogador, arq)
                            pickle.dump(personagem_reserva, arq)
                            pickle.dump(personagem_inimigo, arq)
                            pickle.dump(mala, arq)
                            arq.close
                            print("Save"+str(i)+"foi criado!")
                            i=i+1
                        if(i==10):break
                    else:
                        print('Entrada invalida!\n')
        if(ponto_de_save==0):
            print("\nIniciando novo jogo...\n")
            time.sleep(2)
            print("\n\nVoce e um homem... Qual e o seu nome?\n")
            personagem_jogador[0] = raw_input("-")
            while 1:
                print("Seu nome e "+str(personagem_jogador[0])+ "?")
                while 2:
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        break
                    else:
                        if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                            print("\nEntao qual e o seu nome?\n")
                            personagem_jogador[0] = raw_input("-")
                            break
                        else:
                            print('\nEntrada invalida, digite "sim" ou "nao".\n')
                            time.sleep(0.5)
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    break
            print("Muito prazer, "+str(personagem_jogador[0])+'.')
            time.sleep(2)
            print('Nos ja nos conhecemos?(digite "nao" para ver o tutorial)\n')
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            while 1:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    print('Tem certeza??')
                    time.sleep(2)
                    print('Nao me lembro de voce...')
                    time.sleep(1)
                    print('(eu REALMENTE recomendo que voce digite "nao" para ver o tutorial!)')
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    break
                else:
                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                        break
                    else:
                        print('Entrada invalida! Digite "sim" ou "nao".')
                        time.sleep(0.5)
                        acao_do_personagem = raw_input("-")
                        acao_do_personagem = acao_do_personagem.lower()
            while 1:
                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                    break
                else:
                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                        print('\nSou o narrador da nossa historia, vou apenas te guiar de acordo com as suas decisões...')
                        time.sleep(3)
                        print('Entao saiba que nao vou facilitar as coisas para voce!')
                        time.sleep(4)
                        print('Porem minha funcao e te guiar, ser os seus olhos, ouvidos, maos e nariz,')
                        time.sleep(4)
                        print('e alem disso voce parece precisar de algumas instrucões para tornar disso algo mais divertido.')
                        time.sleep(4)
                        print('\nToda vez antes da sua acao te mostrarei uma lista de acões possiveis de se realizar.')
                        time.sleep(3)
                        print('\nE tambem te mostrarei se a sua acao for invalida.')
                        time.sleep(2)
                        print('\nMas voce so recebera minha atencao quando eu pedir,')
                        time.sleep(5)
                        print('voce percebera isso quando ver um hifen apos a minha pergunta.')
                        time.sleep(5)
                        print('Entendeu?')
                        acao_do_personagem = raw_input("-")
                        acao_do_personagem = acao_do_personagem.lower()
                        while 1:
                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                break
                            if( acao_do_personagem== "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                print('\nVoce e bobo??')
                            else:
                                print('\nEntrada invalida!\n\nVoce pode:\nconcordar comigo dizendo "sim"\n')
                            acao_do_personagem = raw_input("-")
                            acao_do_personagem = acao_do_personagem.lower()
                        print('Bom menino!')
                        time.sleep(2)
                        print('\nAlguns comandos como "salvar o jogo" e "ver ficha do personagem" estarao quase sempre disponiveis.')
                        time.sleep(2)
                        print('\nToda vez que voce descobre algo novo no cenario, a lista de acões muda,')
                        time.sleep(3)
                        print('mas os resultados dessas acões podem mudar de acordo com o que voce faz,')
                        time.sleep(4)
                        print('sendo assim e altamente recomendavel que voce repita algumas acões em um mesmo cenario.')
                        time.sleep(4)
                        print('\nAcho que ja e o bastante para comecarmos, mas posso repetir se voce quiser...')
                        time.sleep(2)
                        print('Voce entendeu tudo o que eu disse?')
                        objeto[0]="ganha presente"
                    else:
                        print('Nao entendi o que voce quis dizer...\nPor favor, digite "sim" ou "nao".\n')
                    acao_do_personagem = raw_input("-")
                    acao_do_personagem = acao_do_personagem.lower()
                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                        acao_do_personagem="sim"
            if(objeto[0]=="ganha presente"):
                print("\nÓtimo, "+str(personagem_jogador[0])+".")
                time.sleep(1)
                print("Acho que comecamos com o pe direito! Fico feliz que voce tenha me escutado como um bom garoto!")
                time.sleep(2)
                print("Por isso deixei um presente para voce no seu guarda-roupas, tenho certeza que voce ficara feliz.")
                time.sleep(2)
            else:
                print("Eu nao me lembro de voce...")
                time.sleep(3)
                print("Entao voce deve ser mesmo irrelevante!")
                time.sleep(3)

#####################----------------------------__INÍCIO DO JOGO__----------------------------#####################
            print("\nCenario: acabou de amanhecer, seu quarto esta desarrumado,")
            time.sleep(2)
            print("voce ainda esta de pijama e atrasado para a aula - nao que voce se importe muito com isso.")
            time.sleep(3)
            print("\n#"+"-"*30+"#\n\nLista de Acões\n\nCenario:"+str(variavel_lugar))
            time.sleep(2)
            print("\n\nVoce pode:\n\nvestir\narrumar o quarto\nolhar\n")
            time.sleep(2)
            if (variavel_cenario[0] == "sim"):
                print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\n\nolhar pela janela\n")
                time.sleep(2)
            print("\nver ficha do personagem\nver mochila\nsair do quarto\n")
            time.sleep(1)
            print("\n#"+ "-"*30+"#\n")
            print("\nO que voce vai fazer, "+str(personagem_jogador[0])+"?\n")
            acao_do_personagem = raw_input("-")
            acao_do_personagem = acao_do_personagem.lower()
            while 1:
                if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
                    ficha_personagem()
                else:
                    if (acao_do_personagem== "vetir" or acao_do_personagem=="vest" or acao_do_personagem=="vesti" or acao_do_personagem=="veti" or acao_do_personagem=="estir" or acao_do_personagem=="esti" or acao_do_personagem=="etir" or acao_do_personagem == "vestir" or acao_do_personagem == "vesir" or acao_do_personagem == "vestir uniforme" or acao_do_personagem == "vestir o uniforme" or acao_do_personagem == "vestir o uniforme estudantil" or acao_do_personagem == "vestir uniforme estudantil" or acao_do_personagem == "se vestir" or acao_do_personagem == "se vestir para a aula" or acao_do_personagem == "se vestir pra aula" or acao_do_personagem == "vestir para a aula" or acao_do_personagem == "me arrumar" or acao_do_personagem == "tomar banho" or acao_do_personagem == "ir ao banheiro" or acao_do_personagem == "cagar" or acao_do_personagem == "mijar" or acao_do_personagem == "fazer xixi" or acao_do_personagem == "trocar de roupa" or acao_do_personagem == "me trocar" or acao_do_personagem == "trocar"):
                        if (temporario[0] == False):
                            print("Voce colocou a mao embaixo do seu travesseiro e achou seu uniforme.\n")
                            time.sleep(1)
                            print("Voce guardou o Uniforme Estudantil na sua mochila!\n")
                            time.sleep(2)
                            item_adicionado=uniforme_estudantil
                            quantidade_adicionada=1
                            adicionaItem()
                            temporario[0] = True
                        else:
                            print("Voce ja pegou seu uniforme!\n")
                            time.sleep(1)
                    else:
                        if (acao_do_personagem == "arrumar o quarto" or acao_do_personagem == "arrumar" or acao_do_personagem == "arrumar quarto" or acao_do_personagem == "arruma" or acao_do_personagem == "arruma o quarto" or acao_do_personagem == "arruma quarto" or acao_do_personagem == "quarto"):
                            if (variavel_cenario[1] == "nao"):
                                print("Voce achou 15 Reais enquanto arrumava o seu quarto!\n")
                                time.sleep(2)
                                personagem_jogador[7] = +15
                                variavel_cenario[1] = "sim"
                            else:
                                print("Voce ja arrumou o seu quarto!\n")
                                time.sleep(1)
                        else:
                            if (acao_do_personagem == "olhar" or acao_do_personagem=="olh" or acao_do_personagem == "ver" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha" or acao_do_personagem == "olhar quarto" or acao_do_personagem == "olha quarto" or acao_do_personagem == "olhar o quarto" or acao_do_personagem == "olha o quarto" or acao_do_personagem == "ve" or acao_do_personagem == "ve"):
                                if (variavel_cenario[1] == "nao"):
                                    print("Voce nao consegue ver nada alem de bagunca, MUITA BAGUNÇA!!!\n")
                                    time.sleep(2)
                                else:
                                    print("Voce ve um quarto arrumado, com um guarda-roupas, uma estante de livros, uma mesa de escritorio com gavetas e uma janela.\n")
                                    time.sleep(3)
                                    variavel_cenario[0] = "sim"
                            else:
                                if (acao_do_personagem == "olhar as gavetas" or acao_do_personagem == "olhar gavetas" or acao_do_personagem == "olha a gaveta" or acao_do_personagem == "olhar a gaveta" or acao_do_personagem == "olhar gaveta" or acao_do_personagem == "olhar as gaveta" or acao_do_personagem == "olha as gavetas" or acao_do_personagem == "olha gaveta" or acao_do_personagem == "olha as gaveta" or acao_do_personagem == "olha a gavetas" or acao_do_personagem == "ver as gavetas" or acao_do_personagem == "ver a gaveta" or acao_do_personagem == "ver as gaveta" or acao_do_personagem == "ver a gavetas" or acao_do_personagem=="gaveta" or acao_do_personagem=="gavetas"):
                                    if (temporario[1] == True):
                                        print("Voce olhou novamente as gavetas, mas nao encontrou nada interessante.\n")
                                        time.sleep(1)
                                    else:
                                        print("Voce achou um Soco-Ingles enquanto olhava as gavetas!\n")
                                        time.sleep(2)
                                        item_adicionado=soco_pvc
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        print("Voce o guardou na mochila!")
                                        time.sleep(2)
                                        temporario[1]=True
                                else:
                                    if (acao_do_personagem == "olhar o guarda-roupas" or acao_do_personagem =="olhar o guarda" or acao_do_personagem =="olhar o garda" or acao_do_personagem == "guarda" or acao_do_personagem=="roupa" or acao_do_personagem == "olha o guarda-roupas" or acao_do_personagem == "olha o guarda-roupa" or acao_do_personagem == "olhar o guarda-roupa" or acao_do_personagem == "olhar guarda-roupas" or acao_do_personagem == "olha guarda-roupas" or acao_do_personagem == "olha guarda-roupa" or acao_do_personagem == "olhar guarda-roupa" or acao_do_personagem == "olhar o guarda roupas" or acao_do_personagem == "olha o guarda roupas" or acao_do_personagem == "olha o guarda roupa" or acao_do_personagem == "olhar o guarda roupa" or acao_do_personagem == "olhar guarda roupas" or acao_do_personagem == "olha guarda roupas" or acao_do_personagem == "olha guarda roupa" or acao_do_personagem == "olhar guarda roupa" or acao_do_personagem == "olhar o guardaroupas" or acao_do_personagem == "olha o guardaroupas" or acao_do_personagem == "olha o guardaroupa" or acao_do_personagem == "olhar o guardaroupa" or acao_do_personagem == "olhar guardaroupas" or acao_do_personagem == "olha guardaroupas" or acao_do_personagem == "olha guardaroupa" or acao_do_personagem == "olhar guardaroupa" or acao_do_personagem == "olhar o guardarroupas" or acao_do_personagem == "olha o guardarroupas" or acao_do_personagem == "olha o guardarroupa" or acao_do_personagem == "olhar o guardarroupa" or acao_do_personagem == "olhar guardarroupas" or acao_do_personagem == "olha guardarroupas" or acao_do_personagem == "olha guardarroupa" or acao_do_personagem == "olhar guardarroupa" or acao_do_personagem == "guarda-roupa" or acao_do_personagem == "guarda-roupas" or acao_do_personagem == "guarda roupa" or acao_do_personagem == "guarda roupas" or acao_do_personagem == "guardaroupa" or acao_do_personagem == "guardaroupas" or acao_do_personagem == "guardarroupa" or acao_do_personagem == "guardarroupas" or acao_do_personagem == "olhar o armario" or acao_do_personagem == "olhar o armario" or acao_do_personagem == "olhar armario" or acao_do_personagem == "olhar armario" or acao_do_personagem == "olha o armario" or acao_do_personagem == "olha o armario" or acao_do_personagem == "olha armario" or acao_do_personagem == "olha armario" or acao_do_personagem == "armario" or acao_do_personagem == "armario" or acao_do_personagem == "sair do armario" or acao_do_personagem == "vestir smoking" or acao_do_personagem == "ver armario" or acao_do_personagem == "ver o armario" or acao_do_personagem == "ver armario" or acao_do_personagem == "ver o armario" or acao_do_personagem == "ver o guarda-roupas" or acao_do_personagem == "ver o guardarroupas" or acao_do_personagem == "ver o guarda roupas" or acao_do_personagem == "ver o guardaroupas" or acao_do_personagem == "ver o guarda-roupa" or acao_do_personagem == "ver o guardarroupa" or acao_do_personagem == "ver o guarda roupa" or acao_do_personagem == "ver o guardaroupa" or acao_do_personagem == "ver guarda-roupas" or acao_do_personagem == "ver guardarroupas" or acao_do_personagem == "ver guarda roupas" or acao_do_personagem == "ver guardaroupas" or acao_do_personagem == "ver guarda-roupa" or acao_do_personagem == "ver guardarroupa" or acao_do_personagem == "ver guarda roupa" or acao_do_personagem == "ver guardaroupa"):
                                        if(objeto[0]=="ganha presente"):
                                            print("Voce encontrou uma bela caixa de presente.")
                                            time.sleep(2)
                                            print("Vai abrir?(sim ou nao)")
                                            while 1:
                                                acao_do_personagem = raw_input("-")
                                                acao_do_personagem = acao_do_personagem.lower()
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    print("Voce desembalou a caixa de presente e...")
                                                    time.sleep(3)
                                                    print("Encontrou um par de Papetes Masculinas!\n")
                                                    time.sleep(1)
                                                    print("Voce guardou as Papetes Masculinas na sua mochila!")
                                                    time.sleep(2)
                                                    item_adicionado=papetes_masculinas
                                                    quantidade_adicionada=1
                                                    adicionaItem()
                                                    objeto[0] = "nao"
                                                    break
                                                else:
                                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                        break
                                                    else:
                                                        print('Entrada Invalida! Digite "sim" ou "nao".')
                                                        time.sleep(0.5)
                                        else:
                                            print("Voce nao ve muitas roupas... Voce e muito pobre, arrume um emprego!\n")
                                            time.sleep(1)
                                    else:
                                        if (acao_do_personagem == "olhar a janela"):###__EASTER-EGG
                                            if (eegg == 1):
                                                print("Voce ve...")
                                                time.sleep(3.5)
                                                print("Voce ve uma janela, sua anta!")
                                                time.sleep(0.5)
                                                print("... Hunf...")
                                                time.sleep(0.5)
                                                print("Volte para as aulas de ortografia!")
                                                time.sleep(0.5)
                                                print("...")
                                                time.sleep(2)
                                                print("O que? Voce acha que eu fui muito grosso?")
                                                time.sleep(1)
                                                print("Okay, "+str(personagem_jogador[0])+", vamos la...")
                                                time.sleep(2.5)
                                                print("Ha uma diferenca muito grande entre olhar A janela e olhar PELA janela!")
                                                time.sleep(3)
                                                print("Tente mais uma vez, sua anta!")
                                                time.sleep(0.5)
                                                eegg = 2
                                            else:
                                                if (eegg == 2):
                                                    print("Digitando errado MAIS UMA VEZ?!")
                                                    time.sleep(0.5)
                                                    print("Okay, "+str(personagem_jogador[0])+", voce ja esta passando dos limites da burrice...")
                                                    time.sleep(1)
                                                    eegg = 3
                                                else:
                                                    if (eegg == 3):
                                                        print("Voce encara a janela...")
                                                        time.sleep(1)
                                                        print("Voce parece um retardado fazendo isso...")
                                                        time.sleep(0.5)
                                                        eegg = 4
                                                    else:
                                                        if (eegg == 4):
                                                            print('Enquanto voce encarava a janela um pombo pousou nela...')
                                                            time.sleep(1)
                                                            print('Ele olhou bem no fundo dos seus olhos e disse "Voce e um idiota."...')
                                                            time.sleep(1)
                                                            print('Nao, ele nao disse isso... Na verdade fui eu quem disse isso, seu idiota.')
                                                            time.sleep(1)
                                                            eegg = 5
                                                        else:
                                                            if (eegg == 5):
                                                                print("Ja chega! Voce esgotou minha paciencia!")
                                                                time.sleep(1.5)
                                                                personagem_inimigo = [ "Narrador", 13, 8, 10, 10, 100, 100]
                                                                batalha()
                                                                if(personagem_jogador[6]<=0):break
                                                                if(personagem_inimigo[6]>0):
                                                                    print("Vou te deixar em paz por agora, mas tente voltar a me irritar para ver o que te acontece!")
                                                                    time.sleep(1)
                                                                else:
                                                                    print("Aaaah! Eu deveria ter me feito mais forte para essa luta...")
                                                                    time.sleep(1)
                                                                    print("Okay, voce venceu... Mas pare de me irritar!")
                                                                    time.sleep(1)
                                                                    eegg = 6
                                                            else:
                                                                if (eegg == 6):
                                                                    print("...")
                                                                    time.sleep(0.5)
                                                                    eegg = 7
                                                                else:
                                                                    print("Voce ve uma janela que abre horizontalmente para as duas direcões,")
                                                                    time.sleep(0.5)
                                                                    print("sendo que o vidro da janela esquerda esta rachado por, provavelmente, um apedrejamento.")
                                                                    time.sleep(1)
                                                                    print("Os batentes sao de madeira antiga, deteriorada pela acao de cupins.")
                                                                    time.sleep(0.5)
                                        else:
                                            if (acao_do_personagem == "olhar pela janela" or acao_do_personagem == "olha pela janela" or acao_do_personagem == "janela" or acao_do_personagem ==  "olhar janela" or acao_do_personagem == "olha janela" or acao_do_personagem=="ver janela" or acao_do_personagem=="ver a janela"):
                                                print("Voce ve uma rua com predios de classe baixa,")
                                                time.sleep(3)
                                                print("poucas pessoas passando com cara de cansadas,")
                                                time.sleep(3)
                                                print("mas voce nao consegue ver o horizonte,")
                                                time.sleep(3)
                                                print("ja que voce mora no primeiro andar e os predios do outro")
                                                time.sleep(4)
                                                print("lado da rua sao altos e proximos demais uns dos outros.")
                                                time.sleep(4)
                                                print("Voce percebe um sujeito te encarando do outro lado da rua...")
                                                time.sleep(4)
                                                print("Ele esta em pe e encostado na grade cinza, empoeirada e enferrujada")
                                                time.sleep(4)
                                                print("do predio da frente um pouco à esquerda da porta dessa grade,")
                                                time.sleep(4)
                                                print("de modo a ficar de frente para a porta do seu predio.")
                                                time.sleep(3)
                                                print("Sua face cheia de raiva expressa com rigidez a sua intencao,")
                                                time.sleep(3)
                                                print("sua jeans e velha, sua camisa e rasgada de forma a parecer uma regata,")
                                                time.sleep(3)
                                                print("enquanto seus bracos cruzados parecem prontos para uma briga!")
                                                time.sleep(5)
                                            else:
                                                if (acao_do_personagem == "olhar a estante" or acao_do_personagem =="ohar a estante" or acao_do_personagem =="ohar estante" or acao_do_personagem == "olhar estante" or acao_do_personagem == "olha a estante" or acao_do_personagem == "olha estante" or acao_do_personagem == "estante" or acao_do_personagem == "ver a estante" or acao_do_personagem == "ver estante" or acao_do_personagem == "ver a estante" or acao_do_personagem == "ver estante" or acao_do_personagem =="olahr a estante"):
                                                    print("Voce ve livros e apostilas rabiscadas na capa e a maioria rasgadas no canto dos furos das espirais.\n...\n Nada muito interessante...\n")
                                                    time.sleep(1)
                                                    print("Mas voce ve um pedaco de papel vermelho colocado entre as paginas de um dos livros...")
                                                    time.sleep(1)
                                                    print("Ler o bilhete?? (sim ou nao)\n")
                                                    while 1:
                                                        acao_do_personagem=raw_input("-")
                                                        acao_do_personagem=acao_do_personagem.lower()
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(' "       Voce pode digitar seus comandos de outras formas, como por exemplo,')
                                                            time.sleep(3)
                                                            print("ao inves de digitar 'ver ficha do personagem' voce pode simplesmente digitar 'ficha'!")
                                                            time.sleep(3)
                                                            print('Tente sempre digitar da forma mais simples, isso facilitara muito o seu jogo!')
                                                            time.sleep(3)
                                                            print('Nao custa nada tentar! ;)')
                                                            time.sleep(3)
                                                            print('                               assinado: Programador "')
                                                            time.sleep(3)
                                                            break
                                                        else:
                                                            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                print("Voce ignorou o bilhete.")
                                                                time.sleep(1)
                                                                break
                                                            else:
                                                                print('Entrada invalida! Digite "sim" ou "Nao"')
                                                                time.sleep(1)
                                                else:
                                                    if (acao_do_personagem == "destruir o universo"): #Easter-Egg para o Yuri
                                                        print("Adeus...")
                                                        time.sleep(0.5)
                                                        while 1:
                                                            acao_do_personagem = raw_input("")
                                                            acao_do_personagem = acao_do_personagem.lower()
                                                            if(acao_do_personagem=="reconstruir o universo" or acao_do_personagem == "reconstruir universo" or acao_do_personagem == "construir o universo" or acao_do_personagem == "criar um novo universo" or acao_do_personagem == "construir um universo" or acao_do_personagem == "criar o universo"):
                                                                break
                                                        print("Ola!")
                                                        time.sleep(1)
                                                    else:
                                                        if(acao_do_personagem=="sair do quarto" or acao_do_personagem=="sair" or acao_do_personagem=="ir para a aula" or acao_do_personagem=="ir pra aula" or acao_do_personagem=="ir para aula" or acao_do_personagem=="ir à aula" or acao_do_personagem=="ir a aula" or acao_do_personagem=="sair quarto"):
                                                            while 1:
                                                                print("Se sair voce nao podera voltar.\n")
                                                                time.sleep(3)
                                                                print("Tem certeza que deseja sair? (sim ou nao)")
                                                                acao_do_personagem=raw_input("-")
                                                                acao_do_personagem=acao_do_personagem.lower()
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    acao_do_personagem="sim"
                                                                    break
                                                                else:
                                                                    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                        print("Voce decidiu nao sair do quarto.")
                                                                        time.sleep(1)
                                                                        break
                                                                    else:
                                                                        print("Entrada invalida!")
                                                                        time.sleep(1)
                                                            if(acao_do_personagem=="sim"):
                                                                break
                                                        else:
                                                            if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventario" or acao_do_personagem=="ver o inventario" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventario" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventario" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="itens" or acao_do_personagem=="item"):
                                                                inventarioPersonagem()
                                                            else:
                                                                print('\nEntrada Invalida!\n')
                print("\n#"+ "-"*30+"#\n\nLista de Acões\n\nCenario:"+str(variavel_lugar))
                time.sleep(0.23)
                print("\n\nVoce pode:\n\nvestir\narrumar o quarto\nolhar\n")
                time.sleep(0.23)
                if (variavel_cenario[0] == "sim"):
                    print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\n\nolhar pela janela\n")
                    time.sleep(0.5)
                print("\nver ficha do personagem\nver mochila\nsair do quarto\n")
                time.sleep(0.5)
                if(eegg > 1 and eegg<6):
                    print("\nVoce nao deve:\nolhar a janela\n")
                    time.sleep(0.23)
                print("\n#"+ "-"*30+"#\n")
                print("\nE agora, "+str(personagem_jogador[0])+", o que voce vai fazer?\n")
                acao_do_personagem = raw_input("-")
                acao_do_personagem = acao_do_personagem.lower()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 1
            variavel_cenario[1] = "nao"
            variavel_cenario[0] = "nao"
            temporario[0] = False
            print("Voce saiu do seu quarto.")
            time.sleep(1)
            save()

##########--------------------------------------------------FIM DA PRIMEIRA PARTE--------------------------------------------------##########
        if(ponto_de_save==1):
            if(variavel_lugar == "seu predio, 1º andar" or variavel_lugar == "seu predio, 2º andar" or variavel_lugar == "seu predio, 3º andar" or variavel_lugar == "seu predio, 4º andar"):
                if(variavel_lugar == "seu predio, 1º andar"):
                    variavel_lugar = "seu predio, 1º andarb"
                if(variavel_lugar == "seu predio, 2º andar"):
                    variavel_lugar = "seu predio, 2º andarb"
                if(variavel_lugar == "seu predio, 3º andar"):
                    variavel_lugar = "seu predio, 3º andarb"
                if(variavel_lugar == "seu predio, 4º andar"):
                    variavel_lugar = "seu predio, 4º andarb"
                seuPredioPrimeiroAndar()
            else:
                print("\nCenario: Voce continua atrasado para a aula - nao que voce deva se importar muito com isso.")
                time.sleep(2)
                variavel_lugar = "seu predio, 1º andar"
                seuPredioPrimeiroAndar()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 2
            variavel_lugar = "em frente ao seu predio"
            save()


##########--------------------------------------------------FIM DA SEGUNDA PARTE--------------------------------------------------##########
        if(ponto_de_save==2):
            print("\nCenario:Agora voce esta na sua rua.\n\n")
            time.sleep(2)
            print("Antes que voce pudesse fazer alguma coisa,")
            time.sleep(3)
            print("foi abordado por um homem aparentemente forte vestindo uma jeans velha")
            time.sleep(3)
            print("e uma camisa que foi rasgada de forma a parecer uma regata...\n")
            time.sleep(3)
            print("Seu rosto era magro, de tao afundadas que as bochechas eram, parecia uma caveira,")
            time.sleep(3)
            print("sua pele queimada pelo Sol era cheia de manchas, seu cabelo crespo crescia por cima das ventas,")
            time.sleep(3)
            print("mas a calvisse da sua fronte se extendia ate a ponta extrema da sua arredondada e fosca cabeca...\n")
            time.sleep(3)
            print(" - Cade o dinheiro que voce roubou do meu esquema?\n")
            time.sleep(2)
            print("Mas voce REALMENTE nao sabia de esquema algum, quanto menos do dinheiro...\n")
            time.sleep(3)
            print("Algo nao parece certo...\n")
            time.sleep(1)
            print(" - Nao adianta negar!!! Escolhe, moleque: a grana ou a vida???\n")
            time.sleep(1)
            print("...")
            time.sleep(3)
            print("Ele saca uma faca do bolso de tras!\n")
            time.sleep(2)
            print(" - EU VOU TE QUEBRAR ATÉ VOCÊ ME DAR O DINHEIRO!!!\n")
            time.sleep(2)
            personagem_inimigo = [ "Bandido", 300, 100, 20, 20, 25000, 25000]
            batalha()
            if(personagem_jogador[6]<=0):
                personagem_jogador[6]=1
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
                print("Voce se levantou rapidamente e pôde, entao, observar a sitiuacao...")
                time.sleep(3)
                print("Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,")
                time.sleep(5)
                print("uma calca preta rasgada nos joelhos e um all-star preto,")
                time.sleep(5)
                print("alem da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titanio.")
                time.sleep(6)
                personagem_reserva = personagem_jogador
                personagem_jogador = [ "Lutador Headbanger", 1200, 800, 50, 50, 100000, 100000,0]
                batalha()
                personagem_jogador = personagem_reserva
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
                print("Sera que voce encontrara alguma pista na escola?")
                time.sleep(5)
            else:
                if(personagem_inimigo[6]>0):
                    while(personagem_inimigo[6]>0):
                        print("Voce correu um pouco mas ele te alcancou de novo!\n")
                        batalha()
                        if(personagem_jogador[6]<=0):
                            personagem_jogador[6]=1
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
                            print("Voce se levantou rapidamente e pôde, entao, observar a sitiuacao...")
                            time.sleep(3)
                            print("Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,")
                            time.sleep(5)
                            print("uma calca preta rasgada nos joelhos e um all-star preto,")
                            time.sleep(5)
                            print("alem da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titanio.")
                            time.sleep(6)
                            personagem_reserva = personagem_jogador
                            personagem_jogador = [ "Lutador Headbanger", 1200, 800, 50, 50, 100000, 100000, 0]
                            batalha()
                            personagem_jogador = personagem_reserva
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
                            print("Sera que voce encontrara alguma pista na escola?")
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
                            print("Sera que voce encontrara alguma pista na escola?")
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
                    personagem_inimigo = [ "Motoqueiro Comparsa", 3000, 10, 50, -5, 50, 50]
                    batalha()
                    if(personagem_jogador[6]<=0): break
                    if(personagem_inimigo[6]>0):
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
            if(variavel_lugar == "seu predio, 1º andar" or variavel_lugar == "seu predio, 2º andar" or variavel_lugar == "seu predio, 3º andar" or variavel_lugar == "seu predio, 4º andar"):
                if(variavel_lugar == "seu predio, 1º andar"):
                    variavel_lugar = "seu predio, 1º andarb"
                if(variavel_lugar == "seu predio, 2º andar"):
                    variavel_lugar = "seu predio, 2º andarb"
                if(variavel_lugar == "seu predio, 3º andar"):
                    variavel_lugar = "seu predio, 3º andarb"
                if(variavel_lugar == "seu predio, 4º andar"):
                    variavel_lugar = "seu predio, 4º andarb"
                seuPredioPrimeiroAndar()
                variavel_lugar = "sua rua"
            else:
                print("Cenario:Voce esta na sua rua, por agora tudo esta calmo....")
                suaRua()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 4
            save()

##########--------------------------------------------------FIM DO JOGO--------------------------------------------------##########
        break
    if(personagem_jogador[6]>0):
        print("\nParabens, "+str(personagem_jogador[0]+"!!! Voce terminou o jogo!!!")
        if(temporario[2]==False):
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
    print("\nVoce deseja jogar novamente, "+str(personagem_jogador[0])+'?("sim" ou "nao")\n')
    while 1:
        acao_do_personagem = raw_input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
            raw_input("\nReiniciando...(APERTE ENTER)\n")
            if (personagem_jogador[6] <= 0):
                print("Voce morreu, "+ personagem_jogador[0]+ "...\nO jogo acabou para voce...")
                #"Nome"[0], atq[1], def[2], agi[3], luk[4], vidamaxima[5], vidaatual[6], dinheiro[7]
                personagem_jogador = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
                personagem_reserva = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
                personagem_inimigo = [ "Inimigo", 10, 8, 1, 1, 100, 100]

                #["Nome"[0], atq[1], def[2], agi[3], luk[4], tipo[5], preco[6], recupera[7]

                desequipado_roupa = ["Nada", 0, 0, 0, 0, "roupa", 0, 0]
                desequipado_capa = ["Nada", 0, 0, 0, 0, "capa", 0, 0]
                desequipado_luva = ["Nada", 0, 0, 0, 0, "luva", 0, 0]
                desequipado_anel = ["Nada", 0, 0, 0, 0, "anel", 0, 0]
                desequipado_maos = ["Nada", 0, 0, 0, 0, "armamento", 0, 0]
                desequipado_calcado = ["Nada", 0, 0, 0, 0, "calcados", 0, 0]
                espaco_vazio = ["Vazio", 0, 0, 0, 0, "inventario", 0, 0]

                pedaco_pizza = ["Pedaco de Pizza", 0, 0, 0, 0, "consumivel", 5, 50]
                bolo_chocolate = ["Bolo de Chocolate", 0, 0, 0, 0, "consumivel", 100, personagem_jogador[5]]

                pijama_inicial = ["Pijama", 0, 0, 0, 5, "roupa", 5, 0]
                uniforme_estudantil = ["Uniforme Estudantil",0,1,0,0,"roupa",5,0]
                malha_ninja = ["Malha Ninja", 5, 20, 5, 1, "roupa", 5000, 0]

                lapis_apontado = ["Lapis Apontado", 3,0,0,1,"armamento",2,0]
                punhal_envelhecido = ["Punhal Envelhecido", 10, 0,0,3,"armamento",300,0]
                talheres_prata = ["Talheres de prata(Garfo e Faca)", 8, 0,0,0,"armamento",10,0]

                jaqueta_imitacao = ["Jaqueta de Imitacao de Couro", 0, 20, 0, 0,"capa",150,0]
                jaqueta_couro = ["Jaqueta de Couro", 0, 200, 0, 10,"capa",2000,0]
                agasalho_la = ["Agasalho de La", 0, 6, 0, 0,"capa",100,0]

                suplemento_alimenticio = ["Suplemento Alimenticio", 10, 0, 0, 0, "consumivel de aprimoramento",5, 0]
                lata_energetico = ["Energetico", 0, 0, 0, 0, "consumivel de aprimoramento",5, 50]

                luva_la = ["Luvas de La", 0, 3, 0, 0, "luva", 20, 0]
                luva_imitacao = ["Luvas de Imitacao de Couro", 3, 3, 0, 0, "luva", 100, 0]
                soco_pvc = ["Soco-Ingles de PVC", 3, 0, 0, 0, "luva", 50, 0]
                luva_couro = ["Luvas de Couro", 8, 8, 0, 0, "luva", 500, 0]
                soco_latao = ["Soco-Ingles de Latao", 10, 0, 0, 0, "luva", 500, 0]
                luva_spikes_alu = ["Luvas de Couro com Spikes de Aluminio", 15, 15, 0, 0, "luva", 700, 0]
                soco_alu = ["Soco-Ingles de Aluminio", 25, 0, 0, 0, "luva", 700, 0]
                luva_spikes_aco = ["Luvas de Couro com Spikes de Aco", 25, 25, 0, 0, "luva", 1000, 0]
                soco_aco = ["Soco-Ingles de Aluminio de Aco", 30, 0, 0, 0, "luva", 1000, 0]
                luva_spikes_ag = ["Luvas de Couro com Spikes de Prata", 25, 25, 0, 5, "luva", 5000, 0]
                soco_ag = ["Soco-Ingles de Prata", 35, 0, 0, 5, "luva", 5000, 0]
                luva_spikes_au = ["Luvas de Couro com Spikes de Ouro", 250, 250, 0, 10, "luva", 10000, 0]
                soco_au = ["Soco-Ingles de Ouro", 350, 0, 0, 10, "luva", 10000, 0]
                luva_spikes_titanio = ["Luvas de Couro com Spikes de Titanio", 2500, 2500, 0, 20, "luva", 50000, 0]
                soco_titanio = ["Soco-Ingles de Titanio", 3500, 0, 0, 20, "luva", 50000, 0]

                anel_forca1 = ["Anel da Forca 1", 10, -2, -2, -2, "anel", 500, 0]
                anel_resistencia1 = ["Anel da Resistencia 1", -2, 10, -2, -2, "anel", 500, 0]
                anel_forca2 = ["Anel da Forca 2", 20, -4, -4, -4, "anel", 1000, 0]
                anel_resistencia2 = ["Anel da Resistencia 2", -4, 20, -4, -4, "anel", 1000, 0]
                anel_forca3 = ["Anel da Forca 2", 40, -8, -8, -8, "anel", 5000, 0]
                anel_resistencia3 = ["Anel da Resistencia 2", -8, 40, -8, -8, "anel", 5000, 0]

                anel_consistencia1 = ["Anel da Consistencia 1", -2, -2, -2, -2, "anel", 500, 10]
                anel_consistencia2 = ["Anel da Consistencia 2", -4, -4, -4, -4, "anel", 1000, 100]
                anel_consistencia3 = ["Anel da Consistencia 3", -8, -8, -8, -8, "anel", 5000, 1000]

                anel_da_imortalidade = ["Anel da Imortalidade", personagem_jogador[1], personagem_jogador[2], personagem_jogador[3], personagem_jogador[4], "anel", 100000, personagem_jogador[5]]
                anel_da_divindade = ["Anel da Divindade", personagem_jogador[1]*2, personagem_jogador[2]*2, personagem_jogador[3]*2, personagem_jogador[4]*2, "anel", 100000000, personagem_jogador[5]*2]

                chinelo_inicial = ["Chinelos", 0, 0, 0, -5, "calcados", 5, 0]
                papetes_masculinas = ["Papetes Masculinas", 0, 0, 1, 0, "calcados", 15, 0]
                tenis_velho = ["Tenis Velho", 0, 0, 2, 0, "calcados", 10, 0]
                tenis_simplorio = ["Tenis Simplorio", 0, 1, 2, 0, "calcados", 50, 0]
                sapato_simplorio = ["Sapato Simplorio", 0, 2, 1, 0, "calcados", 50, 0]
                tenis_comum = ["Tenis Comum", 0, 2, 2, 0, "calcados", 90, 0]
                tenis_trilha = ["Tenis de Trilha", 2, 8, 3, 0, "calcados", 400, 0]
                tenis_caminhada = ["Tenis de Caminhada", 0, 3, 5, 0, "calcados", 300, 0]
                tenis_corrida = ["Tenis de Corrida", 0, 5, 10, 0, "calcados", 500, 0]
                tenis_ZX5000 = ["Tenis ZX-5000", 10, 10, 11, 5, "calcados", 15000, 0]

                item_adicionado=espaco_vazio
                quantidade_adicionada=1

                equipado_roupa = pijama_inicial
                equipado_capa = desequipado_capa
                equipado_luva = desequipado_luva
                equipado_anel = desequipado_anel
                equipado_maos = desequipado_maos
                equipado_calcado = chinelo_inicial

                variavel_cenario = ["nao" ,"nao" ,"nao"]
                #[0]  olhar cenario primeira vez no seu quarto e reciclada no primeiro andar do seu predio
                #[1]  modificar cenario primeira vez no seu quarto
                #[2]  cheirar cenario no primeiro andar do seu predio

                objeto = ["nao", "nao", "nao", "nao", "nao"]
                #[0]  presente do tutorial e reciclada no bebado do 1ºandar
                #[1]  porta do quarto 10
                #[2]  energetico do bebado (acao revistar)
                #[3]  arrombar porta do quarto 10
                #[4]  mulher do bebado - talheres de prata

                situacao = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
                #[0]  dois últimos andares do seu predio
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

                temporario = [False, False, False]
                #[0]  verifica se pegou o uniforme no seu quarto depois e reciclada para verificar se ja venceu o terceiro andar do seu predio
                #[1]  verifica se pegou o soco ingles no seu quarto depois e reciclada para verificar se 
                #[2]  verifica se ja zerou o jogo antes
                
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


                #global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaco_vazio,pedaco_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_la,suplemento_alimenticio,lata_energetico,luva_la,luva_couro,soco_pvc,soco_latao,luva_spikes_alu,soco_alu,luva_spikes_aco,soco_aco,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titanio,soco_titanio,anel_forca1,anel_forca2,anel_forca3,anel_resistencia1,anel_resistencia2,anel_resistencia3,anel_consistencia1,anel_consistencia2,anel_consistencia3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tenis_velho,tenis_simplorio,sapato_simplorio,tenis_comum,tenis_trilha,tenis_caminhada,tenis_corrida,tenis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variavel_cenario,objeto,situacao,temporario,variavel_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variavel_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda

                mala = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio]
                loja_venda = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio,espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio, espaco_vazio]

            break
        else:
            if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                break
            else:
                print('\nEntrada invalida!(digite "sim" ou "nao)\n')
    if(acao_do_personagem == "nao" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="na" or acao_do_personagem=="ao" or acao_do_personagem=="ao" or acao_do_personagem=="ñ" or acao_do_personagem=="ñao" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ña" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
        break
    
exit()
