#--Import--#
#use o python 2.7.4 que é coisa de macho!!!!!!11!!!!!1!!onze!!!! - Lucas Sabião
import random
import configparser
import pickle
import time

#ASSISTA DEVIL SURVIVOR 2

#--Variáveis de Texto--#
nome_do_jogador = "Jogador"
nome_do_inimigo = "Inimigo"
reserva_nome_do_jogador = ""
ação_do_personagem = "" 
batalha_escapar = ""
equipamento_roupa = "Pijama"
equipamento_capa = "Nada"
equipamento_luva = "Nada"
equipamento_mãos = "Nada"
equipamento_botas = "Chinelos"
olhar_o_cenário = "não"
modificar_o_cenário = "não"
cheirar_o_cenário = "não"
objeto_00 = "não" #presente do tutorial e depois passar a ser o bêbado do 1ºandar
objeto_01 = "não" #porta do quarto 10
objeto_02 = "não" #energético do bêbado (ação revistar)
objeto_03 = "não" #
variável_lugar = "seu quarto"
mostrar_save = ''
temporário= False

#--Variáveis de Número--#
ponto_de_save = 0
eegg = 1
vida_máxima_personagem = 100
vida_atual_personagem = 100
dinheiro_do_personagem = 0
ataque_do_personagem = 10
defesa_do_personagem = 8
agilidade_do_personagem = 1
reserva_vida_máxima_personagem = 100
reserva_vida_atual_personagem = 100
reserva_ataque_do_personagem = 10
reserva_defesa_do_personagem = 8
reserva_agilidade_do_personagem = 1
vida_máxima_inimigo = 30
vida_atual_inimigo = 30
ataque_do_inimigo = 5
defesa_do_inimigo = 5
situação_00 = 0 #dois últimos andares do seu prédio
situação_01 = 0 #quarto 11 do seu prédio
situação_02 = 0 #quarto 24 do seu prédio
situação_03 = 0 #quarto 21 do seu prédio
situação_04 = 0 #quarto 22 do seu prédio
situação_05 = 0 #quarto 30 do seu prédio
situação_06 = 0 #quarto 31 do seu prédio
situação_07 = 0 #quarto 32 do seu prédio
situação_08 = 0 #quarto 33 do seu prédio
situação_09 = 0 #quarto 34 do seu prédio
situação_10 = 0 #quarto 20 do seu prédio
teste_de_sorte = 0
calculo_do_dano = 0
calculo_da_fuga = 0
variável_para_comparar = 0
contador_de_batalha= 0
contador_de_rodadas = 0
#global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas

def lojaPadrão():
    print(" - Olá, meu jovem! Em que posso ajudá-lo?\n")
    time.sleep(5)

#--Ficha do Personagem--#
def ficha_personagem():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas
    print("\n#", "-"*30,"#\n", "\nNome:", nome_do_jogador)
    time.sleep(0.23)
    print("\nVida:", vida_atual_personagem, "de", vida_máxima_personagem)
    time.sleep(0.23)
    print("\nAtaque:", ataque_do_personagem, "\nDefesa:", defesa_do_personagem, "\nAgilidade:", agilidade_do_personagem)
    time.sleep(0.23)
    print("\nCapa:", equipamento_capa, "\nRoupa:", equipamento_roupa, "\nCalçados:", equipamento_botas,)
    time.sleep(0.23)
    print("\nLuvas:" ,equipamento_luva,"\nArmamento:", equipamento_mãos)
    time.sleep(0.23)
    print("\nDinheiro:", dinheiro_do_personagem, "Reais\n")
    time.sleep(0.23)
    print("\n#", "-"*30,"#\n")
    time.sleep(0.23)

#--Save--#
def save():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas
    ficha_personagem()
    print('\nDeseja salvar seu progresso?("sim" ou "não")\n')
    while 1:
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
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
                ação_do_personagem=input("-")
                if(ação_do_personagem=="0"):
                    arq = open('\espaço_save00.py', 'wb')
                    break
                else:
                    if(ação_do_personagem=="1"):
                        arq = open('\espaço_save01.py', 'wb')
                        break
                    else:
                        if(ação_do_personagem=="2"):
                            arq = open('\espaço_save02.py', 'wb')
                            break
                        else:
                            if(ação_do_personagem=="3"):
                                arq = open('\espaço_save03.py', 'wb')
                                break
                            else:
                                if(ação_do_personagem=="4"):
                                    arq = open('\espaço_save04.py', 'wb')
                                    break
                                else:
                                    if(ação_do_personagem=="5"):
                                        arq = open('\espaço_save05.py', 'wb')
                                        break
                                    else:
                                        if(ação_do_personagem=="6"):
                                            arq = open('\espaço_save06.py', 'wb')
                                            break
                                        else:
                                            if(ação_do_personagem=="7"):
                                                arq = open('\espaço_save07.py', 'wb')
                                                break
                                            else:
                                                if(ação_do_personagem=="8"):
                                                    arq = open('\espaço_save08.py', 'wb')
                                                    break
                                                else:
                                                    if(ação_do_personagem=="9"):
                                                        arq = open('\espaço_save09.py', 'wb')
                                                        break
                                                    else:
                                                        print("Entrada inválida!\n")
            #recomendo você usar um for aqui :) - Lucas Sabiao
            mostrar_save = ("  Nome:", nome_do_jogador, "  Vida:", vida_máxima_personagem,"  Lugar:", variável_lugar, "  Ataque:", ataque_do_personagem, "  Defesa:", defesa_do_personagem,"  Agilidade:", agilidade_do_personagem)
            pickle.dump(mostrar_save, arq)
            pickle.dump(nome_do_jogador, arq)
            pickle.dump(nome_do_inimigo, arq)
            pickle.dump(reserva_nome_do_jogador, arq)
            pickle.dump(ação_do_personagem, arq)
            pickle.dump(batalha_escapar, arq)
            pickle.dump(equipamento_roupa, arq)
            pickle.dump(equipamento_capa, arq)
            pickle.dump(equipamento_luva, arq)
            pickle.dump(equipamento_mãos, arq)
            pickle.dump(equipamento_botas, arq)
            pickle.dump(olhar_o_cenário, arq)
            pickle.dump(modificar_o_cenário, arq)
            pickle.dump(cheirar_o_cenário, arq)
            pickle.dump(objeto_00, arq)
            pickle.dump(objeto_01, arq)
            pickle.dump(objeto_02, arq)
            pickle.dump(objeto_03, arq)
            pickle.dump(variável_lugar, arq)
            pickle.dump(ponto_de_save, arq)
            pickle.dump(eegg, arq)
            pickle.dump(vida_máxima_personagem, arq)
            pickle.dump(vida_atual_personagem, arq)
            pickle.dump(dinheiro_do_personagem, arq)
            pickle.dump(ataque_do_personagem, arq)
            pickle.dump(defesa_do_personagem, arq)
            pickle.dump(agilidade_do_personagem, arq)
            pickle.dump(reserva_vida_máxima_personagem, arq)
            pickle.dump(reserva_vida_atual_personagem, arq)
            pickle.dump(reserva_ataque_do_personagem, arq)
            pickle.dump(reserva_defesa_do_personagem, arq)
            pickle.dump(reserva_agilidade_do_personagem, arq)
            pickle.dump(vida_máxima_inimigo, arq)
            pickle.dump(vida_atual_inimigo, arq)
            pickle.dump(ataque_do_inimigo, arq)
            pickle.dump(defesa_do_inimigo, arq)
            pickle.dump(situação_00, arq)
            pickle.dump(situação_01, arq)
            pickle.dump(situação_02, arq)
            pickle.dump(situação_03, arq)
            pickle.dump(situação_04, arq)
            pickle.dump(situação_05, arq)
            pickle.dump(situação_06, arq)
            pickle.dump(situação_07, arq)
            pickle.dump(situação_08, arq)
            pickle.dump(situação_09, arq)
            pickle.dump(situação_10, arq)
            pickle.dump(teste_de_sorte, arq)
            pickle.dump(calculo_do_dano, arq)
            pickle.dump(calculo_da_fuga, arq)
            pickle.dump(variável_para_comparar, arq)
            pickle.dump(contador_de_batalha, arq)
            pickle.dump(contador_de_rodadas, arq)
            arq.close
            print("\nPronto!\n")
            break
        else:
            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                break
            else:
                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')

