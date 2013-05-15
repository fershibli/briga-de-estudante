#--Import--#
#use o python 2.7.4 que é coisa de macho!!!!!!11!!!!!1!!onze!!!! - Lucas Sabião
import random
import configparser
import pickle
import time

#ASSISTA DEVIL SURVIVOR 2

#"Nome"[0], atq[1], def[2], agi[3], luk[4], vidamáxima[5], vidaatual[6], dinheiro[7]
personagem_jogador = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
personagem_reserva = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
personagem_inimigo = [ "Inimigo", 10, 8, 1, 1, 100, 100]

#["Nome"[0], atq[1], def[2], agi[3], luk[4], tipo[5], preço[6], recupera[7]

desequipado_roupa = ["Nada", 0, 0, 0, 0, "roupa", 0, 0]
desequipado_capa = ["Nada", 0, 0, 0, 0, "capa", 0, 0]
desequipado_luva = ["Nada", 0, 0, 0, 0, "luva", 0, 0]
desequipado_anel = ["Nada", 0, 0, 0, 0, "anel", 0, 0]
desequipado_maos = ["Nada", 0, 0, 0, 0, "armamento", 0, 0]
desequipado_calcado = ["Nada", 0, 0, 0, 0, "calçados", 0, 0]
espaço_vazio = ["Vazio", 0, 0, 0, 0, "inventário", 0, 0]

pedaço_pizza = ["Pedaço de Pizza", 0, 0, 0, 0, "consumível", 5, 50]
bolo_chocolate = ["Bolo de Chocolate", 0, 0, 0, 0, "consumível", 100, personagem_jogador[5]]

pijama_inicial = ["Pijama", 0, 0, 0, 5, "roupa", 5, 0]
uniforme_estudantil = ["Uniforme Estudantil",0,1,0,0,"roupa",5,0]
malha_ninja = ["Malha Ninja", 5, 20, 5, 1, "roupa", 5000, 0]

lapis_apontado = ["Lápis Apontado", 3,0,0,1,"armamento",2,0]
punhal_envelhecido = ["Punhal Envelhecido", 10, 0,0,3,"armamento",300,0]
talheres_prata = ["Talheres de prata(Garfo e Faca)", 8, 0,0,0,"armamento",10,0]

jaqueta_imitacao = ["Jaqueta de Imitação de Couro", 0, 20, 0, 0,"capa",150,0]
jaqueta_couro = ["Jaqueta de Couro", 0, 200, 0, 10,"capa",2000,0]
agasalho_lã = ["Agasalho de Lã", 0, 6, 0, 0,"capa",100,0]

suplemento_alimentício = ["Suplemento Alimentício", 10, 0, 0, 0, "consumível de aprimoramento",5, 0]
lata_energético = ["Energético", 0, 0, 0, 0, "consumível de aprimoramento",5, 50]

luva_lã = ["Luvas de Lã", 0, 3, 0, 0, "luva", 20, 0]
luva_imitacao = ["Luvas de Imitação de Couro", 3, 3, 0, 0, "luva", 100, 0]
soco_pvc = ["Soco-Inglês de PVC", 3, 0, 0, 0, "luva", 50, 0]
luva_couro = ["Luvas de Couro", 8, 8, 0, 0, "luva", 500, 0]
soco_latão = ["Soco-Inglês de Latão", 10, 0, 0, 0, "luva", 500, 0]
luva_spikes_alu = ["Luvas de Couro com Spikes de Aluminio", 15, 15, 0, 0, "luva", 700, 0]
soco_alu = ["Soco-Inglês de Alumínio", 25, 0, 0, 0, "luva", 700, 0]
luva_spikes_aço = ["Luvas de Couro com Spikes de Aço", 25, 25, 0, 0, "luva", 1000, 0]
soco_aço = ["Soco-Inglês de Alumínio de Aço", 30, 0, 0, 0, "luva", 1000, 0]
luva_spikes_ag = ["Luvas de Couro com Spikes de Prata", 25, 25, 0, 5, "luva", 5000, 0]
soco_ag = ["Soco-Inglês de Prata", 35, 0, 0, 5, "luva", 5000, 0]
luva_spikes_au = ["Luvas de Couro com Spikes de Ouro", 250, 250, 0, 10, "luva", 10000, 0]
soco_au = ["Soco-Inglês de Ouro", 350, 0, 0, 10, "luva", 10000, 0]
luva_spikes_titânio = ["Luvas de Couro com Spikes de Titânio", 2500, 2500, 0, 20, "luva", 50000, 0]
soco_titânio = ["Soco-Inglês de Titânio", 3500, 0, 0, 20, "luva", 50000, 0]

anel_força1 = ["Anel da Força 1", 10, -2, -2, -2, "anel", 500, 0]
anel_resistência1 = ["Anel da Resistência 1", -2, 10, -2, -2, "anel", 500, 0]
anel_força2 = ["Anel da Força 2", 20, -4, -4, -4, "anel", 1000, 0]
anel_resistência2 = ["Anel da Resistência 2", -4, 20, -4, -4, "anel", 1000, 0]
anel_força3 = ["Anel da Força 2", 40, -8, -8, -8, "anel", 5000, 0]
anel_resistência3 = ["Anel da Resistência 2", -8, 40, -8, -8, "anel", 5000, 0]

anel_consistência1 = ["Anel da Consistência 1", -2, -2, -2, -2, "anel", 500, 10]
anel_consistência2 = ["Anel da Consistência 2", -4, -4, -4, -4, "anel", 1000, 100]
anel_consistência3 = ["Anel da Consistência 3", -8, -8, -8, -8, "anel", 5000, 1000]

anel_da_imortalidade = ["Anel da Imortalidade", personagem_jogador[1], personagem_jogador[2], personagem_jogador[3], personagem_jogador[4], "anel", 100000, personagem_jogador[5]]
anel_da_divindade = ["Anel da Divindade", personagem_jogador[1]*2, personagem_jogador[2]*2, personagem_jogador[3]*2, personagem_jogador[4]*2, "anel", 100000000, personagem_jogador[5]*2]

chinelo_inicial = ["Chinelos", 0, 0, 0, -5, "calçados", 5, 0]
papetes_masculinas = ["Papetes Masculinas", 0, 0, 1, 0, "calçados", 15, 0]
tênis_velho = ["Tênis Velho", 0, 0, 2, 0, "calçados", 10, 0]
tênis_simplório = ["Tênis Simplório", 0, 1, 2, 0, "calçados", 50, 0]
sapato_simplório = ["Sapato Simplório", 0, 2, 1, 0, "calçados", 50, 0]
tênis_comum = ["Tênis Comum", 0, 2, 2, 0, "calçados", 90, 0]
tênis_trilha = ["Tênis de Trilha", 2, 8, 3, 0, "calçados", 400, 0]
tênis_caminhada = ["Tênis de Caminhada", 0, 3, 5, 0, "calçados", 300, 0]
tênis_corrida = ["Tênis de Corrida", 0, 5, 10, 0, "calçados", 500, 0]
tênis_ZX5000 = ["Tênis ZX-5000", 10, 10, 11, 5, "calçados", 15000, 0]

item_adicionado=espaço_vazio
quantidade_adicionada=1

equipado_roupa = pijama_inicial
equipado_capa = desequipado_capa
equipado_luva = desequipado_luva
equipado_anel = desequipado_anel
equipado_maos = desequipado_maos
equipado_calcado = chinelo_inicial

variável_cenário = ["não" ,"não" ,"não"]
#[0]  olhar cenário primeira vez no seu quarto e reciclada no primeiro andar do seu prédio
#[1]  modificar cenário primeira vez no seu quarto
#[2]  cheirar cenário no primeiro andar do seu prédio

objeto = ["não", "não", "não", "não", "não"]
#[0]  presente do tutorial e reciclada no bêbado do 1ºandar
#[1]  porta do quarto 10
#[2]  energético do bêbado (ação revistar)
#[3]  arrombar porta do quarto 10
#[4]  mulher do bêbado - talheres de prata

situacao = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
#[0]  dois últimos andares do seu prédio
#[1]  quarto 11 do seu prédio
#[2]  quarto 24 do seu prédio
#[3]  quarto 21 do seu prédio
#[4]  quarto 22 do seu prédio
#[5]  quarto 30 do seu prédio
#[6]  quarto 31 do seu prédio
#[7]  quarto 32 do seu prédio
#[8]  quarto 33 do seu prédio
#[9]  quarto 34 do seu prédio
#[10] quarto 20 do seu prédio

temporário = [False, False]
#[0]  verifica se pegou o uniforme no seu quarto depois é reciclada para verificar se já venceu o terceiro andar do seu prédio
#[1]  verifica se pegou o soco inglês no seu quarto depois é reciclada para verificar se 

variável_lugar = "seu quarto"
ponto_de_save = 0

mostrar_save = ''

eegg = 1

acao_do_personagem = "" 
batalha_escapar = ""

teste_de_sorte = 0
calculo_do_dano = 0
calculo_da_fuga = 0
variável_para_comparar = 0
contador_de_batalha= 0
contador_de_rodadas = 0


#global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda

mala = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio]
loja_venda = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio]

#--Adicionar Item ao Inventário--#
def adicionaItem():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while (quantidade_adicionada>0):
        i=0
        while i<=29:
            if(mala[1][i]==espaço_vazio or mala[1][i][0]=="Nada"):
                mala[1][i]=item_adicionado
                break
            i+=1
        quantidade_adicionada-=1

