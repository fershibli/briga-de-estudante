#--Import--#
import _random
import random
import configparser
import pickle

#--Variáveis de Texto--#
x = "Jogador" #nome do personagem
y = "Inimigo" #nome do inimigo
act = "" #ação do personagem
escapar = "" #variável em batalha e pós batalha para conferir condições de evento
rpa = "Pijama" #"armadura"
cpa = "Nada" #"capa"
lva = "Nada" #"mãos"
mao = "Nada" #"armas"
olh = "não" #confere: se olhou ou não o cenário
cen = "não" #confere: se modificou ou não o cenário
che = "não" #confere: se cheirou ou não o cenário
obj00 = "não" #confere: se modificou ou não o objeto 0
obj01 = "não" #confere: se modificou ou não o objeto 1
obj02 = "não" #confere: se modificou ou não o objeto 2
lug = "seu quarto" #local do cenário
desejajogarnovamente = "" #deseja jogar novamente?
#x, y, act, escapar, rpa, cpa, lva, mao, olh, cen, che, obj00, obj01, obj02, lug, desejajogarnovamente

#--Variáveis de Número--#
z = 0 #variável de ponto de save
eegg = 1 #condição do easter egg 1
hpx = 100 #hp máximo do personagem 
hpa = 100 #hp atual do personagem 
d = 0 #dinheiro do personagem 
atq = 10 #poder de ataque do personagem 
dfs = 8 #poder de defesa do personagem 
hxi = 30 #hp máximo do inimigo 
hai = 30 #hp atual do inimigo 
ati = 5 #poder de ataque do inimigo 
dfi = 5 #poder de defesa do inimigo 
hmr01 = 0 #situação do quarto 11
hmr02 = 0 #situação do quarto 24
hmr03 = 0 #situação do quarto 21
hmr04 = 0 #situação do quarto 22
dado = 0 #variável para testar a sorte
dano = 0 #variável para calcular dano 
fuga = 0 #variável para calcular fuga
comparar = 0 #para uso de comparação
contador01 = 0 #contador no01
contador02 = 0 #contador no02
#z, eegg, hpx, hpa, d, atq, dfs, hxi, hai, ati, dfi, hmr01, hmr02, hmr03, hmr04, dado, dano, fuga, comparar, contador01, contador02

#--Ficha do Personagem--#
def ficha_personagem():
    print("\n#", "-"*30,"#\n", "\nNome:", x)
    input("")
    print("\nVida:", hpa, "de", hpx)
    input("")
    print("\nAtaque:", atq, "\nDefesa:", dfs)
    input("")
    print("\nCapa:", cpa, "\nRoupa:", rpa, "\nLuvas:" ,lva,"\nArmamento:", mao)
    input("")
    print("\nDinheiro:", d, "Reais\n")
    input("")
    print("\n#", "-"*30,"#\n")

#--Save--#
def save():
    ficha_personagem()
    print('\nDeseja salvar seu progresso?("sim" ou "não")\n')
    act = input("-")
    act = act.lower()
    while 1:
        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
            arq = open('\save.py', 'wb')
            pickle.dump(x, arq)
            pickle.dump(rpa, arq)
            pickle.dump(cpa, arq)
            pickle.dump(lva, arq)
            pickle.dump(mao, arq)
            pickle.dump(lug, arq)
            pickle.dump(z, arq)
            pickle.dump(hpx, arq)
            pickle.dump(hpa, arq)
            pickle.dump(d, arq)
            pickle.dump(atq, arq)
            pickle.dump(dfs, arq)
            arq.close
            print("\nPronto!\n")
            break
        else:
            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                break
            else:
                print('ENTRADA INVÁLIDA! Digite "sim" ou "não".\n')
                act = input("-")
                act = act.lower()

