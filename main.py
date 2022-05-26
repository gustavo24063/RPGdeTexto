from asyncio.windows_events import NULL
import random
from re import T
from time import monotonic, sleep
import Funcoes
import personagens
import os
import Effects
import Skills
import Loja
input("Quando você ver esse simbolo '!' : pressione enter para continuar ou espere um pouco")
sleep(1)
os.system('cls') or None

print("\n ------------CLASSES------------")

# --------------------------------- VARIÁVEIS --------------------------------- #

#EVENTOS
encerrarCombate = False
emboscada = False
monologo = False

#CAMINHOS
enfrentarMonstroElite = False
caminhoChefe = False
enfrentarMonstroComun = False
acessarMisterio = False

#STATUS
dano = 0
ouro = 0
marcadorArea = 0
artefatos = []

habilidades = []
classes = ["SA", "S", "R"]
decisaoClasse = ""
efeito = personagens.efx

# --------------------------------- INÍCIO --------------------------------- #

input("Quando você ver esse simbolo '!' : pressione enter para continuar e espere um pouco")
sleep(1)
os.system('cls') or None
nome = input("Digite seu nome: ")
print("\n ------------CLASSES------------")

Funcoes.apresentacaoDeClasse(personagens.Sabel, 'o somelier de estagio(S)')
Funcoes.apresentacaoDeClasse(personagens.Santos, 'o bombado(SA)')
Funcoes.apresentacaoDeClasse(personagens.Reisch, 'o emo feliz(R)')


#ESCOLHA DE CLASSE
while decisaoClasse not in classes:
  decisaoClasse = input("Digite a letra inicial da sua classe : ")
  decisaoClasse = decisaoClasse.upper()
  if decisaoClasse in classes:
    if decisaoClasse == "SA":

        personagens.Santos.artefatos.append("AMDA")#Artefato >Masoquista da academia<        
                                                   #sempre que o jogador recebe dano, o proximo ataque do jogador causa dano extra
        personagens.Santos.habilidades.append("HRDA")
        jogador = personagens.Santos

    elif decisaoClasse == "S":

        personagens.Sabel.artefatos.append("ACC")#Critico recupera vida e ignora o dano mitigado
        personagens.Sabel.habilidades.append("HOAM")
        jogador = personagens.Sabel

    elif decisaoClasse == "R":

        personagens.Reisch.artefatos.append("ACD") #Artefato >Conhecimento da dor<
                                                   #sempre que o jogador recebe dano metade desse dano é convertido em mana
        personagens.Reisch.habilidades.append("HMR")
        jogador = personagens.Reisch