#--Inventário--#
def inventárioPersonagem():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 1:
        print("Mochila:\n")
        time.sleep(0.5)
        i=0
        while i<=29:
            if (mala[1][i]!=espaço_vazio and mala[1][i][0]!="Nada"):
                print(mala[0][i]," : ",mala[1][i][0],"\n     (",mala[1][i][5],")\n")
            i+=1
        while 1:
            print("Para analisar um item digite o número da sua posição!\nPara voltar ao jogo digite voltar.")
            acao_do_personagem = input('-')
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
        if(acao_do_personagem==mala[0][i] and mala[1][i]!=espaço_vazio and mala[1][i][0]!="Nada"):
            if(mala[1][i][5]=="consumível de aprimoramento"):
                print("\nNome:",mala[1][i][0], "\nTipo:",mala[1][i][5],"\nVida:",mala[1][i][7],"\nAtaque:",mala[1][i][1],"\nDefesa:",mala[1][i][2],"\nAgilidade:",mala[1][i][3],"\nSorte:",mala[1][i][4],"\n")
                print("O que deseja fazer? (usar ou descartar)")
                acao_do_personagem=input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="usar"):
                    personagem_jogador[5]=personagem_jogador[5]+mala[1][i][7]
                    personagem_jogador[6]=personagem_jogador[5]
                    personagem_jogador[1]=personagem_jogador[1]+mala[1][i][1]
                    personagem_jogador[2]=personagem_jogador[2]+mala[1][i][2]
                    personagem_jogador[3]=personagem_jogador[3]+mala[1][i][3]
                    personagem_jogador[4]=personagem_jogador[4]+mala[1][i][4]
                    print("\nVocê usou", mala[1][i][0],"!\n")
                    time.sleep(0.5)
                    mala[1][i]=espaço_vazio
                else:
                    if(acao_do_personagem=="descartar"):
                        while 1:
                            print("\nTem certeza que deseja descartar?\n")
                            acao_do_personagem=input("-")
                            acao_do_personagem=acao_do_personagem.lower()
                            if(acao_do_personagem!="não" or acao_do_personagem!="sim"):
                                print("\nENTRADA INVÁLIDA!\n")
                                time.sleep(0.5)
                            else:break
                        if(acao_do_personagem=="sim"):
                            print("\nVocê descartou",mala[1][i][0],"!\n")
                            time.sleep(0.5)
                            mala[1][i]=espaço_vazio
            if(mala[1][i][5]=="consumível"):
                print("\nNome:",mala[1][i][0], "\nTipo:",mala[1][i][5],"\nVida:",mala[1][i][7],"\n")
                print("O que deseja fazer? (usar ou descartar)")
                acao_do_personagem=input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="usar"):
                    personagem_jogador[6]=personagem_jogador[6]+mala[1][i][7]
                    if (personagem_jogador[6]>personagem_jogador[5]+0.1*personagem_jogador[6]):
                        personagem_jogador[6]=personagem_jogador[5]
                    print("\nVocê usou", mala[1][i][0],"!\n")
                    time.sleep(0.5)
                    mala[1][i]=espaço_vazio
                else:
                    if(acao_do_personagem=="descartar"):
                        while 1:
                            print("\nTem certeza que deseja descartar?\n")
                            acao_do_personagem=input("-")
                            acao_do_personagem=acao_do_personagem.lower()
                            if(acao_do_personagem!="não" or acao_do_personagem!="sim"):
                                print("\nENTRADA INVÁLIDA!\n")
                                time.sleep(0.5)
                            else:break
                        if(acao_do_personagem=="sim"):
                            print("\nVocê descartou",mala[1][i][0],"!\n")
                            mala[1][i]=espaço_vazio
            if(mala[1][i][5]!="consumível de aprimoramento" and mala[1][i][5]!="consumível"):
                print("\nNome:",mala[1][i][0],"\nTipo:",mala[1][i][5],"\nAtaque:",mala[1][i][1],"\nDefesa:",mala[1][i][2],"\nAgilidade:",mala[1][i][3],"\nSorte:",mala[1][i][4],"\n")
                print("O que deseja fazer? (equipar ou descartar)")
                acao_do_personagem=input("-")
                acao_do_personagem=acao_do_personagem.lower()
                if(acao_do_personagem=="descartar"):
                    mala[1][i]=espaço_vazio
                else:
                    if(acao_do_personagem=="equipar"):
                        if(mala[1][i][5]=="roupa"):
                            print("Você guardou ", equipado_roupa[0]," e equipou ", mala[1][i][0],"!")
                            personagem_jogador[1] = personagem_jogador[1] - equipado_roupa[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_roupa[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_roupa[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_roupa[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_roupa[7]
                            item_adicionado=equipado_roupa
                            equipado_roupa=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_roupa[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_roupa[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_roupa[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_roupa[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_roupa[7]
                        if(mala[1][i][5]=="capa"):                            
                            personagem_jogador[1] = personagem_jogador[1] - equipado_capa[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_capa[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_capa[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_capa[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_capa[7]
                            item_adicionado=equipado_capa
                            equipado_capa=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_capa[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_capa[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_capa[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_capa[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_capa[7]
                        if(mala[1][i][5]=="luva"):
                            personagem_jogador[1] = personagem_jogador[1] - equipado_luva[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_luva[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_luva[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_luva[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_luva[7]
                            item_adicionado=equipado_luva
                            equipado_luva=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_luva[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_luva[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_luva[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_luva[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_luva[7]
                        if(mala[1][i][5]=="anel"):
                            personagem_jogador[1] = personagem_jogador[1] - equipado_anel[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_anel[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_anel[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_anel[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_anel[7]
                            item_adicionado=equipado_anel
                            equipado_anel=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_anel[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_anel[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_anel[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_anel[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_anel[7]
                        if(mala[1][i][5]=="armamento"):
                            personagem_jogador[1] = personagem_jogador[1] - equipado_maos[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_maos[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_maos[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_maos[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_maos[7]
                            item_adicionado=equipado_maos
                            equipado_maos=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_maos[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_maos[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_maos[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_maos[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_maos[7]
                        if(mala[1][i][5]=="calçados"):
                            personagem_jogador[1] = personagem_jogador[1] - equipado_calcado[1]
                            personagem_jogador[2] = personagem_jogador[2] - equipado_calcado[2]
                            personagem_jogador[3] = personagem_jogador[3] - equipado_calcado[3]
                            personagem_jogador[4] = personagem_jogador[4] - equipado_calcado[4]
                            personagem_jogador[5] = personagem_jogador[5] - equipado_calcado[7]
                            item_adicionado=equipado_calcado
                            equipado_calcado=mala[1][i]
                            mala[1][i]=item_adicionado
                            personagem_jogador[1] = personagem_jogador[1] + equipado_calcado[1]
                            personagem_jogador[2] = personagem_jogador[2] + equipado_calcado[2]
                            personagem_jogador[3] = personagem_jogador[3] + equipado_calcado[3]
                            personagem_jogador[4] = personagem_jogador[4] + equipado_calcado[4]
                            personagem_jogador[5] = personagem_jogador[5] + equipado_calcado[7]                            
                        if(mala[1][i][5]=="consumível" or mala[1][i][5]=="consumível de aprimoramento"):
                            print("você não pode equipar!")
                            time.sleep(0.5)
                    else:
                        print("\nENTRADA INVÁLIDA!\n")
                        time.sleep(0.5)

#--Loja Padrão--#
def lojaPadrão():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    while 2:
        print("\n(comprar, vender ou sair)")
        acao_do_personagem=input("-")
        acao_do_personagem=acao_do_personagem.lower()
        if(acao_do_personagem=="vender"):
            while 1:
                print("Mochila:\n")
                time.sleep(0.5)
                i=0
                while i<=29:
                    if (mala[1][i]!=espaço_vazio and mala[1][i][0]!="Nada"):
                        print(mala[0][i]," : ",mala[1][i][0],"\n     (",mala[1][i][5],")\n")
                    i+=1
                while 1:
                    print("Para analisar um item digite o número da sua posição!\nPara voltar ao jogo digite voltar.")
                    acao_do_personagem = input('-')
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
                if(acao_do_personagem==mala[0][i] and mala[1][i]!=espaço_vazio and mala[1][i][0]!="Nada"):
                    if(mala[1][i][5]=="consumível de aprimoramento"):
                        print("\nNome:",mala[1][i][0], "\nTipo:",mala[1][i][5],"\nVida:",mala[1][i][7],"\nAtaque:",mala[1][i][1],"\nDefesa:",mala[1][i][2],"\nAgilidade:",mala[1][i][3],"\nSorte:",mala[1][i][4],"\n")
                if(mala[1][i][5]=="consumível"):
                    print("\nNome:",mala[1][i][0], "\nTipo:",mala[1][i][5],"\nVida:",mala[1][i][7],"\n")
                if(mala[1][i][5]!="consumível de aprimoramento" and mala[1][i][6]!="consumível"):
                    print("\nNome:",mala[1][i][0],"\nTipo:",mala[1][i][5],"\nAtaque:",mala[1][i][1],"\nDefesa:",mala[1][i][2],"\nAgilidade:",mala[1][i][3],"\nSorte:",mala[1][i][4],"\n")
                while 1:
                    print("Posso comprar por ", mala[1][i][6]*0.5,"Reais.")
                    time.sleep(0.5)
                    print("Vai querer vender?(sim ou não)")
                    acao_do_personagem=input("-")
                    acao_do_personagem=acao_do_personagem.lower()
                    if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                        break
                    else:
                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                            personagem_jogador[7] = personagem_jogador[7] + mala[1][i][6]*0.5
                            mala[1][i]=espaço_vazio
                            print("Obrigado!")
                            time.sleep(0.5)
                            break
                        else:
                            print("ENTRADA INVÁLIDA!")
                            time.sleep(0.5)
        else:
            if(acao_do_personagem == "comprar"):
                while 1:
                    print("Produtos a venda:\n")
                    time.sleep(0.5)
                    i=0
                    while i<=29:
                        if (loja_venda[1][i]!=espaço_vazio):
                            print(loja_venda[0][i]," : ",loja_venda[1][i][0],"\n     (",loja_venda[1][i][5],")\n")
                        i+=1
                    while 1:
                        print("Para analisar um item digite o número da sua posição!\nPara voltar ao jogo digite voltar.")
                        acao_do_personagem = input('-')
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
                    if(acao_do_personagem==loja_venda[0][i] and loja_venda[1][i]!=espaço_vazio):
                        if(loja_venda[1][i][6]=="consumível de aprimoramento"):
                            print("\nNome:",loja_venda[1][i][0], "\nTipo:",loja_venda[1][i][5],"\nVida:",loja_venda[1][i][7],"\nAtaque:",loja_venda[1][i][1],"\nDefesa:",loja_venda[1][i][2],"\nAgilidade:",loja_venda[1][i][3],"\nSorte:",loja_venda[1][i][4],"\n")
                        if(loja_venda[1][i][6]=="consumível"):
                            print("\nNome:",loja_venda[1][i][0], "\nTipo:",loja_venda[1][i][5],"\nVida:",loja_venda[1][i][7],"\n")
                        if(loja_venda[1][i][6]!="consumível de aprimoramento" and loja_venda[1][i][6]!="consumível"):
                            print("\nNome:",loja_venda[1][i][0],"\nTipo:",loja_venda[1][i][5],"\nAtaque:",loja_venda[1][i][1],"\nDefesa:",loja_venda[1][i][2],"\nAgilidade:",loja_venda[1][i][3],"\nSorte:",loja_venda[1][i][4],"\n")
                        while 1:
                            print("Deseja comprar? Quantos?(para desistir da compra digite 0)")
                            acao_do_personagem = input('-')
                            if acao_do_personagem.isnumeric():
                                acao_do_personagem=int(acao_do_personagem)
                                break
                            else:
                                acao_do_personagem=acao_do_personagem.lower()
                                if(acao_do_personagem=="voltar"):break
                                print("ENTRADA INVÁLIDA!")
                                time.sleep(0.5)
                        if(acao_do_personagem=="voltar"):break
                        item_adicionado=loja_venda[1][i]
                        quantidade_adicionada=acao_do_personagem
                        while 1:
                            print("Ficou ", loja_venda[1][i][6]*quantidade_adicionada,"Reais.")
                            print("Vai comprar mesmo?(sim ou não)")
                            acao_do_personagem=input("-")
                            acao_do_personagem=acao_do_personagem.lower()
                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                break
                            else:
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    personagem_jogador[7] = personagem_jogador[7] - loja_venda[1][i][6]*quantidade_adicionada
                                    adicionaItem()
                                    print("Obrigado!")
                                    time.sleep(0.5)
                                    break
                                else:
                                    print("ENTRADA INVÁLIDA!")
                                    time.sleep(0.5)
            else:
                if(acao_do_personagem == "sair"):break
                else:
                    print("ENTRADA INVÁLIDA!")
                    time.sleep(0.5)

#--Ficha do Personagem--#
def ficha_personagem():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    print("\n#", "-"*30,"#\n", "\nNome:", personagem_jogador[0])
    time.sleep(0.23)
    print("\nVida:", personagem_jogador[6], "de", personagem_jogador[5])
    time.sleep(0.23)
    print("\nAtaque:", personagem_jogador[1], "\nDefesa:", personagem_jogador[2], "\nAgilidade:", personagem_jogador[3], "\nSorte:", personagem_jogador[4])
    time.sleep(0.23)
    print("\nCapa:", equipado_capa[0], "\nRoupa:", equipado_roupa[0], "\nCalçados:", equipado_calcado[0],)
    time.sleep(0.23)
    print("\nLuvas:" ,equipado_luva[0],"\nAnel:" ,equipado_anel[0],"\nArmamento:", equipado_maos[0])
    time.sleep(0.23)
    print("\nDinheiro:", personagem_jogador[7], "Reais\n")
    time.sleep(0.23)
    print("\n#", "-"*30,"#\n")
    time.sleep(0.23)

#--Save--#
def save():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    ficha_personagem()
    print('\nDeseja salvar seu progresso?("sim" ou "não")\n')
    time.sleep(0.5)
    while 1:
        acao_do_personagem = input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
            print("\nDeseja salvar em qual espaço?\n")
            time.sleep(0.5)
            arq = open('\espaço_save00.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  0:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save01.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  1:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save02.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  2:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save03.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  3:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save04.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  4:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save05.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  5:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save06.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  6:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save07.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  7:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save08.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  8:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            arq = open('\espaço_save09.py', 'rb')
            mostrar_save = pickle.load(arq)
            print("\nEspaço  9:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
            arq.close
            while 1:
                print("\n(Digite um número entre 0 e 9)")
                acao_do_personagem=input("-")
                if(acao_do_personagem=="0"):
                    arq = open('\espaço_save00.py', 'wb')
                    break
                else:
                    if(acao_do_personagem=="1"):
                        arq = open('\espaço_save01.py', 'wb')
                        break
                    else:
                        if(acao_do_personagem=="2"):
                            arq = open('\espaço_save02.py', 'wb')
                            break
                        else:
                            if(acao_do_personagem=="3"):
                                arq = open('\espaço_save03.py', 'wb')
                                break
                            else:
                                if(acao_do_personagem=="4"):
                                    arq = open('\espaço_save04.py', 'wb')
                                    break
                                else:
                                    if(acao_do_personagem=="5"):
                                        arq = open('\espaço_save05.py', 'wb')
                                        break
                                    else:
                                        if(acao_do_personagem=="6"):
                                            arq = open('\espaço_save06.py', 'wb')
                                            break
                                        else:
                                            if(acao_do_personagem=="7"):
                                                arq = open('\espaço_save07.py', 'wb')
                                                break
                                            else:
                                                if(acao_do_personagem=="8"):
                                                    arq = open('\espaço_save08.py', 'wb')
                                                    break
                                                else:
                                                    if(acao_do_personagem=="9"):
                                                        arq = open('\espaço_save09.py', 'wb')
                                                        break
                                                    else:
                                                        print("Entrada inválida!\n")
                                                        time.sleep(0.5)
            #recomendo você usar um for aqui :) - Lucas Sabiao
            mostrar_save = ("  Nome:", personagem_jogador[0], "  Vida:", personagem_jogador[5],"  Lugar:", variável_lugar, "  Ataque:", personagem_jogador[1], "  Defesa:", personagem_jogador[2],"  Agilidade:", personagem_jogador[3])
            pickle.dump(mostrar_save, arq)
            pickle.dump(equipado_roupa, arq)
            pickle.dump(equipado_capa, arq)
            pickle.dump(equipado_luva, arq)
            pickle.dump(equipado_anel, arq)
            pickle.dump(equipado_maos, arq)
            pickle.dump(equipado_calcado, arq)
            pickle.dump(variável_cenário, arq)
            pickle.dump(objeto, arq)
            pickle.dump(situacao, arq)
            pickle.dump(temporário, arq)
            pickle.dump(variável_lugar, arq)
            pickle.dump(ponto_de_save, arq)
            pickle.dump(personagem_jogador, arq)
            pickle.dump(personagem_reserva, arq)
            pickle.dump(personagem_inimigo, arq)
            pickle.dump(mala, arq)
            arq.close
            print("\nPronto!\n")
            break
        else:
            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                break
            else:
                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                time.sleep(0.5)

#--Sistema de batalha--#
def batalha():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    print("\nBatalha!!!\nÉ hora da briga!!!\n")
    time.sleep(2)
    contador_de_rodadas=1
    while(personagem_inimigo[6]>0):
        if(personagem_jogador[6]<=0):
            break
        print("\n]]", "="*30,"[[\n", "    Início da rodada número ", contador_de_rodadas, "\n]]", "="*30,"[[\n")
        if(personagem_jogador[6]==1):
            if(contador_de_rodadas==1):
                print("\nVocê entrou na batalha com apenas 1 ponto de vida!")
                time.sleep(0.5)
                print("Seu último recurso é a tensão!\n")
                time.sleep(0.5)
            else:
                if(contador_de_batalha==0):
                    print("\nVocê está com apenas 1 ponto de vida!")
                    time.sleep(0.5)
                    print("Seu último recurso é a tensão!\n")
                    time.sleep(0.5)
            if(contador_de_batalha>0):       
                print("\nVocê aguentou mais uma rodada com apenas 1 ponto de vida!")
                time.sleep(0.5)
                print("Você extendeu o limite do seu fôlego e agora o limite dos seus pontos de vida subiu!\n")
                time.sleep(1)
                personagem_jogador[5]=personagem_jogador[5]+((contador_de_batalha)+(random.randrange(personagem_jogador[2])))
            contador_de_batalha=contador_de_batalha+1
        else:
            if(personagem_jogador[6]<=personagem_jogador[5]*0.05):
                teste_de_sorte=random.randrange(150)
                if(teste_de_sorte<=10+personagem_jogador[4]):
                    print("\nVocê está dando o seu melhor para aguentar, isso está melhorando o seu fôlego!")
                    time.sleep(0.5)
                    print("O limite dos seus pontos de vida aumentou!\n")
                    time.sleep(1)
                    personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[2])+1)
        print("\n#", "-"*30,"#\n", "\n\n", personagem_jogador[0], ":\n                    ",personagem_jogador[6], "\n                     de", personagem_jogador[5], " Pontos de Vida\n\n", personagem_inimigo[0], ":\n                    ", personagem_inimigo[6], "\n                     de", personagem_inimigo[5], " Pontos de vida\n")
        time.sleep(0.1)
        print("\n#", "-"*30,"#\nO que você fará agora, ", personagem_jogador[0], "?\nAtacar, defender ou fugir?")
        time.sleep(0.15)
        acao_do_personagem = input("-")
        acao_do_personagem = acao_do_personagem.lower()
        while True:
            if(acao_do_personagem != "atacar" and acao_do_personagem != "defender" and acao_do_personagem != "fugir" and acao_do_personagem!="f" and acao_do_personagem!="fugri" and acao_do_personagem!="fguir" and acao_do_personagem!="fugeir" and acao_do_personagem!="furig" and acao_do_personagem!="fuer" and acao_do_personagem!="ffugri" and acao_do_personagem!="gfuir" and acao_do_personagem!="fiur" and acao_do_personagem!="fugi" and acao_do_personagem!="fugr" and acao_do_personagem!="fug" and acao_do_personagem!="fgir" and acao_do_personagem!="fir" and acao_do_personagem!="fgr" and acao_do_personagem!="ugir" and acao_do_personagem!="gir" and acao_do_personagem!="figr" and acao_do_personagem!="fu" and acao_do_personagem != "d" and acao_do_personagem != "defende" and acao_do_personagem != "defern" and acao_do_personagem != "defenrede" and acao_do_personagem != "ddefender" and acao_do_personagem != "defenrd" and acao_do_personagem != "deffender" and acao_do_personagem != "defendder" and acao_do_personagem != "ddeffender" and acao_do_personagem != "defnder" and acao_do_personagem != "defndr" and acao_do_personagem != "dfnder" and acao_do_personagem != "dfendr" and acao_do_personagem != "defnde" and acao_do_personagem != "defnd" and acao_do_personagem != "dfede" and acao_do_personagem != "def" and acao_do_personagem!="a" and acao_do_personagem!="at" and acao_do_personagem!="ata" and acao_do_personagem!="atac" and acao_do_personagem!="ataca" and acao_do_personagem!="atcar" and acao_do_personagem!="tacar" and acao_do_personagem!="aacar" and acao_do_personagem!="ataar" and acao_do_personagem!="atacr" and acao_do_personagem!="acar" and acao_do_personagem!="aaar" and acao_do_personagem!="aacr" and acao_do_personagem!="aaca" and acao_do_personagem!="atar" and acao_do_personagem!="atcr" and acao_do_personagem!="atca" and acao_do_personagem!="ata" and acao_do_personagem!="ataa" and acao_do_personagem!="atara" and acao_do_personagem!="stssr" and acao_do_personagem!="atavar" and acao_do_personagem!="atahvea" and acao_do_personagem!="atrex" and acao_do_personagem!="atasfa" and acao_do_personagem!="atacart" and acao_do_personagem!="taacar" and acao_do_personagem!="tacaar" and acao_do_personagem!="tacara" and acao_do_personagem!="aactar" and acao_do_personagem!="aacatr" and acao_do_personagem!="aacart" and acao_do_personagem!="aatcar" and acao_do_personagem!="cataar" and acao_do_personagem!="taaacar" and acao_do_personagem!="catar" and acao_do_personagem!="rataca" and acao_do_personagem!="atraca" and acao_do_personagem!="atracar"):
                print("\nComando inválido! Você só pode atacar, defender ou fugir!\n")
                time.sleep(0.5)
                acao_do_personagem = input("-")
                acao_do_personagem = acao_do_personagem.lower()
            else: break
        contador_de_rodadas=contador_de_rodadas+1
        if(acao_do_personagem == "defender" or acao_do_personagem == "d" or acao_do_personagem == "defende" or acao_do_personagem == "defern" or acao_do_personagem == "defenrede" or acao_do_personagem == "ddefender" or acao_do_personagem == "defenrd" or acao_do_personagem == "deffender" or acao_do_personagem == "defendder" or acao_do_personagem == "ddeffender" or acao_do_personagem == "defnder" or acao_do_personagem == "defndr" or acao_do_personagem == "dfnder" or acao_do_personagem == "dfendr" or acao_do_personagem == "defnde" or acao_do_personagem == "defnd" or acao_do_personagem == "dfede" or acao_do_personagem == "def"): #defesa(2personagem_jogador[2]) vs ataque(personagem_inimigo[1])
            print("\nPostura de Batalha:\n", personagem_jogador[0], "-> defensiva\n", personagem_inimigo[0], "-> ofensiva\n")
            time.sleep(1)
            teste_de_sorte = random.randrange(50)
            if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_defesa(3personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                print("\nSua postura de defesa te favoreceu!\n")
                time.sleep(1)
                teste_de_sorte = random.randrange(40)
                if (teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#S_defesa(3personagem_jogador[2]) vs S_ataque(2personagem_inimigo[1])
                    print("\n... Mas o ataque do inimigo foi crítico!\n")
                    time.sleep(1)
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVocê conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em você!")
                        time.sleep(1)
                    else:
                        calculo_do_dano = (2*personagem_inimigo[1])+(random.randrange(personagem_inimigo[1]))*(0.2)-(3*personagem_jogador[2])-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano < 0):#S_defesa(3personagem_jogador[2]) CONTRA-ATACA S_ataque(2personagem_inimigo[1])
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nNão importa, sua defesa é incrível!")
                            time.sleep(1)
                            print("Além de defender você conseguiu contra-atacar, causando ", calculo_do_dano," pontos de dano ao inimigo!\n")
                            time.sleep(1.5)
                            teste_de_sorte = random.randrange(5)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variável_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variável_para_comparar < personagem_jogador[2]):
                                        print("\nVocê testou o seu limite e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(1)
                                    if (variável_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variável_para_comparar
                            if(teste_de_sorte>=4):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            if(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            if(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte==10+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if (calculo_do_dano == 0):#S_defesa(3personagem_jogador[2]) ANULA S_ataque(2personagem_inimigo[1])
                                print("\nDefesa e ataque se anulam! A tensão aumenta!\n")
                                time.sleep(1)
                            else:#S_defesa(3personagem_jogador[2]) APANHA DO S_ataque(2personagem_inimigo[1])
                                print("\nVocê sofreu ", calculo_do_dano, " pontos de dano...\n")
                                time.sleep(1)
                                personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                else:#S_defesa(3personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVocê conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em você!")
                        time.sleep(1)
                    else:
                        calculo_do_dano = (personagem_inimigo[1])+(random.randrange(personagem_inimigo[1]))*(0.2)-(3*personagem_jogador[2])-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano<0):#S_defesa(3personagem_jogador[2]) CONTRA-ATACA ataque(personagem_inimigo[1])
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nSua defesa foi tão grande que, além de bloquear o ataque, você conseguiu contra-atacar, causando ", calculo_do_dano," pontos de dano ao inimigo!\n")
                            time.sleep(1)
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if (calculo_do_dano ==0):#S_defesa(3personagem_jogador[2]) ANULA ataque(personagem_inimigo[1])
                                print("\nSua defesa foi completa!\n")
                                time.sleep(1)
                            else:#S_defesa(3personagem_jogador[2]) APANHA DO ataque(personagem_inimigo[1])
                                print("\nVocê sofreu míseros ", calculo_do_dano, " pontos de dano.\n")
                                time.sleep(1)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
            else:
                teste_de_sorte = random.randrange(40)
                if(teste_de_sorte<=10-personagem_jogador[4]+personagem_inimigo[4]):#defesa(2personagem_jogador[2]) vs S_ataque(2personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVocê conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em você!")
                        time.sleep(1)
                    else:
                        calculo_do_dano = 2*personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))*(0.2)-(1.5)*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))*(0.2)
                        if (calculo_do_dano<0):
                            calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(personagem_jogador[1]))/2)*(0.2)
                            print("\nSua defesa é simplesmente  I M E N S A !")
                            time.sleep(1)
                            print("O inimigo avançou furiosamente mas você o lançou para trás e contra-atacou causando ", calculo_do_dano, " pontos de dano ao inimigo!\n")
                            time.sleep(1.5)
                            teste_de_sorte = random.randrange(6)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variável_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variável_para_comparar < personagem_jogador[2]):
                                        print("\nVocê testou o seu limite e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(1)
                                    if (variável_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variável_para_comparar
                            if(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=40+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            if(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            if(teste_de_sorte==4):
                                teste_de_sorte = random.randrange(300)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            if(teste_de_sorte>=5):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=10+personagem_jogador[4]):
                                    variável_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+(random.randrange(personagem_jogador[1]))
                                    if (variável_para_comparar < personagem_jogador[2]):
                                        print("\nVocê testou o seu limite e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(1)
                                    if (variável_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variável_para_comparar
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if(calculo_do_dano==0):
                                print("\nVocê surpreendeu o inimigo que estava confiante,")
                                time.sleep(1)
                                print("suas forças se anularam numa estrondosa colisão!\n")
                                time.sleep(1)
                                teste_de_sorte=random.randrange(300)
                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nA liberacao de energia durante a colisão despertou novos limites para sua força e agora está mais forte!")
                                    time.sleep(1.5)
                                    print("TODOS os seus pontos subiram!\n")
                                    time.sleep(1.5)
                                    personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[5]))+3
                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                                time.sleep(1)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                else:#defesa(2personagem_jogador[2]) vs ataque(personagem_inimigo[1])
                    teste_de_sorte = random.randrange(300)
                    if(teste_de_sorte<=30+personagem_jogador[3]+personagem_jogador[4]-personagem_inimigo[3]-personagem_inimigo[4]):
                        print("\nVocê conseguiu esquivar de todos os ataques, o inimigo nem pode tocar em você!")
                        time.sleep(1)
                    else:
                        calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-2*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                        if (calculo_do_dano<0):
                            calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(personagem_jogador[1]))/2)
                            print("\nSua defesa É ENORME!")
                            time.sleep(1)
                            print("Você barrou o ataque naturalmente e contra-atacou, causando ", calculo_do_dano, " pontos de dano ao inimigo!\n")
                            time.sleep(1.5)
                            teste_de_sorte = random.randrange(5)#aumento de defesa
                            if(teste_de_sorte<=1):
                                teste_de_sorte = random.randrange(100)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    variável_para_comparar=personagem_jogador[2]
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))
                                    if (variável_para_comparar < personagem_jogador[2]):
                                        print("\nVocê testou o seu limite e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de defesa subiram!\n")
                                        time.sleep(1)
                                    if (variável_para_comparar > personagem_jogador[2]):
                                        personagem_jogador[2]=variável_para_comparar
                            if(teste_de_sorte>=4):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=40+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+1
                            if(teste_de_sorte==3):
                                teste_de_sorte = random.randrange(200)
                                if (teste_de_sorte<=20+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+2
                            if(teste_de_sorte==2):
                                teste_de_sorte = random.randrange(300)
                                if (teste_de_sorte<=30+personagem_jogador[4]):
                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                    time.sleep(1)
                                    print("Seus pontos de defesa subiram!\n")
                                    time.sleep(1)
                                    personagem_jogador[2]=personagem_jogador[2]+(random.randrange(personagem_jogador[2]))+3
                            personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                        else:
                            if(calculo_do_dano==0):
                                print("\nVocê barrou o ataque do inimigo!\n")
                                time.sleep(1)
                            else:
                                print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                                time.sleep(1.5)
                                personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
        else:
            if (acao_do_personagem=="atacar" or acao_do_personagem=="a" or acao_do_personagem=="at" or acao_do_personagem=="ata" or acao_do_personagem=="atac" or acao_do_personagem=="ataca" or acao_do_personagem=="atcar" or acao_do_personagem=="tacar" or acao_do_personagem=="aacar" or acao_do_personagem=="ataar" or acao_do_personagem=="atacr" or acao_do_personagem=="acar" or acao_do_personagem=="aaar" or acao_do_personagem=="aacr" or acao_do_personagem=="aaca" or acao_do_personagem=="atar" or acao_do_personagem=="atcr" or acao_do_personagem=="atca" or acao_do_personagem=="ata" or acao_do_personagem=="ataa" or acao_do_personagem=="atara" or acao_do_personagem=="stssr" or acao_do_personagem=="atavar" or acao_do_personagem=="atahvea" or acao_do_personagem=="atrex" or acao_do_personagem=="atasfa" or acao_do_personagem=="atacart" or acao_do_personagem=="taacar" or acao_do_personagem=="tacaar" or acao_do_personagem=="tacara" or acao_do_personagem=="aactar" or acao_do_personagem=="aacatr" or acao_do_personagem=="aacart" or acao_do_personagem=="aatcar" or acao_do_personagem=="cataar" or acao_do_personagem=="taaacar" or acao_do_personagem=="catar" or acao_do_personagem=="rataca" or acao_do_personagem=="atraca" or acao_do_personagem=="atracar"):
                teste_de_sorte=random.randrange(2)
                if (teste_de_sorte==1):#ataque(personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                    print("\nPostura de Batalha:\n", personagem_jogador[0], "-> ofensiva\n", personagem_inimigo[0], "-> defensiva\n")
                    time.sleep(1)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                        print("\nSeu ataque foi crítico!!!\n")
                        time.sleep(1)
                        teste_de_sorte=random.randrange(50)
                        if (teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#S_ataque(2personagem_jogador[1]) vs S_defesa(3personagem_inimigo[2])
                            print("\nApesar do seu crítico, você é pressionado pela postura de defesa do seu inimigo!\n")
                            time.sleep(1.5)
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, você nem pôde tocar no inimigo!")
                                time.sleep(1)
                            else:
                                calculo_do_dano=2*personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-3*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if (calculo_do_dano<0):#S_ataque(2personagem_jogador[1]) APANHA DE S_defesa(3personagem_inimigo[2])
                                    calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nPor mais que tente, você não consegue atravessar a defesa do seu inimigo!")
                                    time.sleep(1)
                                    print("Além de te bloquear, ele te contra-atacou, causando ", calculo_do_dano, " pontos de dano!\n")
                                    time.sleep(1)
                                    personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                                    teste_de_sorte=random.randrange(200)
                                    if(teste_de_sorte<=20+personagem_jogador[4]):
                                        print("\nVocê tentou ao máximo ultrapassar a defesa do seu inimigo, exigiu muito dos seus músculos que se fortaleceram!\n")
                                        time.sleep(1.5)
                                        print("\nSeus pontos de ataque subiram!\n")
                                        time.sleep(1)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+3
                                else:
                                    if (calculo_do_dano==0):#S_ataque(2personagem_jogador[1]) ANULA S_defesa(3personagem_inimigo[2])
                                        print("\nA disputa de forças é intensa, você e seu inimigo deram o melhor de si, mas nenhum dos dois se sobrepôs!\n")
                                        time.sleep(1.5)
                                    else:#S_ataque(2personagem_jogador[1]) ATACA S_defesa(3personagem_inimigo[2])
                                        print("\nSeu ataque foi explosivo!")
                                        time.sleep(1)
                                        print("Nem o melhor da defesa do seu inimigo foi capaz de conter sua ira!")
                                        time.sleep(1)
                                        print("Você causou ", calculo_do_dano, " pontos de dano ao seu inimigo!\n")
                                        time.sleep(1)
                                        personagem_inimigo[6] = personagem_inimigo[6]-calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte==10+personagem_jogador[4]):
                                            print("\nA explosão de energia dos seus músculos os expandiu definitivamente!\n")
                                            time.sleep(1)
                                            print("\nSeus pontos de ataque subiram!\n")
                                            time.sleep(1)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                        else:#S_ataque(2personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, você nem pôde tocar no inimigo!")
                                time.sleep(1)
                            else:
                                calculo_do_dano = 2*personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-2*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if(calculo_do_dano<0):#S_ataque(2personagem_jogador[1]) APANHA DE defesa(2personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nVocê deu o seu máximo, mas mesmo assim nem se equiparou às habilidades de auto-defesa do seu inimigo!")
                                    time.sleep(1.5)
                                    print("Sem fazer muito esforço ele se defendeu e contra-atacou, te causando ", calculo_do_dano," pontos de dano!\n")
                                    time.sleep(1.5)
                                    personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#S_ataque(2personagem_jogador[1]) ANULA defesa(2personagem_inimigo[2])
                                        print("\nVocê assustou o inimigo por um instante, mas - por muito pouco - ele conseguiu barrar todos os seus movimentos ofensivos...\n")
                                        time.sleep(1.5)
                                    else:
                                        teste_de_sorte=random.randrange(50)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):#XS_ataque(3personagem_jogador[1]) vs defesa(personagem_inimigo[2])
                                            print("\nVocê rompeu a defesa do seu inimigo, causando ", calculo_do_dano," pontos de dano!")
                                            time.sleep(1.5)
                                            print("\nSuper Crítico!!!\n")
                                            time.sleep(2)
                                            print("Você iniciou um ataque em frenesi!!!\n")
                                            time.sleep(1)
                                            personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                            teste_de_sorte=random.randrange(9)+1
                                            while(teste_de_sorte>0):#XS_ataque(3personagem_jogador[1]) ATACA defesa(personagem_inimigo[2])
                                                calculo_do_dano=2*(random.randrange(personagem_jogador[1]))-(random.randrange(personagem_inimigo[2]))
                                                while(calculo_do_dano<=0):
                                                    calculo_do_dano=2*(random.randrange(personagem_jogador[1]))-(random.randrange(personagem_inimigo[2]))
                                                print(calculo_do_dano," pontos de dano!\n")
                                                time.sleep(0.25)
                                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                                teste_de_sorte=teste_de_sorte-1
                                            print("\nVocê desferiu toda sua fúria no inimigo!\n")
                                            time.sleep(1)
                                            teste_de_sorte=random.randrange(3)
                                            if(teste_de_sorte<=1):
                                                teste_de_sorte=random.randrange(100)
                                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                                    print("\nVocê testou o seu limite e agora está mais forte!")
                                                    time.sleep(1)
                                                    print("Seus pontos de ataque subiram!\n")
                                                    time.sleep(1)
                                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                            if(teste_de_sorte>=2):
                                                teste_de_sorte=random.randrange(100)
                                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                                    print("\nVocê ultrapassou o seu limite e agora está mais forte!")
                                                    time.sleep(1)
                                                    print("Seus pontos de ataque subiram!\n")
                                                    time.sleep(1)
                                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+3
                                        else:#S_ataque(2personagem_jogador[1]) ATACA defesa(2personagem_inimigo[2])
                                            print("\nSeu ataque de golpes duplos pressionaram a defesa do seu inimigo, causando ",calculo_do_dano," pontos de dano!\n")
                                            time.sleep(1.5)
                                            teste_de_sorte=random.randrange(200)
                                            if(teste_de_sorte<=20+personagem_jogador[4]):
                                                print("\nVocê aprimorou o ritmo dos seus ataques e agora está mais forte!")
                                                time.sleep(1)
                                                print("Seus pontos de ataque subiram!\n")
                                                time.sleep(1)
                                                personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                            personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                    else:#ataque(personagem_jogador[1])
                        teste_de_sorte=random.randrange(50)
                        if(teste_de_sorte<=10+personagem_inimigo[4]-personagem_jogador[4]):#ataque(personagem_jogador[1]) vs S_defesa(3personagem_inimigo[2])
                            print("\nA postura de defesa do seu inimigo te colocou numa situação difícil!\n")
                            time.sleep(1)
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, você nem pôde tocar no inimigo!")
                                time.sleep(1)
                            else:
                                calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-3*personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                                if(calculo_do_dano<0):#ataque(personagem_jogador[1]) APANHA DE S_defesa(3personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nÉ muito difícil passar por tamanha defesa, seu ataque foi ínfimo, além de ser inutilizado, você sofreu represália...")
                                    time.sleep(1.5)
                                    print("Seu inimigo contra-atacou, causando ", calculo_do_dano, " pontos de dano.\n")
                                    time.sleep(1)
                                    teste_de_sorte=random.randrange(100)
                                    if(teste_de_sorte<=10+personagem_jogador[4]):
                                        print("\nVocê testou o seu limite e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de ataque subiram!\n")
                                        time.sleep(1)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                    personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#ataque(personagem_jogador[1]) ANULA S_defesa(3personagem_inimigo[2])
                                        print("\nO inimigo mal consegue reter seus golpes, mas o suficiente para pará-lo.")
                                        time.sleep(1)
                                        print("Ao mesmo tempo sua força foi o bastante para evitar um contra-ataque!\n")
                                        time.sleep(1)
                                    else:#ataque(personagem_jogador[1]) ATACA S_defesa(3personagem_inimigo[2])
                                        print("\nDepois de alguns golpes, você tornou insignificante a vantagem defensiva do seu inimigo, \ncausando humilhantes, ", calculo_do_dano," pontos de dano a ele!\n")
                                        time.sleep(2)
                                        teste_de_sorte=random.randrange(200)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):
                                            print("\nVocê testou o seu limite e agora está mais forte!")
                                            time.sleep(1)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(1)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                                        personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                        else:#ataque(personagem_jogador[1]) vs defesa(2personagem_inimigo[2])
                            teste_de_sorte = random.randrange(300)
                            if(teste_de_sorte<=30-personagem_jogador[3]-personagem_jogador[4]+personagem_inimigo[3]+personagem_inimigo[4]):
                                print("\nSeu oponente conseguiu esquivar de todos os seus ataques, você nem pôde tocar no inimigo!")
                                time.sleep(1)
                            else:
                                calculo_do_dano = personagem_jogador[1]+(random.randrange(personagem_jogador[1]))-2*personagem_inimigo[2]-(random.randrange(personagem_inimigo[2]))
                                if(calculo_do_dano<0):#ataque(personagem_jogador[1]) APANHA DE defesa(2personagem_inimigo[2])
                                    calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(personagem_inimigo[1]))/2)
                                    print("\nO inimigo se defendeu e contra-atacou, te causando ", calculo_do_dano," pontos de dano!\n")
                                    time.sleep(1)
                                    teste_de_sorte=random.randrange(100)
                                    if(teste_de_sorte<=10+personagem_jogador[4]):
                                        print("\nVocê descobriu mais sobre a sua força durante a disputa e agora está mais forte!")
                                        time.sleep(1)
                                        print("Seus pontos de ataque subiram\n!")
                                        time.sleep(1)
                                        personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+1
                                    personagem_jogador[6] = personagem_jogador[6] - calculo_do_dano
                                else:
                                    if(calculo_do_dano==0):#ataque(personagem_jogador[1]) ANULA defesa(2personagem_inimigo[2])
                                        print("\nSeu oponente defendeu todos os seus golpes, mas você não deu brecha para que ele avançasse!\n")
                                        time.sleep(1)
                                        teste_de_sorte=random.randrange(200)
                                        if(teste_de_sorte<=10+personagem_jogador[4]):
                                            print("\nO trabalho que seu inimigo te deu rendeu frutos!")
                                            time.sleep(1)
                                            print("Você descobriu mais sobre as táticas de luta dele e está mais forte!")
                                            time.sleep(1)
                                            print("Seus pontos de ataque subiram!\n")
                                            time.sleep(1)
                                            personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+(random.randrange(personagem_jogador[4]))+1
                                    else:#ataque(personagem_jogador[1]) ATACA defesa(2personagem_inimigo[2])
                                        print("\nVocê acertou o inimigo durante a disputa de forças, causando ",calculo_do_dano," pontos de dano!\n")
                                        time.sleep(1)
                                        personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                    print("\nPostura de Batalha:\n", personagem_jogador[0], "-> ofensiva\n", personagem_inimigo[0], "-> ofensiva\n")
                    time.sleep(1)
                    teste_de_sorte=random.randrange(40)
                    if (teste_de_sorte<=10+personagem_jogador[4]-personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                        print("\nSeu ataque foi crítico!!!\n")
                        time.sleep(1)
                        teste_de_sorte=random.randrange(40)
                        if (teste_de_sorte<=10-personagem_jogador[4]+personagem_inimigo[4]):#S_ataque(2personagem_jogador[1]) vs S_ataque(2personagem_inimigo[1])
                            print("\nMas o ataque do oponente também foi crítico!!!\n")
                            time.sleep(1)
                            print("\nVocês entraram na briga pra valer!")
                            time.sleep(0.5)
                            print("Avançaram de punhos cerrados, trocando golpes com as defesas abertas!\n")
                            time.sleep(1)
                            calculo_do_dano=2*personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVocê causou significativos ", calculo_do_dano," pontos de dano ao inimigo!\n")
                                time.sleep(1)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                                teste_de_sorte=random.randrange(100)
                                if(teste_de_sorte<=10+personagem_jogador[4]):
                                    print("\nSeus pontos de ataque subiram enquanto você forçava os seus músculos!\n")
                                    time.sleep(1)
                                    personagem_jogador[1]=personagem_jogador[1]+(random.randrange(personagem_jogador[1]))+2
                            else:
                                print("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(1.5)
                            calculo_do_dano=2*personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nEnquanto o oponente te causou ", calculo_do_dano," pontos de dano!\n")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(1.5)
                        else:#S_ataque(2personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                            print("\nVocê avançou violentamente sobre o inimigo, pressionando-o sem compaixão!")
                            time.sleep(1.5)
                            print("Apesar de forçar um leve recuo do inimigo, você não deixou de levar uns bons golpes!\n")
                            time.sleep(1.5)
                            calculo_do_dano=2*personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVocê golpeou o inimigo até lhe causar ", calculo_do_dano," pontos de dano!\n")
                                time.sleep(1)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(1.5)
                            calculo_do_dano=personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nJá o inimigo causou apenas ", calculo_do_dano," pontos de dano à você!\n")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(1.5)
                    else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                        teste_de_sorte=random.randrange(40)
                        if(teste_de_sorte==10+personagem_inimigo[4]-personagem_jogador[4]): #ataque(personagem_jogador[1]) vs S_ataque(2personagem_inimigo[1])
                            print("\nO ataque do oponente foi crítico!...\n")
                            time.sleep(1)
                            print("\nVocê foi pressionado enquanto trocavam golpes, \nos socos e chutes do seu oponente te acertaram em pontos menos resistentes do seu corpo que estavam desprotegidos!")
                            time.sleep(2)
                            print("Mesmo assim você manteve um bom rítmo de ataque!\n")
                            time.sleep(1)
                            calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVocê infringiu ", calculo_do_dano," pontos de dano ao inimigo!\n")
                                time.sleep(1)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(1.5)
                            calculo_do_dano=2*personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nEnquanto o seu inimigo te agrediu violentamente, causando ", calculo_do_dano," pontos de dano à você!\n")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(1.5)
                        else:#ataque(personagem_jogador[1]) vs ataque(personagem_inimigo[1])
                            print("\nVocês se atacaram num ritmo leve, parecem estar testando um ao outro,\n ficou claro que nenhum dos dois mostrou tudo o que é capaz.\n")
                            time.sleep(2)
                            calculo_do_dano=personagem_jogador[1]+random.randrange(personagem_jogador[1])-personagem_inimigo[2]-random.randrange(personagem_inimigo[2])
                            if(calculo_do_dano>0):
                                print("\nVocê feriu seu oponente em ", calculo_do_dano," pontos de dano!\n")
                                time.sleep(1)
                                personagem_inimigo[6]=personagem_inimigo[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                                time.sleep(1.5)
                            calculo_do_dano=personagem_inimigo[1]+random.randrange(personagem_inimigo[1])-personagem_jogador[2]-random.randrange(personagem_jogador[2])
                            if(calculo_do_dano>0):
                                print("\nSeu inimigo te golpeou causando ", calculo_do_dano," pontos de dano!\n")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                            else:
                                print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                time.sleep(1.5)
            else:
                if(acao_do_personagem=="fugir" or acao_do_personagem=="f" or acao_do_personagem=="fugri" or acao_do_personagem=="fguir" or acao_do_personagem=="fugeir" or acao_do_personagem=="furig" or acao_do_personagem=="fuer" or acao_do_personagem=="ffugri" or acao_do_personagem=="gfuir" or acao_do_personagem=="fiur" or acao_do_personagem=="fugi" or acao_do_personagem=="fugr" or acao_do_personagem=="fug" or acao_do_personagem=="fgir" or acao_do_personagem=="fir" or acao_do_personagem=="fgr" or acao_do_personagem=="ugir" or acao_do_personagem=="gir" or acao_do_personagem=="figr" or acao_do_personagem=="fu"):
                    print("\nPostura de Batalha:\n", personagem_jogador[0], "-> fugitiva\n", personagem_inimigo[0], "-> ofensiva\n")
                    time.sleep(1)
                    print("\nVocê tenta aumentar o rítmo de esquiva...\n")
                    time.sleep(1)
                    teste_de_sorte=random.randrange(10)+calculo_da_fuga
                    if(teste_de_sorte==10):
                        print('\nVocê esquivou de qualquer manobra ofensiva do oponente e conseguiu uma brecha para fugir!\n')
                        time.sleep(1.5)
                        print('\nDeseja fugir da luta?("sim" ou "não")\n')
                        time.sleep(0.5)
                        batalha_escapar=""
                        while(batalha_escapar != "não"):
                            batalha_escapar = input('-')
                            batalha_escapar = batalha_escapar.lower()
                            if(batalha_escapar!="não" and batalha_escapar != "sim"):
                                print('\nEntrada invalida! Digite "sim" ou "não".\n')
                                time.sleep(0.5)
                            if(batalha_escapar =="sim"):
                                break
                        if(batalha_escapar =="sim"):
                            break
                    else:
                        if(teste_de_sorte>8):
                            print('\nVocê esquivou de qualquer manobra ofensiva do oponente, mas não conseguiu uma brecha para fugir...\n')
                            time.sleep(1.5)
                        else:
                            if(teste_de_sorte>5):
                                print('\nVocê não conseguiu uma brecha para fugir, nem pode se esquivar, mas pode se defender!\n')
                                time.sleep(1.5)
                                calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-2*personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                if (calculo_do_dano<0):
                                    print('\nSua defesa É ENORME!')
                                    time.sleep(1)
                                    print('Você barrou o ataque naturalmente e conseguiu afastar o inimigo, criando uma brecha para fugir!\n')
                                    time.sleep(1.5)
                                    print('\nDeseja fugir da luta?("sim" ou "não")\n')
                                    time.sleep(0.5)
                                    batalha_escapar=""
                                    while(batalha_escapar != "não"):
                                        batalha_escapar = input('-')
                                        batalha_escapar = batalha_escapar.lower()
                                        if(batalha_escapar!="não" and batalha_escapar != "sim"):
                                            print('\nEntrada invalida! Digite "sim" ou "não".\n')
                                            time.sleep(0.5)
                                        if(batalha_escapar =="sim"):
                                            break
                                    if(batalha_escapar =="sim"):
                                        batalha_escapar="sim"
                                        break
                                else:
                                    if(calculo_do_dano==0):
                                        print("\nVocê barrou o ataque do inimigo!\n")
                                        time.sleep(1)
                                    else:
                                        print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                                        time.sleep(1.5)
                                        personagem_jogador[6] = personagem_jogador[6]-calculo_do_dano
                            else:
                                if(teste_de_sorte>2):
                                    print('\nVocê não conseguiu uma brecha para fugir, se esquivar ou se defender...\n')
                                    time.sleep(1)
                                    calculo_do_dano = personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                    if (calculo_do_dano>0):
                                        print("\nVocê foi atacado diretamente, sofrendo ", calculo_do_dano," pontos de dano!\n")
                                        time.sleep(1.5)
                                        personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                    else:
                                        print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(1.5)
                                else:
                                    print('\nVocê tropeçou ao tentar fugir!\n')
                                    time.sleep(1)
                                    print('\nO golpe do oponente foi crítico!\n')
                                    time.sleep(1)
                                    calculo_do_dano = 2*personagem_inimigo[1]+(random.randrange(personagem_inimigo[1]))-personagem_jogador[2]-(random.randrange(personagem_jogador[2]))
                                    if (calculo_do_dano>0):
                                        print("\nO inimigo aproveitou a abertura na sua defesa e te atacou violentamente, causando ", calculo_do_dano," pontos de dano.\n")
                                        time.sleep(1.5)
                                        personagem_jogador[6]=personagem_jogador[6]-calculo_do_dano
                                        teste_de_sorte=random.randrange(100)
                                        if(teste_de_sorte<=20+personagem_jogador[4]):
                                            print("\nVocê aumentou seu folego enquanto tentava escapar dos golpes que você levou em cheio!")
                                            time.sleep(1)
                                            print("O limite dos seus pontos de vida cresceu!")
                                            time.sleep(1)
                                            personagem_jogador[5]=personagem_jogador[5]+(random.randrange(personagem_jogador[5]))+1
                                    else:
                                        print("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                        time.sleep(1.5)
                    calculo_da_fuga=calculo_da_fuga+((personagem_jogador[3]-personagem_inimigo[3])*0.10)+((personagem_jogador[4]-personagem_inimigo[4])*0.10)
                    if(batalha_escapar =="sim"):
                        break
    batalha_escapar="não"
    variável_para_comparar = 0
    contador_de_batalha = 0
    contador_de_rodadas = 1
    print("\nFim da Batalha!\n")
    time.sleep(1)
    if(personagem_inimigo[6]<=0):
        print("\n",personagem_inimigo[0]," foi derrotado!\n")
        time.sleep(2)
    else:
        if(personagem_jogador[6]<=0):
            print("\nVocê foi derrotado.\n")
            time.sleep(2)
        else:
            if(batalha_escapar =="sim"):
                print("\nVocê conseguiu escapar!\n")
                time.sleep(1.5)
                batalha_escapar="escapou"

#--Matar alguém--#
def matarAlguém():
    input("Você entrou em conflito com a sua consciência(Aperte ENTER)")
    input("Você o matou!")
    input("                                         Você o matou!")
    input("Seu assassino!")
    input("                                Você o matou!")
    input("             Você o matou!")
    input("                                    Seu assassino!")
    input("Você o matou!")
    input("                          Você o matou!")
    input("     Você o matou!")
    input("                 Você o matou!")
    input("Você o matou!")
    input("                                Seu monstro!")
    input("                                      Seu monstro!")
    input("          Você o matou!")
    input("     Você o matou!")
    input("                     Seu monstro!")
    input("                                Você o matou!")
    input("                    Você o matou!")
    input("                                         Você o matou!")
    input("      Você o matou!")
    input("                                Seu monstro!")
    input("Você o matou!")
    input("            Você o matou!")
    input("Seu monstro!")
    input("                                   Você o matou!")
    input("                          Você o matou!")
    input("        Você o matou!")
    input("                               Seu assassino!")
    input("               Você o matou!")
    input("Seu assassino!")
    input("         Você o matou!")
    input("                               Seu assassino!")
    input("                  Você o matou!")
    input("Seu assassino!")
    input("                                         Você o matou!")
    input("                                Você o matou!")
    input("          Você o matou!")
    input("     ")
    print("     Ele...")
    time.sleep(1)
    print("     Ele era um ser vivo...")
    time.sleep(1)
    print("     Ele era um ser humano...")
    time.sleep(1)
    print("                   E você o matou!")
    time.sleep(1)

#--Seu prédio: Quarto Andar--#
def seuPrédioQuartoAndar():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    variável_lugar = "seu prédio, 4º andar"
    temporário[0]= False
    if(situacao[0]<5):
        print("Você foi abordado novamente pelo morador do quarto 44...")
        time.sleep(1)
        print(" - Nós sabemos que você não venceu nem do 3º andar, se não é capaz disso,\nnão é capaz de nos vencer!")
        time.sleep(1)
        print("Ele te empurrou escada abaixo... Você perdeu 5 pontos de vida durante a queda!")
        time.sleep(1)
        personagem_jogador[6]=personagem_jogador[6]-5
        if(personagem_jogador[6]<=0):
            personagem_jogador[6]=1
    while 1:
        if(situacao[0]<5):
            print("Agora você está no terceiro andar.")
            time.sleep(1)
            break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", personagem_jogador[0],", o que você vai fazer?\n")
        acao_do_personagem = input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(40, 41, 42, 43 ou 44)\n")
            acao_do_personagem = input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="40" and acao_do_personagem!="41" and acao_do_personagem!="42" and acao_do_personagem!="43" and acao_do_personagem!="44"):
                acao_do_personagem="entrada inválida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do prédio"):
                print("Você desceu para o terceiro andar.")
                time.sleep(1)
                break
            else:
                if(acao_do_personagem=="40"):
                    if(situacao[0]>6):
                        print("Você já lutou aqui!")
                        time.sleep(1)
                    else:
                        print(' - Aqui no 4º andar moram os mais fortes, mas há muita diferença entre nós!')
                        time.sleep(1)
                        print(' - Por isso há uma ordem para nos enfrentar, começando por mim!')
                        time.sleep(1)
                        print(' - Como não pegamos leve, nós apresentamos um "cartão de visita" ao oponente, para ele saber se é capaz de sobreviver.')
                        time.sleep(1)
                        personagem_inimigo = [ "Estudante Briguento \n do Quarto 40", 30, 15, 5, 5, 360, 360]
                        print(" - Aqui está o meu:")
                        time.sleep(0.5)
                        print("\n", personagem_inimigo[0],":",personagem_inimigo[5],"pontos de vida.\nAtaque : ",personagem_inimigo[1],".     Defesa : ", personagem_inimigo[2],".\n")
                        time.sleep(1)
                        print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                        time.sleep(0.5)
                        while 1:
                            acao_do_personagem = input("-")
                            acao_do_personagem = acao_do_personagem.lower()
                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                break
                            else:
                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                    batalha()
                                    if(personagem_jogador[6]<=0):break
                                    if(personagem_inimigo[6]>0):
                                        while (personagem_inimigo[6]>0):
                                            print(" - O que foi, desistiu?(sim ou não)")
                                            time.sleep(0.5)
                                            while 1:
                                                acao_do_personagem=input("-")
                                                acao_do_personagem = acao_do_personagem.lower()
                                                if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                    print(" - Então vamos voltar a lutar!")
                                                    time.sleep(1)
                                                    batalha()
                                                else:
                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                        print(" - Tem certeza?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                        time.sleep(0.5)
                                                        acao_do_personagem=input("-")
                                                        acao_do_personagem=acao_do_personagem.lower()
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - Muito obrigado pela colaboração financeira! Até outro dia, talvez...")
                                                            time.sleep(1)
                                                            personagem_jogador[7]=personagem_jogador[7]/2
                                                            break
                                                        else:
                                                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                print(" - Então vamos voltar a lutar!")
                                                                time.sleep(1)
                                                                batalha()
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                time.sleep(0.5)
                                                    else:
                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                        time.sleep(0.5)
                                        if(personagem_jogador[6]<=0):break
                                        else:
                                            print(" - Parabéns! Você é realmente forte!")
                                            time.sleep(1)
                                            situacao[0]=situacao[0]+1
                                            break
                                    else:
                                        print(" - Parabéns! Você é realmente forte!")
                                        time.sleep(1)
                                        situacao[0]=situacao[0]+1
                                        break
                                else:
                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                    time.sleep(0.5)
                else:
                    if(acao_do_personagem=="41"):
                        if(situacao[0]==7):
                            print(' - SERÁ que você está PRONTO para brigar comigo, fracote??? Hahahahaha!')
                            time.sleep(1)
                            personagem_inimigo = [ "Estudante Briguento \n do Quarto 41", 50, 30, 10, 10, 550, 550]
                            print(" - Aqui está o meu cartão:")
                            time.sleep(0.5)
                            print("\n", personagem_inimigo[0],":",personagem_inimigo[5],"pontos de vida.\nAtaque : ",personagem_inimigo[1],".     Defesa : ", personagem_inimigo[2],".\n")
                            time.sleep(1)
                            print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                            time.sleep(0.5)
                            while 1:
                                acao_do_personagem = input("-")
                                acao_do_personagem = acao_do_personagem.lower()
                                if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                    break
                                else:
                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                        batalha()
                                        if(personagem_jogador[6]<=0):break
                                        if(personagem_inimigo[6]>0):
                                            while (personagem_inimigo[6]>0):
                                                print(" - O que há? Vai cair fora mesmo???(sim ou não)")
                                                time.sleep(0.5)
                                                while 1:
                                                    acao_do_personagem = input("-")
                                                    acao_do_personagem = acao_do_personagem.lower()
                                                    if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                        print(" - Então cai dentro!!!")
                                                        time.sleep(1)
                                                        batalha()
                                                    else:
                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                            print(" - É sério?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                            time.sleep(0.5)
                                                            acao_do_personagem=input("-")
                                                            acao_do_personagem=acao_do_personagem.lower()
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                print(" - Hahaha! Você não é o primeiro que sai do desafio! Por que você acha que tem um prêmio?")
                                                                time.sleep(0.5)
                                                                print(" - Você pode tentar de novo se quiser compensar a perda! HAHAHAHAHA!")
                                                                time.sleep(0.5)
                                                                personagem_jogador[7]=personagem_jogador[7]/2
                                                                break
                                                            else:
                                                                if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                    print(" - Então cai dentro!!!")
                                                                    time.sleep(1)
                                                                    batalha()
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                    time.sleep(0.5)
                                                        else:
                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                            time.sleep(0.5)
                                            if(personagem_jogador[6]<=0):break
                                            else:
                                                print(" - CARAMBA! E não é que você estava pronto mesmo?! Hahahaha... Tudo bem perder às vezes...")
                                                time.sleep(1)
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print(" - CARAMBA! E não é que você estava pronto mesmo?! Hahahaha... Tudo bem perder às vezes...")
                                            time.sleep(1)
                                            situacao[0]=situacao[0]+1
                                            break
                                    else:
                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                        time.sleep(0.5)
                        else:
                            if(situacao[0]>7):
                                print("Você já lutou aqui!")
                                time.sleep(1)
                            else:
                                print(" - Você não pode me desafiar enquanto não vencer do briguento do quarto 40")
                                time.sleep(1)
                    else:
                        if(acao_do_personagem=="42"):
                            if(situacao[0]==8):
                                print(' - Humhumhumhum... Você vai perder...')
                                time.sleep(1)
                                personagem_inimigo = [ "Estudante Briguento \n do Quarto 42", 90, 70, 15, 15, 790, 790]
                                print(" - Veja:")
                                time.sleep(0.5)
                                print("\n", personagem_inimigo[0],":",personagem_inimigo[5],"pontos de vida.\nAtaque : ",personagem_inimigo[1],".     Defesa : ", personagem_inimigo[2],".\n")
                                time.sleep(1)
                                print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                time.sleep(0.5)
                                while 1:
                                    acao_do_personagem = input("-")
                                    acao_do_personagem = acao_do_personagem.lower()
                                    if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                        break
                                    else:
                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                while (personagem_inimigo[6]>0):
                                                    print(" - Você vai fugir?(sim ou não) Humhumhumhum...")
                                                    time.sleep(0.5)
                                                    while 1:
                                                        acao_do_personagem = input("-")
                                                        acao_do_personagem = acao_do_personagem.lower()
                                                        if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                            print(" - Venha!!!")
                                                            time.sleep(1)
                                                            batalha()
                                                        else:
                                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                print(" - Você vai mesmo?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                time.sleep(0.5)
                                                                acao_do_personagem=input("-")
                                                                acao_do_personagem=acao_do_personagem.lower()
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    print(" - Humhumhumhum... Fraco! Eu sempre soube que você era fraco!")
                                                                    time.sleep(0.5)
                                                                    print(" - Volte quando você deixar de ser fraco! FWUAHAHAHAHAHAHAHA!!! NUNCAAA!!!")
                                                                    time.sleep(0.5)
                                                                    personagem_jogador[7]=personagem_jogador[7]/2
                                                                    break
                                                                else:
                                                                    if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                        print(" - Venha!!!")
                                                                        time.sleep(1)
                                                                        batalha()
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                        time.sleep(0.5)
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                time.sleep(0.5)
                                                if(personagem_jogador[6]<=0):break
                                                else:
                                                    print(" - COMO?! COMO?! Você trapaceou! EU SEI!!! Mas tudo bem, você não conseguirá vencer o próximo, nem trapaceando MUITO!")
                                                    situacao[0]=situacao[0]+1
                                                    break
                                            else:
                                                print(" - COMO?! COMO?! Você trapaceou! EU SEI!!! Mas tudo bem, você não conseguirá vencer o próximo, nem trapaceando MUITO!")
                                                situacao[0]=situacao[0]+1
                                                break
                                        else:
                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                            time.sleep(0.5)
                            else:
                                if(situacao[0]>8):
                                    print("Você já lutou aqui!")
                                    time.sleep(1)
                                else:
                                    print("Você não pode me desafiar enquanto não vencer do briguento do quarto 41")
                                    time.sleep(1)
                        else:
                            if(acao_do_personagem=="43"):
                                if(situacao[0]==9):
                                    print(' - Sua presença é insignificante.')
                                    time.sleep(1)
                                    personagem_inimigo = [ "Estudante Briguento \n do Quarto 43", 180, 100, 20, 20, 1500, 1500]
                                    print(" - Mas vou te dar a honra de apreciar o meu cartão:")
                                    time.sleep(0.5)
                                    print("\n", personagem_inimigo[0],":",personagem_inimigo[5],"pontos de vida.\nAtaque : ",personagem_inimigo[1],".     Defesa : ", personagem_inimigo[2],".\n")
                                    time.sleep(1)
                                    print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                    time.sleep(0.5)
                                    while 1:
                                        acao_do_personagem = input("-")
                                        acao_do_personagem = acao_do_personagem.lower()
                                        if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                            break
                                        else:
                                            if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                batalha()
                                                if(personagem_jogador[6]<=0):break
                                                if(personagem_inimigo[6]>0):
                                                    while (personagem_inimigo[6]>0):
                                                        print(" - ... Fugindo?(sim ou não)")
                                                        time.sleep(0.5)
                                                        while 1:
                                                            acao_do_personagem = input("-")
                                                            acao_do_personagem = acao_do_personagem.lower()
                                                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                print(" - Você vai MORRER!!!")
                                                                time.sleep(1)
                                                                batalha()
                                                            else:
                                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                    print(" - Vai fugir mesmo, lixo?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                    time.sleep(0.5)
                                                                    acao_do_personagem=input("-")
                                                                    acao_do_personagem=acao_do_personagem.lower()
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - São os lixos como você que pagaram o prêmio que NUNCA SERÁ SEU!")
                                                                        time.sleep(0.5)
                                                                        print(" - Volte quando quiser apanhar mais!")
                                                                        time.sleep(0.5)
                                                                        personagem_jogador[7]=personagem_jogador[7]/2
                                                                        break
                                                                    else:
                                                                        if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                            print(" - Você vai MORRER!!!")
                                                                            time.sleep(1)
                                                                            batalha()
                                                                        else:
                                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                            time.sleep(0.5)
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                    time.sleep(0.5)
                                                    if(personagem_jogador[6]<=0):break
                                                    else:
                                                        print(" - Desgraçado... Você é forte demais...")
                                                        time.sleep(1)
                                                        situacao[0]=situacao[0]+1
                                                        break
                                                else:
                                                    print(" - Desgraçado... Você é forte demais...")
                                                    time.sleep(1)
                                                    situacao[0]=situacao[0]+1
                                                    break
                                            else:
                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                time.sleep(0.5)
                                else:
                                    if(situacao[0]>9):
                                        print("Você já lutou aqui!")
                                        time.sleep(1)
                                    else:
                                        print("Você não pode me desafiar enquanto não vencer do briguento do quarto 42")
                                        time.sleep(1)
                            else:
                                if(acao_do_personagem=="44"):
                                    if(situacao[0]==10):
                                        print(' - Me perdôe pelo comportamento daqueles dois... Nenhum deles tem a cabeça no lugar.')
                                        time.sleep(1)
                                        print(" - Mesmo assim, é raro alguém passar do quarto 40, é raríssimo alguém chegar até mim.")
                                        time.sleep(1)
                                        print(" - Você é um briguento e tanto!")
                                        time.sleep(1)
                                        personagem_inimigo = [ "Estudante Briguento \n do Quarto 44", 300, 200, 40, 40, 3200, 3200]
                                        print(" - Vamos logo ao que interessa:")
                                        time.sleep(0.5)
                                        print("\n", personagem_inimigo[0],":",personagem_inimigo[5],"pontos de vida.\nAtaque : ",personagem_inimigo[1],".     Defesa : ", personagem_inimigo[2],".\n")
                                        time.sleep(1)
                                        print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                        time.sleep(0.5)
                                        while 1:
                                            acao_do_personagem = input("-")
                                            acao_do_personagem = acao_do_personagem.lower()
                                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                break
                                            else:
                                                if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                    batalha()
                                                    if(personagem_jogador[6]<=0):break
                                                    if(personagem_inimigo[6]>0):
                                                        while (personagem_inimigo[6]>0):
                                                            print(" - ... Vai abandonar a nossa luta?(sim ou não)")
                                                            time.sleep(0.5)
                                                            while 1:
                                                                acao_do_personagem = input("-")
                                                                acao_do_personagem = acao_do_personagem.lower()
                                                                if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                    print(" - Desde o início, eu sabia que você não era qualquer um!")
                                                                    time.sleep(1)
                                                                    batalha()
                                                                else:
                                                                    if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                        print(" - Certeza, vai abandonar a última luta?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                        time.sleep(0.5)
                                                                        acao_do_personagem=input("-")
                                                                        acao_do_personagem=acao_do_personagem.lower()
                                                                        if(acao_do_personagem=="sim" or acao_do_personagem=="s" or acao_do_personagem=="si" or acao_do_personagem=="sm" or acao_do_personagem=="im" or acao_do_personagem=="ssim"):
                                                                            print(" - Recupere-se e treine mais!")
                                                                            time.sleep(0.5)
                                                                            print(" - Estarei esperando o seu retorno!")
                                                                            time.sleep(0.5)
                                                                            personagem_jogador[7]=personagem_jogador[7]/2
                                                                            break
                                                                        else:
                                                                            if(acao_do_personagem == "não" or acao_do_personagem=="n" or acao_do_personagem=="nao" or acao_do_personagem=="no" or acao_do_personagem=="na" or acao_do_personagem=="nã" or acao_do_personagem=="ao" or acao_do_personagem=="ão" or acao_do_personagem=="ñ" or acao_do_personagem=="ñão" or acao_do_personagem=="ño" or acao_do_personagem=="ñõ" or acao_do_personagem=="ñã" or acao_do_personagem=="ñaõ" or acao_do_personagem=="aõ"):
                                                                                print(" - Ainda bem, não quero deixar a nossa luta para depois!!!")
                                                                                time.sleep(1)
                                                                                batalha()
                                                                            else:
                                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                                time.sleep(0.5)
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                        time.sleep(0.5)
                                                        if(personagem_jogador[6]<=0):break
                                                        else:
                                                            print(" - Incrível... Você é um gênio das batalhas! É realmente dígno do prêmio!")
                                                            time.sleep(1)
                                                            print(" - Aqui está: uma Malha Ninja!")
                                                            time.sleep(0.5)
                                                            print("Você guardou a Malha Ninja na sua Mochila!")
                                                            time.sleep(1)
                                                            quantidade_adicionada=1
                                                            item_adicionado=malha_ninja
                                                            adicionaItem()
                                                            situacao[0]=situacao[0]+1
                                                            break
                                                    else:
                                                        print(" - Incrível... Você é um gênio das batalhas! É realmente dígno do prêmio!")
                                                        time.sleep(1)
                                                        print(" - Aqui está: uma Malha Ninja!")
                                                        time.sleep(0.5)
                                                        print("Você guardou a Malha Ninja na sua Mochila!")
                                                        time.sleep(1)
                                                        quantidade_adicionada=1
                                                        item_adicionado=malha_ninja
                                                        adicionaItem()
                                                        situacao[0]=situacao[0]+1
                                                        break
                                                else:
                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                    else:
                                        if(situacao[0]>10):
                                            print("Você já lutou aqui!")
                                            time.sleep(1)
                                        else:
                                            print(" - Você não pode me desafiar enquanto não vencer do briguento do quarto 43")
                                            time.sleep(1)
                                else:
                                    if(acao_do_personagem == "salvar o jogo" or acao_do_personagem=="guardar o jogo" or acao_do_personagem == "salvar jogo" or acao_do_personagem=="guardar jogo" or acao_do_personagem == "salvar" or acao_do_personagem == "save" or acao_do_personagem == "save game" or acao_do_personagem == "salvar o progresso" or acao_do_personagem == "salvar progresso" or acao_do_personagem == "guardar o progresso" or acao_do_personagem == "guardar progresso" or acao_do_personagem == "save progress" or acao_do_personagem == "salva" or acao_do_personagem == "sava" or acao_do_personagem == "slvar" or acao_do_personagem == "svar" or acao_do_personagem == "svr" or acao_do_personagem == "slvr" or acao_do_personagem == "sav" or acao_do_personagem == "sve" or acao_do_personagem == "sv" or acao_do_personagem == "salvar o game" or acao_do_personagem == "guardar o game" or acao_do_personagem == "salvar game" or acao_do_personagem == "guardar game"):
                                        save()
                                    else:
                                        if(acao_do_personagem=="ver a bolsa" or acao_do_personagem=="ver inventário" or acao_do_personagem=="ver o inventário" or acao_do_personagem=="ver bolsa" or acao_do_personagem=="ver mochila" or acao_do_personagem=="ver mala" or acao_do_personagem=="ver a mochila" or acao_do_personagem=="ver a mala" or acao_do_personagem=="inventário" or acao_do_personagem=="inventario" or acao_do_personagem=="iventario" or acao_do_personagem=="iventário" or acao_do_personagem=="mochila" or acao_do_personagem=="mochla" or acao_do_personagem=="mala" or acao_do_personagem=="bolsa" or acao_do_personagem=="itens" or acao_do_personagem=="ítens" or acao_do_personagem=="item"):
                                            inventárioPersonagem()
                                        else:
                                            print('\nEntrada Inválida!\n')
                                            time.sleep(0.5)
        if(personagem_jogador[6]<=0):break

#--Seu prédio: Terceiro Andar--#
def seuPrédioTerceiroAndar():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitacao,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situacao,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,acao_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if temporário[0]==True:
        print("Agora que você venceu todos os lutadores do 3º andar você subiu ao 4º.")
        time.sleep(1)
        seuPrédioQuartoAndar()
    if(variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioQuartoAndar()
    if(personagem_jogador[6]>0):
        variável_lugar = "seu prédio, 3º andar"
        if(situacao[0]==0):
            print("Você é abordado pelo morador do quarto 44...")
            time.sleep(1)
            print(" - E aí, você é o morador do 13 né?...")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            print(" - Você é um pouco azarado, rapaz! ... Ou sortudo, depende do seu ponto de vista.")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            print(" - Okay, vou te explicar...")
            time.sleep(1)
            print(" - Você sabe que nos dois últimos andares desse prédio, o terceiro e o quarto,")
            time.sleep(1)
            print("só tem quartos de estudantes briguentos, e nós estamos desafiando outros\n arruaceiros a lutarem conosco!")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            print(" - Claro, se você vencer de todos nós, será recompensado!")
            time.sleep(1)
            print(" - Vá em frente, visite um dos quartos para lutar com um de nós!")
            time.sleep(1)
            print(" - Eu estarei lá em cima, no meu quarto, te esperando.")
            time.sleep(1)
            print("\nEle subiu as escadas...")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            situacao[0]+=1
        else:
            if(situacao[0]==1):
                print("Você ainda não venceu nenhuma luta do desafio dos estudantes briguentos!")
                time.sleep(0.5)
            else:
                if(situacao[0]==2):
                    print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                    time.sleep(0.5)
                else:
                    if(situacao[0]>=3 and situacao[0]<6):
                        print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                        time.sleep(0.5)
                    else:
                        if(situacao[0]<9):
                            print("Você já venceu todas as lutas do terceiro andar, \nentão você continuou subindo para o 4º andar.")
                            time.sleep(0.5)
                            seuPrédioQuartoAndar()
                            variável_lugar = "seu prédio, 3º andar"
                        else:
                            print("Você já venceu o desafio dos estudantes briguentos do seu prédio!")
                            time.sleep(1)
    while 1:
        if(personagem_jogador[6]<=0):break
        if(situacao[0]>=9):
            variável_lugar = "seu prédio, 2º andar"
            break
        else:
            if(situacao[0]>6):
                print("Como você já venceu as lutas aqui, você continuou descendo...")
                time.sleep(0.5)
                print("Você desceu para o segundo andar.")
                time.sleep(0.5)
                variável_lugar = "seu prédio, 2º andar"
                break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos: 30, 31, 32, 33 e 34\n")
        print("\nver ficha do personagem\nver mochila\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", personagem_jogador[0],", o que você vai fazer?\n")
        acao_do_personagem = input("-")
        acao_do_personagem = acao_do_personagem.lower()
        if(acao_do_personagem=="checar os quartos" or acao_do_personagem=="checar quartos" or acao_do_personagem=="checar" or acao_do_personagem=="quartos" or acao_do_personagem=="checaros quartos" or acao_do_personagem=="checar osquartos" or acao_do_personagem=="checarosquartos" or acao_do_personagem=="checa os quartos" or acao_do_personagem=="checa os quarto" or acao_do_personagem=="checa o quarto" or acao_do_personagem=="checa o quartos" or acao_do_personagem=="checar os quarto" or acao_do_personagem=="checar o quarto" or acao_do_personagem=="bater na porta de um dos quartos" or acao_do_personagem=="checar um dos quartos" or acao_do_personagem=="bater na porta dos quartos" or acao_do_personagem=="bater a porta dos quartos" or acao_do_personagem=="bater quartos" or acao_do_personagem=="bater"):
            print("Qual dos quartos?(30, 31, 32, 33 ou 34)\n")
            time.sleep(0.5)
            acao_do_personagem = input("-")
            acao_do_personagem = acao_do_personagem.lower()
            if(acao_do_personagem!="30" and acao_do_personagem!="31" and acao_do_personagem!="32" and acao_do_personagem!="33" and acao_do_personagem!="34"):
                acao_do_personagem="entrada inválida!"
        if (acao_do_personagem == "ver ficha do personagem" or acao_do_personagem == "ver a ficha do personagem" or acao_do_personagem == "ver a ficha de personagem" or acao_do_personagem == "ficha" or acao_do_personagem=="ficha do personagem" or acao_do_personagem=="ficha de personagem" or acao_do_personagem=="ver ficha de personagem" or acao_do_personagem=="ver ficha" or acao_do_personagem == "olhar ficha do personagem" or acao_do_personagem == "ver minha ficha" or acao_do_personagem=="minha ficha" or acao_do_personagem=="ficha personagem" or acao_do_personagem=="olhar ficha de personagem" or acao_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(acao_do_personagem=="subir as escadas" or acao_do_personagem=="subir" or acao_do_personagem=="subir escadas" or acao_do_personagem=="subi" or acao_do_personagem=="subi as escadas" or acao_do_personagem=="subir escada" or acao_do_personagem=="subi escada" or acao_do_personagem=="subi a escada" or acao_do_personagem=="sobe"):
                print("Você subiu para o quarto andar, lá você encontrou mais cinco quartos de portas abertas.")
                time.sleep(0.5)
                seuPrédioQuartoAndar()
            else:
                if(acao_do_personagem=="descer as escadas" or acao_do_personagem=="descer escadas" or acao_do_personagem=="descer escada" or acao_do_personagem=="descer a escada" or acao_do_personagem=="sair" or acao_do_personagem=="descer" or acao_do_personagem=="sair do prédio"):
                    print("Você desceu para o segundo andar.")
                    time.sleep(0.5)
                    break
                else:
                    if(acao_do_personagem=="30"):
                        if(situacao[5] == 0):
                            print("Eu sou o seu oponente! Vença todos deste andar para subir!")
                            time.sleep(2)
                            personagem_inimigo = [ "Estudante Briguento \n do Quarto 30", 5, 12, 2, 2, 110, 110]
                            batalha()
                            if(personagem_jogador[6]<=0):
                                personagem_jogador[6]=1
                                print(" - Você é fraco, se fosse uma luta no andar de cima você teria morrido!")
                                time.sleep(0.5)
                                print(" - Vá cuidar desses seus ferimentos e volte para lutar mais!")
                                time.sleep(0.5)
                            else:
                                if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                    while (personagem_inimigo[6]>0):
                                        print(" - Você não pode fugir das lutas, é uma regra para continuar no desafio e ganhar o prêmio!")
                                        time.sleep(1)
                                        batalha()
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
                                            print(" - Você é fraco, se fosse uma luta no andar de cima você teria morrido!")
                                            time.sleep(0.5)
                                            print(" - Vá cuidar desses seus ferimentos e volte para lutar mais!")
                                            time.sleep(0.5)
                                            break
                                        else:
                                            print(" - Isso aí! Você me venceu!")
                                            time.sleep(1)
                                            situacao[0]=situacao[0]+1
                                            situacao[5]=1
                                            if(situacao[0]==6):
                                                temporário[0]= True
                                            else:
                                                if(situacao[0]==2):
                                                    print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                    time.sleep(1)
                                                else:
                                                    if(situacao[0]>=3 and situacao[0]<6):
                                                        print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                        time.sleep(1)
                                            break
                                else:
                                    print(" - Isso aí! Você me venceu!")
                                    time.sleep(1)
                                    situacao[0]=situacao[0]+1
                                    situacao[5]=1
                                    if(situacao[0]==6):
                                        temporário[0]= True
                                    else:
                                        if(situacao[0]==2):
                                            print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                            time.sleep(1)
                                        else:
                                            if(situacao[0]>=3 and situacao[0]<6):
                                                print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                time.sleep(1)
                        else:
                            print("Você já lutou aqui!")
                            time.sleep(1)
                    else:
                        if(acao_do_personagem=="31"):
                            if(situacao[6] == 0):
                                print(" - Você é o desafiante??? Parece um fracote!")
                                time.sleep(2)
                                personagem_inimigo = [ "Estudante Briguento \n do Quarto 31", 13, 4, 5, 1, 130, 130]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Você é mesmo um fracote!")
                                    time.sleep(0.5)
                                    print(" - Vá se curar para continuar tentando subir para o quarto andar!")
                                    time.sleep(0.5)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Volte aqui seu fracote! Não seja um covarde! Você não pode fugir de TODAS as lutas!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Você é mesmo um fracote!")
                                                time.sleep(0.5)
                                                print(" - Vá se curar para continuar tentando subir para o quarto andar!")
                                                time.sleep(0.5)
                                                break
                                            else:
                                                print(" - Não vacile com os caras lá do quarto andar, eles não pegam leve!")
                                                time.sleep(1)
                                                situacao[0]=situacao[0]+1
                                                situacao[6]=1
                                                if(situacao[0]==6):
                                                    temporário[0]= True
                                                else:
                                                    if(situacao[0]==2):
                                                        print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                        time.sleep(1)
                                                    else:
                                                        if(situacao[0]>=3 and situacao[0]<6):
                                                            print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                            time.sleep(1)
                                                break
                                    else:
                                        print(" - Não vacile com os caras lá do quarto andar, eles não pegam leve!")
                                        time.sleep(1)
                                        situacao[0]=situacao[0]+1
                                        situacao[6]=1
                                        if(situacao[0]==6):
                                            temporário[0]= True
                                        else:
                                            if(situacao[0]==2):
                                                print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                time.sleep(1)
                                            else:
                                                if(situacao[0]>=3 and situacao[0]<6):
                                                    print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                    time.sleep(1)
                            else:
                                print("Voce já lutou aqui!")
                                time.sleep(1)
                        else:
                            if(acao_do_personagem=="32"):
                                if(situacao[7]==0):
                                    print(" - Cai dentro, rapá!")
                                    time.sleep(2)
                                    personagem_inimigo = [ "Estudante Briguento \n do Quarto 32", 8, 8, 2, 1, 100, 100]
                                    batalha()
                                    if(personagem_jogador[6]<=0):
                                        personagem_jogador[6]=1
                                        print(" - Moleque criado a leite com pêra!")
                                        time.sleep(0.5)
                                        print(" - Lá em cima ninguém vai te dar essa colher de chá que eu to te dando!")
                                        time.sleep(0.5)
                                    else:
                                        if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                            while (personagem_inimigo[6]>0):
                                                print(" - Ramelão, não foge da luta, não!")
                                                time.sleep(1)
                                                batalha()
                                                if(personagem_jogador[6]<=0):
                                                    personagem_jogador[6]=1
                                                    print(" - Moleque criado a leite com pêra!")
                                                    time.sleep(0.5)
                                                    print(" - Lá em cima ninguém vai te dar essa colher de chá que eu to te dando!")
                                                    time.sleep(0.5)
                                                    break
                                                else:
                                                    print(" - Nada mal, quem sabe você consegue o prêmio! Nunca se sabe... ")
                                                    time.sleep(1)
                                                    situacao[0]=situacao[0]+1
                                                    situacao[7]=1
                                                    if(situacao[0]==6):
                                                        temporário[0]= True
                                                    else:
                                                        if(situacao[0]==2):
                                                            print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                            time.sleep(1)
                                                        else:
                                                            if(situacao[0]>=3 and situacao[0]<6):
                                                                print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                                time.sleep(1)
                                                    break
                                        else:
                                            print(" - Nada mal, quem sabe você consegue o prêmio! Nunca se sabe... ")
                                            time.sleep(1)
                                            situacao[0]=situacao[0]+1
                                            situacao[7]=1
                                            if(situacao[0]==6):
                                                temporário[0]= True
                                            else:
                                                if(situacao[0]==2):
                                                    print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                    time.sleep(1)
                                                else:
                                                    if(situacao[0]>=3 and situacao[0]<6):
                                                        print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                        time.sleep(1)
                                else:
                                    print("Voce já lutou aqui!")
                                    time.sleep(1)
                            else:
                                if(acao_do_personagem=="33"):
                                    if(situacao[8]==0):
                                        print(" - ÔÔô, CIDADÃO!")
                                        time.sleep(2)
                                        personagem_inimigo = [ "Estudante Briguento \n do Quarto 33", 10, 8, 5, 5, 120, 120]
                                        batalha()
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
                                            print(" - Olha lá, o cara não aguenta e depois vai chorando pra casa!")
                                            time.sleep(0.5)
                                            print(" - Se você continuar tropeçando assim, cedo ou tarde o mundo vai te atropelá!")
                                            time.sleep(0.5)
                                        else:
                                            if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                                while (personagem_inimigo[6]>0):
                                                    print(" - Tá na hora de acordar pra vida, cidadão!")
                                                    time.sleep(1)
                                                    batalha()
                                                    if(personagem_jogador[6]<=0):
                                                        personagem_jogador[6]=1
                                                        print(" - Olha lá, o cara não aguenta e depois vai chorando pra casa!")
                                                        time.sleep(0.5)
                                                        print(" - Se você continuar tropeçando assim, cedo ou tarde o mundo vai te atropelá!")
                                                        time.sleep(0.5)
                                                        break
                                                    else:
                                                        print(" - ACORDA CARA! Você não é mais nenhum menininho bobinho, não! ")
                                                        time.sleep(1)
                                                        situacao[0]=situacao[0]+1
                                                        situacao[8]=1
                                                        if(situacao[0]==6):
                                                            temporário[0]= True
                                                        else:
                                                            if(situacao[0]==2):
                                                                print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                                time.sleep(1)
                                                            else:
                                                                if(situacao[0]>=3 and situacao[0]<6):
                                                                    print("Você já venceu",situacao[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                                    time.sleep(1)
                                                        break
                                            else:
                                                print(" - ACORDA CARA! Você não é mais nenhum menininho bobinho, não! ")
                                                time.sleep(1)
                                                situação[0]=situação[0]+1
                                                situação[8]=1
                                                if(situação[0]==6):
                                                    temporário[0]= True
                                                else:
                                                    if(situação[0]==2):
                                                        print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                        time.sleep(1)
                                                    else:
                                                        if(situação[0]>=3 and situação[0]<6):
                                                            print("Você já venceu",situação[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                            time.sleep(1)
                                    else:
                                        print("Você já lutou aqui!")
                                        time.sleep(1)
                                else:
                                    if(ação_do_personagem=="34"):
                                        if(situação[9]==0):
                                            print(" - Qual é, velho? O negócio é descer o murro de ferro na cara do inimigo!")
                                            time.sleep(2)
                                            personagem_inimigo = [ "Estudante Briguento \n do Quarto 34", 20, 20, 6, 6, 66.6, 66.6]
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Você não tem um sangue fervente o suficiente para derreter o metal!")
                                                time.sleep(0.5)
                                                print(" - Você precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                time.sleep(0.5)
                                            else:
                                                if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                                    while (personagem_inimigo[6]>0):
                                                        print(" - As mentiras já são antigas demais, mas você não quer saber!\nCorrer é uma futilidade!")
                                                        time.sleep(1)
                                                        batalha()
                                                        if(personagem_jogador[6]<=0):
                                                            personagem_jogador[6]=1
                                                            print(" - Você não tem um sangue fervente o suficiente para derreter o metal!")
                                                            time.sleep(1)
                                                            print(" - Você precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                            time.sleep(1)
                                                            break
                                                        else:
                                                            print(" - A verdade é mais dura que o aço! Mas a visão nunca morre!")
                                                            time.sleep(1)
                                                            situação[0]=situação[0]+1
                                                            situação[9]=1
                                                            if(situação[0]==6):
                                                                temporário[0]= True
                                                            else:
                                                                if(situação[0]==2):
                                                                    print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                                    time.sleep(1)
                                                                else:
                                                                    if(situação[0]>=3 and situação[0]<6):
                                                                        print("Você já venceu",situação[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                                        time.sleep(1)
                                                            break
                                                else:
                                                    print(" - A verdade é mais dura que o aço! Mas a visão nunca morre!")
                                                    time.sleep(1)
                                                    situação[0]=situação[0]+1
                                                    situação[9]=1
                                                    if(situação[0]==6):
                                                        temporário[0]= True
                                                    else:
                                                        if(situação[0]==2):
                                                            print("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                            time.sleep(1)
                                                        else:
                                                            if(situação[0]>=3 and situação[0]<6):
                                                                print("Você já venceu",situação[0]-1,"lutas do desafio dos estudantes briguentos!")
                                                                time.sleep(1)
                                        else:
                                            print("Você já lutou aqui!")
                                            time.sleep(0.5)
                                    else:
                                        if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                            save()
                                        else:
                                            if(ação_do_personagem=="ver a bolsa" or ação_do_personagem=="ver inventário" or ação_do_personagem=="ver o inventário" or ação_do_personagem=="ver bolsa" or ação_do_personagem=="ver mochila" or ação_do_personagem=="ver mala" or ação_do_personagem=="ver a mochila" or ação_do_personagem=="ver a mala" or ação_do_personagem=="inventário" or ação_do_personagem=="inventario" or ação_do_personagem=="iventario" or ação_do_personagem=="iventário" or ação_do_personagem=="mochila" or ação_do_personagem=="mochla" or ação_do_personagem=="mala" or ação_do_personagem=="bolsa" or ação_do_personagem=="itens" or ação_do_personagem=="ítens" or ação_do_personagem=="item"):
                                                inventárioPersonagem()
                                            else:
                                                print('\nEntrada Inválida!\n')
                                                time.sleep(0.5)

#--Seu prédio: Segundo Andar--#
def seuPrédioSegundoAndar():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitação,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situação,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,ação_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if(variável_lugar == "seu prédio, 3º andarb" or variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioTerceiroAndar()
    variável_lugar = "seu prédio, 2º andar"
    while 1:
        if(personagem_jogador[6]<=0):break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos\n")
        if(situação[2]==1):
            print("\narrombar o quarto 24")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", personagem_jogador[0],", o que você vai fazer?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        if(ação_do_personagem=="checar os quartos" or ação_do_personagem=="checar quartos" or ação_do_personagem=="checar" or ação_do_personagem=="quartos" or ação_do_personagem=="checaros quartos" or ação_do_personagem=="checar osquartos" or ação_do_personagem=="checarosquartos" or ação_do_personagem=="checa os quartos" or ação_do_personagem=="checa os quarto" or ação_do_personagem=="checa o quarto" or ação_do_personagem=="checa o quartos" or ação_do_personagem=="checar os quarto" or ação_do_personagem=="checar o quarto" or ação_do_personagem=="bater na porta de um dos quartos" or ação_do_personagem=="checar um dos quartos" or ação_do_personagem=="bater na porta dos quartos" or ação_do_personagem=="bater a porta dos quartos" or ação_do_personagem=="bater quartos" or ação_do_personagem=="bater"):
            print("Qual dos quartos?(20, 21, 22, 23 ou 24)\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            if(ação_do_personagem!="20" and ação_do_personagem!="21" and ação_do_personagem!="22" and ação_do_personagem!="23" and ação_do_personagem!="24"):
                ação_do_personagem="entrada inválida!"
        if (ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(ação_do_personagem=="subir as escadas" or ação_do_personagem=="subir" or ação_do_personagem=="subir escadas" or ação_do_personagem=="subi" or ação_do_personagem=="subi as escadas" or ação_do_personagem=="subir escada" or ação_do_personagem=="subi escada" or ação_do_personagem=="subi a escada" or ação_do_personagem=="sobe"):
                print("Você subiu para o terceiro andar,")
                time.sleep(0.5)
                print("lá você encontrou cinco quartos de portas abertas e outra escada ascendente.")
                time.sleep(1)
                seuPrédioTerceiroAndar()
                if(personagem_jogador[6]<=0):break
            else:
                if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                    print("Você desceu para o primeiro andar, o andar do seu quarto.")
                    time.sleep(1)
                    break
                else:
                    if(ação_do_personagem=="20"):
                        if(situação[3]==10):
                            print("Você já pegou tudo o que tinha para pegar aqui.")
                            time.sleep(0.5)
                        else:
                            print("Você bate na porta e percebe, pelo barulho do trepidar da maçaneta, que ela está destrancada...")
                            time.sleep(2)
                            print("Abrir a porta?(sim ou não)")
                            while 1:
                                ação_do_personagem = input("-")
                                ação_do_personagem = ação_do_personagem.lower()
                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                    print("Você entrou, não havia ninguém...")
                                    time.sleep(2)
                                    print("Ao revistar o quarto você encontrou 10 Reais!")
                                    time.sleep(1)
                                    personagem_jogador[7]=personagem_jogador[7]+10
                                    situação[10]=1
                                    break
                                else:
                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                        print("Você ignorou o quarto...")
                                        time.sleep(0.75)
                                        break
                                    else:
                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                                        time.sleep(0.5)
                    else:
                        if(ação_do_personagem=="21"):
                            if(situação[3]==7):
                                print("Você bate na porta...")
                                time.sleep(0.5)
                                print(" - Olá! - diz o avô do garoto - Muito obrigado por treinar o meu neto,")
                                time.sleep(1)
                                print("agora ele não precisa se esconder mais dos trombadinhas da escola.")
                                time.sleep(2)
                            if(situação[3]==6):
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
                                            print(" - Não abandone nossa luta!")
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
                                                    situação[3]=7
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Obrigado, mesmo!")
                                            time.sleep(1)
                                            situação[3]=7
                            if(situação[3]==5):
                                print(" - Estou empolgado! Não aguentava mais esperar pela nossa luta!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Forte", 150, 100, 20, 20, 2000, 2000]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                    time.sleep(1)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - A nossa luta não acabou ainda!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                                time.sleep(1)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                                    time.sleep(1)
                                                    situação[3]=6
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                            time.sleep(1)
                                            situação[3]=6
                            if(situação[3]==4):
                                print(" - Dessa vez não vou perder tão fácil!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Sério", 30, 25, 10, 5, 200, 200]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Estou te levando a sério, não vou perder mais!")
                                    time.sleep(0.5)
                                    print(" - Estarei te esperando para uma revanche.")
                                    time.sleep(0.5)
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Honre a nossa luta até o fim!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Estou te levando a sério, não vou perder mais!")
                                                time.sleep(0.5)
                                                print(" - Estarei te esperando para uma revanche.")
                                                time.sleep(0.5)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                                    time.sleep(1)
                                                    situação[3]=5
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                            time.sleep(1)
                                            situação[3]=5
                            if(situação[3]==3):
                                print(" - Eu estava te esperando, panaca!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Convencido", 8, 12, 5, 10, 110, 110]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Não aguenta o tranco, não? Hahaha!")
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
                                                print(" - Não aguenta o tranco, não? Hahaha!")
                                                time.sleep(0.5)
                                                print(" - Volte qualquer hora para apanhar mais!")
                                                time.sleep(0.5)
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                                    time.sleep(1)
                                                    situação[3]=4
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                            time.sleep(1)
                                            situação[3]=4
                            if(situação[3]==2):
                                print(" - Meu avô disse que você viria... - disse o garoto baixinho - Vamos logo ao que interessa!")
                                time.sleep(2)
                                personagem_inimigo = [ "Garoto Fracote", 3, 10, 2, 2, 100, 100]
                                batalha()
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                    print(" - Você não é tão forte quanto meu avô falou.")
                                    time.sleep(1)
                                    situação[3]=3
                                else:
                                    if(personagem_inimigo[6]>0 and personagem_jogador[6]>1):
                                        while (personagem_inimigo[6]>0):
                                            print(" - Meu avô disse para não parar de lutar até eu não aguentar mais!")
                                            time.sleep(1)
                                            batalha()
                                            if(personagem_jogador[6]<=0):
                                                personagem_jogador[6]=1
                                                print(" - Você não é tão forte quanto meu avô falou.")
                                                time.sleep(1)
                                                situação[3]=3
                                            else:
                                                if(personagem_inimigo[6]<=0):
                                                    print(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                                    time.sleep(1)
                                                    situação[3]=3
                                    else:
                                        if(personagem_inimigo[6]<=0):
                                            print(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                            time.sleep(1)
                                            situação[3]=3
                            if(situação[3]==1):
                                print("A porta está trancada.")
                                time.sleep(1)
                            if(situação[3]==0):
                                print("Você bateu na porta...")
                                time.sleep(0.5)
                                print("Um senhor baixo e fracote abriu a porta... Ele parecia muito com um frango")
                                time.sleep(1)
                                print(" - O que que você quer?!")
                                time.sleep(1)
                                print("...")
                                time.sleep(0.5)
                                print(" - Saia daqui então!")
                                time.sleep(2)
                                personagem_inimigo = [ "Senhor Doente", 5, 3, -3, 3, 50, 50]
                                batalha()
                                if(personagem_jogador[6]<=0):break
                                if(personagem_inimigo[6]>0):
                                    print("Depois de se afastar o senhor começou a gritar...")
                                    time.sleep(1)
                                    print("Com a mão no peito, ele começou a tossir...")
                                    time.sleep(1)
                                    print(" - Ahhhh... - gemiu o senhor que caia lentamente.")
                                    time.sleep(1)
                                    print(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                    time.sleep(1)
                                    print("O menino pegou o senhor nos braços antes que tombasse \ne apertou algumas vezes uma bombinha para asma na boca dele...")
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
                                        situação[3]==1
                                    else:
                                        print("O garoto caiu no chão dentro da casa e começou a chorar.")
                                        time.sleep(1)
                                        print(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                        time.sleep(1)
                                        print("Em seguida ele fechou e trancou a porta.")
                                        time.sleep(1)
                                        situação[3]=1
                                else:
                                    print("O senhor caiu no chão com uma mão no peito...")
                                    time.sleep(1)
                                    print("Ele tentava gritar algo enquanto estendia a outra mão...")
                                    time.sleep(1)
                                    print("Mas não conseguia dizer nada, estava tendo crise de asma...")
                                    time.sleep(1)
                                    print("Sua mão apontava para um lugar dentro da casa...")
                                    time.sleep(1)
                                    print("Vai ajudar o idoso?\n")
                                    time.sleep(0.5)
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            print("Você entrou na casa, pegou a bombinha em cima da mesa e a apertou na boca no velho...")
                                            time.sleep(1)
                                            print(" - Ah... Ah... - o senhor tentava recuperar o ar - Você não é um mau rapaz no fim das contas...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Você gosta de lutar, não é garoto? Eu brigava muito quando era mais jovem...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Nem sempre os punhos são o bastante...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.5)
                                            print(" - Não falo do coração na luta, isso você já tem, falo de armas...")
                                            time.sleep(1)
                                            print(" - Tome... Eu usava este punhal no meu tempo... Agora é seu.")
                                            time.sleep(1)
                                            item_adicionado=punhal_envelhecido
                                            quantidade_adicionada=1
                                            adicionaItem()
                                            print("Você guardou o Punhal Envelhecido na mala!")
                                            time.sleep(1)
                                            print(" - Se não for pedir demais, venha sempre que puder para treinar o meu neto... \nEle ainda é muito fraco e eu não tenho mais o mesmo vigor de antes...")
                                            time.sleep(1)
                                            print(" - Não me entenda mal, não é uma troca de favores... \nÉ um pedido de um velho que não consegue ajudar seu neto.")
                                            time.sleep(1)
                                            situação[3]=2
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                print(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                                time.sleep(1)
                                                print("O menino pegou o senhor nos braços antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
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
                                                    situação[3]=1
                                                else:
                                                    print("O garoto caiu no chão dentro da casa e começou a chorar.")
                                                    time.sleep(1)
                                                    print(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                                    time.sleep(1)
                                                    print("Em seguida ele fechou e trancou a porta.")
                                                    time.sleep(1)
                                                    situação[3]=1
                                                break
                                            else:
                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                                                time.sleep(1)
                        else:
                            if(ação_do_personagem=="22"):
                                if(situação[4]==4):
                                    print("Voce bateu na porta...")
                                    time.sleep(0.5)
                                    print("Ninguém te atendeu.")
                                    time.sleep(0.5)
                                if(situação[4]==3):
                                    print(" - E aí, rapaz!")
                                    time.sleep(1.5)
                                    teste_de_sorte = random.randrange(3)
                                    if(teste_de_sorte==1):
                                        print(" - Você chegou em boa hora! Entre e coma um pedaço de pizza comigo!")
                                        time.sleep(1)
                                        print("Você ganhou um pedaço de pizza!")
                                        time.sleep(1)
                                        item_adicionado=pedaço_pizza
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        print(" - Até outra hora, vizinho!")
                                        time.sleep(0.5)
                                    else:
                                        print(" - Estou sem pizza agora... Talvez mais tarde...")
                                        time.sleep(1)
                                if(situação[4]==2):
                                    print(" - O quê você quer aqui?")
                                    time.sleep(1)
                                    print("Você vai dizer a ele que comeu a sua pizza?(sim ou não)")
                                    time.sleep(0.5)
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            print(" - ...")
                                            time.sleep(1.5)
                                            print(" - VOCÊ...")
                                            time.sleep(1.5)
                                            print(" - Você é muito cara de pau mesmo, mas adimiro a sua sinceridade.")
                                            time.sleep(1)
                                            print(" - Eu sempre como pizza, quando você quiser passe aqui para pegar um pedaço.")
                                            time.sleep(1)
                                            situação[4]=3
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                print(" - ...")
                                                time.sleep(1.5)
                                                print(" - Me deixe em paz!")
                                                time.sleep(1)
                                                situação[4]=4
                                                break
                                            else:
                                                print('Entrada inválida! Digite "sim" ou "não".')
                                                time.sleep(0.5)
                                if(situação[4]==1):
                                    print("Você bateu na porta do quarto, que agora está fechado.")
                                    time.sleep(1)
                                    print("Você escuta passos rápidos e violentos vindo à porta")
                                    time.sleep(1)
                                    print(" - EU TO MUITO PUTO! - diz o estudante que abriu violentamente a porta - ENTRARAM E COMERAM A MINHA PIZZA!")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1.5)
                                    print(" - Ah esquece... Nem deve ter sido você...")
                                    time.sleep(1)
                                    situação[4]=2
                                if(situação[4]==0):
                                    print("O quarto está aberto, você entra e vê um estudante vagabundo dormindo num sofá com uma pizza no colo.")
                                    time.sleep(1)
                                    print("E aí, vai pegar essa pizza? (sim ou não)\n")
                                    time.sleep(0.5)
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            print("Você guardou a pizza inteira na mochila!")
                                            time.sleep(1)
                                            item_adicionado=pedaço_pizza
                                            quantidade_adicionada=8
                                            adicionaItem()
                                            situação[4]=1
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                print("Você deixou a pizza para depois!")
                                                time.sleep(1)
                                                break
                                            else:
                                                print('Entrada inválida! Digite "sim" ou "não".')
                                                time.sleep(0.5)
                            else:
                                if(ação_do_personagem=="23"):
                                   print("Você vê um quarto aberto, sujo e vazio...")
                                   time.sleep(0.5)
                                   print("Parece abandonado por um bom tempo... Já tem fauna e flora prória!")
                                   time.sleep(1)
                                else:
                                    if(ação_do_personagem=="24"):
                                        if(situação[2]==0):
                                            print("Você encara um indivíduo de aparencia extravagante e vulgar encostado no batente da porta...")
                                            time.sleep(1)
                                            print(" - Qualé merh-mão? Tá querenu tretá?")
                                            time.sleep(2)
                                            personagem_inimigo = [ "Mané de Boné", 10, 5, 10, 1, 100, 100]
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                print("Ele corre atrás de você e te dá um chute no joelho!")
                                                time.sleep(1)
                                                print("!!!")
                                                time.sleep(0.5)
                                                print("Você perdeu 30 pontos de vida!")
                                                time.sleep(1)
                                                print(" - Fica diboa rapáh!")
                                                time.sleep(1)
                                                personagem_jogador[6]=personagem_jogador[6]-30
                                                if(personagem_jogador[6]<=0):personagem_jogador[6]=1
                                                print("Ele voltou ao batente da porta do quarto e agora está te encarando...")
                                                time.sleep(1)
                                                print("Você me envergonha.")
                                                time.sleep(1)
                                            else:
                                                print(" - Que isso maluco?! Que isso?!")
                                                time.sleep(1)
                                                print("Ele entrou cambaleando para o quarto dele e se trancou!")
                                                time.sleep(1)
                                                situação[2]=1
                                        if(situação[2]==1):
                                            print("O quarto está trancado...")
                                            time.sleep(1)
                                        if(situação[2]==2):
                                            print("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            time.sleep(1)
                                            print("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            time.sleep(1)
                                            print("Dentro você vê muito sangue pelo quarto, os poucos móveis quebrados, ")
                                            time.sleep(1)
                                            print("mas nada de valor...")
                                            time.sleep(1)
                                            matarAlguém()
                                        if(situação[2]==3):
                                            print("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            time.sleep(1)
                                            print("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            time.sleep(1)
                                            print("Também escuta, vindo lá de dentro, soluços em sussurros e sussurros em soluços...")
                                            time.sleep(1)
                                            print("Melhor não entrar... Não há nada de mais lá dentro.")
                                            time.sleep(1)
                                    else:
                                        if(ação_do_personagem=="arrombar a porta do quarto 24" or ação_do_personagem=="arrombar o quarto 24" or ação_do_personagem=="arrombar" or ação_do_personagem=="arrombar a porta" or ação_do_personagem=="entrar no quarto 24"):
                                            if(situação[2]==1):
                                                print("Você pisoteou a porta e entrou no quarto!")
                                                time.sleep(1)
                                                print(" - Não, por favor nao!...")
                                                time.sleep(1)
                                                while 1:
                                                    if(situação[2]==2):
                                                        break
                                                    if(situação[2]==3):
                                                        break
                                                    print("Melhor não continuar...(sim ou não)\n")
                                                    time.sleep(0.5)
                                                    ação_do_personagem=input("-")
                                                    ação_do_personagem=ação_do_personagem.lower()
                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                        while 2:
                                                            print("Eu insisto... É melhor parar... Você está de cabeça quente... (sim ou não)\n")
                                                            time.sleep(0.5)
                                                            ação_do_personagem=input("-")
                                                            ação_do_personagem=ação_do_personagem.lower()
                                                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                input("(Aperte ENTER)")
                                                                input("!!!!!!!!!!!!")
                                                                input(" - NÃO, NÃO!")
                                                                input("!!!!!!!!!!!!")
                                                                input(" - N-NÃo..o!")
                                                                input("!!!!!!!!....")
                                                                input("!!!!........")
                                                                input("....!!!!....")
                                                                input("........!!!!")
                                                                input("!!!!....!!!!")
                                                                print("(Já não há mais motivos para golpear...)")
                                                                time.sleep(1)
                                                                print("Seus punhos vermelhos tremem...")
                                                                time.sleep(1)
                                                                print("Você o espancou até a morte...")
                                                                time.sleep(1)
                                                                print("...")
                                                                time.sleep(1)
                                                                matarAlguém()
                                                                situação[2]=2
                                                                break
                                                            else:
                                                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                    print("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                                    time.sleep(1)
                                                                    print("Você superou seus instintos e respeitou seus princípios...")
                                                                    time.sleep(1)
                                                                    print("Ao recuperar seu fôlego, seus pontos de vida aumentaram.")
                                                                    time.sleep(1)
                                                                    personagem_jogador[5]=personagem_jogador[5]+50
                                                                    personagem_jogador[6]=personagem_jogador[5]
                                                                    situação[2]=3
                                                                    break
                                                                else:
                                                                    print("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                                                                    time.sleep(1)
                                                        break
                                                    else:
                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                            print("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                            time.sleep(1)
                                                            print("Você superou seus instintos e respeitou seus princípios...")
                                                            time.sleep(1)
                                                            print("Ao recuperar seu fôlego, você recuperou seus pontos de vida.")
                                                            time.sleep(1)
                                                            personagem_jogador[6]=personagem_jogador[5]
                                                            situação[2]=3
                                                            break
                                                        else:
                                                            print("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                                                            time.sleep(1)
                                            if(situação[4]==2):
                                                matarAlguém()
                                            if(situação[2]==3):
                                                print("Você já fez o bastante por aqui... Melhor se afastar.")
                                                time.sleep(0.5)
                                        else:
                                            if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                                save()
                                            else:
                                                if(ação_do_personagem=="ver a bolsa" or ação_do_personagem=="ver inventário" or ação_do_personagem=="ver o inventário" or ação_do_personagem=="ver bolsa" or ação_do_personagem=="ver mochila" or ação_do_personagem=="ver mala" or ação_do_personagem=="ver a mochila" or ação_do_personagem=="ver a mala" or ação_do_personagem=="inventário" or ação_do_personagem=="inventario" or ação_do_personagem=="iventario" or ação_do_personagem=="iventário" or ação_do_personagem=="mochila" or ação_do_personagem=="mochla" or ação_do_personagem=="mala" or ação_do_personagem=="bolsa" or ação_do_personagem=="itens" or ação_do_personagem=="ítens" or ação_do_personagem=="item"):
                                                    inventárioPersonagem()
                                                else:
                                                    print('\nEntrada Inválida!\n')
                                                    time.sleep(0.5)

#--Seu prédio: Primeiro Andar--#
def seuPrédioPrimeiroAndar():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitação,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situação,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,ação_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda
    if(variável_lugar == "seu prédio, 2º andarb" or variável_lugar == "seu prédio, 3º andarb" or variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioSegundoAndar()
    if(personagem_jogador[6]>0):
        variável_lugar = "seu prédio, 1º andar"
        print("Agora você está no corredor do primeiro andar do seu prédio.")
        time.sleep(3)
        print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\nolhar\n")
        time.sleep(1)
        if (variável_cenário[0] == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            time.sleep(1)
            if (variável_cenário[2] == "sim" and objeto[0] == "não"):
                print("olhar o bêbado\n")
                time.sleep(1)
        if(objeto[1] == "sim"):
            print("\narrombar o quarto 10\n")
            time.sleep(1)
        if (objeto[0] == "1"):
            print("\nacordar o bêbado\n")
            print("\nrevistar o bêbado\n")
            time.sleep(1)
        if (objeto[0] == "2"):
            print("\nmover o bêbado\n")
            time.sleep(1)
        if (objeto[0] == "3"):
            print("\natacar o bêbado\n")
            time.sleep(1)
        if (objeto[0] == "sim"):
            print("\nabrir a porta dos fundos\n")
            time.sleep(1)
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n", "\n#", "-"*30,"#\n")
        time.sleep(2)
        print("\nO que você vai fazer, ", personagem_jogador[0], "?\n")
        ação_do_personagem = ("-")
        ação_do_personagem = ação_do_personagem.lower()
    while 1:
        if(personagem_jogador[6]<=0):break
        if(ação_do_personagem=="checar os quartos" or ação_do_personagem=="checar quartos" or ação_do_personagem=="checar" or ação_do_personagem=="quartos" or ação_do_personagem=="checaros quartos" or ação_do_personagem=="checar osquartos" or ação_do_personagem=="checarosquartos" or ação_do_personagem=="checa os quartos" or ação_do_personagem=="checa os quarto" or ação_do_personagem=="checa o quarto" or ação_do_personagem=="checa o quartos" or ação_do_personagem=="checar os quarto" or ação_do_personagem=="checar o quarto" or ação_do_personagem=="bater na porta de um dos quartos" or ação_do_personagem=="checar um dos quartos" or ação_do_personagem=="bater na porta dos quartos" or ação_do_personagem=="bater a porta dos quartos" or ação_do_personagem=="bater quartos" or ação_do_personagem=="bater"):
            print("Qual dos quartos?(10, 11, 12 ou 14)\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            if(ação_do_personagem!="10" and ação_do_personagem!="11" and ação_do_personagem!="12" and ação_do_personagem!="13" and ação_do_personagem!="14"):
                ação_do_personagem="entrada inválida!"
        if(ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(ação_do_personagem == "olhar" or ação_do_personagem == "ver" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha" or ação_do_personagem == "olhar quarto" or ação_do_personagem == "olha quarto" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha o quarto" or ação_do_personagem == "ve" or ação_do_personagem == "vê"):
                if (variável_cenário[2] == "1" or variável_cenário[2] == "sim"):
                    print("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                    time.sleep(3)
                    print("Num dos lados desse corredor há uma janela quebrada,")
                    time.sleep(3)
                    print("mas no outro se encontra um bêbado caido no chão, imundo e cercado de vômito encostado na porta dos fundos, impedindo o acesso.")
                    time.sleep(3)
                    print("E ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                    time.sleep(3)
                    print("A mais próxima sobe e a colada à parede desce.")
                    time.sleep(3)
                else:
                    if (objeto[0] == "sim"):
                        print("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                        time.sleep(3)
                        print("Num dos lados desse corredor há uma janela quebrada, mas no outro se encontra a porta dos fundos.")
                        time.sleep(3)
                        print("Ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        time.sleep(3)
                        print("A mais próxima sobe e a colada à parede desce.")
                        time.sleep(3)
                    else:
                        print("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                        time.sleep(3)
                        print("Num dos lados desse corredor há uma janela quebrada,")
                        time.sleep(3)
                        print("mas no outro se encontra, encostado na porta dos fundos e caído no chão coberto por cacos de vidro, um homem sujo, cercado por algum líquido que parece laranja...")
                        time.sleep(3)
                        print("E ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        time.sleep(3)
                        print("A mais próxima sobe e a colada à parede desce.")
                        time.sleep(3)
                        variável_cenário[0] = "sim"
            else:
                if(ação_do_personagem=="cheirar" or ação_do_personagem=="cherar" or ação_do_personagem=="dar um tapa" or ação_do_personagem=="cheira" or ação_do_personagem=="chera"):
                    if(variável_cenário[2]=="não"):
                        variável_cenário[2]="sim"
                    print("Você sente um cheiro forte de álcool e vômito")
                    time.sleep(3)
                else:
                    if(ação_do_personagem=="10"):
                        if(objeto[3]=="sim"):
                            print("Você vê uma porta arrombada... Não há mais nada de interessante dentro do quarto.")
                            time.sleep(3)
                        else:
                            print("Você bateu na porta, mas ninguém atendeu... Ela parece fácil de ser arrombada...")
                            time.sleep(3)
                            objeto[1]="sim"
                    else:
                        if(ação_do_personagem=="11"):
                            if(situação[1]==0):
                                print("Quando você bateu, a porta se abriu no primeiro toque por não ter uma fechadura...")
                                time.sleep(4)
                                print("Você vê, dentro da casa, uma mulher alta de ombros largos, BEM LARGOS, musculosa e com o maxilar largo...")
                                time.sleep(4)
                                print("Ela estava apenas de toalha...")
                                time.sleep(2)
                                print(" - MAS QUE ATREVIMENTO! SUMA DAQUI! - diz a mulher enquanto te epurra com a porta que é fechada violentamente.")
                                time.sleep(4)
                                print("Você perdeu 5 pontos de vida ao cair no corredor...")
                                time.sleep(3)
                                personagem_jogador[6]=personagem_jogador[6]-5
                                if(personagem_jogador[6]<=0):
                                    personagem_jogador[6]=1
                                situação[1]=1
                            else:
                                if(situação[1]==1):
                                    print("Você empurrou a porta sem fechadura, mas moradora que ainda estava te toalha, furiosamente fechou a porta gritando, antes que você pudesse terminar de abrir!")
                                    time.sleep(3)
                                    print("Você perdeu 5 pontos de vida ao cair no corredor...")
                                    time.sleep(3)
                                    personagem_jogador[6]=personagem_jogador[6]-5
                                    if(personagem_jogador[6]<=0):
                                        personagem_jogador[6]=1
                                    situação[1]=2
                                else:
                                    if(situação[1]==2):
                                        print("Você abriu a porta e levou um soco na cara, caindo em seguida no chão do corredor.")
                                        time.sleep(3)
                                        print("Você perdeu 10 pontos de vida...")
                                        time.sleep(3)
                                        personagem_jogador[6]=personagem_jogador[6]-10
                                        if(personagem_jogador[6]<=0):
                                            personagem_jogador[6]=1
                                        situação[1]=3
                                    else:
                                        if(situação[1]==3):
                                            print("Você abriu a porta e viu a mulher de toalha extremamente furiosa com os ombros levemente curvados, deixando à mostra seus braços musculosos e gigantescos.")
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
                                                print("A mulher caiu inconsciente no chão...")
                                                time.sleep(1)
                                                print("Dentro da casa você encontrou 100 reais e um suplemento alimentício")
                                                time.sleep(2)
                                                print("Você guardou ambos na mochila!")
                                                time.sleep(2)
                                                personagem_jogador[7]=personagem_jogador[7]+100
                                                quantidade_adicionada=1
                                                item_adiconado=suplemento_alimentício
                                                adicionaItem()
                                                situação[1]=4
                                        else:
                                            if(situação[1]==4):
                                                print("Você entra no quarto, encontra a mulher que você derrotou caida no chão e mais nada além dos móveis velhos dela.")
                        else:
                            if(ação_do_personagem=="12"):
                                print("Você bateu na porta...")
                                time.sleep(0.5)
                                print(" - Já vai! - exclama uma senhora de dentro da casa.")
                                time.sleep(1)
                                print("...")
                                time.sleep(0.5)
                                print(" - Olá, meu jovem! Por que você não entra e prova um pouco do bolo que eu acabei de fazer?")
                                time.sleep(1)
                                print("...")
                                time.sleep(0.5)
                                print("Você recurperou TODOS os seus pontos de vida!")
                                time.sleep(1)
                                personagem_jogador[6]=personagem_jogador[5]
                            else:
                                if(ação_do_personagem=="14"):
                                    if(objeto[4]=="sim"):
                                        print("Suma daqui seu idiota... Deixe-a em paz...")
                                    else:
                                        if(objeto[0]=="sim" or objeto[0]=="pegou o dinheiro"):
                                            print("Você bateu na porta...")
                                            time.sleep(1)
                                            print("Você escuta passos de dentro vindo à porta...")
                                            time.sleep(1)
                                            print(" - O que você quer? - questionou a mulher que abrira a porta aos prantos")
                                            time.sleep(2)
                                            print("...")
                                            time.sleep(0.5)
                                            print("Ela observa o corpo do marido no chão do corredor...")
                                            time.sleep(1)
                                            print(" - F-Foi você?!...")
                                            time.sleep(1)
                                            print("...")
                                            time.sleep(0.75)
                                            print(" - VOCÊ VAI PAGAR CARO POR MATAR MEU MARIDO!")
                                            time.sleep(1)
                                            personagem_inimigo = [ "Mulher aos Prantos", 20, 20, 10, 10, 100, 900]
                                            batalha()
                                            if(personagem_jogador[6]<=0):break
                                            if(personagem_inimigo[6]>0):
                                                print(" - CHEGA!")
                                                time.sleep(0.5)
                                                print(" - Você matou meu marido...")
                                                time.sleep(1)
                                                print(" - Como você teve a pachorra de me procurar?!")
                                                time.sleep(1)
                                                print("Ela fechou a porta chorando.")
                                                time.sleep(1)
                                            else:
                                                print("A mulher caiu inconsciente no chão...")
                                                time.sleep(2)
                                                print("Dentro da casa você encontrou um par de talheres de prata...")
                                                time.sleep(2)
                                                print("Você os guardou na mochila...")
                                                time.sleep(2)
                                                print("...")
                                                time.sleep(2)
                                                print("Seu idiota...")
                                                time.sleep(3)
                                                quantidade_adicionada=1
                                                item_adiconado=talheres_prata
                                                adicionaItem()
                                                objeto[4]="sim"
                                        else:
                                            print("Você bateu na porta...")
                                            time.sleep(1)
                                            print(" - JÁ DISSE PARA VOCÊ IR EMBORA SEU BÊBADO! - grita uma mulher de dentro da casa - NINGUÉM TE MERECE COMO MARIDO!")
                                            time.sleep(2)
                                else:
                                    if(ação_do_personagem=="13"):
                                        print("Você é bobo?")
                                        time.sleep(0.5)
                                        print("Esse é o seu quarto!")
                                        time.sleep(0.5)
                                        print("Você está atrasado demais para voltar!")
                                        time.sleep(1)
                                    else:
                                        if(ação_do_personagem=="arrombar a porta do quarto 10" or ação_do_personagem=="arrombar 10" or ação_do_personagem=="arrombar quarto 10" or ação_do_personagem=="arrombar o quarto 10" or ação_do_personagem=="arrombar" or ação_do_personagem=="arrombar a porta" or ação_do_personagem=="quarto 10" or ação_do_personagem=="entrar no quarto 10"):
                                            if(objeto[3]=="sim"):
                                                print("Você já arrombou essa porta... Não há mais nada de interessante dentro do quarto.")
                                                time.sleep(1)
                                            else:
                                                print("Você entrou no quarto e encontrou uma Jaqueta de Couro!")
                                                time.sleep(1.5)
                                                print("Você a guardou na mochila!")
                                                time.sleep(1)
                                                item_adiconado=jaqueta_imitação
                                                quantidade_adicionada=1
                                                adicionaItem()
                                                objeto[3]="sim"
                                        else:
                                            if(ação_do_personagem=="subir as escadas" or ação_do_personagem=="subir" or ação_do_personagem=="subir escadas" or ação_do_personagem=="subi" or ação_do_personagem=="subi as escadas" or ação_do_personagem=="subir escada" or ação_do_personagem=="subi escada" or ação_do_personagem=="subi a escada" or ação_do_personagem=="sobe"):
                                                print("Você subiu para o segundo andar, lá você encontrou mais cinco quartos e outra escada ascendente.")
                                                time.sleep(1)
                                                seuPrédioSegundoAndar()
                                                if(personagem_jogador[6]<=0):break
                                            else:
                                                if(ação_do_personagem=="olhar o bêbado" or ação_do_personagem=="olhar bêbado" or ação_do_personagem=="olha o bêbado" or ação_do_personagem=="olha bÊbado" or ação_do_personagem=="olhar o bebado" or ação_do_personagem=="olhar bebado" or ação_do_personagem=="olha o bebado" or ação_do_personagem=="olha bebado"):
                                                    objeto[0]="1"
                                                    print("Você vê um homem de 40 anos, coberto por cacos de vidro, bebida e vômito, dormindo no chão.")
                                                    time.sleep(1)
                                                else:
                                                    if(ação_do_personagem=="revistar o bêbado" or ação_do_personagem=="revistar bêbado" or ação_do_personagem=="revistar" or ação_do_personagem=="revista bêbado" or ação_do_personagem=="revista o bêbado" or ação_do_personagem=="revistar o bebado" or ação_do_personagem=="revistar bebado" or ação_do_personagem=="revistar" or ação_do_personagem=="revista bebado" or ação_do_personagem=="revista o bebado"):
                                                        if(objeto[2]=="não"):
                                                            print("Você achou um energético e o guardou na mochila!")
                                                            time.sleep(1)
                                                            item_adicionado=lata_energético
                                                            quantidade_adicionada=1
                                                            adicionaItem()
                                                            objeto[2]="sim"
                                                        else:
                                                            print("Você não encontrou mais nada...\n")
                                                            time.sleep(2)
                                                    else:
                                                        if(ação_do_personagem=="acordar o bêbado" or ação_do_personagem=="acordar bêbado" or ação_do_personagem=="acorda o bêbado" or ação_do_personagem=="acorda bêbado" or ação_do_personagem=="acordar o bebado" or ação_do_personagem=="acordar bebado" or ação_do_personagem=="acorda o bebado" or ação_do_personagem=="acorda bebado"):
                                                            objeto[0]="2"
                                                            print("Você tenta acordar o bêbado, mas não consegue...")
                                                            time.sleep(1)
                                                        else:
                                                            if(ação_do_personagem=="mover o bêbado" or ação_do_personagem=="mover bêbado" or ação_do_personagem=="move o bêbado" or ação_do_personagem=="move bêbado" or ação_do_personagem=="mover o bebado" or ação_do_personagem=="mover bebado" or ação_do_personagem=="move o bebado" or ação_do_personagem=="move bebado" or ação_do_personagem=="mover" or ação_do_personagem=="move"):
                                                                objeto[0]="3"
                                                                print("Você pensa em mover o bêbado...")
                                                                time.sleep(1)
                                                                print("Mas o cheiro e a sujeira fazem você vomitar em cima dele!")
                                                                time.sleep(2)
                                                                print("...")
                                                                time.sleep(1)
                                                                print("Ele continua dormindo...")
                                                                time.sleep(1)
                                                            else:
                                                                if(ação_do_personagem=="atacar o bêbado" or ação_do_personagem=="atacar bêbado" or ação_do_personagem=="ataca o bêbado" or ação_do_personagem=="ataca bêbado" or ação_do_personagem=="atacar o bebado" or ação_do_personagem=="atacar bebado" or ação_do_personagem=="ataca o bebado" or ação_do_personagem=="ataca bebado" or ação_do_personagem=="atacar" or ação_do_personagem=="ataca"):
                                                                    if(objeto[0]!="sim" or objeto[0]!="pegou o dinheiro"):
                                                                        print("Você chuta várias vezes o bêbado violentamente!")
                                                                        time.sleep(0.5)
                                                                        input("(Aperte Enter)")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        print("(Pronto, você chutou o suficiente!)")
                                                                        time.sleep(0.5)
                                                                        print(" - P-PARA! PARA! PARA! - berra o bêbado que acabou de acordar.")
                                                                        time.sleep(1)
                                                                        print("Ele se levanta e te empurra ganhando distância.")
                                                                        time.sleep(1)
                                                                        print("...")
                                                                        time.sleep(1)
                                                                        print(" - Ssseu muleque i-insstrosmestido!... *hic*\n")
                                                                        time.sleep(2)
                                                                        personagem_inimigo = [ "Bêbado", 4, 4, -3, -3, 30, 500]
                                                                        batalha()
                                                                        if(personagem_jogador[6]<=0):break
                                                                        if(personagem_inimigo[6]>0):
                                                                            print("Você escapa da briga, mas em seguida o bêbado tosse sangue e cái no chão...")
                                                                            time.sleep(2)
                                                                        else:
                                                                            print("O bêbado coberto de bebida, vômito e sangue, cái de costas no chão,")
                                                                            time.sleep(1)
                                                                            print("sendo empalado pelos diversos cacos de vidro...")
                                                                            time.sleep(1)
                                                                            print("O sangue dele escorre pelo corredor até os seus pés...")
                                                                            time.sleep(1.5)
                                                                            print("Você vira o rosto fechando os olhos e abaixando os punhos...")
                                                                            time.sleep(2)
                                                                            print("Agora, desencostado da porta dos fundos, o bêbado já não é mais um impecílio...")
                                                                            time.sleep(1)
                                                                        objeto[0]="sim"
                                                                else:
                                                                    if(ação_do_personagem=="abrir a porta dos fundos"):
                                                                        if(objeto[0]=="sim"):
                                                                            print("Você abre a porta... ")
                                                                            time.sleep(1)
                                                                            print("É um armário de limpesa.")
                                                                            time.sleep(1)
                                                                            print("Em meio às vassouras, rodos e outras coisas, você encontra uma mala...")
                                                                            time.sleep(2)
                                                                            print("Você abre a mala, encontra entre os materiais de escritório e 10 Reais!")
                                                                            time.sleep(1)
                                                                            print("...")
                                                                            time.sleep(2)
                                                                            print("Você também achou um lápis apontado e o guardou na mochila!")
                                                                            time.sleep(1)
                                                                            item_adicionado=lapis_apontado
                                                                            quantidade_adicionada=1
                                                                            adicionaItem()
                                                                            personagem_jogador[7]=personagem_jogador[7]+10
                                                                            objeto[0]="pegou o dinheiro"
                                                                        else:
                                                                            if(objeto[0]=="pegou o dinheiro"):
                                                                                print("Você vê materiais de limpesa e uma mala aberta.")
                                                                                time.sleep(0.5)
                                                                            else:
                                                                                print("Não dá para abrir!")
                                                                                time.sleep(0.5)
                                                                    else:
                                                                        if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                                                                            if(ponto_de_save==1):
                                                                                while 1:
                                                                                    print("Do lado de fora há um oponente MUITO forte.")
                                                                                    time.sleep(3)
                                                                                    print("Tem certeza que está pronto para sair? (sim ou não)")
                                                                                    ação_do_personagem=input("-")
                                                                                    ação_do_personagem=ação_do_personagem.lower()
                                                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                                        ação_do_personagem="sim"
                                                                                        break
                                                                                    else:
                                                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                                            print("Você decidiu não sair do prédio.")
                                                                                            time.sleep(0.5)
                                                                                            break
                                                                                        else:
                                                                                            print("Entrada inválida!")
                                                                                            time.sleep(0.5)
                                                                                if(ação_do_personagem=="sim"):
                                                                                    print("Você desceu as escadas e saiu do prédio...")
                                                                                    time.sleep(0.5)
                                                                                    break
                                                                            else:
                                                                                print("Você desceu as escadas e saiu do prédio...")
                                                                                time.sleep(0.5)
                                                                                suaRua()
                                                                                break
                                                                        else:
                                                                            if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                                                                save()
                                                                            else:
                                                                                if(ação_do_personagem=="ver a bolsa" or ação_do_personagem=="ver inventário" or ação_do_personagem=="ver o inventário" or ação_do_personagem=="ver bolsa" or ação_do_personagem=="ver mochila" or ação_do_personagem=="ver mala" or ação_do_personagem=="ver a mochila" or ação_do_personagem=="ver a mala" or ação_do_personagem=="inventário" or ação_do_personagem=="inventario" or ação_do_personagem=="iventario" or ação_do_personagem=="iventário" or ação_do_personagem=="mochila" or ação_do_personagem=="mochla" or ação_do_personagem=="mala" or ação_do_personagem=="bolsa" or ação_do_personagem=="itens" or ação_do_personagem=="ítens" or ação_do_personagem=="item"):
                                                                                    inventárioPersonagem()
                                                                                else:
                                                                                    print('\nEntrada Inválida!\n')
                                                                                    time.sleep(0.5)
        print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\nolhar\n")
        if (variável_cenário[0] == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            if (variável_cenário[2] == "sim" and objeto[0] == "não"):
                print("olhar o bêbado\n")
        if(objeto[1] == "sim"):
            print("\narrombar o quarto 10\n")
        if (objeto[0] == "1"):
            print("\nacordar o bêbado\n")
            print("\nrevistar o bêbado\n")
        if (objeto[0] == "2"):
            print("\nmover o bêbado\n")
        if (objeto[0] == "3"):
            print("\natacar o bêbado\n")
        if (objeto[0] == "sim"):
            print("\nabrir a porta dos fundos\n")
        print("\nver ficha do personagem\nver mochila\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n", "\n#", "-"*30,"#\n")
        print("\nO que você fará agora, ", personagem_jogador[0],"?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()

#--Sua Rua--#
def suaRua():
    global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitação,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situação,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,ação_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda


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
 | | *=*=*=*=*=*=*=*=*=*=*=*=*=    [começar]    =*=*=*=*=*=*=*=*=*=*=*=*=* | | 
 | | ======================**=**=     ou     =**=**======================= | | 
 | | *=*=*=*=*=*=*=*=*=*=*=*=*=   [continuar]   =*=*=*=*=*=*=*=*=*=*=*=*=* | | 
 | | =============================           ============================= | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | | 
 | | ===================== : ===================== : ===================== | |
 | | ===================== : - - - - - - - - - - - : ===================== | | 
 | | * =* =* =* =* =* =* = : --------------------- : = *= *= *= *= *= *= * | |
 | |_______________________________________________________________________| | 
 |/_________________________________________________________________________\|

 Digite "começar" ou "continuar":''')
        while 1:
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            if(ação_do_personagem =="começar" or ação_do_personagem == "meçar" or ação_do_personagem == "come" or ação_do_personagem =="iniciar" or ação_do_personagem =="inicia" or ação_do_personagem =="inici" or ação_do_personagem =="inicio" or ação_do_personagem =="início" or ação_do_personagem =="new game" or ação_do_personagem =="start new game" or ação_do_personagem =="start" or ação_do_personagem =="start game" or ação_do_personagem =="comecar" or ação_do_personagem =="comeca" or ação_do_personagem =="começa" or ação_do_personagem =="com" or ação_do_personagem =="cmeçar" or ação_do_personagem =="cmecar" or ação_do_personagem =="comcar" or ação_do_personagem =="comçar" or ação_do_personagem =="comear" or ação_do_personagem =="comer" or ação_do_personagem =="cocar" or ação_do_personagem =="ccar" or ação_do_personagem =="cmcr" or ação_do_personagem =="cmecr" or ação_do_personagem =="coçar" or ação_do_personagem =="cçar" or ação_do_personagem =="cmçr" or ação_do_personagem =="cmeçr" or ação_do_personagem =="cumessá" or ação_do_personagem =="comessa" or ação_do_personagem =="comessar"):
                break
            else:
                if (ação_do_personagem == "continuar" or ação_do_personagem == "ccontinuar" or ação_do_personagem == "continuarr" or ação_do_personagem == "conntinuar" or ação_do_personagem == "conttinuar" or ação_do_personagem == "continnuar" or ação_do_personagem == "ccontinuarr" or ação_do_personagem == "cconntinuar" or ação_do_personagem == "cconttinuar" or ação_do_personagem == "ccontinnuar" or ação_do_personagem == "cconnttinuar" or ação_do_personagem == "cconntinnuar" or ação_do_personagem == "cconntinuarr" or ação_do_personagem == "continuart" or ação_do_personagem == "cconttinnuar" or ação_do_personagem == "cconttinuarr" or ação_do_personagem == "cconnttinnuarr" or ação_do_personagem == "cntnr" or ação_do_personagem == "contnr" or ação_do_personagem == "continr" or ação_do_personagem == "continur" or ação_do_personagem == "cntinuar" or ação_do_personagem == "cntnuar" or ação_do_personagem == "cntnar" or ação_do_personagem == "cntinur" or ação_do_personagem == "cntinr" or ação_do_personagem == "cntinar" or ação_do_personagem == "contnur" or ação_do_personagem == "ontinuar" or ação_do_personagem == "cotinuar" or ação_do_personagem == "coninuar" or ação_do_personagem == "contiuar" or ação_do_personagem == "coinar" or ação_do_personagem == "continua" or ação_do_personagem == "cntn" or ação_do_personagem == "contn" or ação_do_personagem == "contin" or ação_do_personagem == "continu" or ação_do_personagem == "cntinua" or ação_do_personagem == "cntnua" or ação_do_personagem == "cntna" or ação_do_personagem == "cntinu" or ação_do_personagem == "cntin" or ação_do_personagem == "cntina" or ação_do_personagem == "contnu" or ação_do_personagem == "ontinua" or ação_do_personagem == "cotinua" or ação_do_personagem == "coninua" or ação_do_personagem == "contiua" or ação_do_personagem == "coina" or ação_do_personagem == "con" or ação_do_personagem == "cont" or ação_do_personagem == "conti" or ação_do_personagem == "ccontin" or ação_do_personagem == "ccontinu"):
                    print("\nDeseja continuar o jogo guardado em qual espaço?\n")
                    time.sleep(1)
                    arq = open('\espaço_save00.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  0:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save01.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  1:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save02.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  2:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save03.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  3:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save04.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  4:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save05.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  5:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save06.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  6:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save07.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  7:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save08.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  8:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    arq = open('\espaço_save09.py', 'rb')
                    mostrar_save = pickle.load(arq)
                    print("\nEspaço  9:     Lugar:",mostrar_save[5], "\n          Nome:",mostrar_save[1],"  Vida:", mostrar_save[3],"\n          Ataque:",mostrar_save[7],"  Defesa:",mostrar_save[9],"  Agilidade:",mostrar_save[11])
                    arq.close
                    while 1:
                        print("\n(Digite um número entre 0 e 9)")
                        ação_do_personagem=input("-")
                        if(ação_do_personagem=="0"):
                            arq = open('\espaço_save00.py', 'rb')
                            break
                        else:
                            if(ação_do_personagem=="1"):
                                arq = open('\espaço_save01.py', 'rb')
                                break
                            else:
                                if(ação_do_personagem=="2"):
                                    arq = open('\espaço_save02.py', 'rb')
                                    break
                                else:
                                    if(ação_do_personagem=="3"):
                                        arq = open('\espaço_save03.py', 'rb')
                                        break
                                    else:
                                        if(ação_do_personagem=="4"):
                                            arq = open('\espaço_save04.py', 'rb')
                                            break
                                        else:
                                            if(ação_do_personagem=="5"):
                                                arq = open('\espaço_save05.py', 'rb')
                                                break
                                            else:
                                                if(ação_do_personagem=="6"):
                                                    arq = open('\espaço_save06.py', 'rb')
                                                    break
                                                else:
                                                    if(ação_do_personagem=="7"):
                                                        arq = open('\espaço_save07.py', 'rb')
                                                        break
                                                    else:
                                                        if(ação_do_personagem=="8"):
                                                            arq = open('\espaço_save08.py', 'rb')
                                                            break
                                                        else:
                                                            if(ação_do_personagem=="9"):
                                                                arq = open('\espaço_save09.py', 'rb')
                                                                break
                                                            else:
                                                                print("Entrada inválida!\n")
                                                                time.sleep(0.5)
                    mostrar_save = pickle.load(arq)
                    equipado_roupa = pickle.load(arq)
                    equipado_capa = pickle.load(arq)
                    equipado_luva = pickle.load(arq)
                    equipado_anel = pickle.load(arq)
                    equipado_maos = pickle.load(arq)
                    equipado_calcado = pickle.load(arq)
                    variável_cenário = pickle.load(arq)
                    objeto = pickle.load(arq)
                    situação = pickle.load(arq)
                    temporário = pickle.load(arq)
                    variável_lugar = pickle.load(arq)
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
                        print("\nERRO: Você não possui dados salvos.\n")
                        time.sleep(0.5)
                    break
                else:            
                    print('Entrada inválida!\n')
        if(ponto_de_save==0):
            print("\nIniciando novo jogo...\n")
            time.sleep(2)
            print("\n\nVocê é um homem... Qual é o seu nome?\n")
            personagem_jogador[0] = input("-")
            while 1:
                print("Seu nome é", personagem_jogador[0], "?")
                while 2:
                    ação_do_personagem = input("-")
                    ação_do_personagem = ação_do_personagem.lower()
                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                        break
                    else:
                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                            print("\nEntão qual é o seu nome?\n")
                            personagem_jogador[0] = input("-")
                            break
                        else:
                            print('\nEntrada inválida, digite "sim" ou "não".\n')
                            time.sleep(0.5)
                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                    break
            print("Muito prazer, ", personagem_jogador[0],'.')
            time.sleep(2)
            print('Nós já nos conhecemos?(digite "não" para ver o tutorial)\n')
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            while 1:
                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                    print('Tem certeza??')
                    time.sleep(2)
                    print('Não me lembro de você...')
                    time.sleep(1)
                    print('(eu REALMENTE recomendo que você digite "não" para ver o tutorial!)')
                    ação_do_personagem = input("-")
                    ação_do_personagem = ação_do_personagem.lower()
                    break
                else:
                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                        break
                    else:
                        print('Entrada inválida! Digite "sim" ou "não".')
                        time.sleep(0.5)
                        ação_do_personagem = input("-")
                        ação_do_personagem = ação_do_personagem.lower()
            while 1:
                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                    break
                else:
                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                        print('\nSou o narrador da nossa história, vou apenas te guiar de acordo com as suas decisões...')
                        time.sleep(3)
                        print('Então saiba que não vou facilitar as coisas para você!')
                        time.sleep(4)
                        print('Porém minha função é te guiar, ser os seus olhos, ouvidos, mãos e nariz,')
                        time.sleep(4)
                        print('e além disso você parece precisar de algumas instruções para tornar disso algo mais divertido.')
                        time.sleep(4)
                        print('\nToda vez antes da sua ação te mostrarei uma lista de ações possíveis de se realizar.')
                        time.sleep(3)
                        print('\nE também te mostrarei se a sua ação for inválida.')
                        time.sleep(2)
                        print('\nMas você só receberá minha atenção quando eu pedir,')
                        time.sleep(5)
                        print('você perceberá isso quando ver um hífen após a minha pergunta.')
                        time.sleep(5)
                        print('Entendeu?')
                        ação_do_personagem = input("-")
                        ação_do_personagem = ação_do_personagem.lower()
                        while 1:
                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                break
                            if( ação_do_personagem== "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                print('\nVocê é bobo??')
                            else:
                                print('\nEntrada inválida!\n\nVocê pode:\nconcordar comigo dizendo "sim"\n')
                            ação_do_personagem = input("-")
                            ação_do_personagem = ação_do_personagem.lower()
                        print('Bom menino!')
                        time.sleep(2)
                        print('\nAlguns comandos como "salvar o jogo" e "ver ficha do personagem" estarão quase sempre disponíveis.')
                        time.sleep(2)
                        print('\nToda vez que você descobre algo novo no cenário, a lista de ações muda,')
                        time.sleep(3)
                        print('mas os resultados dessas ações podem mudar de acordo com o que você faz,')
                        time.sleep(4)
                        print('sendo assim é altamente recomendável que você repita algumas ações em um mesmo cenário.')
                        time.sleep(4)
                        print('\nAcho que já é o bastante para começarmos, mas posso repetir se você quiser...')
                        time.sleep(2)
                        print('Você entendeu tudo o que eu disse?')
                        objeto[0]="ganha presente"
                    else:
                        print('Não entendi o que você quis dizer...\nPor favor, digite "sim" ou "não".\n')
                    ação_do_personagem = input("-")
                    ação_do_personagem = ação_do_personagem.lower()
                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                        ação_do_personagem="sim"
            if(objeto[0]=="ganha presente"):
                print("\nÓtimo, ",personagem_jogador[0],".")
                time.sleep(1)
                print("Acho que começamos com o pé direito! Fico feliz que você tenha me escutado como um bom garoto!")
                time.sleep(2)
                print("Por isso deixei um presente para você no seu guarda-roupas, tenho certeza que você ficará feliz.")
                time.sleep(2)
            else:
                print("Eu não me lembro de você...")
                time.sleep(3)
                print("Então você deve ser mesmo irrelevante!")
                time.sleep(3)

#####################----------------------------__INÍCIO DO JOGO__----------------------------#####################
            print("\nCenário: acabou de amanhecer, seu quarto está desarrumado,")
            time.sleep(2)
            print("você ainda está de pijama e atrasado para a aula - não que você se importe muito com isso.")
            time.sleep(3)
            print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar)
            time.sleep(2)
            print("\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
            time.sleep(2)
            if (variável_cenário[0] == "sim"):
                print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\n\nolhar pela janela\n")
                time.sleep(2)
            print("\nver ficha do personagem\nver mochila\nsair do quarto\n")
            time.sleep(1)
            print("\n#", "-"*30,"#\n")
            print("\nO que você vai fazer", personagem_jogador[0],"?\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            while 1:
                if (ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
                    ficha_personagem()
                else:
                    if (ação_do_personagem== "vetir" or ação_do_personagem=="vest" or ação_do_personagem=="vesti" or ação_do_personagem=="veti" or ação_do_personagem=="estir" or ação_do_personagem=="esti" or ação_do_personagem=="etir" or ação_do_personagem == "vestir" or ação_do_personagem == "vesir" or ação_do_personagem == "vestir uniforme" or ação_do_personagem == "vestir o uniforme" or ação_do_personagem == "vestir o uniforme estudantil" or ação_do_personagem == "vestir uniforme estudantil" or ação_do_personagem == "se vestir" or ação_do_personagem == "se vestir para a aula" or ação_do_personagem == "se vestir pra aula" or ação_do_personagem == "vestir para a aula" or ação_do_personagem == "me arrumar" or ação_do_personagem == "tomar banho" or ação_do_personagem == "ir ao banheiro" or ação_do_personagem == "cagar" or ação_do_personagem == "mijar" or ação_do_personagem == "fazer xixi" or ação_do_personagem == "trocar de roupa" or ação_do_personagem == "me trocar" or ação_do_personagem == "trocar"):
                        if (temporário[0] == False):
                            print("Você colocou a mão embaixo do seu travesseiro e achou seu uniforme.\n")
                            time.sleep(1)
                            print("Você guardou o Uniforme Estudantil na sua mochila!\n")
                            time.sleep(2)
                            item_adicionado=uniforme_estudantil
                            quantidade_adicionada=1
                            adicionaItem()
                            temporário[0] = True
                        else:
                            print("Você já pegou seu uniforme!\n")
                            time.sleep(1)
                    else:
                        if (ação_do_personagem == "arrumar o quarto" or ação_do_personagem == "arrumar" or ação_do_personagem == "arrumar quarto" or ação_do_personagem == "arruma" or ação_do_personagem == "arruma o quarto" or ação_do_personagem == "arruma quarto" or ação_do_personagem == "quarto"):
                            if (variável_cenário[1] == "não"):
                                print("Você achou 15 Reais enquanto arrumava o seu quarto!\n")
                                time.sleep(2)
                                personagem_jogador[7] = +15
                                variável_cenário[1] = "sim"
                            else:
                                print("Você já arrumou o seu quarto!\n")
                                time.sleep(1)
                        else:
                            if (ação_do_personagem == "olhar" or ação_do_personagem=="olh" or ação_do_personagem == "ver" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha" or ação_do_personagem == "olhar quarto" or ação_do_personagem == "olha quarto" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha o quarto" or ação_do_personagem == "ve" or ação_do_personagem == "vê"):
                                if (variável_cenário[1] == "não"):
                                    print("Você não consegue ver nada além de bagunça, MUITA BAGUNÇA!!!\n")
                                    time.sleep(2)
                                else:
                                    print("Você vê um quarto arrumado, com um guarda-roupas, uma estante de livros, uma mesa de escritório com gavetas e uma janela.\n")
                                    time.sleep(3)
                                    variável_cenário[0] = "sim"
                            else:
                                if (ação_do_personagem == "olhar as gavetas" or ação_do_personagem == "olhar gavetas" or ação_do_personagem == "olha a gaveta" or ação_do_personagem == "olhar a gaveta" or ação_do_personagem == "olhar gaveta" or ação_do_personagem == "olhar as gaveta" or ação_do_personagem == "olha as gavetas" or ação_do_personagem == "olha gaveta" or ação_do_personagem == "olha as gaveta" or ação_do_personagem == "olha a gavetas" or ação_do_personagem == "ver as gavetas" or ação_do_personagem == "ver a gaveta" or ação_do_personagem == "ver as gaveta" or ação_do_personagem == "ver a gavetas" or ação_do_personagem=="gaveta" or ação_do_personagem=="gavetas"):
                                    if (temporário[1] == True):
                                        print("Você olhou novamente as gavetas, mas não encontrou nada interessante.\n")
                                        time.sleep(1)
                                    else:
                                        print("Você achou um Soco-Inglês enquanto olhava as gavetas!\n")
                                        time.sleep(2)
                                        item_adicionado=soco_pvc
                                        quantidade_adicionada=1
                                        adicionaItem()
                                        print("Você o guardou na mochila!")
                                        time.sleep(2)
                                        temporário[1]=True
                                else:
                                    if (ação_do_personagem == "olhar o guarda-roupas" or ação_do_personagem =="olhar o guarda" or ação_do_personagem =="olhar o garda" or ação_do_personagem == "guarda" or ação_do_personagem=="roupa" or ação_do_personagem == "olha o guarda-roupas" or ação_do_personagem == "olha o guarda-roupa" or ação_do_personagem == "olhar o guarda-roupa" or ação_do_personagem == "olhar guarda-roupas" or ação_do_personagem == "olha guarda-roupas" or ação_do_personagem == "olha guarda-roupa" or ação_do_personagem == "olhar guarda-roupa" or ação_do_personagem == "olhar o guarda roupas" or ação_do_personagem == "olha o guarda roupas" or ação_do_personagem == "olha o guarda roupa" or ação_do_personagem == "olhar o guarda roupa" or ação_do_personagem == "olhar guarda roupas" or ação_do_personagem == "olha guarda roupas" or ação_do_personagem == "olha guarda roupa" or ação_do_personagem == "olhar guarda roupa" or ação_do_personagem == "olhar o guardaroupas" or ação_do_personagem == "olha o guardaroupas" or ação_do_personagem == "olha o guardaroupa" or ação_do_personagem == "olhar o guardaroupa" or ação_do_personagem == "olhar guardaroupas" or ação_do_personagem == "olha guardaroupas" or ação_do_personagem == "olha guardaroupa" or ação_do_personagem == "olhar guardaroupa" or ação_do_personagem == "olhar o guardarroupas" or ação_do_personagem == "olha o guardarroupas" or ação_do_personagem == "olha o guardarroupa" or ação_do_personagem == "olhar o guardarroupa" or ação_do_personagem == "olhar guardarroupas" or ação_do_personagem == "olha guardarroupas" or ação_do_personagem == "olha guardarroupa" or ação_do_personagem == "olhar guardarroupa" or ação_do_personagem == "guarda-roupa" or ação_do_personagem == "guarda-roupas" or ação_do_personagem == "guarda roupa" or ação_do_personagem == "guarda roupas" or ação_do_personagem == "guardaroupa" or ação_do_personagem == "guardaroupas" or ação_do_personagem == "guardarroupa" or ação_do_personagem == "guardarroupas" or ação_do_personagem == "olhar o armário" or ação_do_personagem == "olhar o armario" or ação_do_personagem == "olhar armário" or ação_do_personagem == "olhar armario" or ação_do_personagem == "olha o armário" or ação_do_personagem == "olha o armario" or ação_do_personagem == "olha armário" or ação_do_personagem == "olha armario" or ação_do_personagem == "armário" or ação_do_personagem == "armario" or ação_do_personagem == "sair do armário" or ação_do_personagem == "vestir smoking" or ação_do_personagem == "ver armário" or ação_do_personagem == "ver o armário" or ação_do_personagem == "ver armario" or ação_do_personagem == "ver o armario" or ação_do_personagem == "ver o guarda-roupas" or ação_do_personagem == "ver o guardarroupas" or ação_do_personagem == "ver o guarda roupas" or ação_do_personagem == "ver o guardaroupas" or ação_do_personagem == "ver o guarda-roupa" or ação_do_personagem == "ver o guardarroupa" or ação_do_personagem == "ver o guarda roupa" or ação_do_personagem == "ver o guardaroupa" or ação_do_personagem == "ver guarda-roupas" or ação_do_personagem == "ver guardarroupas" or ação_do_personagem == "ver guarda roupas" or ação_do_personagem == "ver guardaroupas" or ação_do_personagem == "ver guarda-roupa" or ação_do_personagem == "ver guardarroupa" or ação_do_personagem == "ver guarda roupa" or ação_do_personagem == "ver guardaroupa"):
                                        if(objeto[0]=="ganha presente"):
                                            print("Você encontrou uma bela caixa de presente.")
                                            time.sleep(2)
                                            print("Vai abrir?(sim ou não)")
                                            while 1:
                                                ação_do_personagem = input("-")
                                                ação_do_personagem = ação_do_personagem.lower()
                                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                    print("Você desembalou a caixa de presente e...")
                                                    time.sleep(3)
                                                    print("Encontrou um par de Papetes Masculinas!\n")
                                                    time.sleep(1)
                                                    print("Você guardou as Papetes Masculinas na sua mochila!")
                                                    time.sleep(2)
                                                    item_adicionado=papetes_masculinas
                                                    quantidade_adicionada=1
                                                    adicionaItem()
                                                    objeto[0] = "não"
                                                    break
                                                else:
                                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                        break
                                                    else:
                                                        print('Entrada Inválida! Digite "sim" ou "não".')
                                                        time.sleep(0.5)
                                        else:
                                            print("Você não vê muitas roupas... Você é muito pobre, arrume um emprego!\n")
                                            time.sleep(1)
                                    else:
                                        if (ação_do_personagem == "olhar a janela"):###__EASTER-EGG
                                            if (eegg == 1):
                                                print("Você vê...")
                                                time.sleep(3.5)
                                                print("Você vê uma janela, sua anta!")
                                                time.sleep(0.5)
                                                print("... Hunf...")
                                                time.sleep(0.5)
                                                print("Volte para as aulas de ortografia!")
                                                time.sleep(0.5)
                                                print("...")
                                                time.sleep(2)
                                                print("O quê? Você acha que eu fui muito grosso?")
                                                time.sleep(1)
                                                print("Okay, ", personagem_jogador[0],", vamos lá...")
                                                time.sleep(2.5)
                                                print("Há uma diferença muito grande entre olhar A janela e olhar PELA janela!")
                                                time.sleep(3)
                                                print("Tente mais uma vez, sua anta!")
                                                time.sleep(0.5)
                                                eegg = 2
                                            else:
                                                if (eegg == 2):
                                                    print("Digitando errado MAIS UMA VEZ?!")
                                                    time.sleep(0.5)
                                                    print("Okay, ", personagem_jogador[0],", você já está passando dos limites da burrice...")
                                                    time.sleep(1)
                                                    eegg = 3
                                                else:
                                                    if (eegg == 3):
                                                        print("Você encara a janela...")
                                                        time.sleep(1)
                                                        print("Você parece um retardado fazendo isso...")
                                                        time.sleep(0.5)
                                                        eegg = 4
                                                    else:
                                                        if (eegg == 4):
                                                            print('Enquanto você encarava a janela um pombo pousou nela...')
                                                            time.sleep(1)
                                                            print('Ele olhou bem no fundo dos seus olhos e disse "Você é um idiota."...')
                                                            time.sleep(1)
                                                            print('Não, ele não disse isso... Na verdade fui eu quem disse isso, seu idiota.')
                                                            time.sleep(1)
                                                            eegg = 5
                                                        else:
                                                            if (eegg == 5):
                                                                print("Já chega! Você esgotou minha paciência!")
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
                                                                    print("Okay, você venceu... Mas pare de me irritar!")
                                                                    time.sleep(1)
                                                                    eegg = 6
                                                            else:
                                                                if (eegg == 6):
                                                                    print("...")
                                                                    time.sleep(0.5)
                                                                    eegg = 7
                                                                else:
                                                                    print("Você vê uma janela que abre horizontalmente para as duas direções,")
                                                                    time.sleep(0.5)
                                                                    print("sendo que o vidro da janela esquerda está rachado por, provavelmente, um apedrejamento.")
                                                                    time.sleep(1)
                                                                    print("Os batentes são de madeira antiga, deteriorada pela ação de cupins.")
                                                                    time.sleep(0.5)
                                        else:
                                            if (ação_do_personagem == "olhar pela janela" or ação_do_personagem == "olha pela janela" or ação_do_personagem == "janela" or ação_do_personagem ==  "olhar janela" or ação_do_personagem == "olha janela" or ação_do_personagem=="ver janela" or ação_do_personagem=="ver a janela"):
                                                print("Você vê uma rua com prédios de classe baixa,")
                                                time.sleep(3)
                                                print("poucas pessoas passando com cara de cansadas,")
                                                time.sleep(3)
                                                print("mas você não consegue ver o horizonte,")
                                                time.sleep(3)
                                                print("já que você mora no primeiro andar e os prédios do outro")
                                                time.sleep(4)
                                                print("lado da rua são altos e próximos demais uns dos outros.")
                                                time.sleep(4)
                                                print("Você percebe um sujeito te encarando do outro lado da rua...")
                                                time.sleep(4)
                                                print("Ele está em pé e encostado na grade cinza, empoeirada e enferrujada")
                                                time.sleep(4)
                                                print("do prédio da frente um pouco à esquerda da porta dessa grade,")
                                                time.sleep(4)
                                                print("de modo a ficar de frente para a porta do seu prédio.")
                                                time.sleep(3)
                                                print("Sua face cheia de raiva expressa com rigidez a sua intenção,")
                                                time.sleep(3)
                                                print("sua jeans é velha, sua camisa é rasgada de forma a parecer uma regata,")
                                                time.sleep(3)
                                                print("enquanto seus braços cruzados parecem prontos para uma briga!")
                                                time.sleep(5)
                                            else:
                                                if (ação_do_personagem == "olhar a estante" or ação_do_personagem =="ohar a estante" or ação_do_personagem =="ohar estante" or ação_do_personagem == "olhar estante" or ação_do_personagem == "olha a estante" or ação_do_personagem == "olha estante" or ação_do_personagem == "estante" or ação_do_personagem == "ver a estante" or ação_do_personagem == "ver estante" or ação_do_personagem == "ver a estante" or ação_do_personagem == "ver estante" or ação_do_personagem =="olahr a estante"):
                                                    print("Você vê livros e apostilas rabiscadas na capa e a maioria rasgadas no canto dos furos das espirais.\n...\n Nada muito interessante...\n")
                                                    time.sleep(1)
                                                    print("Mas você vê um pedaço de papel vermelho colocado entre as páginas de um dos livros...")
                                                    time.sleep(1)
                                                    print("Ler o bilhete??\n")
                                                    while 1:
                                                        ação_do_personagem=input("-")
                                                        ação_do_personagem=ação_do_personagem.lower()
                                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                            print(' "       Você pode digitar seus comandos de outras formas, como por exemplo,')
                                                            time.sleep(3)
                                                            print("ao invés de digitar 'ver ficha do personagem' você pode simplesmente digitar 'ficha'!")
                                                            time.sleep(3)
                                                            print('Tente sempre digitar da forma mais simples, isso facilitará muito o seu jogo!')
                                                            time.sleep(3)
                                                            print('Não custa nada tentar! ;)')
                                                            time.sleep(3)
                                                            print('                               assinado: Programador "')
                                                            break
                                                        else:
                                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                print("Você ignorou o bilhete.")
                                                                time.sleep(1)
                                                                break
                                                            else:
                                                                print('Entrada inválida! Digite "sim" ou "Não"')
                                                else:
                                                    if (ação_do_personagem == "destruir o universo"): #Easter-Egg para o Yuri
                                                        print("Adeus...")
                                                        time.sleep(0.5)
                                                        while 1:
                                                            ação_do_personagem = input("")
                                                            ação_do_personagem = ação_do_personagem.lower()
                                                            if(ação_do_personagem=="reconstruir o universo" or ação_do_personagem == "construir o universo" or ação_do_personagem == "criar um novo universo" or ação_do_personagem == "construir um universo" or ação_do_personagem == "criar o universo"):
                                                                break
                                                        print("Olá!")
                                                        time.sleep(1)
                                                    else:
                                                        if(ação_do_personagem=="sair do quarto" or ação_do_personagem=="sair" or ação_do_personagem=="ir para a aula" or ação_do_personagem=="ir pra aula" or ação_do_personagem=="ir para aula" or ação_do_personagem=="ir à aula" or ação_do_personagem=="ir a aula" or ação_do_personagem=="sair quarto"):
                                                            while 1:
                                                                print("Se sair você nao poderá voltar.\n")
                                                                time.sleep(3)
                                                                print("Tem certeza que deseja sair? (sim ou não)")
                                                                ação_do_personagem=input("-")
                                                                ação_do_personagem=ação_do_personagem.lower()
                                                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                    ação_do_personagem="sim"
                                                                    break
                                                                else:
                                                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                        print("Você decidiu não sair do quarto.")
                                                                        time.sleep(1)
                                                                        break
                                                                    else:
                                                                        print("Entrada inválida!")
                                                                        time.sleep(1)
                                                            if(ação_do_personagem=="sim"):
                                                                break
                                                        else:
                                                            if(ação_do_personagem=="ver a bolsa" or ação_do_personagem=="ver inventário" or ação_do_personagem=="ver o inventário" or ação_do_personagem=="ver bolsa" or ação_do_personagem=="ver mochila" or ação_do_personagem=="ver mala" or ação_do_personagem=="ver a mochila" or ação_do_personagem=="ver a mala" or ação_do_personagem=="inventário" or ação_do_personagem=="inventario" or ação_do_personagem=="iventario" or ação_do_personagem=="iventário" or ação_do_personagem=="mochila" or ação_do_personagem=="mochla" or ação_do_personagem=="mala" or ação_do_personagem=="bolsa" or ação_do_personagem=="itens" or ação_do_personagem=="ítens" or ação_do_personagem=="item"):
                                                                inventárioPersonagem()
                                                            else:
                                                                print('\nEntrada Inválida!\n')
                print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar)
                time.sleep(0.23)
                print("\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
                time.sleep(0.23)
                if (variável_cenário[0] == "sim"):
                    print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\n\nolhar pela janela\n")
                    time.sleep(0.5)
                print("\nver ficha do personagem\nver mochila\nsair do quarto\n")
                time.sleep(0.5)
                if(eegg > 1 and eegg<6):
                    print("\nVocê não deve:\nolhar a janela\n")
                    time.sleep(0.23)
                print("\n#", "-"*30,"#\n")
                print("\nE agora, ", personagem_jogador[0],", o que você vai fazer?\n")
                ação_do_personagem = input("-")
                ação_do_personagem = ação_do_personagem.lower()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 1
            variável_cenário[1] = "não"
            variável_cenário[0] = "não"
            print("Você saiu do seu quarto.")
            time.sleep(1)
            save()

##########--------------------------------------------------FIM DA PRIMEIRA PARTE--------------------------------------------------##########
        if(ponto_de_save==1):
            if(variável_lugar == "seu prédio, 1º andar" or variável_lugar == "seu prédio, 2º andar" or variável_lugar == "seu prédio, 3º andar" or variável_lugar == "seu prédio, 4º andar"):
                if(variável_lugar == "seu prédio, 1º andar"):
                    variável_lugar = "seu prédio, 1º andarb"
                if(variável_lugar == "seu prédio, 2º andar"):
                    variável_lugar = "seu prédio, 2º andarb"
                if(variável_lugar == "seu prédio, 3º andar"):
                    variável_lugar = "seu prédio, 3º andarb"
                if(variável_lugar == "seu prédio, 4º andar"):
                    variável_lugar = "seu prédio, 4º andarb"
                seuPrédioPrimeiroAndar()
            else:
                print("\nCenário: Você continua atrasado para a aula - não que você deva se importar muito com isso.")
                time.sleep(2)
                variável_lugar = "seu prédio, 1º andar"
                seuPrédioPrimeiroAndar()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 2
            variável_lugar = "em frente ao seu prédio"
            save()


##########--------------------------------------------------FIM DA SEGUNDA PARTE--------------------------------------------------##########
        if(ponto_de_save==2):
            print("\nCenário:Agora você está na sua rua.\n\n")
            time.sleep(2)
            print("Antes que você pudesse fazer alguma coisa,")
            time.sleep(3)
            print("foi abordado por um homem aparentemente forte vestindo uma jeans velha")
            time.sleep(3)
            print("e uma camisa que foi rasgada de forma a parecer uma regata...\n")
            time.sleep(3)
            print("Seu rosto era magro, de tão afundadas que as bochechas eram, parecia uma caveira,")
            time.sleep(3)
            print("sua pele queimada pelo Sol era cheia de manchas, seu cabelo crespo crescia por cima das ventas,")
            time.sleep(3)
            print("mas a calvisse da sua fronte se extendia até a ponta extrema da sua arredondada e fosca cabeça...\n")
            time.sleep(3)
            print(" - Cadê o dinheiro que você roubou do meu esquema?\n")
            time.sleep(2)
            print("Mas você REALMENTE não sabia de esquema algum, quanto menos do dinheiro...\n")
            time.sleep(3)
            print("Algo não parece certo...\n")
            time.sleep(1)
            print(" - Não adianta negar!!! Escolhe, moleque: a grana ou a vida???\n")
            time.sleep(1)
            print("...")
            time.sleep(3)
            print("Ele saca uma faca do bolso de trás!\n")
            time.sleep(2)
            print(" - EU VOU TE QUEBRAR ATÉ VOCÊ ME DAR O DINHEIRO!!!\n")
            time.sleep(2)
            personagem_inimigo = [ "Bandido", 300, 100, 20, 20, 25000, 25000]
            batalha()
            if(personagem_jogador[6]<=0):
                personagem_jogador[6]=1
                print("Você caiu no chão...")
                time.sleep(3)
                print("Ajoelhado na sua barriga e com o antebraço apoiado no seu pescoço")
                print("o bandido abriu um largo e amargo sorriso enquanto te fitava com seu olhar insano!")
                time.sleep(4)
                print(" - HAHAHAHA! Você vai morrer!")
                time.sleep(3)
                print("Você esta rendido...")
                time.sleep(4)
                print("Com a outra mão ergueu a faca apontada para o seu peito!")
                time.sleep(3)
                print("...")
                time.sleep(5)
                print("!!!")
                time.sleep(3)
                print("O bandido foi violentamente atingido por um soco...")
                time.sleep(4)
                print("Você se levantou rapidamente e pôde, então, observar a sitiuação...")
                time.sleep(3)
                print("Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,")
                time.sleep(5)
                print("uma calça preta rasgada nos joelhos e um all-star preto,")
                time.sleep(5)
                print("além da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titânio.")
                time.sleep(6)
                personagem_reserva = personagem_jogador
                personagem_jogador = [ "Lutador Headbanger", 1200, 800, 50, 50, 100000, 100000,0]
                batalha()
                personagem_jogador = personagem_reserva
                print(" - Pare! Por favor!\n")
                time.sleep(3)
                print("...")
                time.sleep(3)
                print("Antes que você e o Headbanger pudessem perceber o som da moto, um comparsa o resgatou...")
                time.sleep(3)
                print("O Headbanger se virou e olhou para você.")
                time.sleep(3)
                print(" - Você é fraco demais, mas tem muito potencial.")
                time.sleep(3)
                print(" - Não sei o que você fez para eles, mas você parece precisar de ajuda.")
                time.sleep(3)
                print(" - Vou procurar saber o que está acontecendo... Faça o mesmo, você também!")
                time.sleep(3)
                print(" - Ele sumiu pelos becos da rua...")
                time.sleep(3)
                print("Voce continua sem respostas...")
                time.sleep(3)
                print("Será que você encontrará alguma pista na escola?")
                time.sleep(5)
            else:
                if(personagem_inimigo[6]>0):
                    while(personagem_inimigo[6]>0):
                        print("Você correu um pouco mas ele te alcançou de novo!\n")
                        batalha()
                        if(personagem_jogador[6]<=0):
                            personagem_jogador[6]=1
                            print("Você caiu no chão...")
                            time.sleep(3)
                            print("Ajoelhado na sua barriga e com o antebraço apoiado no seu pescoço")
                            print("o bandido abriu um largo e amargo sorriso enquanto te fitava com seu olhar insano!")
                            time.sleep(4)
                            print(" - HAHAHAHA! Você vai morrer!")
                            time.sleep(3)
                            print("Você esta rendido...")
                            time.sleep(4)
                            print("Com a outra mão ergueu a faca apontada para o seu peito!")
                            time.sleep(3)
                            print("...")
                            time.sleep(5)
                            print("!!!")
                            time.sleep(3)
                            print("O bandido foi violentamente atingido por um soco...")
                            time.sleep(4)
                            print("Você se levantou rapidamente e pôde, então, observar a sitiuação...")
                            time.sleep(3)
                            print("Ele vestia uma blusa preta com a capa do The Rules of Hell do Black Sabbath estampada em cinza nela,")
                            time.sleep(5)
                            print("uma calça preta rasgada nos joelhos e um all-star preto,")
                            time.sleep(5)
                            print("além da jaqueta de couro, luvas, pulseiras e cinto, todos esses ultimos com spikes de titânio.")
                            time.sleep(6)
                            personagem_reserva = personagem_jogador
                            personagem_jogador = [ "Lutador Headbanger", 1200, 800, 50, 50, 100000, 100000, 0]
                            batalha()
                            personagem_jogador = personagem_reserva
                            print(" - Pare! Por favor!\n")
                            time.sleep(3)
                            print("...")
                            time.sleep(3)
                            print("Antes que você e o Headbanger pudessem perceber o som da moto, um comparsa o resgatou...")
                            time.sleep(3)
                            print("O Headbanger se virou e olhou para você.")
                            time.sleep(3)
                            print(" - Você é fraco demais, mas tem muito potencial.")
                            time.sleep(3)
                            print(" - Não sei o que você fez para eles, mas você parece precisar de ajuda.")
                            time.sleep(3)
                            print(" - Vou procurar saber o que está acontecendo... Faça o mesmo, você também!")
                            time.sleep(3)
                            print(" - Ele sumiu pelos becos da rua...")
                            time.sleep(3)
                            print("Voce continua sem respostas...")
                            time.sleep(3)
                            print("Será que você encontrará alguma pista na escola?")
                            time.sleep(5)
                        else:
                            print(" - Pare! Por favor!\n")
                            time.sleep(3)
                            print("...")
                            time.sleep(3)
                            print("Antes que você pudesse perceber o som da moto, um comparsa o resgatou...")
                            time.sleep(3)
                            print("Voce continua sem respostas...")
                            time.sleep(3)
                            print("Será que você encontrará alguma pista na escola?")
                            time.sleep(5)
                else:
                    print(" - Pare! Por favor!\n")
                    time.sleep(3)
                    print("...")
                    time.sleep(3)
                    print("Você escuta um som de moto ao fundo...")
                    time.sleep(3)
                    print("Um comparsa motoqueiro tentou te atropelar, mas você conseguiu executar uma evasão rolando para a calçada!")
                    time.sleep(3)
                    print(" - Agora você vai entregar o dinheiro, ou não vai?! - inqueriu, o motoqueiro montado em sua Twister 250.")
                    time.sleep(3)
                    personagem_inimigo = [ "Motoqueiro Comparsa", 3000, 10, 50, -5, 50, 50]
                    batalha()
                    if(personagem_jogador[6]<=0): break
                    if(personagem_inimigo[6]>0):
                        print("Correndo entre uns becos da sua rua, você conseguiu se esconder...")
                        time.sleep(2)
                        print("...")
                        time.sleep(2)
                        print("...")
                        time.sleep(2)
                        print("Você conseguiu despitá-los...")
                        time.sleep(2)
                    else:
                        print("Você derrotou os dois!")
                        time.sleep(2)
                        print("Eles estão desmaiados na rua...")
                        time.sleep(2)
                        print("Mas antes que você pudesse pensar em algo, o barrulho de várias sirenes te alertou!")
                        time.sleep(2)
                        print("Você se escondeu em um dos becos, mas pode assistir os policiais prendendo os dois bandidos...")
                        time.sleep(2)
                        print("Você conseguiu se manter escondido até a cena esfriar, mas continua sem respostas...")
                        time.sleep(2)
            ponto_de_save = 3
            variável_lugar = "sua rua"
            save()

##########--------------------------------------------------FIM DA TERCEIRA PARTE--------------------------------------------------##########
        if(ponto_de_save==3):
            if(variável_lugar == "seu prédio, 1º andar" or variável_lugar == "seu prédio, 2º andar" or variável_lugar == "seu prédio, 3º andar" or variável_lugar == "seu prédio, 4º andar"):
                if(variável_lugar == "seu prédio, 1º andar"):
                    variável_lugar = "seu prédio, 1º andarb"
                if(variável_lugar == "seu prédio, 2º andar"):
                    variável_lugar = "seu prédio, 2º andarb"
                if(variável_lugar == "seu prédio, 3º andar"):
                    variável_lugar = "seu prédio, 3º andarb"
                if(variável_lugar == "seu prédio, 4º andar"):
                    variável_lugar = "seu prédio, 4º andarb"
                seuPrédioPrimeiroAndar()
                variável_lugar = "sua rua"
            else:
                print("Cenário:Você está na sua rua, por agora tudo está calmo....")
                suaRua()
            if(personagem_jogador[6]<=0):break
            ponto_de_save = 4
            save()

##########--------------------------------------------------FIM DO JOGO--------------------------------------------------##########
        break
    if (personagem_jogador[6] <= 0):
        print("Você morreu, ", personagem_jogador[0], "...\nO jogo acabou para você...")
        #"Nome"[0], atq[1], def[2], agi[3], luk[4], vidamáxima[5], vidaatual[6], dinheiro[7]
        personagem_jogador = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
        personagem_reserva = [ "Jogador", 10, 8, 1, 1, 100, 100, 0]
        personagem_inimigo = [ "Inimigo", 10, 8, 1, 1, 100, 100]

        #["Nome"[0], atq[1], def[2], agi[3], luk[4], tipo[5], preço[6], recupera[7]

        desequipado_roupa = ["Nada", 0, 0, 0, 0, "roupa", 0, 0]
        desequipado_capa = ["Nada", 0, 0, 0, 0, "capa", 0, 0]
        desequipado_luva = ["Nada", 0, 0, 0, 0, "luva", 0, 0]
        desequipado_anel = ["Nada", 0, 0, 0, 0, "anel", 0, 0]
        desequipado_maos = ["Nada", 0, 0, 0, 0, "armamento", 0, 0]
        desequipado_calcado = ["Nada", 0, 0, 0, 0, "calçados", 0, 0]
        espaço_vazio = ["Vazio", 0, 0, 0, 0, "inventário", 0, 0]

        pedaço_pizza = ["Pedaço de Pizza", 0, 0, 0, 0, "consumível", 5, 50]
        bolo_chocolate = ["Bolo de Chocolate", 0, 0, 0, 0, "consumível", 100, personagem_jogador[5]]

        pijama_inicial = ["Pijama", 0, 0, 0, 5, "roupa", 5, 0]
        uniforme_estudantil = ["Uniforme Estudantil",0,1,0,0,"roupa",5,0]
        malha_ninja = ["Malha Ninja", 5, 20, 5, 1, "roupa", 5000, 0]

        lapis_apontado = ["Lápis Apontado", 3,0,0,1,"armamento",2,0]
        punhal_envelhecido = ["Punhal Envelhecido", 10, 0,0,3,"armamento",300,0]
        talheres_prata = ["Talheres de prata(Garfo e Faca)", 8, 0,0,0,"armamento",10,0]

        jaqueta_imitação = ["Jaqueta de Imitação de Couro", 0, 20, 0, 0,"capa",150,0]
        jaqueta_couro = ["Jaqueta de Couro", 0, 200, 0, 10,"capa",2000,0]
        agasalho_lã = ["Agasalho de Lã", 0, 6, 0, 0,"capa",100,0]

        suplemento_alimentício = ["Suplemento Alimentício", 10, 0, 0, 0, "consumível de aprimoramento",5, 0]
        lata_energético = ["Energético", 0, 0, 0, 0, "consumível de aprimoramento",5, 50]

        luva_lã = ["Luvas de Lã", 0, 3, 0, 0, "luva", 20, 0]
        luva_imitação = ["Luvas de Imitação de Couro", 3, 3, 0, 0, "luva", 100, 0]
        soco_pvc = ["Soco-Inglês de PVC", 3, 0, 0, 0, "luva", 50, 0]
        luva_couro = ["Luvas de Couro", 8, 8, 0, 0, "luva", 500, 0]
        soco_latão = ["Soco-Inglês de Latão", 10, 0, 0, 0, "luva", 500, 0]
        luva_spikes_alu = ["Luvas de Couro com Spikes de Aluminio", 15, 15, 0, 0, "luva", 700, 0]
        soco_alu = ["Soco-Inglês de Alumínio", 25, 0, 0, 0, "luva", 700, 0]
        luva_spikes_aço = ["Luvas de Couro com Spikes de Aço", 25, 25, 0, 0, "luva", 1000, 0]
        soco_aço = ["Soco-Inglês de Alumínio de Aço", 30, 0, 0, 0, "luva", 1000, 0]
        luva_spikes_ag = ["Luvas de Couro com Spikes de Prata", 25, 25, 0, 5, "luva", 5000, 0]
        soco_ag = ["Soco-Inglês de Prata", 35, 0, 0, 5, "luva", 5000, 0]
        luva_spikes_au = ["Luvas de Couro com Spikes de Ouro", 250, 250, 0, 10, "luva", 10000, 0]
        soco_au = ["Soco-Inglês de Ouro", 350, 0, 0, 10, "luva", 10000, 0]
        luva_spikes_titânio = ["Luvas de Couro com Spikes de Titânio", 2500, 2500, 0, 20, "luva", 50000, 0]
        soco_titânio = ["Soco-Inglês de Titânio", 3500, 0, 0, 20, "luva", 50000, 0]

        anel_força1 = ["Anel da Força 1", 10, -2, -2, -2, "anel", 500, 0]
        anel_resistência1 = ["Anel da Resistência 1", -2, 10, -2, -2, "anel", 500, 0]
        anel_força2 = ["Anel da Força 2", 20, -4, -4, -4, "anel", 1000, 0]
        anel_resistência2 = ["Anel da Resistência 2", -4, 20, -4, -4, "anel", 1000, 0]
        anel_força3 = ["Anel da Força 2", 40, -8, -8, -8, "anel", 5000, 0]
        anel_resistência3 = ["Anel da Resistência 2", -8, 40, -8, -8, "anel", 5000, 0]

        anel_consistência1 = ["Anel da Consistência 1", -2, -2, -2, -2, "anel", 500, 10]
        anel_consistência2 = ["Anel da Consistência 2", -4, -4, -4, -4, "anel", 1000, 100]
        anel_consistência3 = ["Anel da Consistência 3", -8, -8, -8, -8, "anel", 5000, 1000]

        anel_da_imortalidade = ["Anel da Imortalidade", personagem_jogador[1], personagem_jogador[2], personagem_jogador[3], personagem_jogador[4], "anel", 100000, personagem_jogador[5]]
        anel_da_divindade = ["Anel da Divindade", personagem_jogador[1]*2, personagem_jogador[2]*2, personagem_jogador[3]*2, personagem_jogador[4]*2, "anel", 100000000, personagem_jogador[5]*2]

        chinelo_inicial = ["Chinelos", 0, 0, 0, -5, "calçados", 5, 0]
        papetes_masculinas = ["Papetes Masculinas", 0, 0, 1, 0, "calçados", 15, 0]
        tênis_velho = ["Tênis Velho", 0, 0, 2, 0, "calçados", 10, 0]
        tênis_simplório = ["Tênis Simplório", 0, 1, 2, 0, "calçados", 50, 0]
        sapato_simplório = ["Sapato Simplório", 0, 2, 1, 0, "calçados", 50, 0]
        tênis_comum = ["Tênis Comum", 0, 2, 2, 0, "calçados", 90, 0]
        tênis_trilha = ["Tênis de Trilha", 2, 8, 3, 0, "calçados", 400, 0]
        tênis_caminhada = ["Tênis de Caminhada", 0, 3, 5, 0, "calçados", 300, 0]
        tênis_corrida = ["Tênis de Corrida", 0, 5, 10, 0, "calçados", 500, 0]
        tênis_ZX5000 = ["Tênis ZX-5000", 10, 10, 11, 5, "calçados", 15000, 0]

        item_adicionado=espaço_vazio
        quantidade_adicionada=1

        equipado_roupa = pijama_inicial
        equipado_capa = desequipado_capa
        equipado_luva = desequipado_luva
        equipado_anel = desequipado_anel
        equipado_maos = desequipado_maos
        equipado_calcado = chinelo_inicial

        variável_cenário = ["não" ,"não" ,"não"]
        #[0]  olhar cenário primeira vez no seu quarto e reciclada no primeiro andar do seu prédio
        #[1]  modificar cenário primeira vez no seu quarto
        #[2]  cheirar cenário no primeiro andar do seu prédio

        objeto = ["não", "não", "não", "não", "não"]
        #[0]  presente do tutorial e reciclada no bêbado do 1ºandar
        #[1]  porta do quarto 10
        #[2]  energético do bêbado (ação revistar)
        #[3]  arrombar porta do quarto 10
        #[4]  mulher do bêbado - talheres de prata

        situação = [0  ,0,0,0 ,0,0  ,0,0,0 ,0,0]
        #[0]  dois últimos andares do seu prédio
        #[1]  quarto 11 do seu prédio
        #[2]  quarto 24 do seu prédio
        #[3]  quarto 21 do seu prédio
        #[4]  quarto 22 do seu prédio
        #[5]  quarto 30 do seu prédio
        #[6]  quarto 31 do seu prédio
        #[7]  quarto 32 do seu prédio
        #[8]  quarto 33 do seu prédio
        #[9]  quarto 34 do seu prédio
        #[10] quarto 20 do seu prédio

        temporário = [False, False]
        #[0]  verifica se pegou o uniforme no seu quarto depois é reciclada para verificar se já venceu o terceiro andar do seu prédio
        #[1]  verifica se pegou o soco inglês no seu quarto depois é reciclada para verificar se 

        variável_lugar = "seu quarto"
        ponto_de_save = 0

        mostrar_save = ''

        eegg = 1

        ação_do_personagem = "" 
        batalha_escapar = ""

        teste_de_sorte = 0
        calculo_do_dano = 0
        calculo_da_fuga = 0
        variável_para_comparar = 0
        contador_de_batalha= 0
        contador_de_rodadas = 0


        #global desequipado_roupa,desequipado_capa,desequipado_luva,desequipado_maos,desequipado_calcado,espaço_vazio,pedaço_pizza,bolo_chocolate,pijama_inicial,uniforme_estudantil,malha_ninja,lapis_apontado,punhal_envelhecido,talheres_prata,jaqueta_imitação,jaqueta_couro,agasalho_lã,suplemento_alimentício,lata_energético,luva_lã,luva_couro,soco_pvc,soco_latão,luva_spikes_alu,soco_alu,luva_spikes_aço,soco_aço,luva_spikes_ag,soco_ag,luva_spikes_au,soco_au,luva_spikes_titânio,soco_titânio,anel_força1,anel_força2,anel_força3,anel_resistência1,anel_resistência2,anel_resistência3,anel_consistência1,anel_consistência2,anel_consistência3,anel_da_imortalidade,anel_da_divindade,chinelo_inicial,papetes_masculinas,tênis_velho,tênis_simplório,sapato_simplório,tênis_comum,tênis_trilha,tênis_caminhada,tênis_corrida,tênis_ZX5000,item_adicionado,quantidade_adicionada,equipado_roupa,equipado_capa,equipado_luva,equipado_anel,equipado_maos,equipado_calcado,variável_cenário,objeto,situação,temporário,variável_lugar,ponto_de_save,mostrar_save, personagem_jogador,personagem_reserva,personagem_inimigo,eegg,ação_do_personagem,batalha_escapar,teste_de_sorte,calculo_do_dano,calculo_da_fuga,variável_para_comparar,contador_de_batalha,contador_de_rodadas,mala,loja_venda

        mala = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio]
        loja_venda = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio,espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio, espaço_vazio]

    else:
        print("\nParabéns, ", personagem_jogador[0],"!!! Você terminou o jogo!!!")
    print("\nVocê deseja jogar novamente, ", personagem_jogador[0],'?("sim" ou "não")\n')
    while 1:
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
            input("\nReiniciando...(APERTE ENTER)\n")
            break
        else:
            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                break
            else:
                print('\nEntrada inválida!(digite "sim" ou "não)\n')
    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
        break
    
exit()
