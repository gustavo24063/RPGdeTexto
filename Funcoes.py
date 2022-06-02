from asyncio.windows_events import NULL
import random
from sre_constants import OP_UNICODE_IGNORE
import Artefacts
from time import sleep
from re import S

def vidaLimite (jogador):
    if jogador.vida > jogador.vidaMax:
        jogador.vida = jogador.vidaMax

def manaLimite (jogador):
    if jogador.mana > jogador.manaMax:
        jogador.mana = jogador.manaMax

def adicionarHabilidade (jogador, efeito):
    habilidade = []
    if "HRDA" in jogador.habilidades:
        habilidade.append("(HRDA) Custo: [3] Rap de Academia -- Aumenta o dano do proximo ataque, se o inimigo sobreviver o jogador e atordoado ")
    if "HMR" in jogador.habilidades:
        habilidade.append("(HMR) Custo: [4] Multilação Regenerativa -- Perde até 2 de vida, causa dano baseado em INT + ATT, o dano causado é convertido em vida")
    if "HOAM" in jogador.habilidades:
        habilidade.append("(HOAM) Custo: [3] Organizar a Mente -- Recupera um pouco de vida, o proximo ataque será Critico")
    if "HCL" in jogador.habilidades:
        habilidade.append("(HCL) Custo: [5] Cura Leve -- Recupera vida baseado na sua inteligencia")
    if "HPA" in jogador.habilidades:
        habilidade.append("(HPA) Custo: [3] Pancada Atordoante -- Causa dano e tem 1/2 chance de atordoar")
    if "HEO" in jogador.habilidades:
        habilidade.append("(HEO) Custo: [2] Enfraquecer Oponente -- Reduz o dano do proximo ataque pela metade")
    for elemento in habilidade:
        if elemento not in jogador.habilidadesDesc:
            jogador.habilidadesDesc.append(f"{efeito.quantidadeHabilidades} - " + elemento)
            efeito.quantidadeHabilidades += 1

def calculaDano(atacante, defensor):
    mitiga = (defensor.defesa/100)+1
    vidaReal = defensor.vidaMax*mitiga
    atacante.danoReal = int((atacante.dano * defensor.vidaMax)/vidaReal)
    

def atacar(jogador, monstro, efeito):

    jogador.dano = (jogador.ataque + (random.randint(0, int(jogador.ataque*0.7))))
    jogador.dano += jogador.danoAumentado
    calculaDano(jogador, monstro)
    if random.randint(0, 100) < jogador.critico or jogador.criticoGarantido == True:
        jogador.danoReal *= 2
        print("DANO CRITICO!!!")
        jogador.foiCritico = True
            
    Artefacts.cabeloColorido(jogador)
    Artefacts.lagrimaBerserker(jogador, efeito)
    Artefacts.golpeGanancioso(jogador, monstro)
    monstro.vida -= jogador.danoReal
    vidaLimite(jogador)
    jogador.danoAumentado = 0
    jogador.criticoGarantido = False
    jogador.foiCritico = False
    jogador.passar = True
    print(f"VOCÊ INFLINGE: {jogador.danoReal}(-{jogador.dano-jogador.danoReal}) DE DANO")
    sleep(0.5)

    
def monstroAtacar(jogador, monstro, efeito):
    monstro.dano = ((monstro.ataque - efeito.ataque) + (random.randint(0, int((monstro.ataque-efeito.ataque)*0.7))))
    calculaDano(monstro, jogador)
    Artefacts.conhecimentoDor(jogador, monstro)
    Artefacts.masoquistaAcademia(jogador, monstro)
    print(f"VOCÊ SOFREU: {int(monstro.danoReal)}(-{int(monstro.dano-monstro.danoReal)}) DE DANO")
    if jogador.vida == NULL:
        jogador.vida = 0
    jogador.vida -= int(monstro.danoReal)
    

def status(jogador):
    print(f"STATUS {jogador.nome} \nVIDA : {jogador.vida}\nATAQUE : {jogador.ataque}\nDEFESA : {jogador.defesa}\nMANA : {jogador.mana}")
    return "\b"