#--Sistema de batalha--#
def batalha():
    global x, y, act, escapar, rpa, cpa, lva, mao, olh, cen, che, obj00, obj01, obj02, lug, desejajogarnovamente, z, eegg, hpx, hpa, d, atq, dfs, hxi, hai, ati, dfi, hmr01, hmr02, hmr03, hmr04, dado, dano, fuga, comparar, contador01, contador02
    input("\nBatalha!!!\nÉ hora da briga!!!\n")
    contador02=1
    while(hai>0):
        if(hpa<=0):
            break
        print("\n]]", "="*30,"[[\n", "Início da rodada número ", contador02, "\n]]", "="*30,"[[\n")
        if(hpa==1):
            if(contador02==1):
                input("\nVocê entrou na batalha com apenas 1 ponto de vida!")
                input("Seu último recurso é a tensão!\n")            
            else:
                if(contador01==0):
                    input("\nVocê está com apenas 1 ponto de vida!")
                    input("Seu último recurso é a tensão!\n")            
            if(contador01>0):       
                input("\nVocê aguentou mais uma rodada com apenas 1 ponto de vida!")
                input("Você extendeu o limite do seu fôlego e agora o limite dos seus pontos de vida subiu!\n")
                hpx=hpx+((contador01)+(random.randrange(dfs)))*(0.1)
            contador01=contador01+1
        else:
            if(hpa<=hpx*0.05):
                dado=random.randrange(30)
                if(dado==1):
                    input("\nVocê está dando o seu melhor para aguentar, isso está melhorando o seu fôlego!")
                    input("O limite dos seus pontos de vida aumentou!\n")
                    hpx=hpx+(random.randrange(dfs)+1)*(0.05)
                else:
                    if(dado==5 or dado==6):
                        input("\nVocê está dando o seu melhor para aguentar, isso está melhorando o seu fôlego!")
                        input("O limite dos seus pontos de vida aumentou!\n")
                        hpx=hpx+(random.randrange(dfs)+1)*(0.1)
        print("\n#", "-"*30,"#\n", "\n", x, ":", hpa, "de", hpx, " Pontos de Vida\n", y, ":", hai, "de", hxi, " Pontos de vida\n\n#", "-"*30,"#\nO que você fará agora, ", x, "?\nAtacar, defender ou fugir?")
        act = input("-")
        act = act.lower()
        while True:
            if(act != "atacar" and act != "defender" and act != "fugir"):
                print("\nComando inválido! Você só pode atacar, defender ou fugir!\n")
                act = input("-")
                act = act.lower()
            else: break
        contador02=contador02+1
        if(act == "defender"): #defesa(2dfs) vs ataque(ati)
            print("\nPostura de Batalha:\n", x, "-> defensiva\n", y, "-> ofensiva\n")
            input("...")
            dado = random.randrange(5)
            if (dado==1):#S_defesa(3dfs) vs ataque(ati)
                input("\nSua postura de defesa te favoreceu!\n")
                dado = random.randrange(4)
                if (dado==1):#S_defesa(3dfs) vs S_ataque(2ati)
                    input("\n... Mas o ataque do inimigo foi crítico!\n")
                    dano = (2*ati)+(random.randrange(ati))*(0.2)-(3*dfs)-(random.randrange(dfs))*(0.2)
                    if (dano < 0):#S_defesa(3dfs) CONTRA-ATACA S_ataque(2ati)
                        dano = (dano/2)*(-1)+((random.randrange(atq))/2)*(0.2)
                        input("\nNão importa, sua defesa é incrível!")
                        print("Além de defender você conseguiu contra-atacar, causando ", dano," pontos de dano ao inimigo!\n")
                        input("")
                        dado = random.randrange(100)#aumento de defesa
                        if (dado==10 or dado==20 or dado==30):
                            comparar=dfs
                            dfs=dfs+(random.randrange(dfs))*(0.1)
                            if (comparar < dfs):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (comparar > dfs):
                                dfs=comparar
                        if (dado==40 or dado==50):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))*(0.1)+1
                        if (dado==60):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))*(0.1)+2
                        if (dado==70):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))*(0.1)+3
                        hai = hai-dano
                    else:
                        if (dano == 0):#S_defesa(3dfs) ANULA S_ataque(2ati)
                            input("\nDefesa e ataque se anulam! A tensão aumenta!\n")
                        else:#S_defesa(3dfs) APANHA DO S_ataque(2ati)
                            print("\nVocê sofreu ", dano, " pontos de dano...\n")
                            input("")
                            hpa = hpa - dano
                else:#S_defesa(3dfs) vs ataque(ati)
                    dano = (ati)+(random.randrange(ati))*(0.2)-(3*dfs)-(random.randrange(dfs))*(0.2)
                    if (dano<0):#S_defesa(3dfs) CONTRA-ATACA ataque(ati)
                        dano = (dano/2)*(-1)+((random.randrange(atq))/2)*(0.2)
                        print("\nSua defesa foi tão grande que, além de bloquear o ataque, você conseguiu contra-atacar, causando ", dano," pontos de dano ao inimigo!\n")
                        input("")
                        hai = hai-dano
                    else:
                        if (dano ==0):#S_defesa(3dfs) ANULA ataque(ati)
                            input("\nSua defesa foi completa!\n")
                        else:#S_defesa(3dfs) APANHA DO ataque(ati)
                            print("\nVocê sofreu míseros ", dano, " pontos de dano.\n")
                            input("")
                            hpa = hpa-dano
            else:
                dado = random.randrange(4)
                if(dado==1):#defesa(2dfs) vs S_ataque(2ati)
                    dano = 2*ati+(random.randrange(ati))*(0.2)-(1.5)*dfs-(random.randrange(dfs))*(0.2)
                    if (dano<0):
                        dano = (dano/2)*(-1)+((random.randrange(atq))/2)*(0.2)
                                            
                        input("\nSua defesa é simplesmente  I M E N S A !")
                        print("O inimigo avançou furiosamente mas você o lançou para trás e contra-atacou causando ", dano, " pontos de dano ao inimigo!\n")
                        input("")
                        dado = random.randrange(75)#aumento de defesa
                        if (dado==1 or dado==15 or dado==30):
                            comparar=dfs
                            dfs=dfs+(random.randrange(dfs))
                            if (comparar < dfs):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (comparar > dfs):
                                dfs=comparar
                        if (dado==20 or dado==40):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+1
                        if (dado==45):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+2
                        if (dado==55):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+3
                        if (dado==70):
                            comparar=dfs
                            dfs=dfs+(random.randrange(dfs))+(random.randrange(atq))
                            if (comparar < dfs):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (comparar > dfs):
                                dfs=comparar
                        hai = hai-dano
                    else:
                        if(dano==0):
                            input("\nVocê surpreendeu o inimigo que estava confiante,")
                            input("suas forças se anularam numa estrondosa colisão!\n")
                            dado=random.randrange(100)
                            if(dado==1):
                                input("\nA liberação de energia durante a colisão despertou novos limites para sua força e agora está mais forte!")
                                input("TODOS os seus pontos subiram!\n")
                                hpx=hpx+(random.randrange(hpx))+10
                                atq=atq+(random.randrange(atq))+2
                                dfs=dfs+(random.randrange(dfs))+1
                        else:
                            print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", dano, " pontos de dano!\n")
                            input("")
                            hpa = hpa-dano
                else:#defesa(2dfs) vs ataque(ati)
                    dano = ati+(random.randrange(ati))-2*dfs-(random.randrange(dfs))
                    if (dano<0):
                        dano = dano*(-1)+((random.randrange(atq))/2)
                        input("\nSua defesa É ENORME!")
                        print("Você barrou o ataque naturalmente e contra-atacou, causando ", dano, " pontos de dano ao inimigo!\n")
                        input("")
                        dado = random.randrange(80)#aumento de defesa
                        if (dado==1 or dado==15 or dado==30):
                            comparar=dfs
                            dfs=dfs+(random.randrange(dfs))
                            if (comparar < dfs):
                                input("\nVocê testou o seu limite e agora está mais forte!")
                                input("Seus pontos de defesa subiram!\n")
                            if (comparar > dfs):
                                dfs=comparar
                        if (dado==20 or dado==40):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+1
                        if (dado==45):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+2
                        if (dado==55):
                            input("\nVocê testou o seu limite e agora está mais forte!")
                            input("Seus pontos de defesa subiram!\n")
                            dfs=dfs+(random.randrange(dfs))+3
                        hai = hai-dano
                    else:
                        if(dano==0):
                            input("\nVocê barrou o ataque do inimigo!\n")
                        else:
                            print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", dano, " pontos de dano!\n")
                            input("")
                            hpa = hpa-dano
        else:
            if (act=="atacar"):
                dado=random.randrange(2)
                if (dado==1):#ataque(atq) vs defesa(2dfi)
                    print("\nPostura de Batalha:\n", x, "-> ofensiva\n", y, "-> defensiva\n")
                    input("...")
                    dado=random.randrange(4)
                    if (dado==1):#S_ataque(2atq) vs defesa(2dfi)
                        input("\nSeu ataque foi crítico!!!\n")
                        dado=random.randrange(5)
                        if (dado==1):#S_ataque(2atq) vs S_defesa(3dfi)
                            input("\nApesar do seu crítico, você é pressionado pela postura de defesa do seu inimigo!\n")
                            dano=2*atq+(random.randrange(atq))-3*dfi-(random.randrange(dfi))
                            if (dano<0):#S_ataque(2atq) APANHA DE S_defesa(3dfi)
                                dano = dano*(-1)+((random.randrange(ati))/2)
                                input("\nPor mais que tente, você não consegue atravessar a defesa do seu inimigo!")
                                print("Além de te bloquear, ele te contra-atacou, causando ", dano, " pontos de dano!\n")
                                input("")
                                hpa = hpa-dano
                            else:
                                if (dano==0):#S_ataque(2atq) ANULA S_defesa(3dfi)
                                    input("\nA disputa de forças é intensa, você e seu inimigo deram o melhor de si, mas nenhum dos dois se sobrepôs!\n")
                                else:#S_ataque(2atq) ATACA S_defesa(3dfi)
                                    input("\nSeu ataque foi explosivo!")
                                    input("Nem o melhor da defesa do seu inimigo foi capaz de conter sua ira!")
                                    print("Você causou ", dano, " pontos de dano ao seu inimigo!\n")
                                    input("")
                                    hai = hai-dano
                        else:#S_ataque(2atq) vs defesa(2dfi)
                            dano = 2*atq+(random.randrange(atq))-2*dfi-(random.randrange(dfi))
                            if(dano<0):#S_ataque(2atq) APANHA DE defesa(2dfi)
                                dano=dano*(-1)+((random.randrange(ati))/2)
                                input("\nVocê deu o seu máximo, mas mesmo assim nem se equiparou às habilidades de auto-defesa do seu inimigo!")
                                print("Sem fazer muito esforço ele se defendeu e contra-atacou, te causando ", dano," pontos de dano!\n")
                                input("")
                                hpa = hpa - dano
                            else:
                                if(dano==0):#S_ataque(2atq) ANULA defesa(2dfi)
                                    input("\nVocê assustou o inimigo por um instante, mas - por muito pouco - ele conseguiu barrar todos os seus movimentos ofensivos...\n")
                                else:
                                    dado=random.randrange(5)
                                    if(dado==1):#XS_ataque(3atq) vs defesa(dfi)
                                        print("\nVocê rompeu a defesa do seu inimigo, causando ", dano," pontos de dano!")
                                        input("")
                                        input("\nSuper Crítico!!!\n")
                                        input("Você iniciou um ataque em frenesi!!!\n")
                                        hai=hai-dano
                                        dado=random.randrange(10)+1
                                        while(dado>0):#XS_ataque(3atq) ATACA defesa(dfi)
                                            dano=2*(random.randrange(atq))-(random.randrange(dfi))
                                            print(dano," pontos de dano!\n")
                                            input("")
                                            hai=hai-dano
                                            dado=dado-1
                                        input("\nVocê desferiu toda sua fúria no inimigo!\n")
                                        dado=random.randrange(5)
                                        if(dado<4):
                                            input("\nVocê testou o seu limite e agora está mais forte!")
                                            input("Seus pontos de ataque subiram!\n")
                                            atq=atq+(random.randrange(atq))+5
                                        if(dado==4):
                                            input("\nVocê ultrapassou o seu limite e agora está mais forte!")
                                            input("Seus pontos de ataque subiram!\n")
                                            atq=atq+(random.randrange(atq))+10
                                    else:#S_ataque(2atq) ATACA defesa(2dfi)
                                        print("\nSeu ataque de golpes duplos pressionaram a defesa do seu inimigo, causando ",dano," pontos de dano!\n")
                                        input("")
                                        hai=hai-dano
                    else:#ataque(atq)
                        dado=random.randrange(5)
                        if(dado==1):#ataque(atq) vs S_defesa(3dfi)
                            input("\nA postura de defesa do seu inimigo te colocou numa situação difícil!\n")
                            dano=atq+random.randrange(atq)-3*dfi-random.randrange(dfi)
                            if(dano<0):#ataque(atq) APANHA DE S_defesa(3dfi)
                                dano=dano*(-1)+((random.randrange(ati))/2)
                                input("\nÉ muito difícil passar por tamanha defesa, seu ataque foi ínfimo, além de ser inutilizado, você sofreu represália...")
                                print("Seu inimigo contra-atacou, causando ", dano, " pontos de dano.\n")
                                input("")
                                dado=random.randrange(20)
                                if(dado==1):
                                    input("\nVocê testou o seu limite e agora está mais forte!")
                                    input("Seus pontos de ataque subiram!\n")
                                    atq=atq+(random.randrange(atq))+1
                                hpa=hpa-dano
                            else:
                                if(dano==0):#ataque(atq) ANULA S_defesa(3dfi)
                                    print("\nO inimigo mal consegue reter seus golpes, mas o suficiente para pará-lo.")
                                    input("Ao mesmo tempo sua força foi o bastante para evitar um contra-ataque!\n")
                                else:#ataque(atq) ATACA S_defesa(3dfi)
                                    print("\nDepois de alguns golpes, você tornou insignificante a vantagem defensiva do seu inimigo, causando humilhantes, ", dano," pontos de dano a ele!\n")
                                    input("")
                                    dado=random.randrange(20)
                                    if(dado==1):
                                        input("\nVocê testou o seu limite e agora está mais forte!")
                                        input("Seus pontos de ataque subiram!\n")
                                        atq=atq+(random.randrange(atq))+2
                                    hai=hai-dano
                        else:#ataque(atq) vs defesa(2dfi)
                            dano = atq+(random.randrange(atq))-2*dfi-(random.randrange(dfi))
                            if(dano<0):#ataque(atq) APANHA DE defesa(2dfi)
                                dano=dano*(-1)+((random.randrange(ati))/2)
                                print("\nO inimigo se defendeu e contra-atacou, te causando ", dano," pontos de dano!\n")
                                input("")
                                hpa = hpa - dano
                            else:
                                if(dano==0):#ataque(atq) ANULA defesa(2dfi)
                                    input("\nSeu oponente defendeu todos os seus golpes, mas você não deu brecha para que ele avançasse!\n")
                                else:#ataque(atq) ATACA defesa(2dfi)
                                    print("\nVocê acertou o inimigo durante a disputa de forças, causando ",dano," pontos de dano!\n")
                                    input("")
                                    hai=hai-dano
                else:#ataque(atq) vs ataque(ati)
                    print("\nPostura de Batalha:\n", x, "-> ofensiva\n", y, "-> ofensiva\n")
                    input("...")
                    dado=random.randrange(4)
                    if (dado==1):#S_ataque(2atq) vs ataque(ati)
                        input("\nSeu ataque foi crítico!!!\n")
                        dado=random.randrange(4)
                        if (dado==1):#S_ataque(2atq) vs S_ataque(2ati)
                            input("\nMas o ataque do oponente também foi crítico!!!\n")
                            input("\nVocês entraram na briga pra valer!")
                            input("Avançaram de punhos cerrados, trocando golpes com as defesas abertas!\n")
                            dano=2*atq+random.randrange(atq)-dfi-random.randrange(dfi)
                            if(dano>0):
                                print("\nVocê causou significativos ", dano," pontos de dano ao inimigo!\n")
                                input("")
                                hai=hai-dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            dano=2*ati+random.randrange(ati)-dfs-random.randrange(dfs)
                            if(dano>0):
                                print("\nEnquanto o oponente te causou ", dano," pontos de dano!\n")
                                input("")
                                hpa=hpa-dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                        else:#S_ataque(2atq) vs ataque(ati)
                            input("\nVocê avançou violentamente sobre o inimigo, pressionando-o sem compaixão!")
                            input("Apesar de forçar um leve recuo do inimigo, você não deixou de levar uns bons golpes!\n")                            
                            dano=2*atq+random.randrange(atq)-dfi-random.randrange(dfi)
                            if(dano>0):
                                print("\nVocê golpeou o inimigo até lhe causar ", dano," pontos de dano!\n")
                                input("")
                                hai=hai-dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            dano=ati+random.randrange(ati)-dfs-random.randrange(dfs)
                            if(dano>0):
                                print("\nJá o inimigo causou apenas ", dano," pontos de dano à você!\n")
                                input("")
                                hpa=hpa-dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                    else:#ataque(atq) vs ataque(ati)
                        dado=random.randrange(4)
                        if(dado==1): #ataque(atq) vs S_ataque(2ati)
                            input("\nO ataque do oponente foi crítico!...\n")
                            input("\nVocê foi pressionado enquanto trocavam golpes, os socos e chutes do seu oponente te acertaram em pontos menos resistentes do seu corpo que estavam desprotegidos!")
                            input("Mesmo assim você manteve um bom rítmo de ataque!\n")
                            dano=atq+random.randrange(atq)-dfi-random.randrange(dfi)
                            if(dano>0):
                                print("\nVocê infringiu ", dano," pontos de dano ao inimigo!\n")
                                input("")
                                hai=hai-dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            dano=2*ati+random.randrange(ati)-dfs-random.randrange(dfs)
                            if(dano>0):
                                print("\nEnquanto o seu inimigo te agrediu violentamente, causando ", dano," pontos de dano à você!\n")
                                input("")
                                hpa=hpa-dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")                                
                        else:#ataque(atq) vs ataque(ati)
                            input("\nVocês se atacaram num ritmo leve, parecem estar testando um ao outro, ficou claro que nenhum dos dois mostrou tudo o que é capaz.\n")
                            dano=atq+random.randrange(atq)-dfi-random.randrange(dfi)
                            if(dano>0):
                                print("\nVocê feriu seu oponente em ", dano," pontos de dano!\n")
                                input("")
                                hai=hai-dano
                            else:
                                input("\nMesmo sem se defender, a constituição do inimigo foi alta o suficiente para resistir ao seu ataque.\n")
                            dano=ati+random.randrange(ati)-dfs-random.randrange(dfs)
                            if(dano>0):
                                print("\nSeu inimigo te golpeou causando ", dano," pontos de dano!\n")
                                input("")
                                hpa=hpa-dano
                            else:
                                input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
            else:
                if(act=="fugir"):
                    print("\nPostura de Batalha:\n", x, "-> fugiva\n", y, "-> ofensiva\n")
                    input("...")
                    input("\nVocê tenta aumentar o rítmo de esquiva...\n")
                    dado=random.randrange(10)+fuga
                    if(dado==10):
                        input('\nVocê esquivou de qualquer manobra ofensiva do oponente e conseguiu uma brecha para fugir!\n')
                        print('\nDeseja fugir da luta?("sim" ou "não")\n')
                        escapar=""
                        while(escapar != "não"):
                            escapar = input('-')
                            escapar = escapar.lower()
                            if(escapar!="não" and escapar != "sim"):
                                print('\nEntrada invalida! Digite "sim" ou "não".\n')
                            if(escapar =="sim"):
                                break
                        if(escapar =="sim"):
                            break
                    else:
                        if(dado>8):
                            input('\nVocê esquivou de qualquer manobra ofensiva do oponente, mas não conseguiu uma brecha para fugir...\n')
                        else:
                            if(dado>5):
                                input('\nVocê não conseguiu uma brecha para fugir, nem pode se esquivar, mas pode se defender!\n')
                                dano = ati+(random.randrange(ati))-2*dfs-(random.randrange(dfs))
                                if (dano<0):
                                    input('\nSua defesa É ENORME!')
                                    input('Você barrou o ataque naturalmente e conseguiu afastar o inimigo, criando uma brecha para fugir!\n')
                                    print('\nDeseja fugir da luta?("sim" ou "não")\n')
                                    escapar=""
                                    while(escapar != "não"):
                                        escapar = input('-')
                                        escapar = escapar.lower()
                                        if(escapar!="não" and escapar != "sim"):
                                            print('\nEntrada invalida! Digite "sim" ou "não".\n')
                                        if(escapar =="sim"):
                                            break
                                    if(escapar =="sim"):
                                        escapar="sim"
                                        break
                                else:
                                    if(dano==0):
                                        input("\nVocê barrou o ataque do inimigo!\n")
                                    else:
                                        print("\nMesmo se defendendo, o impacto do ataque inimigo te causou ", dano, " pontos de dano!\n")
                                        input("")
                                        hpa = hpa-dano
                            else:
                                if(dado>2):
                                    input('\nVocê não conseguiu uma brecha para fugir, se esquivar ou se defender...\n')
                                    dano = ati+(random.randrange(ati))-dfs-(random.randrange(dfs))
                                    if (dano>0):
                                        print("\nVocê foi atacado diretamente, sofrendo ", dano," pontos de dano!\n")
                                        input("")
                                        hpa=hpa-dano
                                    else:
                                        input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                                else:
                                    input('\nVocê tropeçou ao tentar fugir!\n')
                                    input('\nO golpe do oponente foi crítico!\n')
                                    dano = 2*ati+(random.randrange(ati))-dfs-(random.randrange(dfs))
                                    if (dano>0):
                                        print("\nO inimigo aproveitou a abertura na sua defesa e te atacou violentamente, causando ", dano," pontos de dano.\n")
                                        input("")
                                        hpa=hpa-dano
                                    else:
                                        input("\nMesmo sem se defender, sua constituição foi alta o suficiente para resistir ao ataque do oponente.\n")
                    fuga=fuga+0.5
                    if(escapar =="sim"):
                        break
    escapar="não"
    comparar = 0
    contador01 = 0
    contador02 = 1
    input("\nFim da Batalha!\n")
    if(hai<=0):
        print("\n",y," foi derrotado!\n")
        input("")
    else:
        if(hpa<=0):
            input("\nVocê morreu.\n")
        else:
            if(escapar =="sim"):
                input("\nVocê conseguiu escapar!\n")
                escapar="escapou"

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