jogador.nome = input("Digite seu nome: ")
os.system('cls') or None
print(f"CLASSE {jogador.classe} ESCOLHIDA")
sleep(2)
os.system('cls') or None
#ENQUANTO A VIDA DO JOGADOR FOR MAIOR QUE 0 O JOGO VAI CONTINUAR RODANDO
while jogador.vida > 0:
    if marcadorArea == 0 and not monologo:
        input("Você adentra a floresta de Cornwood, o sol se torna apenas um borrão entre as árvores... !:")
        os.system('cls') or None
        monologo = True
    elif marcadorArea == 1 and monologo:
        input("!:")
        monologo = False

    print("~~~~~~Caminhos~~~~~~\n")
    caminhoMisterio = False
    caminhoMonstroComun = False
    caminhoMonstroElite = False
    caminhoLoja = False
    jogador.passar = False

    while not jogador.passar:
        jogador.caminhado += 1
        caminhos = random.randint(4,5)
        print(f"Seu saldo: {jogador.ouro}\n\nVocê pode: ")
        cont = 0
        if jogador.caminhado < 10 and jogador.caminhado != 1:
            while cont < caminhos:
                escolha = random.randint(1, 100)
                if escolha > 0 and escolha <= 50:
                    print(f"Lutar com um monstro comun(C)\n")
                    caminhoMonstroComun = True
                elif escolha > 50 and escolha <= 80:
                    print(f"Lutar com um monstro de Elite(E)\n")
                    caminhoMonstroElite = True
                elif escolha > 80 and escolha <= 100:
                    print(f"Entrar na loja(L)\n")
                    caminhoLoja = True
                cont+= 1
        elif jogador.caminhado == 1:
            print(f"Lutar com um monstro comun(C)\n")
            caminhoMonstroComun = True
        else:
            input(f"Você sente uma presença ameaçadora !:")
            caminhoChefe = True
            jogador.caminhado = 0
            jogador.passar = True
            break

        while True:

            decisaoExplorar = input("\nQual sua escolha: ")
            decisaoExplorar = decisaoExplorar.upper()

            if caminhoChefe:
                
                jogador.passar = True
            elif decisaoExplorar == "C" and caminhoMonstroComun:
                enfrentarMonstroComun = True
                jogador.passar = True
                break

            elif decisaoExplorar == "E" and caminhoMonstroElite:
                enfrentarMonstroElite = True
                jogador.passar = True
                break

            elif decisaoExplorar == "L" and caminhoLoja:
                Loja.comprarNaLoja(jogador)
                break
                
            elif decisaoExplorar == "M" and caminhoMisterio:
                acessarMisterio = True
                jogador.passar = True
                break

            else:
                print("Decisao Invalida")

        os.system('cls') or None

    #A PARTIR DE UMA INT ALEATORIA É ESCOLHIDO UM MONSTRO PARA BATALHAR
    decisaoMonstro = random.randint(0,1)
    if marcadorArea == 0:
        if decisaoMonstro == 0 and enfrentarMonstroComun:

            print("UM SLIME APARECE!!!\n")
            monstro = personagens.npc(vida = 20, vidaMax= 20, ataque= 4, defesa= 24,
                nome="SLIME", critico= 5, ouro= 23, podeAgir = True, dano = 0, danoReal = 0)
            enfrentarMonstroComun = False

        elif decisaoMonstro == 1 and enfrentarMonstroComun:
            print("UM GOBLIN APARECE!!!\n")
            monstro = personagens.npc(vida = 17, vidaMax= 17, ataque= 6, defesa= 15,
                nome="GOBLIN", critico= 7, ouro=23, podeAgir = True, dano = 0, danoReal = 0)
            enfrentarMonstroComun = False

        elif enfrentarMonstroElite:
            print("UM GOLEM BEBE APARECE!!!\n")
            monstro = personagens.npc(vida = 35, vidaMax= 35, ataque= 8, defesa= 41,
                nome="GOLEM BEBE", critico= 0, ouro= 40, podeAgir = True, dano = 0, danoReal = 0)
            efeito.monstroAgir = 1
            enfrentarMonstroElite = False

        elif caminhoChefe:
            print("O REI SLIME SE IRRITOU COM SEUS ATOS!!!\n")
            monstro = personagens.npc(vida = 75, vidaMax= 75, ataque= 13, defesa= 36,
                nome="REI SLIME", critico= 0, ouro= 100, podeAgir = True, dano = 0, danoReal = 0)
            caminhoChefe = False
            marcadorArea = 1

    #O COMBATE VAI OCORRER ENQUANTO A CONDIÇÃO "encerrarCombate" FOR FALSA
    encerrarCombate = False
    efeito.tempoCombate = 0
    
    #monstro.danoMitigado = monstro.defesa

    while not encerrarCombate:
        jogador.passar = False
        efeito.tempoCombate += 1
        #AREA QUE CONTROLA BUFFS QUE DURAM MAIS DE UM TURNO
        #if efeito.defesa == 0:
        #    jogador.danoMitigado = jogador.defesa
        #else:
        #    efeito.defesa -= 1
        #MELHORAR O SISTEMA DE STUN
        Effects.atordoar(jogador, efeito)
        #BUFFAR DANO
        if efeito.danoAumentado == 0:
            jogador.danoAumentado = 0
        else:
            efeito.danoAumentado = efeito.danoAumentado - 1

        #MOSTRA OS STATUS ATUAIS DO JOGADOR E DO MONSTRO
        Funcoes.status(monstro)
        Funcoes.status(jogador)
        Funcoes.continuar()
        #MOSTRA AS DECISOES DE COMBATE PARA O JOGADOR
        if jogador.podeAgir:
            jogador.passar = False
            while not jogador.passar:

                print("AÇÕES :\n(A)ATACAR\n(H)HABILIDADES\n(F)FUGIR\n(I)ITENS\n")
                decisaoCombate = input("ESCOLHA UMA AÇÃO: ")
                decisaoCombate = decisaoCombate.upper()
                os.system('cls') or None

                if decisaoCombate == "A":
                    Funcoes.atacar(jogador, monstro, efeito)
                elif decisaoCombate == "H":

                    while True:
                        Funcoes.adicionarHabilidade(jogador)
                        for habilidade in jogador.habilidadesDesc:
                            print(habilidade)

                        print("Voltar(V)")
                        decisaoHabilidade = (input("ESCOLHA UMA HABILIDADE: ")).upper()

                        if decisaoHabilidade == "HMR" and "HMR" in jogador.habilidades and jogador.mana >= 3:
                            sleep(1)
                            Skills.multilacaoRegenerativa(jogador, monstro)
                            break

                        elif decisaoHabilidade == "HOAM" and "HOAM" in jogador.habilidades:
                            Skills.organizarAMente(jogador)
                            break

                        elif decisaoHabilidade == "HRDA" and "HRDA" in jogador.habilidades:
                            Skills.rapDeAcademia(jogador, efeito)
                            break

                        elif decisaoHabilidade == "HCL" and "HCL" in jogador.habilidades:
                            Skills.curaLeve(jogador)
                            break

                        elif "V":
                            break

                        else:
                            print("")

                elif decisaoCombate == "F":
                    encerrarCombate = True
                    jogador.passar = True
                elif decisaoCombate == "I":
                    Funcoes.todosOsStatus(jogador)
                else:
                    print("")

        #CALCULA, APLICA E MOSTRA O DANO DO MONSTRO ALEM DE VERIFICAR SE UMA EMBOSCADA JA FOI REALIZADA
        if monstro.vida > 0 and efeito.monstroAgir == 0:
           Funcoes.monstroAtacar(jogador, monstro)

        elif efeito.monstroAgir > 0:
            efeito.monstroAgir -= 1

        if jogador.vida <= 0:
            encerrarCombate = True
            print("Você morreu... ")
            sleep(2)
            exit(0)

        elif monstro.vida <=0:
            print("O MONSTRO MORREU!")
            encerrarCombate = True
            Funcoes.continuar()
            ouro = random.randint(int(monstro.ouro),int(monstro.ouro*1.5))
            print(f"+{ouro}G")
            jogador.ouro += ouro
            efeito.podeAgir = 0