#--Sistema de batalha--#
def batalha():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas
    input("\nBatalha!!!\nÉ hora da briga!!!\n")
    contador_de_rodadas=1
    while(vida_atual_inimigo>0):
        if(vida_atual_personagem<=0):
            break
        print("\n]]", "="*30,"[[\n", "    Início da rodada número ", contador_de_rodadas, "\n]]", "="*30,"[[\n")
        if(vida_atual_personagem==1):
            if(contador_de_rodadas==1):
                input("\nVocê entrou na batalha com apenas 1 ponto de vida!")
                input("Seu último recurso é a tensão!\n")            
            else:
                if(contador_de_batalha==0):
                    input("\nVocê está com apenas 1 ponto de vida!")
                    input("Seu último recurso é a tensão!\n")            
            if(contador_de_batalha>0):       
                input("\nVocê aguentou mais uma rodada com apenas 1 ponto de vida!")
                input("Você extendeu o limite do seu fôlego e agora o limite dos seus pontos de vida subiu!\n")
                vida_máxima_personagem=vida_máxima_personagem+((contador_de_batalha)+(random.randrange(defesa_do_personagem)))
            contador_de_batalha=contador_de_batalha+1
        else:
            if(vida_atual_personagem<=vida_máxima_personagem*0.05):
                teste_de_sorte=random.randrange(15)
                if(teste_de_sorte==1):
                    input("\nVocê está dando o seu melhor para aguentar, isso está melhorando o seu fôlego!")
                    input("O limite dos seus pontos de vida aumentou!\n")
                    vida_máxima_personagem=vida_máxima_personagem+(random.randrange(defesa_do_personagem)+1)
                else:
                    if(teste_de_sorte==5 or teste_de_sorte==6):
                        input("\nVocê está dando o seu melhor para aguentar, isso está melhorando o seu fôlego!")
                        input("O limite dos seus pontos de vida aumentou!\n")
                        vida_máxima_personagem=vida_máxima_personagem+(random.randrange(defesa_do_personagem)+1)
        print("\n#", "-"*30,"#\n", "\n\n", nome_do_jogador, ":\n                    ",vida_atual_personagem, "\n                     de", vida_máxima_personagem, " Pontos de Vida\n\n", nome_do_inimigo, ":\n                    ", vida_atual_inimigo, "\n                     de", vida_máxima_inimigo, " Pontos de vida\n")
        print("\n#", "-"*30,"#\nO que você fará agora, ", nome_do_jogador, "?\nAtacar, defender ou fugir?")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        while True:
            if(ação_do_personagem != "atacar" and ação_do_personagem != "defender" and ação_do_personagem != "fugir"):
                print("\nComando inválido! Você só pode atacar, defender ou fugir!\n")
                ação_do_personagem = input("-")
                ação_do_personagem = ação_do_personagem.lower()
            else: break
        contador_de_rodadas=contador_de_rodadas+1
        if(ação_do_personagem == "defender"): #defesa(2defesa_do_personagem) vs ataque(ataque_do_inimigo)
            print("\nPostura de Batalha:\n", nome_do_jogador, "-> defensiva\n", nome_do_inimigo, "-> ofensiva\n")
            input("...")
            teste_de_sorte = random.randrange(5)
            if (teste_de_sorte==1):#S_defesa(3defesa_do_personagem) vs ataque(ataque_do_inimigo)
                input("\nSua postura de defesa te favoreceu!\n")
                teste_de_sorte = random.randrange(4)
                if (teste_de_sorte==1):#S_defesa(3defesa_do_personagem) vs S_ataque(2ataque_do_inimigo)
                    input("\n... Mas o ataque do inimigo foi crítico!\n")
                    calculo_do_dano = (2*ataque_do_inimigo)+(random.randrange(ataque_do_inimigo))*(0.2)-(3*defesa_do_personagem)-(random.randrange(defesa_do_personagem))*(0.2)
                    if (calculo_do_dano < 0):#S_defesa(3defesa_do_personagem) CONTRA-ATACA S_ataque(2ataque_do_inimigo)
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(ataque_do_personagem))/2)*(0.2)
                        input("\nNão importa, sua defesa é incrível!")
                        print("Além de defender você conseguiu contra-atacar, causando ", calculo_do_dano," pontos de dano ao inimigo!\n")
                        input("")
                        teste_de_sorte = random.randrange(140)#aumento de defesa
                        if (teste_de_sorte==10 or teste_de_sorte==20 or teste_de_sorte==30):
                            variável_para_comparar=defesa_do_personagem
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))
                            if (variável_para_comparar < defesa_do_personagem):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (variável_para_comparar > defesa_do_personagem):
                                defesa_do_personagem=variável_para_comparar
                        if (teste_de_sorte==40 or teste_de_sorte==50):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+1
                        if (teste_de_sorte==100):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+2
                        if (teste_de_sorte==130):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+3
                        vida_atual_inimigo = vida_atual_inimigo-calculo_do_dano
                    else:
                        if (calculo_do_dano == 0):#S_defesa(3defesa_do_personagem) ANULA S_ataque(2ataque_do_inimigo)
                            input("\nDefesa e ataque se anulam! A tensão aumenta!\n")
                        else:#S_defesa(3defesa_do_personagem) APANHA DO S_ataque(2ataque_do_inimigo)
                            print("\nVocê sofreu ", calculo_do_dano, " pontos de dano...\n")
                            input("")
                            vida_atual_personagem = vida_atual_personagem - calculo_do_dano
                else:#S_defesa(3defesa_do_personagem) vs ataque(ataque_do_inimigo)
                    calculo_do_dano = (ataque_do_inimigo)+(random.randrange(ataque_do_inimigo))*(0.2)-(3*defesa_do_personagem)-(random.randrange(defesa_do_personagem))*(0.2)
                    if (calculo_do_dano<0):#S_defesa(3defesa_do_personagem) CONTRA-ATACA ataque(ataque_do_inimigo)
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(ataque_do_personagem))/2)*(0.2)
                        print("\nSua defesa foi tão grande que, além de bloquear o ataque, você conseguiu contra-atacar, causando ", calculo_do_dano," pontos de dano ao inimigo!\n")
                        input("")
                        vida_atual_inimigo = vida_atual_inimigo-calculo_do_dano
                    else:
                        if (calculo_do_dano ==0):#S_defesa(3defesa_do_personagem) ANULA ataque(ataque_do_inimigo)
                            input("\nSua defesa foi completa!\n")
                        else:#S_defesa(3defesa_do_personagem) APANHA DO ataque(ataque_do_inimigo)
                            print("\nVocê sofreu míseros ", calculo_do_dano, " pontos de dano.\n")
                            input("")
                            vida_atual_personagem = vida_atual_personagem-calculo_do_dano
            else:
                teste_de_sorte = random.randrange(4)
                if(teste_de_sorte==1):#defesa(2defesa_do_personagem) vs S_ataque(2ataque_do_inimigo)
                    calculo_do_dano = 2*ataque_do_inimigo+(random.randrange(ataque_do_inimigo))*(0.2)-(1.5)*defesa_do_personagem-(random.randrange(defesa_do_personagem))*(0.2)
                    if (calculo_do_dano<0):
                        calculo_do_dano = (calculo_do_dano/2)*(-1)+((random.randrange(ataque_do_personagem))/2)*(0.2)
                                            
                        input("\nSua defesa é simplesmente  I M E N S A !")
                        print("O inimigo avançou furiosamente mas você o lançou para trás e contra-atacou causando ", calculo_do_dano, " pontos de dano ao inimigo!\n")
                        input("")
                        teste_de_sorte = random.randrange(100)#aumento de defesa
                        if (teste_de_sorte==1 or teste_de_sorte==15 or teste_de_sorte==30):
                            variável_para_comparar=defesa_do_personagem
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))
                            if (variável_para_comparar < defesa_do_personagem):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (variável_para_comparar > defesa_do_personagem):
                                defesa_do_personagem=variável_para_comparar
                        if (teste_de_sorte==20 or teste_de_sorte==40):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+1
                        if (teste_de_sorte==45):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+2
                        if (teste_de_sorte==55):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+3
                        if (teste_de_sorte==70):
                            variável_para_comparar=defesa_do_personagem
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+(random.randrange(ataque_do_personagem))
                            if (variável_para_comparar < defesa_do_personagem):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (variável_para_comparar > defesa_do_personagem):
                                defesa_do_personagem=variável_para_comparar
                        vida_atual_inimigo = vida_atual_inimigo-calculo_do_dano
                    else:
                        if(calculo_do_dano==0):
                            input("\nVocê surpreendeu o inimigo que estava confiante,")
                            input("suas forças se anularam numa estrondosa colisão!\n")
                            teste_de_sorte=random.randrange(30)
                            if(teste_de_sorte==1):
                                input("\nA liberação de energia durante a colisão despertou novos limites para sua força e agora está mais forte!")
                                input("TODOS os seus pontos subiram!\n")
                                vida_máxima_personagem=vida_máxima_personagem+(random.randrange(vida_máxima_personagem))+3
                                ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+2
                                defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+1
                        else:
                            print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                            input("")
                            vida_atual_personagem = vida_atual_personagem-calculo_do_dano
                else:#defesa(2defesa_do_personagem) vs ataque(ataque_do_inimigo)
                    calculo_do_dano = ataque_do_inimigo+(random.randrange(ataque_do_inimigo))-2*defesa_do_personagem-(random.randrange(defesa_do_personagem))
                    if (calculo_do_dano<0):
                        calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(ataque_do_personagem))/2)
                        input("\nSua defesa É ENORME!")
                        print("Você barrou o ataque naturalmente e contra-atacou, causando ", calculo_do_dano, " pontos de dano ao inimigo!\n")
                        input("")
                        teste_de_sorte = random.randrange(100)#aumento de defesa
                        if (teste_de_sorte==1 or teste_de_sorte==15 or teste_de_sorte==30):
                            variável_para_comparar=defesa_do_personagem
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))
                            if (variável_para_comparar < defesa_do_personagem):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (variável_para_comparar > defesa_do_personagem):
                                defesa_do_personagem=variável_para_comparar
                        if (teste_de_sorte==20 or teste_de_sorte==40):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+1
                        if (teste_de_sorte==45):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+2
                        if (teste_de_sorte==55):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            defesa_do_personagem=defesa_do_personagem+(random.randrange(defesa_do_personagem))+3
                        vida_atual_inimigo = vida_atual_inimigo-calculo_do_dano
                    else:
                        if(calculo_do_dano==0):
                            input("\nVocê barrou o ataque do inimigo!\n")
                        else:
                            print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                            input("")
                            vida_atual_personagem = vida_atual_personagem-calculo_do_dano
        else:
            if (ação_do_personagem=="atacar"):
                teste_de_sorte=random.randrange(2)
                if (teste_de_sorte==1):#ataque(ataque_do_personagem) vs defesa(2defesa_do_inimigo)
                    print("\nPostura de Batalha:\n", nome_do_jogador, "-> ofensiva\n", nome_do_inimigo, "-> defensiva\n")
                    input("...")
                    teste_de_sorte=random.randrange(4)
                    if (teste_de_sorte==1):#S_ataque(2ataque_do_personagem) vs defesa(2defesa_do_inimigo)
                        input("\nSeu ataque foi crítico!!!\n")
                        teste_de_sorte=random.randrange(5)
                        if (teste_de_sorte==1):#S_ataque(2ataque_do_personagem) vs S_defesa(3defesa_do_inimigo)
                            input("\nApesar do seu crítico, você é pressionado pela postura de defesa do seu inimigo!\n")
                            calculo_do_dano=2*ataque_do_personagem+(random.randrange(ataque_do_personagem))-3*defesa_do_inimigo-(random.randrange(defesa_do_inimigo))
                            if (calculo_do_dano<0):#S_ataque(2ataque_do_personagem) APANHA DE S_defesa(3defesa_do_inimigo)
                                calculo_do_dano = calculo_do_dano*(-1)+((random.randrange(ataque_do_inimigo))/2)
                                input("\nPor mais que tente, você não consegue atravessar a defesa do seu inimigo!")
                                print("Além de te bloquear, ele te contra-atacou, causando ", calculo_do_dano, " pontos de dano!\n")
                                input("")
                                vida_atual_personagem = vida_atual_personagem-calculo_do_dano
                                teste_de_sorte=random.randrange(10)
                                if(teste_de_sorte==2):
                                    input("\nVocê tentou ao máximo ultrapassar a defesa do seu inimigo, exigiu muito dos seus músculos que se fortaleceram!\n")
                                    input("\nSeus pontos de ataque subiram!\n")
                                    ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+3
                            else:
                                if (calculo_do_dano==0):#S_ataque(2ataque_do_personagem) ANULA S_defesa(3defesa_do_inimigo)
                                    input("\nA disputa de forças é intensa, você e seu inimigo deram o melhor de si, mas nenhum dos dois se sobrepôs!\n")
                                else:#S_ataque(2ataque_do_personagem) ATACA S_defesa(3defesa_do_inimigo)
                                    input("\nSeu ataque foi explosivo!")
                                    input("Nem o melhor da defesa do seu inimigo foi capaz de conter sua ira!")
                                    print("Você causou ", calculo_do_dano, " pontos de dano ao seu inimigo!\n")
                                    input("")
                                    vida_atual_inimigo = vida_atual_inimigo-calculo_do_dano
                                    teste_de_sorte=random.randrange(10)
                                    if(teste_de_sorte==3):
                                        input("\nA explosão de energia dos seus músculos os expandiu definitivamente!\n")
                                        input("\nSeus pontos de ataque subiram!\n")
                                        ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+2
                        else:#S_ataque(2ataque_do_personagem) vs defesa(2defesa_do_inimigo)
                            calculo_do_dano = 2*ataque_do_personagem+(random.randrange(ataque_do_personagem))-2*defesa_do_inimigo-(random.randrange(defesa_do_inimigo))
                            if(calculo_do_dano<0):#S_ataque(2ataque_do_personagem) APANHA DE defesa(2defesa_do_inimigo)
                                calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(ataque_do_inimigo))/2)
                                input("\nVocê deu o seu máximo, mas mesmo assim nem se equiparou às habilidades de auto-defesa do seu inimigo!")
                                print("Sem fazer muito esforço ele se defendeu e contra-atacou, te causando ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_personagem = vida_atual_personagem - calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#S_ataque(2ataque_do_personagem) ANULA defesa(2defesa_do_inimigo)
                                    input("\nVocê assustou o inimigo por um instante, mas - por muito pouco - ele conseguiu barrar todos os seus movimentos ofensivos...\n")
                                else:
                                    teste_de_sorte=random.randrange(5)
                                    if(teste_de_sorte==1):#XS_ataque(3ataque_do_personagem) vs defesa(defesa_do_inimigo)
                                        print("\nVocê rompeu a defesa do seu inimigo, causando ", calculo_do_dano," pontos de dano!")
                                        input("")
                                        input("\nSuper Crítico!!!\n")
                                        input("Você iniciou um ataque em frenesi!!!\n")
                                        vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                                        teste_de_sorte=random.randrange(9)+1
                                        while(teste_de_sorte>0):#XS_ataque(3ataque_do_personagem) ATACA defesa(defesa_do_inimigo)
                                            calculo_do_dano=2*(random.randrange(ataque_do_personagem))-(random.randrange(defesa_do_inimigo))
                                            while(calculo_do_dano<=0):
                                                calculo_do_dano=2*(random.randrange(ataque_do_personagem))-(random.randrange(defesa_do_inimigo))
                                            print(calculo_do_dano," pontos de dano!\n")
                                            input("")
                                            vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                                            teste_de_sorte=teste_de_sorte-1
                                        input("\nVocê desferiu toda sua fúria no inimigo!\n")
                                        teste_de_sorte=random.randrange(5)
                                        if(teste_de_sorte<4):
                                            input("\nVocê testou o seu limite e agora está mais forte!")
                                            input("Seus pontos de ataque subiram!\n")
                                            ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+2
                                        if(teste_de_sorte==4):
                                            input("\nVocê ultrapassou o seu limite e agora está mais forte!")
                                            input("Seus pontos de ataque subiram!\n")
                                            ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+3
                                    else:#S_ataque(2ataque_do_personagem) ATACA defesa(2defesa_do_inimigo)
                                        print("\nSeu ataque de golpes duplos pressionaram a defesa do seu inimigo, causando ",calculo_do_dano," pontos de dano!\n")
                                        input("")
                                        vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                    else:#ataque(ataque_do_personagem)
                        teste_de_sorte=random.randrange(5)
                        if(teste_de_sorte==1):#ataque(ataque_do_personagem) vs S_defesa(3defesa_do_inimigo)
                            input("\nA postura de defesa do seu inimigo te colocou numa situação difícil!\n")
                            calculo_do_dano=ataque_do_personagem+random.randrange(ataque_do_personagem)-3*defesa_do_inimigo-random.randrange(defesa_do_inimigo)
                            if(calculo_do_dano<0):#ataque(ataque_do_personagem) APANHA DE S_defesa(3defesa_do_inimigo)
                                calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(ataque_do_inimigo))/2)
                                input("\nÉ muito difícil passar por tamanha defesa, seu ataque foi ínfimo, além de ser inutilizado, você sofreu represália...")
                                print("Seu inimigo contra-atacou, causando ", calculo_do_dano, " pontos de dano.\n")
                                input("")
                                teste_de_sorte=random.randrange(20)
                                if(teste_de_sorte==1):
                                    input("\nVocê testou o seu limite e agora está mais forte!")
                                    input("Seus pontos de ataque subiram!\n")
                                    ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+1
                                vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#ataque(ataque_do_personagem) ANULA S_defesa(3defesa_do_inimigo)
                                    print("\nO inimigo mal consegue reter seus golpes, mas o suficiente para pará-lo.")
                                    input("Ao mesmo tempo sua força foi o bastante para evitar um contra-ataque!\n")
                                else:#ataque(ataque_do_personagem) ATACA S_defesa(3defesa_do_inimigo)
                                    print("\nDepois de alguns golpes, você tornou insignificante a vantagem defensiva do seu inimigo, causando humilhantes, ", calculo_do_dano," pontos de dano a ele!\n")
                                    input("")
                                    teste_de_sorte=random.randrange(10)
                                    if(teste_de_sorte==1):
                                        input("\nVocê testou o seu limite e agora está mais forte!")
                                        input("Seus pontos de ataque subiram!\n")
                                        ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+2
                                    vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                        else:#ataque(ataque_do_personagem) vs defesa(2defesa_do_inimigo)
                            calculo_do_dano = ataque_do_personagem+(random.randrange(ataque_do_personagem))-2*defesa_do_inimigo-(random.randrange(defesa_do_inimigo))
                            if(calculo_do_dano<0):#ataque(ataque_do_personagem) APANHA DE defesa(2defesa_do_inimigo)
                                calculo_do_dano=calculo_do_dano*(-1)+((random.randrange(ataque_do_inimigo))/2)
                                print("\nO inimigo se defendeu e contra-atacou, te causando ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_personagem = vida_atual_personagem - calculo_do_dano
                            else:
                                if(calculo_do_dano==0):#ataque(ataque_do_personagem) ANULA defesa(2defesa_do_inimigo)
                                    input("\nSeu oponente defendeu todos os seus golpes, mas você não deu brecha para que ele avançasse!\n")
                                else:#ataque(ataque_do_personagem) ATACA defesa(2defesa_do_inimigo)
                                    print("\nVocê acertou o inimigo durante a disputa de forças, causando ",calculo_do_dano," pontos de dano!\n")
                                    input("")
                                    vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                else:#ataque(ataque_do_personagem) vs ataque(ataque_do_inimigo)
                    print("\nPostura de Batalha:\n", nome_do_jogador, "-> ofensiva\n", nome_do_inimigo, "-> ofensiva\n")
                    input("...")
                    teste_de_sorte=random.randrange(4)
                    if (teste_de_sorte==1):#S_ataque(2ataque_do_personagem) vs ataque(ataque_do_inimigo)
                        input("\nSeu ataque foi crítico!!!\n")
                        teste_de_sorte=random.randrange(4)
                        if (teste_de_sorte==1):#S_ataque(2ataque_do_personagem) vs S_ataque(2ataque_do_inimigo)
                            input("\nMas o ataque do oponente também foi crítico!!!\n")
                            input("\nVocês entraram na briga pra valer!")
                            input("Avançaram de punhos cerrados, trocando golpes com as defesas abertas!\n")
                            calculo_do_dano=2*ataque_do_personagem+random.randrange(ataque_do_personagem)-defesa_do_inimigo-random.randrange(defesa_do_inimigo)
                            if(calculo_do_dano>0):
                                print("\nVocê causou significativos ", calculo_do_dano," pontos de dano ao inimigo!\n")
                                input("")
                                vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                                teste_de_sorte=random.randrange(10)
                                if(teste_de_sorte==1):
                                    input("\nSeus pontos de ataque subiram enquanto você forçava os seus músculos!\n")
                                    ataque_do_personagem=ataque_do_personagem+(random.randrange(ataque_do_personagem))+2
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            calculo_do_dano=2*ataque_do_inimigo+random.randrange(ataque_do_inimigo)-defesa_do_personagem-random.randrange(defesa_do_personagem)
                            if(calculo_do_dano>0):
                                print("\nEnquanto o oponente te causou ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                        else:#S_ataque(2ataque_do_personagem) vs ataque(ataque_do_inimigo)
                            input("\nVocê avançou violentamente sobre o inimigo, pressionando-o sem compaixão!")
                            input("Apesar de forçar um leve recuo do inimigo, você não deixou de levar uns bons golpes!\n")                            
                            calculo_do_dano=2*ataque_do_personagem+random.randrange(ataque_do_personagem)-defesa_do_inimigo-random.randrange(defesa_do_inimigo)
                            if(calculo_do_dano>0):
                                print("\nVocê golpeou o inimigo até lhe causar ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            calculo_do_dano=ataque_do_inimigo+random.randrange(ataque_do_inimigo)-defesa_do_personagem-random.randrange(defesa_do_personagem)
                            if(calculo_do_dano>0):
                                print("\nJá o inimigo causou apenas ", calculo_do_dano," pontos de dano à você!\n")
                                input("")
                                vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                    else:#ataque(ataque_do_personagem) vs ataque(ataque_do_inimigo)
                        teste_de_sorte=random.randrange(4)
                        if(teste_de_sorte==1): #ataque(ataque_do_personagem) vs S_ataque(2ataque_do_inimigo)
                            input("\nO ataque do oponente foi crítico!...\n")
                            input("\nVocê foi pressionado enquanto trocavam golpes, os socos e chutes do seu oponente te acertaram em pontos menos resistentes do seu corpo que estavam desprotegidos!")
                            input("Mesmo assim você manteve um bom rítmo de ataque!\n")
                            calculo_do_dano=ataque_do_personagem+random.randrange(ataque_do_personagem)-defesa_do_inimigo-random.randrange(defesa_do_inimigo)
                            if(calculo_do_dano>0):
                                print("\nVocê infringiu ", calculo_do_dano," pontos de dano ao inimigo!\n")
                                input("")
                                vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            calculo_do_dano=2*ataque_do_inimigo+random.randrange(ataque_do_inimigo)-defesa_do_personagem-random.randrange(defesa_do_personagem)
                            if(calculo_do_dano>0):
                                print("\nEnquanto o seu inimigo te agrediu violentamente, causando ", calculo_do_dano," pontos de dano à você!\n")
                                input("")
                                vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                        else:#ataque(ataque_do_personagem) vs ataque(ataque_do_inimigo)
                            input("\nVocês se atacaram num ritmo leve, parecem estar testando um ao outro, ficou claro que nenhum dos dois mostrou tudo o que é capaz.\n")
                            calculo_do_dano=ataque_do_personagem+random.randrange(ataque_do_personagem)-defesa_do_inimigo-random.randrange(defesa_do_inimigo)
                            if(calculo_do_dano>0):
                                print("\nVocê feriu seu oponente em ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_inimigo=vida_atual_inimigo-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            calculo_do_dano=ataque_do_inimigo+random.randrange(ataque_do_inimigo)-defesa_do_personagem-random.randrange(defesa_do_personagem)
                            if(calculo_do_dano>0):
                                print("\nSeu inimigo te golpeou causando ", calculo_do_dano," pontos de dano!\n")
                                input("")
                                vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
            else:
                if(ação_do_personagem=="fugir"):
                    print("\nPostura de Batalha:\n", nome_do_jogador, "-> fugitiva\n", nome_do_inimigo, "-> ofensiva\n")
                    input("...")
                    input("\nVocê tenta aumentar o rítmo de esquiva...\n")
                    teste_de_sorte=random.randrange(10)+calculo_da_fuga
                    if(teste_de_sorte==10):
                        input('\nVocê esquivou de qualquer manobra ofensiva do oponente e conseguiu uma brecha para fugir!\n')
                        print('\nDeseja fugir da luta?("sim" ou "não")\n')
                        batalha_escapar=""
                        while(batalha_escapar != "não"):
                            batalha_escapar = input('-')
                            batalha_escapar = batalha_escapar.lower()
                            if(batalha_escapar!="não" and batalha_escapar != "sim"):
                                print('\nEntrada invalida! Digite "sim" ou "não".\n')
                            if(batalha_escapar =="sim"):
                                break
                        if(batalha_escapar =="sim"):
                            break
                    else:
                        if(teste_de_sorte>8):
                            input('\nVocê esquivou de qualquer manobra ofensiva do oponente, mas não conseguiu uma brecha para fugir...\n')
                        else:
                            if(teste_de_sorte>5):
                                input('\nVocê não conseguiu uma brecha para fugir, nem pode se esquivar, mas pode se defender!\n')
                                calculo_do_dano = ataque_do_inimigo+(random.randrange(ataque_do_inimigo))-2*defesa_do_personagem-(random.randrange(defesa_do_personagem))
                                if (calculo_do_dano<0):
                                    input('\nSua defesa É ENORME!')
                                    input('Você barrou o ataque naturalmente e conseguiu afastar o inimigo, criando uma brecha para fugir!\n')
                                    print('\nDeseja fugir da luta?("sim" ou "não")\n')
                                    batalha_escapar=""
                                    while(batalha_escapar != "não"):
                                        batalha_escapar = input('-')
                                        batalha_escapar = batalha_escapar.lower()
                                        if(batalha_escapar!="não" and batalha_escapar != "sim"):
                                            print('\nEntrada invalida! Digite "sim" ou "não".\n')
                                        if(batalha_escapar =="sim"):
                                            break
                                    if(batalha_escapar =="sim"):
                                        batalha_escapar="sim"
                                        break
                                else:
                                    if(calculo_do_dano==0):
                                        input("\nVocê barrou o ataque do inimigo!\n")
                                    else:
                                        print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", calculo_do_dano, " pontos de dano!\n")
                                        input("")
                                        vida_atual_personagem = vida_atual_personagem-calculo_do_dano
                            else:
                                if(teste_de_sorte>2):
                                    input('\nVocê não conseguiu uma brecha para fugir, se esquivar ou se defender...\n')
                                    calculo_do_dano = ataque_do_inimigo+(random.randrange(ataque_do_inimigo))-defesa_do_personagem-(random.randrange(defesa_do_personagem))
                                    if (calculo_do_dano>0):
                                        print("\nVocê foi atacado diretamente, sofrendo ", calculo_do_dano," pontos de dano!\n")
                                        input("")
                                        vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                                    else:
                                        input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                else:
                                    input('\nVocê tropeçou ao tentar fugir!\n')
                                    input('\nO golpe do oponente foi crítico!\n')
                                    calculo_do_dano = 2*ataque_do_inimigo+(random.randrange(ataque_do_inimigo))-defesa_do_personagem-(random.randrange(defesa_do_personagem))
                                    if (calculo_do_dano>0):
                                        print("\nO inimigo aproveitou a abertura na sua defesa e te atacou violentamente, causando ", calculo_do_dano," pontos de dano.\n")
                                        input("")
                                        vida_atual_personagem=vida_atual_personagem-calculo_do_dano
                                        teste_de_sorte=random.randrange(5)
                                        if(teste_de_sorte==1):
                                            input("\nVocê aumentou seu folego enquanto tentava escapar dos golpes que você levou em cheio!")
                                            input("O limite dos seus pontos de vida cresceu!")
                                            vida_máxima_personagem=vida_máxima_personagem+(random.randrange(vida_máxima_personagem))+1
                                    else:
                                        input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                    calculo_da_fuga=calculo_da_fuga+(agilidade_do_personagem*0.25)
                    if(batalha_escapar =="sim"):
                        break
    batalha_escapar="não"
    variável_para_comparar = 0
    contador_de_batalha = 0
    contador_de_rodadas = 1
    input("\nFim da Batalha!\n")
    if(vida_atual_inimigo<=0):
        print("\n",nome_do_inimigo," foi derrotado!\n")
        input("")
    else:
        if(vida_atual_personagem<=0):
            input("\nVocê foi derrotado.\n")
        else:
            if(batalha_escapar =="sim"):
                input("\nVocê conseguiu escapar!\n")
                batalha_escapar="escapou"

#--Matar alguém--#
def matarAlguém():
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
    input("     Ele...")
    input("     Ele era um ser vivo...")
    input("     Ele era um ser humano...")
    input("                   E você o matou!")

#--Seu prédio: Quarto Andar--#
def seuPrédioQuartoAndar():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas,temporário
    variável_lugar = "seu prédio, 4º andar"
    temporário= False
    if(situação_00<5):
        input("Você foi abordado novamente pelo morador do quarto 44...")
        input(" - Nós sabemos que você não venceu nem do 3º andar, se não é capaz disso,\nnão é capaz de nos vencer!")
        input("Ele te empurrou escada abaixo... Você perdeu 5 pontos de vida durante a queda!")
        vida_atual_personagem=vida_atual_personagem-5
        if(vida_atual_personagem<=0):
            vida_atual_personagem=1
    while 1:
        if(situação_00<5):
            input("Agora você está no terceiro andar.")
            break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos\n")
        print("\nver ficha do personagem\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", nome_do_jogador,", o que você vai fazer?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        if(ação_do_personagem=="checar os quartos" or ação_do_personagem=="checar quartos" or ação_do_personagem=="checar" or ação_do_personagem=="quartos" or ação_do_personagem=="checaros quartos" or ação_do_personagem=="checar osquartos" or ação_do_personagem=="checarosquartos" or ação_do_personagem=="checa os quartos" or ação_do_personagem=="checa os quarto" or ação_do_personagem=="checa o quarto" or ação_do_personagem=="checa o quartos" or ação_do_personagem=="checar os quarto" or ação_do_personagem=="checar o quarto" or ação_do_personagem=="bater na porta de um dos quartos" or ação_do_personagem=="checar um dos quartos" or ação_do_personagem=="bater na porta dos quartos" or ação_do_personagem=="bater a porta dos quartos" or ação_do_personagem=="bater quartos" or ação_do_personagem=="bater"):
            print("Qual dos quartos?(40, 41, 42, 43 ou 44)\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            if(ação_do_personagem!="40" and ação_do_personagem!="41" and ação_do_personagem!="42" and ação_do_personagem!="43" and ação_do_personagem!="44"):
                ação_do_personagem="entrada inválida!"
        if (ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                input("Você desceu para o terceiro andar.")
                break
            else:
                if(ação_do_personagem=="40"):
                    if(situação_00>6):
                        input("Você já lutou aqui!")
                    else:
                        input(' - Aqui no 4º andar moram os mais fortes, mas há muita diferença entre nós!')
                        input(' - Por isso há uma ordem para nos enfrentar, começando por mim!')
                        input(' - Como não pegamos leve, nós apresentamos um "cartão de visita" ao oponente, para ele saber se é capaz de sobreviver.')
                        nome_do_inimigo="Estudante Briguento \n do Quarto 40"
                        vida_máxima_inimigo=360
                        vida_atual_inimigo=360
                        ataque_do_inimigo=30
                        defesa_do_inimigo=15
                        input(" - Aqui está o meu:")
                        print("\n", nome_do_inimigo,":",vida_máxima_inimigo,"pontos de vida.\nAtaque : ",ataque_do_inimigo,".     Defesa : ", defesa_do_inimigo,".\n")
                        print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                        while 1:
                            ação_do_personagem = input("-")
                            ação_do_personagem = ação_do_personagem.lower()
                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                break
                            else:
                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                    batalha()
                                    if(vida_atual_personagem<=0):break
                                    if(vida_atual_inimigo>0):
                                        while (vida_atual_inimigo>0):
                                            input(" - O que foi, desistiu?(sim ou não)")
                                            while 1:
                                                ação_do_personagem=input("-")
                                                ação_do_personagem = ação_do_personagem.lower()
                                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                    input(" - Então vamos voltar a lutar!")
                                                    batalha()
                                                else:
                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                        input(" - Tem certeza?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                            input(" - Muito obrigado pela colaboração financeira! Até outro dia, talvez...")
                                                            dinheiro_do_personagem=dinheiro_do_personagem/2
                                                            break
                                                        else:
                                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                input(" - Então vamos voltar a lutar!")
                                                                batalha()
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                    else:
                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                        if(vida_atual_personagem<=0):break
                                        else:
                                            input(" - Parabéns! Você é realmente forte!")
                                            situação_00=situação_00+1
                                            break
                                    else:
                                        input(" - Parabéns! Você é realmente forte!")
                                        situação_00=situação_00+1
                                        break
                                else:
                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                else:
                    if(ação_do_personagem=="41"):
                        if(situação_00==7):
                            input(' - Será que você está pronto para brigar comigo, fracote??? Hahahahaha!')
                            nome_do_inimigo="Estudante Briguento \n do Quarto 41"
                            vida_máxima_inimigo=550
                            vida_atual_inimigo=550
                            ataque_do_inimigo=50
                            defesa_do_inimigo=30
                            input(" - Aqui está o meu cartão:")
                            print("\n", nome_do_inimigo,":",vida_máxima_inimigo,"pontos de vida.\nAtaque : ",ataque_do_inimigo,".     Defesa : ", defesa_do_inimigo,".\n")
                            print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                            while 1:
                                ação_do_personagem = input("-")
                                ação_do_personagem = ação_do_personagem.lower()
                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                    break
                                else:
                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                        batalha()
                                        if(vida_atual_personagem<=0):break
                                        if(vida_atual_inimigo>0):
                                            while (vida_atual_inimigo>0):
                                                input(" - O que há? Vai cair fora mesmo???(sim ou não)")
                                                while 1:
                                                    ação_do_personagem = input("-")
                                                    ação_do_personagem = ação_do_personagem.lower()
                                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                        input(" - Então cai dentro!!!")
                                                        batalha()
                                                    else:
                                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                            input(" - É sério?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                input(" - Hahaha! Você não é o primeiro que sai do desafio! Por que você acha que tem um prêmio?")
                                                                input(" - Você pode tentar de novo se quiser compensar a perda! HAHAHAHAHA!")
                                                                dinheiro_do_personagem=dinheiro_do_personagem/2
                                                                break
                                                            else:
                                                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                    input(" - Então cai dentro!!!")
                                                                    batalha()
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                        else:
                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                            if(vida_atual_personagem<=0):break
                                            else:
                                                input(" - CARAMBA! E não é que você estava pronto mesmo?! Hahahaha... Tudo bem perder às vezes...")
                                                situação_00=situação_00+1
                                                break
                                        else:
                                            input(" - Parabéns! Você é realmente forte!")
                                            situação_00=situação_00+1
                                            break
                                    else:
                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                        else:
                            if(situação_00>7):
                                input("Você já lutou aqui!")
                            else:
                                input(" - Você não pode me desafiar enquanto não vencer do briguento do quarto 40")
                    else:
                        if(ação_do_personagem=="42"):
                            if(situação_00==8):
                                input(' - Humhumhumhum... Você vai perder...')
                                nome_do_inimigo="Estudante Briguenta \n do Quarto 42"
                                vida_máxima_inimigo=790
                                vida_atual_inimigo=790
                                ataque_do_inimigo=90
                                defesa_do_inimigo=70
                                input(" - Veja:")
                                print("\n", nome_do_inimigo,":",vida_máxima_inimigo,"pontos de vida.\nAtaque : ",ataque_do_inimigo,".     Defesa : ", defesa_do_inimigo,".\n")
                                print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                while 1:
                                    ação_do_personagem = input("-")
                                    ação_do_personagem = ação_do_personagem.lower()
                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                        break
                                    else:
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            batalha()
                                            if(vida_atual_personagem<=0):break
                                            if(vida_atual_inimigo>0):
                                                while (vida_atual_inimigo>0):
                                                    input(" - Você vai fugir?(sim ou não) Humhumhumhum...")
                                                    while 1:
                                                        ação_do_personagem = input("-")
                                                        ação_do_personagem = ação_do_personagem.lower()
                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                            input(" - Venha!!!")
                                                            batalha()
                                                        else:
                                                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                input(" - Você vai mesmo?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                    input(" - Humhumhumhum... Fraco! Eu sempre soube que você era fraco!")
                                                                    input(" - Volte quando você deixar de ser fraco! FWUAHAHAHAHAHAHAHA!!! NUNCAAA!!!")
                                                                    dinheiro_do_personagem=dinheiro_do_personagem/2
                                                                    break
                                                                else:
                                                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                        input(" - Venha!!!")
                                                                        batalha()
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                            else:
                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                if(vida_atual_personagem<=0):break
                                                else:
                                                    input(" - COMO?! COMO?! Você trapaceou! EU SEI!!! Mas tudo bem, você não conseguirá vencer o próximo, nem trapaceando MUITO!")
                                                    situação_00=situação_00+1
                                                    break
                                            else:
                                                input(" - COMO?! COMO?! Você trapaceou! EU SEI!!! Mas tudo bem, você não conseguirá vencer o próximo, nem trapaceando MUITO!")
                                                situação_00=situação_00+1
                                                break
                                        else:
                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                            else:
                                if(situação_00>8):
                                    input("Você já lutou aqui!")
                                else:
                                    input("Você não pode me desafiar enquanto não vencer do briguento do quarto 41")
                        else:
                            if(ação_do_personagem=="43"):
                                if(situação_00==9):
                                    input(' - Sua presença é insignificante.')
                                    nome_do_inimigo="Estudante Briguento \n do Quarto 43"
                                    vida_máxima_inimigo=1500
                                    vida_atual_inimigo=1500
                                    ataque_do_inimigo=180
                                    defesa_do_inimigo=100
                                    input(" - Mas vou te dar a honra de apreciar o meu cartão:")
                                    print("\n", nome_do_inimigo,":",vida_máxima_inimigo,"pontos de vida.\nAtaque : ",ataque_do_inimigo,".     Defesa : ", defesa_do_inimigo,".\n")
                                    print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                            break
                                        else:
                                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                batalha()
                                                if(vida_atual_personagem<=0):break
                                                if(vida_atual_inimigo>0):
                                                    while (vida_atual_inimigo>0):
                                                        input(" - ... Fugindo?(sim ou não)")
                                                        while 1:
                                                            ação_do_personagem = input("-")
                                                            ação_do_personagem = ação_do_personagem.lower()
                                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                input(" - Você vai MORRER!!!")
                                                                batalha()
                                                            else:
                                                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                    input(" - Vai fugir mesmo, lixo?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                        input(" - São os lixos como você que pagaram o prêmio que NUNCA SERÁ SEU!")
                                                                        input(" - Volte quando quiser apanhar mais!")
                                                                        dinheiro_do_personagem=dinheiro_do_personagem/2
                                                                        break
                                                                    else:
                                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                            input(" - Você vai MORRER!!!")
                                                                            batalha()
                                                                        else:
                                                                            print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                else:
                                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                    if(vida_atual_personagem<=0):break
                                                    else:
                                                        input(" - Desgraçado... Você é forte demais...")
                                                        situação_00=situação_00+1
                                                        break
                                                else:
                                                    input(" - Desgraçado... Você é forte demais...")
                                                    situação_00=situação_00+1
                                                    break
                                            else:
                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                else:
                                    if(situação_00>9):
                                        input("Você já lutou aqui!")
                                    else:
                                        input("Você não pode me desafiar enquanto não vencer do briguento do quarto 42")
                            else:
                                if(ação_do_personagem=="44"):
                                    if(situação_00==10):
                                        input(' - Me perdôe pelo comportamento daqueles dois... Nenhum deles tem a cabeça no lugar.')
                                        input(" - Mesmo assim, é raro alguém passar do quarto 40, é raríssimo alguém chegar até mim.")
                                        input(" - Você é um briguento e tanto!")
                                        nome_do_inimigo="Estudante Briguento \n do Quarto 44"
                                        vida_máxima_inimigo=3200
                                        vida_atual_inimigo=3200
                                        ataque_do_inimigo=300
                                        defesa_do_inimigo=200
                                        input(" - Vamos logo ao que interessa:")
                                        print("\n", nome_do_inimigo,":",vida_máxima_inimigo,"pontos de vida.\nAtaque : ",ataque_do_inimigo,".     Defesa : ", defesa_do_inimigo,".\n")
                                        print('\nDeseja prosseguir com a luta?("sim" ou "não")\n')
                                        while 1:
                                            ação_do_personagem = input("-")
                                            ação_do_personagem = ação_do_personagem.lower()
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                break
                                            else:
                                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                    batalha()
                                                    if(vida_atual_personagem<=0):break
                                                    if(vida_atual_inimigo>0):
                                                        while (vida_atual_inimigo>0):
                                                            input(" - ... Vai abandonar a nossa luta?(sim ou não)")
                                                            while 1:
                                                                ação_do_personagem = input("-")
                                                                ação_do_personagem = ação_do_personagem.lower()
                                                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                    input(" - Desde o início, eu sabia que você não era qualquer um!")
                                                                    batalha()
                                                                else:
                                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                        input(" - Certeza, vai abandonar a última luta?(sim ou não) ... Se você fugir, deixará METADE DE TODO O SEU DINHEIRO conosco!")
                                                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                            input(" - Recupere-se e treine mais!")
                                                                            input(" - Estarei esperando o seu retorno!")
                                                                            dinheiro_do_personagem=dinheiro_do_personagem/2
                                                                            break
                                                                        else:
                                                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                                input(" - Ainda bem, não quero deixar a nossa luta para depois!!!")
                                                                                batalha()
                                                                            else:
                                                                                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                                    else:
                                                                        print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                                        if(vida_atual_personagem<=0):break
                                                        else:
                                                            input(" - Incrível... Você é um gênio das batalhas! É realmente dígno do prêmio!")
                                                            input(" - Aqui está: uma Malha Ninja!")
                                                            input("Você vestiu a Malha Ninja!")
                                                            input("Sua agilidade aumentou em 3 pontos!")
                                                            input("Sua defesa aumentou em 20 pontos!")
                                                            equipamento_roupa="Malha Ninja"
                                                            defesa_do_personagem=defesa_do_personagem+20
                                                            agilidade_do_personagem=agilidade_do_personagem+3
                                                            situação_00=situação_00+1
                                                            break
                                                    else:
                                                        input(" - Incrível... Você é um gênio das batalhas! É realmente dígno do prêmio!")
                                                        input(" - Aqui está: uma Malha Ninja!")
                                                        input("Você vestiu a Malha Ninja!")
                                                        input("Sua agilidade aumentou em 3 pontos!")
                                                        input("Sua defesa aumentou em 20 pontos!")
                                                        equipamento_roupa="Malha Ninja"
                                                        defesa_do_personagem=defesa_do_personagem+20
                                                        agilidade_do_personagem=agilidade_do_personagem+3
                                                        situação_00=situação_00+1
                                                        break
                                                else:
                                                    print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                                    else:
                                        if(situação_00>10):
                                            input("Você já lutou aqui!")
                                        else:
                                            input("Você não pode me desafiar enquanto não vencer do briguento do quarto 43")
                                else:
                                    if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                        save()
                                    else:
                                        input("Entrada Inválida!")
        if(vida_atual_personagem<=0):break

#--Seu prédio: Terceiro Andar--#
def seuPrédioTerceiroAndar():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas,temporário
    if temporário==True:
        input("Agora que você venceu todos os lutadores do 3º andar você subiu ao 4º.")
        seuPrédioQuartoAndar()
    if(variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioQuartoAndar()
    if(vida_atual_personagem>0):
        variável_lugar = "seu prédio, 3º andar"
        if(situação_00==0):
            input("Você é abordado pelo morador do quarto 44...")
            input(" - E aí, você é o morador do 13 né?...")
            input("...")
            input(" - Você é um pouco azarado, rapaz! ... Ou sortudo, depende do seu ponto de vista.")
            print("...")
            input(" - Okay, vou te explicar...")
            input(" - Você sabe que nos dois últimos andares desse prédio, o terceiro e o quarto,")
            input("só tem quartos de estudantes briguentos, e nós estamos desafiando outros\n arruaceiros a lutarem conosco!")
            print("...")
            input(" - Claro, se você vencer de todos nós, será recompensado!")
            input(" - Vá em frente, visite um dos quartos para lutar com um de nós!")
            input(" - Eu estarei lá em cima, no meu quarto, te esperando.")
            input("\nEle subiu as escadas...")
            input("...")
            situação_00+=1
        else:
            if(situação_00==1):
                input("Você ainda não venceu nenhuma luta do desafio dos estudantes briguentos!")
            else:
                if(situação_00==2):
                    input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                else:
                    if(situação_00>=3 and situação_00<6):
                        print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                        input("")
                    else:
                        if(situação_00<9):
                            input("Você já venceu todas as lutas do terceiro andar, \nentão você continuou subindo para o 4º andar.")
                            seuPrédioQuartoAndar()
                            variável_lugar = "seu prédio, 3º andar"
                        else:
                            input("Você já venceu o desafio dos estudantes briguentos do seu prédio!")
    while 1:
        if(vida_atual_personagem<=0):break
        if(situação_00>=9):
            variável_lugar = "seu prédio, 2º andar"
            break
        else:
            if(situação_00>6):
                print("Como você já venceu as lutas aqui, você continuou descendo...")
                input("Você desceu para o segundo andar.")
                variável_lugar = "seu prédio, 2º andar"
                break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos: 30, 31, 32, 33 e 34\n")
        print("\nver ficha do personagem\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", nome_do_jogador,", o que você vai fazer?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
        if(ação_do_personagem=="checar os quartos" or ação_do_personagem=="checar quartos" or ação_do_personagem=="checar" or ação_do_personagem=="quartos" or ação_do_personagem=="checaros quartos" or ação_do_personagem=="checar osquartos" or ação_do_personagem=="checarosquartos" or ação_do_personagem=="checa os quartos" or ação_do_personagem=="checa os quarto" or ação_do_personagem=="checa o quarto" or ação_do_personagem=="checa o quartos" or ação_do_personagem=="checar os quarto" or ação_do_personagem=="checar o quarto" or ação_do_personagem=="bater na porta de um dos quartos" or ação_do_personagem=="checar um dos quartos" or ação_do_personagem=="bater na porta dos quartos" or ação_do_personagem=="bater a porta dos quartos" or ação_do_personagem=="bater quartos" or ação_do_personagem=="bater"):
            print("Qual dos quartos?(30, 31, 32, 33 ou 34)\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            if(ação_do_personagem!="30" and ação_do_personagem!="31" and ação_do_personagem!="32" and ação_do_personagem!="33" and ação_do_personagem!="34"):
                ação_do_personagem="entrada inválida!"
        if (ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
            ficha_personagem()
        else:
            if(ação_do_personagem=="subir as escadas" or ação_do_personagem=="subir" or ação_do_personagem=="subir escadas" or ação_do_personagem=="subi" or ação_do_personagem=="subi as escadas" or ação_do_personagem=="subir escada" or ação_do_personagem=="subi escada" or ação_do_personagem=="subi a escada" or ação_do_personagem=="sobe"):
                input("Você subiu para o quarto andar, lá você encontrou mais cinco quartos de portas abertas.")
                seuPrédioQuartoAndar()
            else:
                if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                    input("Você desceu para o segundo andar.")
                    break
                else:
                    if(ação_do_personagem=="30"):
                        if(situação_05 == 0):
                            input("Eu sou o seu oponente! Vença todos deste andar para subir!")
                            nome_do_inimigo="Estudante Briguento \n do Quarto 30"
                            vida_máxima_inimigo=110
                            vida_atual_inimigo=110
                            ataque_do_inimigo=5
                            defesa_do_inimigo=12
                            batalha()
                            if(vida_atual_personagem<=0):
                                vida_atual_personagem=1
                                input(" - Você é fraco, se fosse uma luta no andar de cima você teria morrido!")
                                input(" - Vá cuidar desses seus ferimentos e volte para lutar mais!")
                            else:
                                if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                    while (vida_atual_inimigo>0):
                                        input(" - Você não pode fugir das lutas, é uma regra para continuar no desafio e ganhar o prêmio!")
                                        batalha()
                                        if(vida_atual_personagem<=0):
                                            vida_atual_personagem=1
                                            input(" - Você é fraco, se fosse uma luta no andar de cima você teria morrido!")
                                            input(" - Vá cuidar desses seus ferimentos e volte para lutar mais!")
                                            break
                                        else:
                                            input(" - Isso aí! Você me venceu!")
                                            situação_00=situação_00+1
                                            situação_05=1
                                            if(situação_00==6):
                                                temporário= True
                                            else:
                                                if(situação_00==2):
                                                    input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                else:
                                                    if(situação_00>=3 and situação_00<6):
                                                        print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                        input("")
                                            break
                                else:
                                    input(" - Isso aí! Você me venceu!")
                                    situação_00=situação_00+1
                                    situação_05=1
                                    if(situação_00==6):
                                        temporário= True
                                    else:
                                        if(situação_00==2):
                                            input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                        else:
                                            if(situação_00>=3 and situação_00<6):
                                                print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                input("")
                                        
                        else:
                            input("Você já lutou aqui!")
                    else:
                        if(ação_do_personagem=="31"):
                            if(situação_06 == 0):
                                input(" - Você é o desafiante??? Parece um fracote!")
                                nome_do_inimigo="Estudante Briguento \n do Quarto 31"
                                vida_máxima_inimigo=130
                                vida_atual_inimigo=130
                                ataque_do_inimigo=13
                                defesa_do_inimigo=4
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Você é mesmo um fracote!")
                                    input(" - Vá se curar para continuar tentando subir para o quarto andar!")
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - Volte aqui seu fracote! Não seja um covarde! Você não pode fugir de TODAS as lutas!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Você é mesmo um fracote!")
                                                input(" - Vá se curar para continuar tentando subir para o quarto andar!")
                                                break
                                            else:
                                                input(" - Não vacile com os caras lá do quarto andar, eles não pegam leve!")
                                                situação_00=situação_00+1
                                                situação_06=1
                                                if(situação_00==6):
                                                    temporário= True
                                                else:
                                                    if(situação_00==2):
                                                        input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                    else:
                                                        if(situação_00>=3 and situação_00<6):
                                                            print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                            input("")
                                                break
                                    else:
                                        input(" - Não vacile com os caras lá do quarto andar, eles não pegam leve!")
                                        situação_00=situação_00+1
                                        situação_06=1
                                        if(situação_00==6):
                                            temporário= True
                                        else:
                                            if(situação_00==2):
                                                input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                            else:
                                                if(situação_00>=3 and situação_00<6):
                                                    print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                    input("")
                            else:
                                input("Voce já lutou aqui!")
                        else:
                            if(ação_do_personagem=="32"):
                                if(situação_07==0):
                                    input(" - Cai dentro, rapá!")
                                    nome_do_inimigo="Estudante Briguento \n do Quarto 32"
                                    vida_máxima_inimigo=100
                                    vida_atual_inimigo=100
                                    ataque_do_inimigo=8
                                    defesa_do_inimigo=8
                                    batalha()
                                    if(vida_atual_personagem<=0):
                                        vida_atual_personagem=1
                                        input(" - Moleque criado a leite com pêra!")
                                        input(" - Lá em cima ninguém vai te dar essa colher de chá que eu to te dando!")
                                    else:
                                        if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                            while (vida_atual_inimigo>0):
                                                input(" - Ramelão, não foge da luta, não!")
                                                batalha()
                                                if(vida_atual_personagem<=0):
                                                    vida_atual_personagem=1
                                                    input(" - Moleque criado a leite com pêra!")
                                                    input(" - Lá em cima ninguém vai te dar essa colher de chá que eu to te dando!")
                                                    break
                                                else:
                                                    input(" - Nada mal, quem sabe você consegue o prêmio! Nunca se sabe... ")
                                                    situação_00=situação_00+1
                                                    situação_07=1
                                                    if(situação_00==6):
                                                        temporário= True
                                                    else:
                                                        if(situação_00==2):
                                                            input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                        else:
                                                            if(situação_00>=3 and situação_00<6):
                                                                print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                                input("")
                                                    break
                                        else:
                                            input(" - Nada mal, quem sabe você consegue o prêmio! Nunca se sabe... ")
                                            situação_00=situação_00+1
                                            situação_07=1
                                            if(situação_00==6):
                                                temporário= True
                                            else:
                                                if(situação_00==2):
                                                    input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                else:
                                                    if(situação_00>=3 and situação_00<6):
                                                        print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                        input("")
                                else:
                                    input("Voce já lutou aqui!")
                            else:
                                if(ação_do_personagem=="33"):
                                    if(situação_08==0):
                                        input(" - ÔÔô, CIDADÃO!")
                                        nome_do_inimigo="Estudante Briguento \n do Quarto 33"
                                        vida_máxima_inimigo=120
                                        vida_atual_inimigo=120
                                        ataque_do_inimigo=10
                                        defesa_do_inimigo=8
                                        batalha()
                                        if(vida_atual_personagem<=0):
                                            vida_atual_personagem=1
                                            input(" - Olha lá, o cara não aguenta e depois vai chorando pra casa!")
                                            input(" - Se você continuar tropeçando assim, cedo ou tarde o mundo vai te atropelá!")
                                        else:
                                            if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                                while (vida_atual_inimigo>0):
                                                    input(" - Tá na hora de acordar pra vida, cidadão!")
                                                    batalha()
                                                    if(vida_atual_personagem<=0):
                                                        vida_atual_personagem=1
                                                        input(" - Olha lá, o cara não aguenta e depois vai chorando pra casa!")
                                                        input(" - Se você continuar tropeçando assim, cedo ou tarde o mundo vai te atropelá!")
                                                        break
                                                    else:
                                                        input(" - ACORDA CARA! Você não é mais nenhum menininho bobinho, não! ")
                                                        situação_00=situação_00+1
                                                        situação_08=1
                                                        if(situação_00==6):
                                                            temporário= True
                                                        else:
                                                            if(situação_00==2):
                                                                input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                            else:
                                                                if(situação_00>=3 and situação_00<6):
                                                                    print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                                    input("")
                                                        break
                                            else:
                                                input(" - ACORDA CARA! Você não é mais nenhum menininho bobinho, não! ")
                                                situação_00=situação_00+1
                                                situação_08=1
                                                if(situação_00==6):
                                                    temporário= True
                                                else:
                                                    if(situação_00==2):
                                                        input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                    else:
                                                        if(situação_00>=3 and situação_00<6):
                                                            print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                            input("")
                                    else:
                                        input("Você já lutou aqui!")
                                else:
                                    if(ação_do_personagem=="34"):
                                        if(situação_09==0):
                                            input(" - Qual é, velho? O negócio é descer o murro de ferro na cara do inimigo!")
                                            nome_do_inimigo="Estudante Briguento \n do Quarto 34"
                                            vida_máxima_inimigo=66.6
                                            vida_atual_inimigo=66.6
                                            ataque_do_inimigo=10
                                            defesa_do_inimigo=15
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Você não tem um sangue fervente o suficiente para derreter o metal!")
                                                input(" - Você precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                            else:
                                                if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                                    while (vida_atual_inimigo>0):
                                                        input(" - As mentiras já são antigas demais, mas você não quer saber!\nCorrer é uma futilidade!")
                                                        batalha()
                                                        if(vida_atual_personagem<=0):
                                                            vida_atual_personagem=1
                                                            input(" - Você não tem um sangue fervente o suficiente para derreter o metal!")
                                                            input(" - Você precisa cauterizar suas feridas para chagas maiores tomarem o resto do seu corpo!")
                                                            break
                                                        else:
                                                            input(" - A verdade é mais dura que o aço! Mas a visão nunca morre!")
                                                            situação_00=situação_00+1
                                                            situação_09=1
                                                            if(situação_00==6):
                                                                temporário= True
                                                            else:
                                                                if(situação_00==2):
                                                                    input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                                else:
                                                                    if(situação_00>=3 and situação_00<6):
                                                                        print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                                        input("")
                                                            break
                                                else:
                                                    input(" - A verdade é mais dura que o aço! Mas a visão nunca morre!")
                                                    situação_00=situação_00+1
                                                    situação_09=1
                                                    if(situação_00==6):
                                                        temporário= True
                                                    else:
                                                        if(situação_00==2):
                                                            input("Você já venceu 1 luta do desafio dos estudantes briguentos!")
                                                        else:
                                                            if(situação_00>=3 and situação_00<6):
                                                                print("Você já venceu",situação_00-1,"lutas do desafio dos estudantes briguentos!")
                                                                input("")
                                        else:
                                            input("Você já lutou aqui!")
                                    else:
                                        if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                            save()
                                        else:
                                            input("Entrada Inválida!")

#--Seu prédio: Segundo Andar--#
def seuPrédioSegundoAndar():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas
    if(variável_lugar == "seu prédio, 3º andarb" or variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioTerceiroAndar()
    variável_lugar = "seu prédio, 2º andar"
    while 1:
        if(vida_atual_personagem<=0):break
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\n\nchecar os quartos\n")
        if(situação_02==1):
            print("\narrombar o quarto 24")
        print("\nver ficha do personagem\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", nome_do_jogador,", o que você vai fazer?\n")
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
                input("Você subiu para o terceiro andar, lá você encontrou cinco quartos de portas abertas e outra escada ascendente.")
                seuPrédioTerceiroAndar()
                if(vida_atual_personagem<=0):break
            else:
                if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                    input("Você desceu para o primeiro andar, o andar do seu quarto.")
                    break
                else:
                    if(ação_do_personagem=="20"):
                        if(situação_03==10):
                            input("Você já pegou tudo o que tinha para pegar aqui.")
                        else:
                            input("Você bate na porta e percebe, pelo barulho do trepidar da maçaneta, que ela está destrancada...")
                            print("Abrir a porta?(sim ou não)")
                            while 1:
                                ação_do_personagem = input("-")
                                ação_do_personagem = ação_do_personagem.lower()
                                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                    input("Você entrou, não havia ninguém...")
                                    input("Ao revistar o quarto você encontrou 30 Reais.")
                                    dinheiro_do_personagem=dinheiro_do_personagem+30
                                    situação_10=1
                                    break
                                else:
                                    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                        input("Você ignorou o quarto...")
                                        break
                                    else:
                                        input('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                    else:
                        if(ação_do_personagem=="21"):
                            if(situação_03==7):
                                input("Você bate na porta...")
                                input(" - Olá! - diz o avô do garoto - Muito obrigado por treinar o meu neto,")
                                input("agora ele não precisa se esconder mais dos trombadinhas da escola.")
                            if(situação_03==6):
                                input(" - Obrigado por me treinar, senhor.")
                                nome_do_inimigo="Garoto, um Homem."
                                vida_máxima_inimigo=20000
                                vida_atual_inimigo=20000
                                ataque_do_inimigo=1500
                                defesa_do_inimigo=1000
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Me supere. Estarei te esperando.")
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - Não abandone nossa luta!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Me supere. Estarei te esperando.")
                                            else:
                                                if(vida_atual_inimigo<=0):
                                                    input(" - Obrigado, mesmo!")
                                                    situação_03=7
                                    else:
                                        if(vida_atual_inimigo<=0):
                                            input(" - Obrigado, mesmo!")
                                            situação_03=7
                            if(situação_03==5):
                                input(" - Estou empolgado! Não aguentava mais esperar pela nossa luta!")
                                nome_do_inimigo="Garoto Forte"
                                vida_máxima_inimigo=2000
                                vida_atual_inimigo=2000
                                ataque_do_inimigo=100
                                defesa_do_inimigo=150
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - A nossa luta não acabou ainda!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                            else:
                                                if(vida_atual_inimigo<=0):
                                                    input(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                                    situação_03=6
                                    else:
                                        if(vida_atual_inimigo<=0):
                                            input(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                            situação_03=6
                            if(situação_03==4):
                                input(" - Dessa vez não vou perder tão fácil!")
                                nome_do_inimigo="Garoto Sério"
                                vida_máxima_inimigo=200
                                vida_atual_inimigo=200
                                ataque_do_inimigo=30
                                defesa_do_inimigo=25
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Estou te levando a sério, não vou perder mais!")
                                    input(" - Estarei te esperando para uma revanche.")
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - Honre a nossa luta até o fim!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Estou te levando a sério, não vou perder mais!")
                                                input(" - Estarei te esperando para uma revanche.")
                                            else:
                                                if(vida_atual_inimigo<=0):
                                                    input(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                                    situação_03=5
                                    else:
                                        if(vida_atual_inimigo<=0):
                                            input(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                            situação_03=5
                            if(situação_03==3):
                                input(" - Eu estava te esperando, panaca!")
                                nome_do_inimigo="Garoto Convencido"
                                vida_máxima_inimigo=110
                                vida_atual_inimigo=110
                                ataque_do_inimigo=8
                                defesa_do_inimigo=12
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Não aguenta o tranco, não? Hahaha!")
                                    input(" - Volte qualquer hora para apanhar mais!")
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - Volte aqui seu panaca!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Não aguenta o tranco, não? Hahaha!")
                                                input(" - Volte qualquer hora para apanhar mais!")
                                            else:
                                                if(vida_atual_inimigo<=0):
                                                    input(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                                    situação_03=4
                                    else:
                                        if(vida_atual_inimigo<=0):
                                            input(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                            situação_03=4
                            if(situação_03==2):
                                input(" - Meu avô disse que você viria... - disse o garoto baixinho - Vamos logo ao que interessa!")
                                nome_do_inimigo="Garoto Fracote"
                                vida_máxima_inimigo=100
                                vida_atual_inimigo=100
                                ataque_do_inimigo=3
                                defesa_do_inimigo=10
                                batalha()
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                    input(" - Você não é tão forte quanto meu avô falou.")
                                    situação_03=3
                                else:
                                    if(vida_atual_inimigo>0 and vida_atual_personagem>1):
                                        while (vida_atual_inimigo>0):
                                            input(" - Meu avô disse para não parar de lutar até eu não aguentar mais!")
                                            batalha()
                                            if(vida_atual_personagem<=0):
                                                vida_atual_personagem=1
                                                input(" - Você não é tão forte quanto meu avô falou.")
                                                situação_03=3
                                            else:
                                                if(vida_atual_inimigo<=0):
                                                    input(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                                    situação_03=3
                                    else:
                                        if(vida_atual_inimigo<=0):
                                            input(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                            situação_03=3
                            if(situação_03==1):
                                input("A porta está trancada.")
                            if(situação_03==0):
                                input("Você bateu na porta...")
                                input("Um senhor baixo e fracote abriu a porta... Ele parecia muito com um frango")
                                input(" - O que que você quer?!")
                                input("...")
                                input(" - Saia daqui então!")
                                nome_do_inimigo="Senhor Doente"
                                vida_máxima_inimigo=50
                                vida_atual_inimigo=50
                                ataque_do_inimigo=5
                                defesa_do_inimigo=3
                                batalha()
                                if(vida_atual_personagem<=0):break
                                if(vida_atual_inimigo>0):
                                    input("Depois de se afastar o senhor começou a gritar...")
                                    input("Com a mão no peito, ele começou a tossir...")
                                    input(" - Ahhhh... - gemiu o senhor que caia lentamente.")
                                    input(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                    input("O menino pegou o senhor nos braços antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
                                    input(" - VOCÊ VAI PAGAR CARO!")
                                    nome_do_inimigo="Garoto Perturbado"
                                    vida_máxima_inimigo=100
                                    vida_atual_inimigo=100
                                    ataque_do_inimigo=3
                                    defesa_do_inimigo=10
                                    batalha()
                                    if(vida_atual_personagem<=0):break
                                    if(vida_atual_inimigo>0):
                                        input(" - SAIA JÁ DAQUI!")
                                        input("Em seguida ele fechou e trancou a porta.")
                                        situação_03==1
                                    else:
                                        input("O garoto caiu no chão dentro da casa e começou a chorar.")
                                        input(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                        input("Em seguida ele fechou e trancou a porta.")
                                        situação_03=1
                                else:
                                    input("O senhor caiu no chão com uma mão no peito...")
                                    input("Ele tentava gritar algo enquanto estendia a outra mão...")
                                    input("Mas não conseguia dizer nada, estava tendo crise de asma...")
                                    input("Sua mão apontava para um lugar dentro da casa...")
                                    print("Vai ajudar o idoso?\n")
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            input("Você entrou na casa, pegou a bombinha em cima da mesa e a apertou na boca no velho...")
                                            input(" - Ah... Ah... - o senhor tentava recuperar o ar - Você não é um mau rapaz no fim das contas...")
                                            input(" - ...")
                                            input(" - Você gosta de lutar, não é garoto? Eu brigava muito quando era mais jovem...")
                                            input(" - ...")
                                            input(" - Nem sempre os punhos são o bastante...")
                                            input(" - ...")
                                            input(" - Não falo do coração na luta, isso você já tem, falo de armas...")
                                            input(" - Tome... Eu usava este punhal no meu tempo... Agora é seu.")
                                            equipamento_mãos = "Punhal Envelhecido"
                                            ataque_do_personagem = ataque_do_personagem+10
                                            input("Seu ataque aumentou em 10 pontos!")
                                            input(" - Se não for pedir demais, venha sempre que puder para treinar o meu neto... Ele ainda é muito fraco e eu não tenho mais o mesmo vigor de antes...")
                                            situação_03=2
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                input(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                                input("O menino pegou o senhor nos braços antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
                                                input(" - VOCÊ VAI PAGAR CARO!")
                                                nome_do_inimigo="Garoto Irritado"
                                                vida_máxima_inimigo=100
                                                vida_atual_inimigo=100
                                                ataque_do_inimigo=10
                                                defesa_do_inimigo=10
                                                batalha()
                                                if(vida_atual_personagem<=0):break
                                                if(vida_atual_inimigo>0):
                                                    input(" - SAIA JÁ DAQUI!")
                                                    input("Em seguida ele fechou e trancou a porta.")
                                                    situação_03=1
                                                else:
                                                    input("O garoto caiu no chão dentro da casa e começou a chorar.")
                                                    input(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                                    input("Em seguida ele fechou e trancou a porta.")
                                                    situação_03=1
                                                break
                                            else:
                                                input('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                        else:
                            if(ação_do_personagem=="22"):
                                if(situação_04==4):
                                    input("Voce bateu na porta...")
                                    input("Ninguém te atendeu.")
                                if(situação_04==3):
                                    input(" - E aí, rapaz!")
                                    teste_de_sorte = random.randrange(3)
                                    if(teste_de_sorte==1):
                                        input(" - Você chegou em boa hora! Entre e coma um pedaço de pizza comigo!")
                                        input("Você recuperou 50 pontos de vida!")
                                        vida_atual_personagem = vida_atual_personagem + 50
                                        if(vida_atual_personagem>(vida_máxima_personagem+100)):
                                            vida_atual_personagem=vida_máxima_personagem+100
                                        input(" - Até outra hora, vizinho!")
                                    else:
                                        input(" - Estou sem pizza agora... Talvez mais tarde...")
                                if(situação_04==2):
                                    input(" - O quê você quer aqui?")
                                    print("Você vai dizer a ele que comeu a sua pizza?(sim ou não)")
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            input(" - ...")
                                            input(" - VOCÊ...")
                                            input(" - Você é muito cara de pau mesmo, mas adimiro a sua sinceridade.")
                                            input(" - Eu sempre como pizza, quando você quiser passe aqui para pegar um pedaço.")
                                            situação_04=3
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                input(" - ...")
                                                input(" - Me deixe em paz!")
                                                situação_04=4
                                                break
                                            else:
                                                input('Entrada inválida! Digite "sim" ou "não".')
                                if(situação_04==1):
                                    input("Você bateu na porta do quarto, que agora está fechado.")
                                    input("Você escuta passos rápidos e violentos vindo à porta")
                                    input(" - EU TO MUITO PUTO! - diz o estudante que abriu violentamente a porta - ENTRARAM E COMERAM A MINHA PIZZA!")
                                    input("...")
                                    input(" - Ah esquece... Nem deve ter sido você...")
                                    situação_04=2
                                if(situação_04==0):
                                    input("O quarto está aberto, você entra e vê um estudante vagabundo dormindo num sofá com uma pizza no colo.")
                                    print("E aí, vai pegar essa pizza? (sim ou não)\n")
                                    while 1:
                                        ação_do_personagem = input("-")
                                        ação_do_personagem = ação_do_personagem.lower()
                                        if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                            input("Você comeu a pizza e recuperou todos os seus pontos de vida!")
                                            vida_atual_personagem=vida_máxima_personagem
                                            situação_04=1
                                            break
                                        else:
                                            if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                input("Você deixou a pizza para depois!")
                                                break
                                            else:
                                                input('Entrada inválida! Digite "sim" ou "não".')
                            else:
                                if(ação_do_personagem=="23"):
                                   input("Você vê um quarto aberto, sujo e vazio...")
                                   input("Parece abandonado por um bom tempo... Já tem fauna e flora prória!")
                                else:
                                    if(ação_do_personagem=="24"):
                                        if(situação_02==0):
                                            input("Você encara um indivíduo de aparencia extravagante e vulgar encostado no batente da porta...")
                                            input(" - Qualé merh-mão? Tá querenu tretá?")
                                            nome_do_inimigo="Mané de Boné"
                                            vida_máxima_inimigo=100
                                            vida_atual_inimigo=100
                                            ataque_do_inimigo=10
                                            defesa_do_inimigo=5
                                            batalha()
                                            if(vida_atual_personagem<=0):break
                                            if(vida_atual_inimigo>0):
                                                input("Ele corre atrás de você e te dá um chute no joelho!")
                                                input("!!!")
                                                input("Você perdeu 30 pontos de vida!")
                                                input(" - Fica diboa rapáh!")
                                                vida_atual_personagem=vida_atual_personagem-30
                                                input("Ele voltou ao batente da porta do quarto e agora está te encarando...")
                                                input("Você me envergonha.")
                                            else:
                                                input(" - Que isso maluco?! Que isso?!")
                                                input("Ele entrou cambaleando para o quarto dele e se trancou!")
                                                situação_02=1
                                        if(situação_02==1):
                                            input("O quarto está trancado...")
                                        if(situação_02==2):
                                            input("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            input("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            input("Dentro você vê muito sangue pelo quarto, os poucos móveis quebrados, ")
                                            input("mas nada de valor...")
                                            matarAlguém()
                                        if(situação_02==3):
                                            input("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            input("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            input("Também escuta, vindo lá de dentro, soluços em sussurros e sussurros em soluços...")
                                            input("Melhor não entrar... Não há nada de mais lá dentro.")
                                    else:
                                        if(ação_do_personagem=="arrombar a porta do quarto 24" or ação_do_personagem=="arrombar o quarto 24" or ação_do_personagem=="arrombar" or ação_do_personagem=="arrombar a porta" or ação_do_personagem=="entrar no quarto 24"):
                                            if(situação_02==1):
                                                input("Você pisoteou a porta e entrou no quarto!")
                                                input(" - Não, por favor nao!...")
                                                while 1:
                                                    if(situação_02==2):
                                                        break
                                                    if(situação_02==3):
                                                        break
                                                    print("Melhor não continuar...(sim ou não)\n")
                                                    ação_do_personagem=input("-")
                                                    ação_do_personagem=ação_do_personagem.lower()
                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                        while 2:
                                                            print("Eu insisto... É melhor parar... Você está de cabeça quente... (sim ou não)\n")
                                                            ação_do_personagem=input("-")
                                                            ação_do_personagem=ação_do_personagem.lower()
                                                            if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                ação_do_personagem=input("-")
                                                                ação_do_personagem=ação_do_personagem.lower()
                                                                input("!!!!!!!!!!!!")
                                                                input(" - NÃO, NÃO!")
                                                                input("!!!!!!!!!!!!")
                                                                input(" - N-NÃo..o!")
                                                                input("!!!!!!!!....")
                                                                input("!!!!........")
                                                                input("....!!!!....")
                                                                input("........!!!!")
                                                                input("!!!!....!!!!")
                                                                input("Seus punhos vermelhos tremem...")
                                                                input("Você o espancou até a morte...")
                                                                input("...")
                                                                matarAlguém()
                                                                situação_02=2
                                                                break
                                                            else:
                                                                if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                    input("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                                    vida_máxima_personagem=vida_máxima_personagem+50
                                                                    vida_atual_personagem=vida_máxima_personagem
                                                                    situação_02=3
                                                                    break
                                                                else:
                                                                    input("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                                                        break
                                                    else:
                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                            input("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                            vida_atual_personagem=vida_máxima_personagem
                                                            situação_02=3
                                                            break
                                                        else:
                                                            input("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                                            if(situação_04==2):
                                                matarAlguém()
                                            if(situação_02==3):
                                                input("Você já fez o bastante por aqui... Melhor se afastar.")
                                        else:
                                            if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                                save()
                                            else:
                                                input('Entrada Inválida!')

#--Seu prédio: Primeiro Andar--#
def seuPrédioPrimeiroAndar():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas
    if(variável_lugar == "seu prédio, 2º andarb" or variável_lugar == "seu prédio, 3º andarb" or variável_lugar == "seu prédio, 4º andarb"):
        seuPrédioSegundoAndar()
    if(vida_atual_personagem>0):
        variável_lugar = "seu prédio, 1º andar"
        print("Agora você está no corredor do primeiro andar do seu prédio.")
        time.sleep(3)
        print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\nolhar\n")
        time.sleep(1)
        if (olhar_o_cenário == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            time.sleep(1)
            if (cheirar_o_cenário == "sim" and objeto_00 == "não"):
                print("olhar o bêbado\n")
                time.sleep(1)
        if(objeto_01 == "sim"):
            print("\narrombar o quarto 10\n")
            time.sleep(1)
        if (objeto_00 == "1"):
            print("\nacordar o bêbado\n")
            print("\nrevistar o bêbado\n")
            time.sleep(1)
        if (objeto_00 == "2"):
            print("\nmover o bêbado\n")
            time.sleep(1)
        if (objeto_00 == "3"):
            print("\natacar o bêbado\n")
            time.sleep(1)
        if (objeto_00 == "sim"):
            print("\nabrir a porta dos fundos\n")
            time.sleep(1)
        print("\nver ficha do personagem\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n", "\n#", "-"*30,"#\n")
        time.sleep(2)
        print("\nO que você vai fazer, ", nome_do_jogador, "?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()
    while 1:
        if(vida_atual_personagem<=0):break
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
                if (cheirar_o_cenário == "1" or cheirar_o_cenário == "sim"):
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
                    if (objeto_00 == "sim"):
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
                        olhar_o_cenário = "sim"
            else:
                if(ação_do_personagem=="cheirar" or ação_do_personagem=="cherar" or ação_do_personagem=="dar um tapa" or ação_do_personagem=="cheira" or ação_do_personagem=="chera"):
                    if(cheirar_o_cenário=="não"):
                        cheirar_o_cenário="sim"
                    print("Você sente um cheiro forte de álcool e vômito")
                    time.sleep(3)
                else:
                    if(ação_do_personagem=="10"):
                        if(equipamento_capa=="Jaqueta de Couro"):
                            print("Você vê uma porta arrombada... Não há mais nada de interessante dentro do quarto.")
                            time.sleep(3)
                        else:
                            print("Você bateu na porta, mas ninguém atendeu... Ela parece fácil de ser arrombada...")
                            time.sleep(3)
                            objeto_01="sim"
                    else:
                        if(ação_do_personagem=="11"):
                            if(situação_01==0):
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
                                vida_atual_personagem=vida_atual_personagem-5
                                if(vida_atual_personagem<=0):
                                    vida_atual_personagem=1
                                situação_01=1
                            else:
                                if(situação_01==1):
                                    print("Você empurrou a porta sem fechadura, mas moradora que ainda estava te toalha, furiosamente fechou a porta gritando, antes que você pudesse terminar de abrir!")
                                    time.sleep(3)
                                    print("Você perdeu 5 pontos de vida ao cair no corredor...")
                                    time.sleep(3)
                                    vida_atual_personagem=vida_atual_personagem-5
                                    if(vida_atual_personagem<=0):
                                        vida_atual_personagem=1
                                    situação_01=2
                                else:
                                    if(situação_01==2):
                                        print("Você abriu a porta e levou um soco na cara, caindo em seguida no chão do corredor.")
                                        time.sleep(3)
                                        print("Você perdeu 10 pontos de vida...")
                                        time.sleep(3)
                                        vida_atual_personagem=vida_atual_personagem-10
                                        if(vida_atual_personagem<=0):
                                            vida_atual_personagem=1
                                        situação_01=3
                                    else:
                                        if(situação_01==3):
                                            print("Você abriu a porta e viu a mulher de toalha extremamente furiosa com os ombros levemente curvados, deixando à mostra seus braços musculosos e gigantescos.")
                                            time.sleep(3)
                                            print(" - VOCÊ VAI APANHAR MUITO AGORA!")
                                            time.sleep(3)
                                            nome_do_inimigo="Mulher de Toalha"
                                            vida_máxima_inimigo=800
                                            vida_atual_inimigo=800
                                            ataque_do_inimigo=20
                                            defesa_do_inimigo=20
                                            batalha()
                                            if(vida_atual_personagem<=0):break
                                            if(vida_atual_inimigo>0):
                                                print(" - E NÃO VOLTE MAIS AQUI!")
                                                time.sleep(3)
                                            else:
                                                input("A mulher caiu inconsciente no chão...")
                                                input("Dentro da casa você encontrou 200 reais e um suplemento alimentício")
                                                input("Você tomou o suplemento e aumentou seu ataque em 5 pontos!")
                                                dinheiro_do_personagem=dinheiro_do_personagem+200
                                                ataque_do_personagem=ataque_do_personagem+5
                                                situação_01=4
                                        else:
                                            if(situação_01==4):
                                                input("Você entra no quarto, encontra a mulher que você derrotou caida no chão e mais nada além dos móveis velhos dela.")
                        else:
                            if(ação_do_personagem=="12"):
                                input("Você bateu na porta...")
                                input(" - Já vai! - exclama uma senhora de dentro da casa.")
                                input("...")
                                input(" - Olá, meu jovem! Por que você não entra e prova um pouco do bolo que eu acabei de fazer?")
                                input("...")
                                input("Você recurperou TODOS os seus pontos de vida!")
                                vida_atual_personagem=vida_máxima_personagem
                            else:
                                if(ação_do_personagem=="14"):
                                    input("Você bateu na porta...")
                                    input(" - JÁ DISSE PARA VOCÊ IR EMBORA SEU BÊBADO! - grita uma mulher de dentro da casa - NINGUÉM TE MERECE COMO MARIDO!")
                                else:
                                    if(ação_do_personagem=="13"):
                                        input("Você é bobo?")
                                        input("Esse é o seu quarto!")
                                        input("Você está atrasado demais para voltar!")
                                    else:
                                        if(ação_do_personagem=="arrombar a porta do quarto 10" or ação_do_personagem=="arrombar 10" or ação_do_personagem=="arrombar quarto 10" or ação_do_personagem=="arrombar o quarto 10" or ação_do_personagem=="arrombar" or ação_do_personagem=="arrombar a porta" or ação_do_personagem=="quarto 10" or ação_do_personagem=="entrar no quarto 10"):
                                            if(objeto_03=="sim"):
                                                input("Você já arrombou essa porta... Não há mais nada de interessante dentro do quarto.")
                                            else:
                                                input("Você entrou no quarto e encontrou uma Jaqueta de Couro!")
                                                input("Você a vestiu.")
                                                input("Sua defesa aumentou em 6 pontos!")
                                                equipamento_capa="Jaqueta de Couro"
                                                defesa_do_personagem=defesa_do_personagem+6
                                                objeto_03="sim"
                                        else:
                                            if(ação_do_personagem=="subir as escadas" or ação_do_personagem=="subir" or ação_do_personagem=="subir escadas" or ação_do_personagem=="subi" or ação_do_personagem=="subi as escadas" or ação_do_personagem=="subir escada" or ação_do_personagem=="subi escada" or ação_do_personagem=="subi a escada" or ação_do_personagem=="sobe"):
                                                input("Você subiu para o segundo andar, lá você encontrou mais cinco quartos e outra escada ascendente.")
                                                seuPrédioSegundoAndar() #MUDA DE MAPA SEM SALVAR
                                                if(vida_atual_personagem<=0):break
                                            else:
                                                if(ação_do_personagem=="olhar o bêbado" or ação_do_personagem=="olhar bêbado" or ação_do_personagem=="olha o bêbado" or ação_do_personagem=="olha bÊbado" or ação_do_personagem=="olhar o bebado" or ação_do_personagem=="olhar bebado" or ação_do_personagem=="olha o bebado" or ação_do_personagem=="olha bebado"):
                                                    objeto_00="1"
                                                    input("Você vê um homem de 40 anos, coberto por cacos de vidro, bebida e vômito, dormindo no chão.")
                                                else:
                                                    if(ação_do_personagem=="revistar o bêbado" or ação_do_personagem=="revistar bêbado" or ação_do_personagem=="revistar" or ação_do_personagem=="revista bêbado" or ação_do_personagem=="revista o bêbado" or ação_do_personagem=="revistar o bebado" or ação_do_personagem=="revistar bebado" or ação_do_personagem=="revistar" or ação_do_personagem=="revista bebado" or ação_do_personagem=="revista o bebado"):
                                                        if(objeto_02=="não"):
                                                            input("Você achou um energético!")
                                                            input("Você aumentou o limite da vida em 50 pontos ao beber o energético!")
                                                            input("E também recuperou seus pontos atuais de vida ao novo limite estabelecido!")
                                                            vida_máxima_personagem=vida_máxima_personagem+50
                                                            vida_atual_personagem=vida_máxima_personagem
                                                            objeto_02="sim"
                                                        else:
                                                            input("Você não encontrou mais nada...\n")
                                                    else:
                                                        if(ação_do_personagem=="acordar o bêbado" or ação_do_personagem=="acordar bêbado" or ação_do_personagem=="acorda o bêbado" or ação_do_personagem=="acorda bêbado" or ação_do_personagem=="acordar o bebado" or ação_do_personagem=="acordar bebado" or ação_do_personagem=="acorda o bebado" or ação_do_personagem=="acorda bebado"):
                                                            objeto_00="2"
                                                            input("Você tenta acordar o bêbado, mas não consegue...")
                                                        else:
                                                            if(ação_do_personagem=="mover o bêbado" or ação_do_personagem=="mover bêbado" or ação_do_personagem=="move o bêbado" or ação_do_personagem=="move bêbado" or ação_do_personagem=="mover o bebado" or ação_do_personagem=="mover bebado" or ação_do_personagem=="move o bebado" or ação_do_personagem=="move bebado" or ação_do_personagem=="mover" or ação_do_personagem=="move"):
                                                                objeto_00="3"
                                                                input("Você pensa em mover o bêbado, mas o cheiro e a sujeira fazem você vomitar em cima dele!")
                                                                input("...")
                                                                input("Ele continua dormindo...")
                                                            else:
                                                                if(ação_do_personagem=="atacar o bêbado" or ação_do_personagem=="atacar bêbado" or ação_do_personagem=="ataca o bêbado" or ação_do_personagem=="ataca bêbado" or ação_do_personagem=="atacar o bebado" or ação_do_personagem=="atacar bebado" or ação_do_personagem=="ataca o bebado" or ação_do_personagem=="ataca bebado" or ação_do_personagem=="atacar" or ação_do_personagem=="ataca"):
                                                                    if(objeto_00!="sim" or objeto_00!="pegou o dinheiro"):
                                                                        input("Você chuta várias vezes o bêbado violentamente!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input("!!!")
                                                                        input(" - P-PARA! PARA! PARA! - berra o bêbado que acabou de acordar.")
                                                                        input("Ele se levanta e te empurra ganhando distância.")
                                                                        input("...")
                                                                        input(" - Ssseu muleque i-insstrosmestido!... *hic*\n")
                                                                        nome_do_inimigo="Bêbado"
                                                                        vida_máxima_inimigo=500
                                                                        vida_atual_inimigo=30
                                                                        ataque_do_inimigo=4
                                                                        defesa_do_inimigo=4
                                                                        batalha()
                                                                        if(vida_atual_personagem<=0):break
                                                                        if(vida_atual_inimigo>0):
                                                                            input("Você escapa da briga, mas em seguida o bêbado tosse sangue e cái no chão...")
                                                                        else:
                                                                            input("O bêbado coberto de bebida, vômito e sangue, cái de costas no chão,")
                                                                            input("sendo empalado pelos diversos cacos de vidro...")
                                                                            input("O sangue dele escorre pelo corredor até os seus pés...")
                                                                            input("Você vira o rosto fechando os olhos e abaixando os punhos...")
                                                                            input("Agora, desencostado da porta dos fundos, o bêbado já não é mais um impecílio...")
                                                                        objeto_00="sim"
                                                                else:
                                                                    if(ação_do_personagem=="abrir a porta dos fundos"):
                                                                        if(objeto_00=="sim"):
                                                                            input("Você abre a porta... ")
                                                                            input("É um armário de limpesa.")
                                                                            input("Em meio às vassouras, rodos e outras coisas, você encontra uma mala...")
                                                                            input("Você abre a mala, encontra entre os materiais de escritório e 10 Reais!")
                                                                            dinheiro_do_personagem=dinheiro_do_personagem+10
                                                                            objeto_00="pegou o dinheiro"
                                                                        else:
                                                                            if(objeto_00=="pegou o dinheiro"):
                                                                                input("Você vê materiais de limpesa e uma maleta aberta.")
                                                                            else:
                                                                                input("Não dá para abrir!")
                                                                    else:
                                                                        if(ação_do_personagem=="descer as escadas" or ação_do_personagem=="descer escadas" or ação_do_personagem=="descer escada" or ação_do_personagem=="descer a escada" or ação_do_personagem=="sair" or ação_do_personagem=="descer" or ação_do_personagem=="sair do prédio"):
                                                                            if(ponto_de_save==1):
                                                                                while 1:
                                                                                    input("Do lado de fora há um oponente forte.")
                                                                                    print("Tem certeza que está pronto para sair? (sim ou não)")
                                                                                    ação_do_personagem=input("-")
                                                                                    ação_do_personagem=ação_do_personagem.lower()
                                                                                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                                                                                        ação_do_personagem="sim"
                                                                                        break
                                                                                    else:
                                                                                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                                                                                            input("Você decidiu não sair do prédio.")
                                                                                            break
                                                                                        else:
                                                                                            input("Entrada inválida!")
                                                                                if(ação_do_personagem=="sim"):
                                                                                    input("Você desceu as escadas e saiu do prédio...")
                                                                                    break
                                                                            else:
                                                                                input("Você desceu as escadas e saiu do prédio...")
                                                                                suaRua()
                                                                                break
                                                                        else:
                                                                            if(ação_do_personagem == "salvar o jogo" or ação_do_personagem=="guardar o jogo" or ação_do_personagem == "salvar jogo" or ação_do_personagem=="guardar jogo" or ação_do_personagem == "salvar" or ação_do_personagem == "save" or ação_do_personagem == "save game" or ação_do_personagem == "salvar o progresso" or ação_do_personagem == "salvar progresso" or ação_do_personagem == "guardar o progresso" or ação_do_personagem == "guardar progresso" or ação_do_personagem == "save progress" or ação_do_personagem == "salva" or ação_do_personagem == "sava" or ação_do_personagem == "slvar" or ação_do_personagem == "svar" or ação_do_personagem == "svr" or ação_do_personagem == "slvr" or ação_do_personagem == "sav" or ação_do_personagem == "sve" or ação_do_personagem == "sv" or ação_do_personagem == "salvar o game" or ação_do_personagem == "guardar o game" or ação_do_personagem == "salvar game" or ação_do_personagem == "guardar game"):
                                                                                save()
                                                                            else:
                                                                                input('Entrada Inválida!')
        print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", variável_lugar,"\n\nVocê pode:\nolhar\n")
        if (olhar_o_cenário == "sim"):
            print("\ncheirar\nchecar os quartos\n")
            if (cheirar_o_cenário == "sim" and objeto_00 == "não"):
                print("olhar o bêbado\n")
        if(objeto_01 == "sim"):
            print("\narrombar o quarto 10\n")
        if (objeto_00 == "1"):
            print("\nacordar o bêbado\n")
            print("\nrevistar o bêbado\n")
        if (objeto_00 == "2"):
            print("\nmover o bêbado\n")
        if (objeto_00 == "3"):
            print("\natacar o bêbado\n")
        if (objeto_00 == "sim"):
            print("\nabrir a porta dos fundos\n")
        print("\nver ficha do personagem\nsubir as escadas\ndescer as escadas\n\nsalvar o jogo\n", "\n#", "-"*30,"#\n")
        print("\nO que você fará agora, ", nome_do_jogador,"?\n")
        ação_do_personagem = input("-")
        ação_do_personagem = ação_do_personagem.lower()

#--Sua Rua--#
def suaRua():
    global nome_do_jogador, nome_do_inimigo,reserva_nome_do_jogador, ação_do_personagem, batalha_escapar, equipamento_roupa, equipamento_capa, equipamento_luva, equipamento_mãos, equipamento_botas, olhar_o_cenário, modificar_o_cenário, cheirar_o_cenário, objeto_00, objeto_01, objeto_02, objeto_03,variável_lugar,mostrar_save,ponto_de_save, eegg, vida_máxima_personagem, vida_atual_personagem, dinheiro_do_personagem, ataque_do_personagem, defesa_do_personagem, agilidade_do_personagem,reserva_vida_máxima_personagem,reserva_vida_atual_personagem,reserva_ataque_do_personagem,reserva_defesa_do_personagem,reserva_agilidade_do_personagem, vida_máxima_inimigo, vida_atual_inimigo, ataque_do_inimigo, defesa_do_inimigo,situação_00, situação_01, situação_02, situação_03, situação_04,situação_05,situação_06,situação_07,situação_08,situação_09,situação_10, teste_de_sorte, calculo_do_dano, calculo_da_fuga, variável_para_comparar, contador_de_batalha, contador_de_rodadas


#####################----------------------------__BRIGA DE ESTUDANTE__----------------------------#####################
while 1:
    while (vida_atual_personagem>0):
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
                    nome_do_jogador = pickle.load(arq)
                    nome_do_inimigo = pickle.load(arq)
                    reserva_nome_do_jogador = pickle.load(arq)
                    ação_do_personagem = pickle.load(arq)
                    batalha_escapar = pickle.load(arq)
                    equipamento_roupa = pickle.load(arq)
                    equipamento_capa = pickle.load(arq)
                    equipamento_luva = pickle.load(arq)
                    equipamento_mãos = pickle.load(arq)
                    equipamento_botas = pickle.load(arq)
                    olhar_o_cenário = pickle.load(arq)
                    modificar_o_cenário = pickle.load(arq)
                    cheirar_o_cenário = pickle.load(arq)
                    objeto_00 = pickle.load(arq)
                    objeto_01 = pickle.load(arq)
                    objeto_02 = pickle.load(arq)
                    objeto_03 = pickle.load(arq)
                    variável_lugar = pickle.load(arq)
                    ponto_de_save = pickle.load(arq)
                    eegg = pickle.load(arq)
                    vida_máxima_personagem = pickle.load(arq)
                    vida_atual_personagem = pickle.load(arq)
                    dinheiro_do_personagem = pickle.load(arq)
                    ataque_do_personagem = pickle.load(arq)
                    defesa_do_personagem = pickle.load(arq)
                    agilidade_do_personagem = pickle.load(arq)
                    reserva_vida_máxima_personagem = pickle.load(arq)
                    reserva_vida_atual_personagem = pickle.load(arq)
                    reserva_ataque_do_personagem = pickle.load(arq)
                    reserva_defesa_do_personagem = pickle.load(arq)
                    reserva_agilidade_do_personagem = pickle.load(arq)
                    vida_máxima_inimigo = pickle.load(arq)
                    vida_atual_inimigo = pickle.load(arq)
                    ataque_do_inimigo = pickle.load(arq)
                    defesa_do_inimigo = pickle.load(arq)
                    situação_00 = pickle.load(arq)
                    situação_01 = pickle.load(arq)
                    situação_02 = pickle.load(arq)
                    situação_03 = pickle.load(arq)
                    situação_04 = pickle.load(arq)
                    situação_05 = pickle.load(arq)
                    situação_06 = pickle.load(arq)
                    situação_07 = pickle.load(arq)
                    situação_08 = pickle.load(arq)
                    situação_09 = pickle.load(arq)
                    situação_10 = pickle.load(arq)
                    teste_de_sorte = pickle.load(arq)
                    calculo_do_dano = pickle.load(arq)
                    calculo_da_fuga = pickle.load(arq)
                    variável_para_comparar = pickle.load(arq)
                    contador_de_batalha= pickle.load(arq)
                    contador_de_rodadas = pickle.load(arq)
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
            nome_do_jogador = input("-")
            while 1:
                print("Seu nome é", nome_do_jogador, "?")
                while 2:
                    ação_do_personagem = input("-")
                    ação_do_personagem = ação_do_personagem.lower()
                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                        break
                    else:
                        if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
                            print("\nEntão qual é o seu nome?\n")
                            nome_do_jogador = input("-")
                            break
                        else:
                            print('\nEntrada inválida, digite "sim" ou "não".\n')
                            time.sleep(0.5)
                if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                    break
            print("Muito prazer, ", nome_do_jogador,'.')
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
                        objeto_00="ganha presente"
                    else:
                        print('Não entendi o que você quis dizer...\nPor favor, digite "sim" ou "não".\n')
                    ação_do_personagem = input("-")
                    ação_do_personagem = ação_do_personagem.lower()
                    if(ação_do_personagem=="sim" or ação_do_personagem=="s" or ação_do_personagem=="si" or ação_do_personagem=="sm" or ação_do_personagem=="im" or ação_do_personagem=="ssim"):
                        ação_do_personagem="sim"
            if(objeto_00=="ganha presente"):
                print("\nÓtimo, ",nome_do_jogador,".")
                time.sleep(1)
                print("Acho que começamos com o pé direito! Fico feliz que você tenha me escutado como um bom garoto!")
                time.sleep(2)
                print("Por isso deixei um presente para você no seu guarda-roupas, tenho certeza que você ficará feliz.")
                time.sleep(2)
            else:
                print("Eu não me lembro de você...")
                time.sleep(5)
                print("Então você deve ser mesmo irrelevante!")
                time.sleep(5)

#####################----------------------------__INÍCIO DO JOGO__----------------------------#####################
            print("\nCenário: acabou de amanhecer, seu quarto está desarrumado,")
            time.sleep(2)
            print("você ainda está de pijama e atrasado para a aula - não que você se importe muito com isso.")
            time.sleep(3)
            print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar)
            time.sleep(2)
            print("\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
            time.sleep(2)
            if (olhar_o_cenário == "sim"):
                print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\nolhar pela janela\n")
                time.sleep(2)
            print("\nver ficha do personagem\nsair do quarto\n")
            time.sleep(1)
            print("\n#", "-"*30,"#\n")
            print("\nO que você vai fazer", nome_do_jogador,"?\n")
            ação_do_personagem = input("-")
            ação_do_personagem = ação_do_personagem.lower()
            while 1:
                if (ação_do_personagem == "ver ficha do personagem" or ação_do_personagem == "ver a ficha do personagem" or ação_do_personagem == "ver a ficha de personagem" or ação_do_personagem == "ficha" or ação_do_personagem=="ficha do personagem" or ação_do_personagem=="ficha de personagem" or ação_do_personagem=="ver ficha de personagem" or ação_do_personagem=="ver ficha" or ação_do_personagem == "olhar ficha do personagem" or ação_do_personagem == "ver minha ficha" or ação_do_personagem=="minha ficha" or ação_do_personagem=="ficha personagem" or ação_do_personagem=="olhar ficha de personagem" or ação_do_personagem=="olhar ficha"):
                    ficha_personagem()
                else:
                    if (ação_do_personagem== "vetir" or ação_do_personagem=="vest" or ação_do_personagem=="vesti" or ação_do_personagem=="veti" or ação_do_personagem=="estir" or ação_do_personagem=="esti" or ação_do_personagem=="etir" or ação_do_personagem == "vestir" or ação_do_personagem == "vestir uniforme" or ação_do_personagem == "vestir o uniforme" or ação_do_personagem == "vestir o uniforme estudantil" or ação_do_personagem == "vestir uniforme estudantil" or ação_do_personagem == "se vestir" or ação_do_personagem == "se vestir para a aula" or ação_do_personagem == "se vestir pra aula" or ação_do_personagem == "vestir para a aula" or ação_do_personagem == "me arrumar" or ação_do_personagem == "tomar banho" or ação_do_personagem == "ir ao banheiro" or ação_do_personagem == "cagar" or ação_do_personagem == "mijar" or ação_do_personagem == "fazer xixi" or ação_do_personagem == "trocar de roupa" or ação_do_personagem == "me trocar" or ação_do_personagem == "trocar"):
                        if (equipamento_roupa == "Pijama"):
                            print("Você se vestiu para a aula.\n")
                            time.sleep(1)
                            equipamento_roupa = "Uniforme Estudantil"
                            defesa_do_personagem=defesa_do_personagem+1
                            print("Sua defesa aumentou em 1 ponto!\n")
                            time.sleep(2)
                        else:
                            print("Você já está vestido para a aula!\n")
                            time.sleep(1)
                    else:
                        if (ação_do_personagem == "arrumar o quarto" or ação_do_personagem == "arrumar" or ação_do_personagem == "arrumar quarto" or ação_do_personagem == "arruma" or ação_do_personagem == "arruma o quarto" or ação_do_personagem == "arruma quarto" or ação_do_personagem == "quarto"):
                            if (modificar_o_cenário == "não"):
                                print("Você achou 30 Reais enquanto arrumava o seu quarto!\n")
                                time.sleep(2)
                                dinheiro_do_personagem = +30
                                modificar_o_cenário = "sim"
                            else:
                                print("Você já arrumou o seu quarto!\n")
                                time.sleep(1)
                        else:
                            if (ação_do_personagem == "olhar" or ação_do_personagem=="olh" or ação_do_personagem == "ver" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha" or ação_do_personagem == "olhar quarto" or ação_do_personagem == "olha quarto" or ação_do_personagem == "olhar o quarto" or ação_do_personagem == "olha o quarto" or ação_do_personagem == "ve" or ação_do_personagem == "vê"):
                                if (modificar_o_cenário == "não"):
                                    print("Você não consegue ver nada além de bagunça, MUITA BAGUNÇA!!!\n")
                                    time.sleep(2)
                                else:
                                    print("Você vê um quarto arrumado, com um guarda-roupas, uma estante de livros, uma mesa de escritório com gavetas e uma janela.\n")
                                    time.sleep(3)
                                    olhar_o_cenário = "sim"
                            else:
                                if (ação_do_personagem == "olhar as gavetas" or ação_do_personagem == "olhar gavetas" or ação_do_personagem == "olha a gaveta" or ação_do_personagem == "olhar a gaveta" or ação_do_personagem == "olhar gaveta" or ação_do_personagem == "olhar as gaveta" or ação_do_personagem == "olha as gavetas" or ação_do_personagem == "olha gaveta" or ação_do_personagem == "olha as gaveta" or ação_do_personagem == "olha a gavetas" or ação_do_personagem == "ver as gavetas" or ação_do_personagem == "ver a gaveta" or ação_do_personagem == "ver as gaveta" or ação_do_personagem == "ver a gavetas" or ação_do_personagem=="gaveta" or ação_do_personagem=="gavetas"):
                                    if (equipamento_luva == "Soco-Inglês"):
                                        print("Você olhou novamente as gavetas, mas não encontrou nada interessante.\n")
                                        time.sleep(1)
                                    else:
                                        print("Você achou um Soco-Inglês enquanto olhava as gavetas!\n")
                                        time.sleep(2)
                                        ataque_do_personagem = ataque_do_personagem +3;
                                        equipamento_luva = "Soco-Inglês"
                                        print("Seu ataque aumentou em 3 pontos!")
                                        time.sleep(2)
                                else:
                                    if (ação_do_personagem == "olhar o guarda-roupas" or ação_do_personagem =="olhar o guarda" or ação_do_personagem =="olhar o garda" or ação_do_personagem == "guarda" or ação_do_personagem=="roupa" or ação_do_personagem == "olha o guarda-roupas" or ação_do_personagem == "olha o guarda-roupa" or ação_do_personagem == "olhar o guarda-roupa" or ação_do_personagem == "olhar guarda-roupas" or ação_do_personagem == "olha guarda-roupas" or ação_do_personagem == "olha guarda-roupa" or ação_do_personagem == "olhar guarda-roupa" or ação_do_personagem == "olhar o guarda roupas" or ação_do_personagem == "olha o guarda roupas" or ação_do_personagem == "olha o guarda roupa" or ação_do_personagem == "olhar o guarda roupa" or ação_do_personagem == "olhar guarda roupas" or ação_do_personagem == "olha guarda roupas" or ação_do_personagem == "olha guarda roupa" or ação_do_personagem == "olhar guarda roupa" or ação_do_personagem == "olhar o guardaroupas" or ação_do_personagem == "olha o guardaroupas" or ação_do_personagem == "olha o guardaroupa" or ação_do_personagem == "olhar o guardaroupa" or ação_do_personagem == "olhar guardaroupas" or ação_do_personagem == "olha guardaroupas" or ação_do_personagem == "olha guardaroupa" or ação_do_personagem == "olhar guardaroupa" or ação_do_personagem == "olhar o guardarroupas" or ação_do_personagem == "olha o guardarroupas" or ação_do_personagem == "olha o guardarroupa" or ação_do_personagem == "olhar o guardarroupa" or ação_do_personagem == "olhar guardarroupas" or ação_do_personagem == "olha guardarroupas" or ação_do_personagem == "olha guardarroupa" or ação_do_personagem == "olhar guardarroupa" or ação_do_personagem == "guarda-roupa" or ação_do_personagem == "guarda-roupas" or ação_do_personagem == "guarda roupa" or ação_do_personagem == "guarda roupas" or ação_do_personagem == "guardaroupa" or ação_do_personagem == "guardaroupas" or ação_do_personagem == "guardarroupa" or ação_do_personagem == "guardarroupas" or ação_do_personagem == "olhar o armário" or ação_do_personagem == "olhar o armario" or ação_do_personagem == "olhar armário" or ação_do_personagem == "olhar armario" or ação_do_personagem == "olha o armário" or ação_do_personagem == "olha o armario" or ação_do_personagem == "olha armário" or ação_do_personagem == "olha armario" or ação_do_personagem == "armário" or ação_do_personagem == "armario" or ação_do_personagem == "sair do armário" or ação_do_personagem == "vestir smoking" or ação_do_personagem == "ver armário" or ação_do_personagem == "ver o armário" or ação_do_personagem == "ver armario" or ação_do_personagem == "ver o armario" or ação_do_personagem == "ver o guarda-roupas" or ação_do_personagem == "ver o guardarroupas" or ação_do_personagem == "ver o guarda roupas" or ação_do_personagem == "ver o guardaroupas" or ação_do_personagem == "ver o guarda-roupa" or ação_do_personagem == "ver o guardarroupa" or ação_do_personagem == "ver o guarda roupa" or ação_do_personagem == "ver o guardaroupa" or ação_do_personagem == "ver guarda-roupas" or ação_do_personagem == "ver guardarroupas" or ação_do_personagem == "ver guarda roupas" or ação_do_personagem == "ver guardaroupas" or ação_do_personagem == "ver guarda-roupa" or ação_do_personagem == "ver guardarroupa" or ação_do_personagem == "ver guarda roupa" or ação_do_personagem == "ver guardaroupa"):
                                        if(objeto_00=="ganha presente"):
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
                                                    print("Você trocou seu par de", equipamento_botas,"pelo par de Papetes Masculinas!")
                                                    time.sleep(2)
                                                    equipamento_botas = "Papetes Masculinas"
                                                    agilidade_do_personagem = agilidade_do_personagem + 1
                                                    print("Sua agilidade aumentou em 1 ponto!\n")
                                                    time.sleep(2)
                                                    objeto_00 = "não"
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
                                                print("Okay, ", nome_do_jogador,", vamos lá...")
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
                                                    print("Okay, ", nome_do_jogador,", você já está passando dos limites da burrice...")
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
                                                                nome_do_inimigo="Narrador"
                                                                vida_máxima_inimigo=100
                                                                vida_atual_inimigo=100
                                                                ataque_do_inimigo=13
                                                                defesa_do_inimigo=8
                                                                batalha()
                                                                if(vida_atual_personagem<=0):break
                                                                if(vida_atual_inimigo>0):
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
                                                            print('\nEntrada Inválida!\n')
                print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", variável_lugar)
                time.sleep(0.23)
                print("\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
                time.sleep(0.23)
                if (olhar_o_cenário == "sim"):
                    print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\nolhar pela janela\n")
                    time.sleep(0.5)
                print("\nver ficha do personagem\nsair do quarto\n")
                time.sleep(0.5)
                if(eegg > 1 and eegg<6):
                    print("\nVocê não deve:\nolhar a janela\n")
                    time.sleep(0.23)
                print("\n#", "-"*30,"#\n")
                print("\nE agora, ", nome_do_jogador,", o que você vai fazer?\n")
                ação_do_personagem = input("-")
                ação_do_personagem = ação_do_personagem.lower()
            if(vida_atual_personagem<=0):break
            ponto_de_save = 1
            modificar_o_cenário = "não"
            olhar_o_cenário = "não"
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
                input("\nCenário: Você continua atrasado para a aula - não que você deva se importar muito com isso.")
                variável_lugar = "seu prédio, 1º andar"
                seuPrédioPrimeiroAndar()
            if(vida_atual_personagem<=0):break
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
            nome_do_inimigo="Bandido"
            vida_máxima_inimigo=25000
            vida_atual_inimigo=25000
            ataque_do_inimigo=300
            defesa_do_inimigo=100
            batalha()
            if(vida_atual_personagem<=0):
                vida_atual_personagem=1
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
                reserva_nome_do_jogador = nome_do_jogador
                reserva_vida_máxima_personagem = vida_máxima_personagem
                reserva_vida_atual_personagem = vida_atual_personagem
                reserva_ataque_do_personagem = ataque_do_personagem
                reserva_defesa_do_personagem = defesa_do_personagem
                reserva_agilidade_do_personagem = agilidade_do_personagem
                nome_do_jogador = "Lutador Headbanger"
                vida_máxima_personagem = 100000
                vida_atual_personagem = 100000
                ataque_do_personagem = 1200
                defesa_do_personagem = 800
                agilidade_do_personagem = 5
                batalha()
                nome_do_jogador = reserva_nome_do_jogador
                vida_máxima_personagem = reserva_vida_máxima_personagem
                vida_atual_personagem = reserva_vida_atual_personagem
                ataque_do_personagem = reserva_ataque_do_personagem
                defesa_do_personagem = reserva_defesa_do_personagem
                agilidade_do_personagem = reserva_agilidade_do_personagem
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
                if(vida_atual_inimigo>0):
                    while(vida_atual_inimigo>0):
                        print("Você correu um pouco mas ele te alcançou de novo!\n")
                        batalha()
                        if(vida_atual_personagem<=0):
                            vida_atual_personagem=1
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
                            reserva_nome_do_jogador = nome_do_jogador
                            reserva_vida_máxima_personagem = vida_máxima_personagem
                            reserva_vida_atual_personagem = vida_atual_personagem
                            reserva_ataque_do_personagem = ataque_do_personagem
                            reserva_defesa_do_personagem = defesa_do_personagem
                            reserva_agilidade_do_personagem = agilidade_do_personagem
                            nome_do_jogador = "Lutador Headbanger"
                            vida_máxima_personagem = 100000
                            vida_atual_personagem = 100000
                            ataque_do_personagem = 1200
                            defesa_do_personagem = 800
                            agilidade_do_personagem = 5
                            batalha()
                            nome_do_jogador = reserva_nome_do_jogador
                            vida_máxima_personagem = reserva_vida_máxima_personagem
                            vida_atual_personagem = reserva_vida_atual_personagem
                            ataque_do_personagem = reserva_ataque_do_personagem
                            defesa_do_personagem = reserva_defesa_do_personagem
                            agilidade_do_personagem = reserva_agilidade_do_personagem
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
                    nome_do_inimigo="Motoqueiro Comparsa"
                    vida_máxima_inimigo=5000
                    vida_atual_inimigo=5000
                    ataque_do_inimigo=3000
                    defesa_do_inimigo=100
                    batalha()
                    if(vida_atual_personagem<=0): break
                    if(vida_atual_inimigo>0):
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
                input("Cenário:Você está na sua rua, por agora tudo está calmo....")
                suaRua()
            if(vida_atual_personagem<=0):break
            ponto_de_save = 4
            save()

##########--------------------------------------------------FIM DO JOGO--------------------------------------------------##########
        break
    if (vida_atual_personagem <= 0):
        print("Você morreu, ", nome_do_jogador, "...\nO jogo acabou para você...")
        nome_do_jogador = "Jogador"
        nome_do_inimigo = "Inimigo"
        ação_do_personagem = "" 
        batalha_escapar = ""
        equipamento_roupa = "Pijama"
        equipamento_capa = "Nada"
        equipamento_luva = "Nada"
        equipamento_mãos = "Nada"
        olhar_o_cenário = "não"
        modificar_o_cenário = "não"
        cheirar_o_cenário = "não"
        objeto_00 = "não"
        objeto_01 = "não"
        objeto_02 = "não"
        variável_lugar = "seu quarto"
        ponto_de_save = 0
        eegg = 1
        vida_máxima_personagem = 100
        vida_atual_personagem = 100
        dinheiro_do_personagem = 0
        ataque_do_personagem = 10
        defesa_do_personagem = 8
        vida_máxima_inimigo = 30
        vida_atual_inimigo = 30
        ataque_do_inimigo = 5
        defesa_do_inimigo = 5
        situação_01 = 0
        situação_02 = 0
        situação_03 = 0
        situação_04 = 0
        teste_de_sorte = 0
        calculo_do_dano = 0
        calculo_da_fuga = 0
        variável_para_comparar = 0
        contador_de_batalha= 0
        contador_de_rodadas = 0
    else:
        print("\nParabéns, ", nome_do_jogador,"!!! Você terminou o jogo!!!")
    print("\nVocê deseja jogar novamente, ", nome_do_jogador,'?("sim" ou "não")\n')
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
                input('\nEntrada inválida!(digite "sim" ou "não)\n')
    if(ação_do_personagem == "não" or ação_do_personagem=="n" or ação_do_personagem=="nao" or ação_do_personagem=="no" or ação_do_personagem=="na" or ação_do_personagem=="nã" or ação_do_personagem=="ao" or ação_do_personagem=="ão" or ação_do_personagem=="ñ" or ação_do_personagem=="ñão" or ação_do_personagem=="ño" or ação_do_personagem=="ñõ" or ação_do_personagem=="ñã" or ação_do_personagem=="ñaõ" or ação_do_personagem=="aõ"):
        break
    
exit()
