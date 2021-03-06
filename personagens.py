from asyncio.format_helpers import _format_callback_source

class CriarPersonagem():
    def __init__(self, vida, vidaMax, ataque, defesa, classe, nome, critico,
    inteligencia, mana, manaMax, regenMana, habilidades, habilidadesDesc, artefatosDesc, 
    ouro, caminhado, artefatos, danoAumentado, passar, podeAgir, criticoGarantido, foiCritico,
    dano, danoReal, acaoBonus):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.classe = classe
        self.critico = critico
        self.inteligencia = inteligencia
        self.mana = mana
        self.manaMax = manaMax
        self.regenMana = regenMana
        self.habilidades = habilidades
        self.habilidadesDesc = habilidadesDesc
        self.nome = nome
        self.ouro = ouro
        self.caminhado = caminhado
        self.artefatos = artefatos
        self.artefatosDesc = artefatosDesc
        self.danoAumentado = danoAumentado
        self.passar = passar
        self.podeAgir = podeAgir
        self.criticoGarantido = criticoGarantido
        self.foiCritico = foiCritico
        self.dano = dano
        self.danoReal = danoReal
        self.acaoBonus = acaoBonus
        


class timers():
    def __init__(self, defesa, podeAgir, danoAumentado, monstroAgir, tempoCombate, quantidadeHabilidades, ataque, tempoAtaque, custoMana, encantamentoAtivo):
        self.defesa = defesa
        self.podeAgir = podeAgir
        self.danoAumentado = danoAumentado
        self.monstroAgir = monstroAgir
        self.tempoCombate = tempoCombate
        self.quantidadeHabilidades = quantidadeHabilidades
        self.ataque = ataque
        self.tempoAtaque = tempoAtaque
        self.custoMana = custoMana
        self.encantamentoAtivo = encantamentoAtivo


class npc():
    def __init__(self, vida, vidaMax, ataque, defesa, nome, critico, ouro, podeAgir, dano, danoReal, envenenamento):
        self.vida = vida
        self.vidaMax = vidaMax
        self.ataque = ataque
        self.defesa = defesa
        self.nome = nome
        self.critico = critico
        self.ouro = ouro
        self.podeAgir = podeAgir
        self.dano = dano
        self.danoReal = danoReal
        self.envenenamento = envenenamento

class loja():
    def __init__(self, artefatosComprados, habilidadesComprados):
        self.artefatosComprados = artefatosComprados
        self.habilidadesComprados = habilidadesComprados
class carregar():
    def __init__ (self, listaNumerosSave ,listaHabilidades, listaArtefatos, contSave):
        self.listaNumerosSave = listaNumerosSave
        self.contSave = contSave
        self.listaHabilidades = listaHabilidades
        self.listaArtefatos = listaArtefatos
        

#-------------------------------------------- Personagens ---------------------------------------------------------
habilidades = []
habilidadesDesc = []
artefatos = []
artefatosDesc = []
salvo = carregar(listaNumerosSave= [],
                listaHabilidades= [],
                contSave = 50,
                listaArtefatos = [])

efx = timers(defesa = 0,
            podeAgir= 0,
            danoAumentado = 0,
            monstroAgir = 0,
            tempoCombate=0,
            quantidadeHabilidades = 0,
            ataque= 0,
            tempoAtaque = 0,
            custoMana = 0,
            encantamentoAtivo= {0:0})
Compraveis = loja   (artefatosComprados = ['ALB','AGG','AIX','APP','AHSS','AIE'],
                    habilidadesComprados = ['HCL','HPA','HEO','HFD','HEP','HEF'])

Sabel = CriarPersonagem(vida=26,
                        vidaMax=26,
                        ataque=8,
                        defesa=34,
                        classe="SABEL",
                        critico=8,
                        nome='Greg',
                        inteligencia=4,
                        mana=7,
                        manaMax=7,
                        regenMana=1,
                        habilidades=habilidades,
                        artefatos=artefatos,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        ouro= 85,
                        caminhado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False,
                        dano = 0,
                        danoReal= 0,
                        acaoBonus=True)

Santos = CriarPersonagem(vida=35,
                        vidaMax=35,
                        ataque=6,
                        defesa=55,
                        classe="SANTOS",
                        critico=6,
                        nome='Maicon',
                        inteligencia=3,
                        mana=6,
                        manaMax=6,
                        regenMana=1,
                        habilidades=habilidades,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        artefatos=artefatos,
                        ouro=85,
                        caminhado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False,
                        dano = 0,
                        danoReal= 0,
                        acaoBonus=True)

Reisch = CriarPersonagem(vida=21,
                        vidaMax=21,
                        ataque=9,
                        defesa=29,
                        classe="REISCH",
                        critico=3,
                        nome='Vinicius',
                        inteligencia=6,
                        mana=9,
                        manaMax=9,
                        regenMana=1,
                        habilidades=habilidades,
                        habilidadesDesc=habilidadesDesc,
                        artefatosDesc= artefatosDesc,
                        artefatos=artefatos,
                        ouro= 85,
                        caminhado=0,
                        danoAumentado=0,
                        passar = False,
                        podeAgir= True,
                        criticoGarantido = False,
                        foiCritico= False,
                        dano = 0,
                        danoReal= 0,
                        acaoBonus=True)