def statusMonstro(monstro):
    print(f"STATUS {monstro.nome} \nVIDA : {monstro.vida}\nATAQUE : {monstro.ataque}\nDEFESA : {monstro.defesa}\n")
    return "\b"


def continuar():
    input("PRESSIONE ENTER PARA CONTINUAR")


def todosOsStatus(jogador):
    print(f"Vida: {jogador.vida}")
    print(f"Ataque: {jogador.ataque}")
    print(f"Inteligencia: {jogador.inteligencia}")
    print(f"Mana: {jogador.mana}")
    print(f"Defesa: {jogador.defesa}")
    print(f"Ouro: {jogador.ouro}")
    print(f"Habilidades: {jogador.habilidades}")
    print(f"Artefatos: {jogador.artefatos}")
    print(f"Critico: {jogador.critico}")

def apresentacaoDeClasse(classe, caracteristica):
  print(f"""{classe.classe}, {caracteristica}
    ATAQUE:       {classe.ataque}
    DEFESA:       {classe.defesa}
    VIDA:         {classe.vida}
    INTELIGENCIA: {classe.inteligencia}
    MANA:         {classe.mana}
    OURO:         {classe.ouro}            
  """)

def apresentacaoDeClasses1(classes):

  cabeca = f'Classe - Ata - Def - Vid - Int'
  atributos = ''
  nome = ''

  for c in classes:
    espacoAtributo = 4
    espacoClasse = 8 - len(c[0].classe)

    # Ifs para que o tamanho, em string, das variáveis seja o mesmo
    # caso o valor seja menor q 10, ou seja, tenha apenas um digito, é adicionado um espaço antes
    ataque       = '' if c[0].ataque > 9 else ' '  
    defesa       = '' if c[0].defesa > 9 else ' ' 
    vida         = '' if c[0].vida > 9 else ' '  
    inteligencia = '' if c[0].inteligencia > 9 else ' '  

    nome         += f'{c[0].classe}{" "*espacoClasse}'
    ataque       += f'{c[0].ataque}{" "*espacoAtributo} '
    defesa       += f'{c[0].defesa}{" "*espacoAtributo} '
    vida         += f'{c[0].vida}{" "*espacoAtributo} '
    inteligencia += f'{c[0].inteligencia}\n'

    atributos += nome + ataque + defesa + vida + inteligencia


  print('\n')
  print(cabeca)
  print(atributos)
  print('\n')


def apresentacaoDeClasses2(classes):

  cabeca       = f'CLASSES:   '
  ataque       = f'Ata:       '
  defesa       = f'Def:       '
  vida         = f'Vid:       '
  inteligencia = f'Int:       '


  for classe in classes:
    espaco = len(classe[0].classe) + 5
    
    # ifs para que o tamanho, em string, das variáveis seja o mesmo
    # caso o valor seja menor q 10, ou seja, tenha apenas um digito, é adicionado um espaço antes 
    ataque       += '' if classe[0].ataque > 9 else ' '  
    defesa       += '' if classe[0].defesa > 9 else ' '  
    vida         += '' if classe[0].vida > 9 else ' '  
    inteligencia += '' if classe[0].inteligencia > 9 else ' '  

    cabeca       += f'{classe[1]} {classe[0].classe} - '
    ataque       += f'{classe[0].ataque}{" "*espaco}'
    defesa       += f'{classe[0].defesa}{" "*espaco}'
    vida         += f'{classe[0].vida}{" "*espaco}'
    inteligencia += f'{classe[0].inteligencia}{" "*espaco}'


  print(f"""{cabeca}
  {ataque}  
  {defesa}  
  {vida}
  {inteligencia}
  """)
  print('\n')
  print('\n')





# print('\n ~~teste apresentacaoDeClasses1 apresentacaoDeClasses2~~~~')
# import personagens
# apresentacaoDeClasses1( [[personagens.Sabel, '(S)'], 
#                         [personagens.Santos, '(SA)'], 
#                         [personagens.Reisch, '(R)']] )

# apresentacaoDeClasses2( [[personagens.Sabel, '(S)'], 
#                         [personagens.Santos, '(SA)'], 
#                         [personagens.Reisch, '(R)']] )                        