#--Segundo Andar--#
def terceiroAndar():
    global x, y, act, escapar, rpa, cpa, lva, mao, olh, cen, che, obj00, obj01, obj02, lug, desejajogarnovamente, z, eegg, hpx, hpa, d, atq, dfs, hxi, hai, ati, dfi, hmr01, hmr02, hmr03, hmr04, dado, dano, fuga, comparar, contador01, contador02
    while 1:
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\n\ndescer as escadas\nchecar os quartos\n")
        print("\nver ficha do personagem\nsair do quarto\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", x,", o que você vai fazer?\n")
        act = input("-")
        act = act.lower()
        if(act=="subir as escadas" or act=="subir" or act=="subir escadas" or act=="subi" or act=="subi as escadas" or act=="subir escada" or act=="subi escada" or act=="subi a escada" or act=="sobe"):
            input("Você subiu para o quarto andar, lá você encontrou mais cinco quartos.")
            quartoAndar()
        else:
            if(act=="descer as escadas" or act=="descer escadas" or act=="descer escada" or act=="descer a escada" or act=="sair" or act=="descer" or act=="sair do prédio"):
                input("Você desceu para o segundo andar.")
                break

        
#--Segundo Andar--#
def segundoAndar():
    global x, y, act, escapar, rpa, cpa, lva, mao, olh, cen, che, obj00, obj01, obj02, lug, desejajogarnovamente, z, eegg, hpx, hpa, d, atq, dfs, hxi, hai, ati, dfi, hmr01, hmr02, hmr03, hmr04, dado, dano, fuga, comparar, contador01, contador02
    while 1:
        print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\n\nsubir as escadas\ndescer as escadas\nchecar os quartos\n")
        if(hmr02==1):
            print("\narrombar a porta do quarto 24")
        print("\nver ficha do personagem\nsair do quarto\n")
        print("\n#", "-"*30,"#\n")
        print("\nE agora, ", x,", o que você vai fazer?\n")
        act = input("-")
        act = act.lower()
        if(act=="subir as escadas" or act=="subir" or act=="subir escadas" or act=="subi" or act=="subi as escadas" or act=="subir escada" or act=="subi escada" or act=="subi a escada" or act=="sobe"):
            input("Você subiu para o terceiro andar, lá você encontrou mais cinco quartos e outra escada ascendente.")
            terceiroAndar()
        else:
            if(act=="descer as escadas" or act=="descer escadas" or act=="descer escada" or act=="descer a escada" or act=="sair" or act=="descer" or act=="sair do prédio"):
                input("Você desceu para o primeiro andar, o andar do seu quarto.")
                break
            else:
                if(act=="checar os quartos" or act=="checar quartos" or act=="checar" or act=="quartos" or act=="checaros quartos" or act=="checar osquartos" or act=="checarosquartos" or act=="checa os quartos" or act=="checa os quarto" or act=="checa o quarto" or act=="checa o quartos" or act=="checar os quarto" or act=="checar o quarto" or act=="bater na porta de um dos quartos" or act=="checar um dos quartos" or act=="bater na porta dos quartos" or act=="bater a porta dos quartos" or act=="bater quartos" or act=="bater"):
                    print("Qual dos quartos?(20, 21, 22, 23 ou 24)\n")
                    act = input("-")
                    act = act.lower()
                    if(act=="20"):
                        if(hmr03==1):
                            input("Você já pegou tudo o que tinha para pegar aqui.")
                        else:
                            input("Você bate na porta e percebe, pelo barulho do trepidar da maçaneta, que ela está destrancada...")
                            print("Abrir a porta?(sim ou não)")
                            while 1:
                                act = input("-")
                                act = act.lower()
                                if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                    input("Você entrou, não havia ninguém...")
                                    input("Ao revistar o quarto você encontrou 30 Reais.")
                                    d=d+30
                                    hmr03==1
                                    break
                                else:
                                    if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                        input("Você ignorou o quarto...")
                                        break
                                    else:
                                        input('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                    else:
                        if(act=="21"):
                            if(hmr03==7):
                                input("Você bate na porta...")
                                input(" - Olá! - diz o avô do garoto - Muito obrigado por treinar o meu neto,")
                                input("agora ele não precisa se esconder mais dos trombadinhas da escola.")
                            if(hmr03==6):
                                input(" - Obrigado por me treinar, senhor.")
                                y="Garoto, um Homem."
                                hxi=20000
                                hai=20000
                                ati=1500
                                dfi=1000
                                batalha()
                                if(hpa<=0):
                                    hpa=1
                                    input(" - Me supere. Estarei te esperando.")
                                if(hai>0):
                                    while (hai>0):
                                        input(" - Não abandone nossa luta!")
                                        batalha()
                                    if(hpa<=0):
                                        hpa=1
                                        input(" - Me supere. Estarei te esperando.")
                                    else:
                                        input(" - Obrigado, mesmo!")
                                        hmr03=7
                                else:
                                    input(" - Obrigado, mesmo!")
                                    hmr03=7
                            if(hmr03==5):
                                input(" - Estou empolgado! Não aguentava mais esperar pela nossa luta!")
                                y="Garoto Forte"
                                hxi=2000
                                hai=2000
                                ati=100
                                dfi=150
                                batalha()
                                if(hpa<=0):
                                    hpa=1
                                    input(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                if(hai>0):
                                    while (hai>0):
                                        input(" - A nossa luta não acabou ainda!")
                                        batalha()
                                    if(hpa<=0):
                                        hpa=1
                                        input(" - Quando você estiver pronto para uma revanche, me procure novamente.")
                                    else:
                                        input(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                        hmr03=6
                                else:
                                    input(" - Incrível, você sempre me surpreende! Se prepare, da próxima vez estarei ainda mais forte!")
                                    hmr03=6
                            if(hmr03==4):
                                input(" - Dessa vez não vou perder tão fácil!")
                                y="Garoto Sério"
                                hxi=200
                                hai=200
                                ati=30
                                dfi=25
                                batalha()
                                if(hpa<=0):
                                    hpa=1
                                    input(" - Estou te levando a sério, não vou perder mais!")
                                    input(" - Estarei te esperando para uma revanche.")
                                if(hai>0):
                                    while (hai>0):
                                        input(" - Honre a nossa luta até o fim!")
                                        batalha()
                                    if(hpa<=0):
                                        hpa=1
                                        input(" - Estou te levando a sério, não vou perder mais!")
                                        input(" - Estarei te esperando para uma revanche.")
                                    else:
                                        input(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                        hmr03=5
                                else:
                                    input(" - Você é mesmo forte! Treinarei mais e estarei te esperando para o nosso próximo confronto!")
                                    hmr03=5
                            if(hmr03==3):
                                input(" - Eu estava te esperando, panaca!")
                                y="Garoto Convencido"
                                hxi=110
                                hai=110
                                ati=8
                                dfi=12
                                batalha()
                                if(hpa<=0):
                                    hpa=1
                                    input(" - Não aguenta o tranco, não? Hahaha!")
                                    input(" - Volte qualquer hora para apanhar mais!")
                                if(hai>0):
                                    while (hai>0):
                                        input(" - Volte aqui seu panaca!")
                                        batalha()
                                    if(hpa<=0):
                                        hpa=1
                                        input(" - Não aguenta o tranco, não? Hahaha!")
                                        input(" - Volte qualquer hora para apanhar mais!")
                                    else:
                                        input(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                        hmr03=4
                                else:
                                    input(" - Você é mesmo forte! Continuarei treinando e esperarei o nosso próximo confronto!")
                                    hmr03=4
                            if(hmr03==2):
                                input(" - Meu avô disse que você viria... - disse o garoto baixinho - Vamos logo ao que interessa!")
                                y="Garoto Fracote"
                                hxi=100
                                hai=100
                                ati=3
                                dfi=10
                                batalha()
                                if(hpa<=0):
                                    hpa=1
                                    input(" - Você não é tão forte quanto meu avô falou.")
                                    hmr03=3
                                if(hai>0):
                                    while (hai>0):
                                        input(" - Meu avô disse para não parar de lutar até eu não aguentar mais!")
                                        batalha()
                                    if(hpa<=0):
                                        hpa=1
                                        input(" - Você não é tão forte quanto meu avô falou.")
                                        hmr03=3
                                    else:
                                        input(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                        hmr03=3
                                else:
                                    input(" - Você é muito forte!!! Vou treinar e estarei te esperando para uma próxima luta!")
                                    hmr03=3
                            if(hmr03==1):
                                input("A porta está trancada.")
                            if(hmr03==0):
                                input("Você bateu na porta...")
                                input("Um senhor baixo e fracote abriu a porta... Ele parecia muito com um frango")
                                input(" - O que que você quer?!")
                                input("...")
                                input(" - Saia daqui então!")
                                y="Senhor Doente"
                                hxi=50
                                hai=50
                                ati=5
                                dfi=3
                                batalha()
                                if(hpa<=0):break
                                if(hai>0):
                                    input("Depois de se afastar o senhor começou a gritar...")
                                    input("Com a mão no peito, ele começou a tossir...")
                                    input(" - Ahhhh... - gemiu o senhor que caia lentamente.")
                                    input(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                    input("O menino pegou o senhor nos braços antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
                                    input(" - VOCÊ VAI PAGAR CARO!")
                                    y="Garoto Perturbado"
                                    hxi=100
                                    hai=100
                                    ati=3
                                    dfi=10
                                    batalha()
                                    if(hpa<=0):break
                                    if(hai>0):
                                        input(" - SAIA JÁ DAQUI!")
                                        input("Em seguida ele fechou e trancou a porta.")
                                        hmr03==1
                                    else:
                                        input("O garoto caiu no chão dentro da casa e começou a chorar.")
                                        input(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                        input("Em seguida ele fechou e trancou a porta.")
                                        hmr03=1
                                else:
                                    input("O senhor caiu no chão com uma mão no peito...")
                                    input("Ele tentava gritar algo enquanto estendia a outra mão...")
                                    input("Mas não conseguia dizer nada, estava tendo crise de asma...")
                                    input("Sua mão apontava para um lugar dentro da casa...")
                                    print("Vai ajudar o idoso?\n")
                                    while 1:
                                        act = input("-")
                                        act = act.lower()
                                        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                            input("Você entrou na casa, pegou a bombinha em cima da mesa e a apertou na boca no velho...")
                                            input(" - Ah... Ah... - o senhor tentava recuperar o ar - Você não é um mau rapaz no fim das contas...")
                                            input(" - ...")
                                            input(" - Você gosta de lutar, não é garoto? Eu brigava muito quando era mais jovem...")
                                            input(" - ...")
                                            input(" - Nem sempre os punhos são o bastante...")
                                            input(" - ...")
                                            input(" - Não falo do coração na luta, isso você já tem, falo de armas...")
                                            input("Tome... Eu usava este punhal no meu tempo... Agora é seu.")
                                            mao = "Punhal Envelhecido"
                                            atq = atq+10
                                            input(" - Se não for pedir demais, venha sempre que puder para treinar o meu neto... Ele ainda é muito fraco e eu não tenho mais o mesmo vigor de antes...")
                                            hmr03=2
                                            break
                                        else:
                                            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                input(" - O QUÊ VOCÊ FEZ COM MEU AVÔ?! - era a voz de um menino vindo lá de dentro do quarto.")
                                                input("O menino pegou o senhor nos braços antes que tombasse e apertou algumas vezes uma bombinha para asma na boca dele...")
                                                input(" - VOCÊ VAI PAGAR CARO!")
                                                y="Garoto Irritado"
                                                hxi=100
                                                hai=100
                                                ati=10
                                                dfi=10
                                                batalha()
                                                if(hpa<=0):break
                                                if(hai>0):
                                                    input(" - SAIA JÁ DAQUI!")
                                                    input("Em seguida ele fechou e trancou a porta.")
                                                    hmr03=1
                                                else:
                                                    input("O garoto caiu no chão dentro da casa e começou a chorar.")
                                                    input(" - SAIA DAQUI ANTES QUE EU CHAME A POLÍCIA! - disse o senhor que já estava um pouco melhor...")
                                                    input("Em seguida ele fechou e trancou a porta.")
                                                    hmr03=1
                                                break
                                            else:
                                                input('ENTRADA INVÁLIDA! Digite "sim" ou "não"')
                        else:
                            if(act=="22"):
                                if(hmr04==4):
                                    input("Voce bateu na porta...")
                                    input("Ninguém te atendeu.")
                                if(hmr04==3):
                                    input(" - E aí, rapaz!")
                                    dado = randomrange(3)
                                    if(dado==1):
                                        input(" - Você chegou em boa hora! Entre e coma um pedaço de pizza comigo!")
                                        input("Você recuperou 50 pontos de vida!")
                                        hpa = hpa + 50
                                        input(" - Até outra hora, vizinho!")
                                    else:
                                        input(" - Estou sem pizza agora... Talvez mais tarde...")
                                if(hmr04==2):
                                    input(" - O quê você quer aqui?")
                                    print("Você vai dizer a ele que comeu a sua pizza?(sim ou não)")
                                    while 1:
                                        act = input("-")
                                        act = act.lower()
                                        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                            input(" - ...")
                                            input(" - VOCÊ...")
                                            input(" - Você é muito cara de pau mesmo, mas adimiro a sua sinceridade.")
                                            input(" - Eu sempre como pizza, quando você quiser passe aqui para pegar um pedaço.")
                                            hmr04=3
                                            break
                                        else:
                                            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                input(" - ...")
                                                input(" - Me deixe em paz!")
                                                hmr04=4
                                                break
                                            else:
                                                input('Entrada inválida! Digite "sim" ou "não".')
                                if(hmr04==1):
                                    input("Você bateu na porta do quarto, que agora está fechado.")
                                    input("Você escuta passos rápidos e violentos vindo à porta")
                                    input(" - EU TO MUITO PUTO! - diz o estudante que abriu violentamente a porta - ENTRARAM E COMERAM A MINHA PIZZA!")
                                    input("...")
                                    input(" - Ah esquece... Nem deve ter sido você...")
                                    hmr04=2
                                if(hmr04==0):
                                    input("O quarto está aberto, você entra e vê um estudante vagabundo dormindo num sofá com uma pizza no colo.")
                                    print("E aí, vai pegar essa pizza? (sim ou não)\n")
                                    while 1:
                                        act = input("-")
                                        act = act.lower()
                                        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                            input("Você comeu a pizza e recuperou todos os seus pontos de vida!")
                                            hpa=hpx
                                            hmr04=1
                                            break
                                        else:
                                            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                input("Você deixou a pizza para depois!")
                                                break
                                            else:
                                                input('Entrada inválida! Digite "sim" ou "não".')
                            else:
                                if(act=="23"):
                                   input("Você vê um quarto aberto, sujo e vazio...")
                                   input("Parece abandonado por um bom tempo... Já tem fauna e flora prória!")
                                else:
                                    if(act=="24"):
                                        if(hmr02==0):
                                            input("Você encara um indivíduo de aparencia extravagante e vulgar encostado no batente da porta...")
                                            input(" - Qualé merh-mão? Tá querenu tretá?")
                                            y="Mané de Boné"
                                            hxi=100
                                            hai=100
                                            ati=10
                                            dfi=5
                                            batalha()
                                            if(hpa<=0):break
                                            if(hai>0):
                                                input("Ele corre atrás de você e te dá um chute no joelho!")
                                                input("!!!")
                                                input("Você perdeu 30 pontos de vida!")
                                                input(" - Fica diboa rapáh!")
                                                hpa=hpa-30
                                                input("Ele voltou ao batente da porta do quarto e agora está te encarando...")
                                                input("Você me envergonha.")
                                            else:
                                                input(" - Que isso maluco?! Que isso?!")
                                                input("Ele entrou cambaleando para o quarto dele e se trancou!")
                                                hmr02=1
                                        if(hmr02==1):
                                            input("O quarto está trancado...")
                                        if(hmr02==2):
                                            input("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            input("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            input("Dentro você vê muito sangue pelo quarto, os poucos móveis quebrados, ")
                                            input("mas nada de valor...")
                                            matarAlguém()
                                        if(hmr02==3):
                                            input("Você ve uma porta quebrada ao meio, caída, mas presa apenas pela dobradiça inferior, ")
                                            input("a superior segurava apenas um pedaço de madeira desprendido da porta.")
                                            input("Também escuta, vindo lá de dentro, soluços em sussurros e sussurros em soluços...")
                                            input("Melhor não entrar... Não há nada de mais lá dentro.")
                                    else:
                                        input("Entrada inválida.")
                else:
                    if(act=="arrombar a porta do quarto 24" or act=="arrombar o quarto 24" or act=="arrombar" or act=="arrombar a porta" or act=="quarto 24" or act=="entrar no quarto 24"):
                        if(hmr02==1):
                            input("Você pisoteou a porta e entrou no quarto!")
                            input(" - Não, por favor nao!...")
                            while 1:
                                if(hmr02==2):
                                    break
                                if(hmr02==3):
                                    break
                                print("Melhor não continuar...(sim ou não)\n")
                                act=input("-")
                                act=act.lower()
                                if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                    while 2:
                                        print("Eu insisto... É melhor parar... Você está de cabeça quente... (sim ou não)\n")
                                        act=input("-")
                                        act=act.lower()
                                        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                            act=input("-")
                                            act=act.lower()
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
                                            hmr02=2
                                            break
                                        else:
                                            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                input("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                                hpx=hpx+50
                                                hpa=hpx
                                                hmr02=3
                                                break
                                            else:
                                                input("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                                    break
                                else:
                                    if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                        input("Você respirou fundo, abaixou os punhos e se retirou do quarto...")
                                        hpa=hpx
                                        hmr02=3
                                        break
                                    else:
                                        input("Entrada inválida... A situação é tensa, mantenha a seriedade e responda corretamente.")
                        if(hrm02==2):
                            matarAlguém()
                        if(hmr02==3):
                            input("Você já fez o bastante por aqui... Melhor se afastar.")
                    #else:
                        ######
                            

#--Primeiro Andar--#
def primeiroAndar():
    global x, y, act, escapar, rpa, cpa, lva, mao, olh, cen, che, obj00, obj01, obj02, lug, desejajogarnovamente, z, eegg, hpx, hpa, d, atq, dfs, hxi, hai, ati, dfi, hmr01, hmr02, hmr03, hmr04, dado, dano, fuga, comparar, contador01, contador02
    lug = "seu prédio, 1º andar"
    input("Agora você está no corredor do primeiro andar do seu prédio.")
    print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\nolhar\n")
    if (olh == "sim"):
        print("\ncheirar\nchecar os quartos\nsubir as escadas\n")
        if (che == "sim" and obj00 == "não"):
            print("olhar o bêbado\n")
    if(obj01 == "sim"):
        print("\narrombar o quarto 10\n")
    if (obj00 == "1"):
        print("\nacordar o bêbado\n")
        print("\nrevistar o bêbado\n")
    if (obj00 == "2"):
        print("\nmover o bêbado\n")
    if (obj00 == "3"):
        print("\natacar o bêbado\n")
    if (obj00 == "sim"):
        print("\nabrir a porta dos fundos\n")
    print("\nver ficha do personagem\ndescer as escadas\n", "\n#", "-"*30,"#\n")
    print("\nO que você vai fazer, ", x, "?\n")
    act = input("-")
    act = act.lower()
    while 1:
        if(act == "ver ficha do personagem" or act == "ficha" or act=="ficha do personagem" or act=="ficha de personagem" or act=="ver ficha de personagem" or act=="ver ficha" or act == "olhar ficha do personagem" or act == "ver minha ficha" or act=="minha ficha" or act=="ficha personagem" or act=="olhar ficha de personagem" or act=="olhar ficha"):
            ficha_personagem()
        else:
            if(act == "olhar" or act == "ver" or act == "olhar o quarto" or act == "olha" or act == "olhar quarto" or act == "olha quarto" or act == "olhar o quarto" or act == "olha o quarto" or act == "ve" or act == "vê"):
                if (che == "1" or che == "sim"):
                    input("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                    input("Num dos lados desse corredor há uma janela quebrada,")
                    input("mas no outro se encontra um bêbado caido no chão, imundo e cercado de vômito encostado na porta dos fundos, impedindo o acesso.")
                    input("E ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                    input("A mais próxima sobe e a colada à parede desce.")
                else:
                    if (obj00 == "sim"):
                        input("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                        input("Num dos lados desse corredor há uma janela quebrada, mas no outro se encontra a porta dos fundos.")
                        input("Ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        input("A mais próxima sobe e a colada à parede desce.")
                    else:
                        input("Você vê um corredor estreito com 5 portas, o seu e os outros quartos desse andar do prédio.")
                        input("Num dos lados desse corredor há uma janela quebrada,")
                        input("mas no outro se encontra, encostado na porta dos fundos e caído no chão coberto por cacos de vidro, um homem sujo, cercado por algum líquido que parece laranja...")
                        input("E ao longo do corredor, em frente aos quartos há um par de escadas azul-pastel um pouco alaranjada ao redor das ferrugens.")
                        input("A mais próxima sobe e a colada à parede desce.")
                        olh = "sim"
            else:
                if(act=="cheirar" or act=="cherar" or act=="dar um tapa" or act=="cheira" or act=="chera"):
                    if(che=="não"):
                        che="sim"
                    input("Você sente um cheiro forte de álcool e vômito")
                else:
                    if(act=="checar os quartos" or act=="checar quartos" or act=="checar" or act=="quartos" or act=="checaros quartos" or act=="checar osquartos" or act=="checarosquartos" or act=="checa os quartos" or act=="checa os quarto" or act=="checa o quarto" or act=="checa o quartos" or act=="checar os quarto" or act=="checar o quarto" or act=="bater na porta de um dos quartos" or act=="checar um dos quartos" or act=="bater na porta dos quartos" or act=="bater a porta dos quartos" or act=="bater quartos" or act=="bater"):
                        print("Qual dos quartos?(10, 11, 12 ou 14)\n")
                        act = input("-")
                        act = act.lower()
                        if(act=="10"):
                            if(cpa=="Jaqueta de Couro"):
                                input("Você vê uma porta arrombada... Não há mais nada de interessante dentro do quarto.")
                            else:
                                input("Você bateu na porta, mas ninguém atendeu... Ela parece fácil de ser arrombada...")
                                obj01="sim"
                        else:
                            if(act=="11"):
                                if(hmr01==0):
                                    input("Quando você bateu, a porta se abriu no primeiro toque por não ter uma fechadura...")
                                    input("Você vê, dentro da casa, uma mulher alta de ombros largos, BEM LARGOS, musculosa e com o maxilar largo...")
                                    input("Ela estava apenas de toalha...")
                                    input(" - MAS QUE ATREVIMENTO! SUMA DAQUI! - diz a mulher enquanto te epurra com a porta que é fechada violentamente.")
                                    input("Você perdeu 10 pontos de vida ao cair no corredor...")
                                    hpa=hpa-10
                                    hmr01=1
                                else:
                                    if(hmr01==1):
                                        input("Você empurrou a porta sem fechadura, mas moradora que ainda estava te toalha, furiosamente fechou a porta gritando, antes que você pudesse terminar de abrir!")
                                        input("Você perdeu 10 pontos de vida ao cair no corredor...")
                                        hpa=hpa-10
                                        hmr01=2
                                    else:
                                        if(hmr01==2):
                                            input("Você abriu a porta e levou um soco na cara, caindo em seguida no chão do corredor.")
                                            input("Você perdeu 30 pontos de vida...")
                                            hpa=hpa-30
                                            hmr01=3
                                        else:
                                            if(hmr01==3):
                                                input("Você abriu a porta e viu a mulher de toalha extremamente furiosa com os ombros levemente curvados, deixando à mostra seus braços musculosos e gigantescos.")
                                                input(" - VOCÊ VAI APANHAR MUITO AGORA!")
                                                y="Mulher de Toalha"
                                                hxi=80000
                                                hai=80000
                                                ati=440
                                                dfi=220
                                                batalha()
                                                if(hpa<=0):break
                                                if(hai>0):
                                                    input(" - E NÃO VOLTE MAIS AQUI!")
                                                else:
                                                    input("A mulher caiu inconsciente no chão...")
                                                    input("Dentro da casa você encontrou 200 reais e um suplemento alimentício")
                                                    input("Você tomou o suplemento e aumentou seus pontos de ataque!")
                                                    d=d+200
                                                    atq=atq+50
                                                    hmr01=4
                                            else:
                                                if(hmr01==4):
                                                    input("Você entra no quarto, encontra a mulher que você derrotou caida no chão e mais nada além dos móveis velhos dela.")
                            else:
                                if(act=="12"):
                                    input("Você bateu na porta...")
                                    input(" - Já vai! - exclama uma senhora de dentro da casa.")
                                    input("...")
                                    input(" - Olá, meu jovem! Por que você não entra e prova um pouco do bolo que eu acabei de fazer?")
                                    input("...")
                                    input("Você recurperou seus pontos de vida!")
                                    hpa=hpx
                                else:
                                    if(act=="14"):
                                        input("Você bateu na porta...")
                                        input(" - JÁ DISSE PARA VOCÊ IR EMBORA SEU BÊBADO! - grita uma mulher de dentro da casa - NINGUÉM TE MERECE COMO MARIDO!")
                                    else:
                                        if(act=="13"):
                                            input("Você é bobo?")
                                            input("Esse é o seu quarto!")
                                            input("Você está atrasado demais para voltar!")
                                        else:
                                            input("Entrada inválida.")
                    else:
                        if(act=="arrombar a porta do quarto 10" or act=="arrombar o quarto 10" or act=="arrombar" or act=="arrombar a porta" or act=="quarto 10" or act=="entrar no quarto 10"):
                            if(cpa=="Jaqueta de Couro"):
                                input("Você já arrombou essa porta... Não há mais nada de interessante dentro do quarto.")
                            else:
                                input("Você entrou no quarto e encontrou uma Jaqueta de Couro!")
                                input("Você a vestiu.")
                                cpa="Jaqueta de Couro"
                                dfs=dfs+100
                        else:
                            if(act=="subir as escadas" or act=="subir" or act=="subir escadas" or act=="subi" or act=="subi as escadas" or act=="subir escada" or act=="subi escada" or act=="subi a escada" or act=="sobe"):
                                input("Você subiu para o segundo andar, lá você encontrou mais cinco quartos e outra escada ascendente.")
                                segundoAndar() #MUDA DE MAPA SEM SALVAR
                            else:
                                if(act=="olhar o bêbado" or act=="olhar bêbado" or act=="olha o bêbado" or act=="olha bÊbado" or act=="olhar o bebado" or act=="olhar bebado" or act=="olha o bebado" or act=="olha bebado"):
                                    obj00="1"
                                    input("Você vê um homem de 40 anos, coberto por cacos de vidro, bebida e vômito, dormindo no chão.")
                                else:
                                    if(act=="revistar o bêbado" or act=="revistar bêbado" or act=="revistar" or act=="revista bêbado" or act=="revista o bêbado" or act=="revistar o bebado" or act=="revistar bebado" or act=="revistar" or act=="revista bebado" or act=="revista o bebado"):
                                        if(obj02!="sim"):
                                            input("Você achou um energético!")
                                            input("Você aumentou o limite dos seus pontos de vida ao beber o energético!")
                                            hpx=hpx+500
                                            hpa=hpx
                                            obj02="sim"
                                        else:
                                            input("Você não encontrou mais nada...\n")
                                    else:
                                        if(act=="acordar o bêbado" or act=="acordar bêbado" or act=="acorda o bêbado" or act=="acorda bêbado" or act=="acordar o bebado" or act=="acordar bebado" or act=="acorda o bebado" or act=="acorda bebado"):
                                            obj00="2"
                                            input("Você tenta acordar o bêbado, mas não consegue...")
                                        else:
                                            if(act=="mover o bêbado" or act=="mover bêbado" or act=="move o bêbado" or act=="move bêbado" or act=="mover o bebado" or act=="mover bebado" or act=="move o bebado" or act=="move bebado" or act=="mover" or act=="move"):
                                                obj00="3"
                                                input("Você pensa em mover o bêbado, mas o cheiro e a sujeira fazem você vomitar em cima dele!")
                                                input("...")
                                                input("Ele continua dormindo...")
                                            else:
                                                if(act=="atacar o bêbado" or act=="atacar bêbado" or act=="ataca o bêbado" or act=="ataca bêbado" or act=="atacar o bebado" or act=="atacar bebado" or act=="ataca o bebado" or act=="ataca bebado" or act=="atacar" or act=="ataca"):
                                                    if(obj00!="sim" or obj00!="pegou o dinheiro"):
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
                                                        y="Bêbado"
                                                        hxi=5000
                                                        hai=328
                                                        ati=10
                                                        dfi=5
                                                        batalha()
                                                        if(hpa<=0):break
                                                        if(hai>0):
                                                            input("Você escapa da briga, mas em seguida o bêbado tosse sangue e cái no chão")
                                                        else:
                                                            input("O bêbado coberto de bebida, vômito e sangue, cái de costas no chão,")
                                                            input("sendo empalado pelos diversos cacos de vidro...")
                                                            input("O sangue dele escorre pelo corredor até os seus pés...")
                                                            input("Você vira o rosto fechando os olhos e abaixando os punhos...")
                                                            input("Agora, desencostado da porta dos fundos, o bêbado já não é mais um impecílio...")
                                                            obj00="sim"
                                                else:
                                                    if(act=="abrir a porta dos fundos"):
                                                        if(obj00=="sim"):
                                                            input("Você abre a porta... ")
                                                            input("É um armário de limpesa.")
                                                            input("Em meio às vassouras, rodos e outras coisas, você encontra uma mala...")
                                                            input("Você abre a mala, encontra entre os materiais de escritório e 10 Reais!")
                                                            d=d+10
                                                            obj00="pegou o dinheiro"
                                                        else:
                                                            if(obj00=="pegou o dinheiro"):
                                                                input("Você vê materiais de limpesa e uma maleta aberta.")
                                                            else:
                                                                input("Não dá para abrir!")
                                                    else:
                                                        if(act=="descer as escadas" or act=="descer escadas" or act=="descer escada" or act=="descer a escada" or act=="sair" or act=="descer" or act=="sair do prédio"):
                                                            if(z==1):
                                                                while 1:
                                                                    input("Do lado de fora há um oponente forte.")
                                                                    print("Tem certeza que está pronto para sair? (sim ou não)")
                                                                    act=input("-")
                                                                    act=act.lower()
                                                                    if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                                                        act="sim"
                                                                        break
                                                                    else:
                                                                        if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                                            input("Você decidiu não sair do prédio.")
                                                                            break
                                                                        else:
                                                                            input("Entrada inválida!")
                                                                if(act=="sim"):
                                                                    input("Você desceu as escadas e saiu do prédio...")
                                                                    break
                                                            else:
                                                                suaRua()
                                                                input("Você desceu as escadas e saiu do prédio...")
                                                                break
                                                        else:
                                                            input('Entrada Inválida!')
                                                            input("Você pode:")
                                                            input("olhar")
                                                            if (olh == "sim"):
                                                                input("cheirar")
                                                                input("checar os quartos")
                                                                input("subir as escadas")
                                                                if (che == "sim" and obj00 == "não"):
                                                                    input("olhar o bêbado")
                                                            if(obj01 == "sim"):
                                                                input("arrombar o quarto 10")
                                                            if (obj00 == "1"):
                                                                input("acordar o bêbado")
                                                                input("revistar o bêbado")
                                                            if (obj00 == "2"):
                                                                input("mover o bêbado")
                                                            if (obj00 == "3"):
                                                                input("atacar o bêbado")
                                                            if (obj00 == "sim"):
                                                                input("abrir a porta dos fundos")
                                                            input("ver ficha do personagem")
                                                            input("descer as escadas")
        print("\n#", "-"*30,"#\n", "\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\nolhar\n")
        if (olh == "sim"):
            print("\ncheirar\nchecar os quartos\nsubir as escadas\n")
            if (che == "sim" and obj00 == "não"):
                print("olhar o bêbado\n")
        if(obj01 == "sim"):
            print("\narrombar o quarto 10\n")
        if (obj00 == "1"):
            print("\nacordar o bêbado\n")
            print("\nrevistar o bêbado\n")
        if (obj00 == "2"):
            print("\nmover o bêbado\n")
        if (obj00 == "3"):
            print("\natacar o bêbado\n")
        if (obj00 == "sim"):
            print("\nabrir a porta dos fundos\n")
        print("\nver ficha do personagem\ndescer as escadas\n", "\n#", "-"*30,"#\n")
        print("\nO que você fará agora, ", x,"?\n")
        act = input("-")
        act = act.lower()


#####################----------------------------__BRIGA DE ESTUDANTE__----------------------------#####################
while (desejajogarnovamente != "não"):
    while (hpa>0):
        print("\n"," ","_"*69," ","\n","|"," "*69,"|","\n","|","="*69,"|","\n","|","="*69,"|","\n","|","="*69,"|","\n","|","="*69,"|","\n","|","="*24,"Briga de Estudante","="*25,"|","\n","|","="*19,"por:Fernando Luiz Neme Chibli","="*19,"|","\n","|","="*69,"|","\n","|","="*29,"[começar]","="*29,"|","\n","|","="*32,"ou","="*33,"|","\n","|","="*28,"[continuar]","="*28,"|","\n","|","="*69,"|","\n","|","="*69,"|","\n","|","="*69,"|","\n","|","="*69,"|\n","|","_"*69,"|",'\n\nDigite "começar" ou "continuar":')
        while(act!="começar"):
            act = input("-")
            act = act.lower()
            if (act == "continuar"):
                arq = open('\save.py', 'rb')
                x = pickle.load(arq)
                cpa = pickle.load(arq)
                rpa = pickle.load(arq)
                lva = pickle.load(arq)
                mao = pickle.load(arq)
                lug = pickle.load(arq)
                z = pickle.load(arq)
                hpx = pickle.load(arq)
                hpa = pickle.load(arq)
                d = pickle.load(arq)
                atq = pickle.load(arq)
                dfs = pickle.load(arq)
                arq.close
                if(z>0):
                    print("\nCarregado!\n")
                    ficha_personagem()
                else:
                    print("\nERRO: Você não possui dados salvos.\n")
                act="começar"
            else:
                if(act !="começar"):
                    print('Entrada inválida!\n')
        if(z==0):
            input("\nIniciando novo jogo(aperte enter)\n")
            print("\n\nVocê é um homem... Qual é o seu nome?\n")
            x = input("-")
            print("Muito prazer, ", x,'.\nNós já nos conhecemos?(digite "não" para ver o tutorial)\n')
            act = input("-")
            act = act.lower()
            while 1:
                if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                    break
                else:
                    if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):#tutorial
                        input('Sou o narrador da nossa história, vou apenas te guiar de acordo com as suas decisões...')
                        input('Então saiba que não vou facilitar as coisas para você!')
                        input('Porém minha função é te guiar, ser os seus olhos, ouvidos, mãos e nariz,')
                        input('e além disso você parece precisar de algumas instruções para tornar disso algo mais divertido.')
                        input('\nToda vez antes da sua ação te mostrarei uma lista de ações possíveis de se realizar.')
                        input('\nE também te mostrarei se a sua ação for inválida.')
                        input('\nMas você só receberá minha atenção quando eu pedir,')
                        input('você perceberá isso quando ver um hífen após a minha pergunta.')
                        print('Entendeu?')
                        variávelinútildotutorial = input("-")
                        variávelinútildotutorial = variávelinútildotutorial.lower()
                        while 1:
                            if(variávelinútildotutorial=="sim" or variávelinútildotutorial=="s" or variávelinútildotutorial=="si" or variávelinútildotutorial=="sm" or variávelinútildotutorial=="im" or variávelinútildotutorial=="ssim"):
                                break
                            if( variávelinútildotutorial== "não" or variávelinútildotutorial=="n" or variávelinútildotutorial=="nao" or variávelinútildotutorial=="no" or variávelinútildotutorial=="na" or variávelinútildotutorial=="nã" or variávelinútildotutorial=="ao" or variávelinútildotutorial=="ão" or variávelinútildotutorial=="ñ" or variávelinútildotutorial=="ñão" or variávelinútildotutorial=="ño" or variávelinútildotutorial=="ñõ" or variávelinútildotutorial=="ñã" or variávelinútildotutorial=="ñaõ" or variávelinútildotutorial=="aõ"):
                                print('\nVocê é bobo??')
                            else:
                                print('\nEntrada inválida!\n\nVocê pode:\nconcordar comigo dizendo "sim"\n')
                            variávelinútildotutorial = input("-")
                            variávelinútildotutorial = variávelinútildotutorial.lower()
                        input('Bom menino!')
                        input('\nToda vez que você descobre algo, a lista muda.')
                        input('\nAlguns comandos como "olhar" e "ver ficha do personagem" estarão sempre disponíveis,')
                        input('mas o resultado dessas ações podem mudar de acordo com o que você faz,')
                        input('sendo assim é altamente recomendável que você repita algumas ações em um mesmo cenário.')
                        input('\nAcho que já é o bastante para começarmos, mas posso repetir se você quiser...')
                        print('Você entendeu tudo o que eu disse?')
                    else:
                        print('Não entendi o que você quis dizer...\nPor favor, digite "sim" ou "não".\n')
                    act = input("-")
                    act = act.lower()
                    if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                        act="sim"
            print("Ótimo, ",x,".")
            input("\n")

#####################----------------------------__INÍCIO DO JOGO__----------------------------#####################
            input("Cenário: acabou de amanhecer, seu quarto está desarrumado, você ainda está de pijama e atrasado para a aula - não que você se importe muito com isso.")
            print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
            if (olh == "sim"):
                print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\nolhar pela janela\n")
            print("\nver ficha do personagem\nsair do quarto\n\n#", "-"*30,"#\n")
            print("\nO que você vai fazer", x,"?\n")
            act = input("-")
            act = act.lower()
            while 1:
                if (act == "ver ficha do personagem" or act == "ficha" or act=="ficha do personagem" or act=="ficha de personagem" or act=="ver ficha de personagem" or act=="ver ficha" or act == "olhar ficha do personagem" or act == "ver minha ficha" or act=="minha ficha" or act=="ficha personagem" or act=="olhar ficha de personagem" or act=="olhar ficha"):
                    ficha_personagem()
                else:
                    if (act== "vetir" or act=="vesti" or act=="veti" or act=="estir" or act=="esti" or act=="etir" or act == "vestir" or act == "vestir uniforme" or act == "vestir o uniforme" or act == "vestir o uniforme estudantil" or act == "vestir uniforme estudantil" or act == "se vestir" or act == "se vestir para a aula" or act == "se vestir pra aula" or act == "vestir para a aula" or act == "me arrumar" or act == "tomar banho" or act == "ir ao banheiro" or act == "cagar" or act == "mijar" or act == "fazer xixi" or act == "trocar de roupa" or act == "me trocar" or act == "trocar"):
                        if (rpa == "Pijama"):
                            input("Você se vestiu para a aula.\n")
                            rpa = "Uniforme Estudantil"
                            dfs=dfs+1
                        else:
                            input("Você já está vestido para a aula!\n")
                    else:
                        if (act == "arrumar o quarto" or act == "arrumar" or act == "arrumar quarto" or act == "arruma" or act == "arruma o quarto" or act == "arruma quarto" or act == "quarto"):
                            if (cen == "não"):
                                input("Você achou 30 Reais enquanto arrumava o seu quarto!\n")
                                d = +30
                                cen = "sim"
                            else:
                                input("Você já arrumou o seu quarto!\n")
                        else:
                            if (act == "olhar" or act == "ver" or act == "olhar o quarto" or act == "olha" or act == "olhar quarto" or act == "olha quarto" or act == "olhar o quarto" or act == "olha o quarto" or act == "ve" or act == "vê"):
                                if (cen == "não"):
                                    input("Você não consegue ver nada além de bagunça, MUITA BAGUNÇA!!!\n")
                                else:
                                    input("Você vê um quarto arrumado, com um guarda-roupas, uma estante de livros, uma mesa de escritório com gavetas e uma janela.\n")
                                    olh = "sim"
                            else:
                                if (act == "olhar as gavetas" or act == "olha a gaveta" or act == "olhar a gaveta" or act == "olhar gaveta" or act == "olhar as gaveta" or act == "olha as gavetas" or act == "olha gaveta" or act == "olha as gaveta" or act == "olha a gavetas" or act == "ver as gavetas" or act == "ver a gaveta" or act == "ver as gaveta" or act == "ver a gavetas" or act=="gaveta" or act=="gavetas"):
                                    if (mao == "Soco-Inglês"):
                                        input("Você olhou novamente as gavetas, mas não encontrou nada interessante.\n")
                                    else:
                                        input("Você achou um Soco-Inglês enquanto olhava as gavetas!\n")
                                        atq = atq +10;
                                        lva = "Soco-Inglês"
                                else:
                                    if (act == "olhar o guarda-roupas" or act == "olha o guarda-roupas" or act == "olha o guarda-roupa" or act == "olhar o guarda-roupa" or act == "olhar guarda-roupas" or act == "olha guarda-roupas" or act == "olha guarda-roupa" or act == "olhar guarda-roupa" or act == "olhar o guarda roupas" or act == "olha o guarda roupas" or act == "olha o guarda roupa" or act == "olhar o guarda roupa" or act == "olhar guarda roupas" or act == "olha guarda roupas" or act == "olha guarda roupa" or act == "olhar guarda roupa" or act == "olhar o guardaroupas" or act == "olha o guardaroupas" or act == "olha o guardaroupa" or act == "olhar o guardaroupa" or act == "olhar guardaroupas" or act == "olha guardaroupas" or act == "olha guardaroupa" or act == "olhar guardaroupa" or act == "olhar o guardarroupas" or act == "olha o guardarroupas" or act == "olha o guardarroupa" or act == "olhar o guardarroupa" or act == "olhar guardarroupas" or act == "olha guardarroupas" or act == "olha guardarroupa" or act == "olhar guardarroupa" or act == "guarda-roupa" or act == "guarda-roupas" or act == "guarda roupa" or act == "guarda roupas" or act == "guardaroupa" or act == "guardaroupas" or act == "guardarroupa" or act == "guardarroupas" or act == "olhar o armário" or act == "olhar o armario" or act == "olhar armário" or act == "olhar armario" or act == "olha o armário" or act == "olha o armario" or act == "olha armário" or act == "olha armario" or act == "armário" or act == "armario" or act == "sair do armário" or act == "vestir smoking" or act == "ver armário" or act == "ver o armário" or act == "ver armario" or act == "ver o armario" or act == "ver o guarda-roupas" or act == "ver o guardarroupas" or act == "ver o guarda roupas" or act == "ver o guardaroupas" or act == "ver o guarda-roupa" or act == "ver o guardarroupa" or act == "ver o guarda roupa" or act == "ver o guardaroupa" or act == "ver guarda-roupas" or act == "ver guardarroupas" or act == "ver guarda roupas" or act == "ver guardaroupas" or act == "ver guarda-roupa" or act == "ver guardarroupa" or act == "ver guarda roupa" or act == "ver guardaroupa"):
                                        input("Você não vê muitas roupas... Você é muito pobre, arrume um emprego!\n")
                                    else:
                                        if (act == "olhar a janela"):###__EASTER-EGG
                                            if (eegg == 1):
                                                input("Você vê...")
                                                input("...")
                                                input("Você vê uma janela, sua anta!")
                                                input("...")
                                                input("Hunf...")
                                                input("Volte para as aulas de ortografia!")
                                                input("...")
                                                input("O quê?")
                                                input("Você acha que eu fui muito grosso?")
                                                print("Okay, ", x,", vamos lá...")
                                                input("")
                                                input("Há uma diferença muito grande entre olhar A janela e olhar PELA janela!")
                                                input("Tente mais uma vez, sua anta!")
                                                eegg = 2
                                            else:
                                                if (eegg == 2):
                                                    input("Digitando errado MAIS UMA VEZ?!")
                                                    print("Okay, ", x,", você já está passando dos limites da burrice...")
                                                    input("")
                                                    eegg = 3
                                                else:
                                                    if (eegg == 3):
                                                        input("Você encara a janela...")
                                                        input("Você parece um retardado fazendo isso...")
                                                        eegg = 4
                                                    else:
                                                        if (eegg == 4):
                                                            input('Enquanto você encarava a janela um pombo pousou nela...')
                                                            input('Ele olhou bem no fundo dos seus olhos e disse "Você é um idiota."...')
                                                            input('Não, ele não disse isso... Na verdade fui eu quem disse isso, seu idiota.')
                                                            eegg = 5
                                                        else:
                                                            if (eegg == 5):
                                                                input("Já chega! Você esgotou minha paciência!")
                                                                y="Narrador"
                                                                hxi=100
                                                                hai=100
                                                                ati=13
                                                                dfi=8
                                                                batalha()
                                                                if(hpa<=0):break
                                                                if(hai>0):
                                                                    input("Vou te deixar em paz por agora, mas tente voltar a me irritar para ver o que te acontece!")
                                                                else:
                                                                    input("Aaaah! Eu deveria ter me feito mais forte para essa luta...")
                                                                    input("Okay, você venceu... Mas pare de me irritar!")
                                                                    eegg = 6
                                                            else:
                                                                if (eegg == 6):
                                                                    input("...")
                                                                    eegg = 7
                                                                else:
                                                                    input("Você vê uma janela que abre horizontalmente para as duas direções, sendo que o vidro da janela esquerda está rachado por provavelmente um apedrejamento. Os batentes são de madeira antiga, deteriorada pela ação de cupins.")
                                        else:
                                            if (act == "olhar pela janela" or act == "olha pela janela" or act == "janela" or act ==  "olhar janela" or act == "olha janela" or act=="ver janela" or act=="ver a janela"):
                                                input("Você vê uma rua com prédios de classe baixa,")
                                                input("poucas pessoas passando com cara de cansadas,")
                                                input("mas você não consegue ver o horizonte,")
                                                input("já que você mora no primeiro andar e os prédios do outro lado da rua são altos e próximos demais uns dos outros.")
                                                input("Você percebe um sujeito te encarando do outro lado da rua...")
                                                input("Ele está em pé e encostado na grade cinza, empoeirada e enferrujada do prédio da frente um pouco à esquerda da porta dessa grade, de modo a ficar de frente para a porta do seu prédio.\nSua face cheia de raiva expressa com rigidez a sua intenção, sua jeans é velha, sua camisa é rasgada de forma a parecer uma regata, enquanto seus braços cruzados parecem prontos para uma briga!")
                                            else:
                                                if (act == "olhar a estante" or act == "olhar estante" or act == "olha a estante" or act == "olha estante" or act == "estante" or act == "ver a estante" or act == "ver estante" or act == "ver a estante" or act == "ver estante"):
                                                    input("Você vê livros e apostilas rabiscadas na capa e a maioria rasgadas no canto dos furos das espirais.\n...\n Nada muito interessante...\n")
                                                    input("Mas você vê um pedaço de papel vermelho colocado entre as páginas de um dos livros...")
                                                    print("Ler o bilhete??\n")
                                                    while 1:
                                                        act=input("-")
                                                        act=act.lower()
                                                        if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                                            input(' "       Você pode digitar seus comandos de outras formas, como por exemplo,')
                                                            input("ao invés de digitar 'ver ficha do personagem' você pode simplesmente digitar 'ficha'!")
                                                            input('Tente sempre digitar da forma mais simples, isso facilitará muito o seu jogo!')
                                                            input('Não custa nada tentar! ;)')
                                                            input('                               assinado: Programador "')
                                                            break
                                                        else:
                                                            if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                                input("Você ignorou o bilhete.")
                                                                break
                                                            else:
                                                                input('Entrada inválida! Digite "sim" ou "Não"')
                                                else:
                                                    if (act == "destruir o universo"): #Easter-Egg
                                                        input("Adeus...")
                                                        while(act != "reconstruir o universo"):
                                                            act = input("")
                                                            act = act.lower()
                                                            if(act == "construir o universo" or act == "criar um novo universo" or act == "construir um universo" or act == "criar o universo"):
                                                                act="reconstruir o universo"
                                                        input("Olá!")
                                                    else:
                                                        if(act=="sair do quarto" or act=="sair" or act=="ir para a aula" or act=="ir pra aula" or act=="ir para aula" or act=="ir à aula" or act=="ir a aula" or act=="sair quarto"):
                                                            while 1:
                                                                input("Se sair você nao poderá voltar.")
                                                                print("Tem certeza que deseja sair? (sim ou não)")
                                                                act=input("-")
                                                                act=act.lower()
                                                                if(act=="sim" or act=="s" or act=="si" or act=="sm" or act=="im" or act=="ssim"):
                                                                    act="sim"
                                                                    break
                                                                else:
                                                                    if(act == "não" or act=="n" or act=="nao" or act=="no" or act=="na" or act=="nã" or act=="ao" or act=="ão" or act=="ñ" or act=="ñão" or act=="ño" or act=="ñõ" or act=="ñã" or act=="ñaõ" or act=="aõ"):
                                                                        input("Você decidiu não sair do quarto.")
                                                                        break
                                                                    else:
                                                                        input("Entrada inválida!")
                                                            if(act=="sim"):
                                                                break
                                                        else:
                                                            input('\nEntrada Inválida!\n')
                                                            input("Você pode:")
                                                            input("vestir")
                                                            input("arrumar o quarto")
                                                            input("olhar")
                                                            if (olh == "sim"):
                                                                input("olhar as gavetas")
                                                                input("olhar o guarda-roupas")
                                                                input("olhar a estante")
                                                                input("olhar pela janela")
                                                            input("ver ficha do personagem")
                                                            input("sair do quarto\n")
                print("\n#", "-"*30,"#\n\nLista de Ações\n\nCenário:", lug,"\n\nVocê pode:\n\nvestir\narrumar o quarto\nolhar\n")
                if (olh == "sim"):
                    print("\nolhar as gavetas\nolhar o guarda-roupas\nolhar a estante\nolhar pela janela\n")
                print("\nver ficha do personagem\nsair do quarto\n")
                if(eegg > 1 and eegg<6):
                    print("\nVocê não deve:\nolhar a janela\n")
                print("\n#", "-"*30,"#\n")
                print("\nE agora, ", x,", o que você vai fazer?\n")
                act = input("-")
                act = act.lower()
            if(hpa<=0):break
            z = 1
            cen = "não"
            olh = "não"
            lug = "seu prédio, 1º andar"
            input("Você saiu do seu quarto.")
            save()

##########--------------------------------------------------FIM DA PRIMEIRA PARTE--------------------------------------------------##########
        if(z==1):
            input("\nCenário: Você continua atrasado para a aula - não que você deva se importar muito com isso.")
            primeiroAndar()
            if(hpa<=0):break
            z = 2
            lug = "em frente ao seu prédio"
            hmr01 = 0
            save()

##########--------------------------------------------------FIM DA SEGUNDA PARTE--------------------------------------------------##########
        if(z==2):
            input("Cenário:Agora você está na sua rua.\n")
            input("Antes que você pudesse fazer alguma coisa,")
            input("foi abordado por um homem forte vestindo uma jeans velha e uma camisa que foi rasgada de forma a parecer uma regata...\n")
            input(" - Cadê o dinheiro que você roubou do meu esquema?\n")
            input("Mas você REALMENTE não sabia de esquema algum, quanto menos do dinheiro...")
            input("Algo não parece certo...\n")
            input(" - Não adianta negar!!! Escolhe, moleque: a grana ou a vida???")
            print("...")
            input("Ele saca uma faca do bolso de trás!\n")
            input(" - EU VOU TE QUEBRAR ATÉ VOCÊ ME DAR O DINHEIRO!!!\n")
            y="Bandido"
            hxi=2500
            hai=2500
            ati=300
            dfi=100
            batalha()
            if(hpa<=0):break
            if(hai>0):
                while(hai>0):
                    input("Você correu um pouco mas ele te alcançou de novo!\n")
                    batalha()
                if(hpa<=0):break
                input(" - Pare! Por favor!\n")
                print("...")
                input("Antes que você pudesse perceber o som da moto, um comparsa o resgatou...")
                input("Voce continua sem respostas...")
                input("Será que você encontrará alguma pista na escola?")
            else:
                input(" - Pare! Por favor!\n")
                print("...")
                input("Antes que você pudesse perceber o som da moto, um comparsa o resgatou...")
                input("Voce continua sem respostas...")
                input("Será que você encontrará alguma pista na escola?")
            z = 3
            lug = "sua rua"
            save()

##########--------------------------------------------------FIM DA TERCEIRA PARTE--------------------------------------------------##########
        if(z==3):
            input("Cenário:\n")
            

##########--------------------------------------------------FIM DO JOGO--------------------------------------------------##########
        break
    if (hpa <= 0):
        print("Você morreu, ", x, "...\nO jogo acabou para você...")
        #--Variáveis de Texto--#
        x = "" #nome do personagem
        y = "Inimigo" #nome do inimigo
        act = "" #ação do personagem
        escapar = "" #variável em batalha e pós batalha para conferir condições de evento
        rpa = "Pijama" #"armadura"
        mao = "Nada" #"arma"
        
        olh = "não" #confere: se olhou ou não o cenário
        cen = "não" #confere: se modificou ou não o cenário
        che = "não" #confere: se cheirou ou não o cenário
        obj00 = "não" #confere: se modificou ou não o objeto 0
        obj01 = "não" #confere: se modificou ou não o objeto 0
        lug = "seu quarto" #local do cenário
        desejajogarnovamente = "" #deseja jogar novamente?
        #--Variáveis de Número--#
        z = 0 #variável de ponto de save
        eegg = 1 #condição do easter egg 1
        hpx = 1000 #hp máximo do personagem 
        hpa = 1000 #hp atual do personagem 
        d = 0 #dinheiro do personagem 
        atq = 100 #poder de ataque do personagem 
        dfs = 80 #poder de defesa do personagem 
        hxi = 30 #hp máximo do inimigo 
        hai = 30 #hp atual do inimigo 
        ati = 5 #poder de ataque do inimigo 
        dfi = 5 #poder de defesa do inimigo 
        hmr01 = 0 #humor da moradora do quarto 11 
        dado = 0 #variável para testar a sorte
        dano = 0 #variável para calcular dano 
        fuga = 0 #variável para calcular fuga
        comparar = 0 #para uso de comparação
        contador01 = 0 #contador no01
        contador02 = 0 #contador no02
    else:
        print("\nParabéns, ", x,"!!! Você terminou o jogo!!!")
    print("\nVocê deseja jogar novamente, ", x,'?("sim" ou "não")\n')
    desejajogarnovamente = input("-")
    desejajogarnovamente = desejajogarnovamente.lower()
    if(desejajogarnovamente!="sim" and desejajogarnovamente!="não"):
        print('\nEntrada inválida!(digite "sim" ou "não)\n')
        desejajogarnovamente = input("-")
        desejajogarnovamente = desejajogarnovamente.lower()
exit()
