# -*- coding: utf-8 -*-
"""
FUTEBOL ROBO - Simulacao com a biblioteca Turtle
--------------------------------------------------
Um "robo" (representado pela propria tartaruga) desenha um campo de
futebol oficial completo, monta o cenario do estadio (arquibancada,
torcida, sol, nuvens, placar, nome do estadio) e, em seguida, anima a
entrada dos jogadores de dois times (azul e vermelho), do arbitro e da
bola. Ao final, e exibido "APITO INICIAL!" e a partida comeca com a
bola rolando ate o centro e um jogador dando o primeiro toque.

Bibliotecas utilizadas: turtle, math, time, random (todas nativas do
Python - nenhuma biblioteca externa e necessaria).
"""

import turtle
import math
import time
import random

# ============================================================
# CONFIGURACAO GERAL DA TELA
# ============================================================
tela = turtle.Screen()
tela.setup(width=1150, height=950)
tela.title("Robo Desenhista - Estadio de Futebol")
tela.bgcolor("#87CEEB")  # ceu azul
tela.tracer(0)           # desliga atualizacao automatica (animacao manual)

# Tartaruga "robo" usada para todos os desenhos estaticos do cenario/campo
robo = turtle.Turtle()
robo.hideturtle()
robo.speed(0)
robo.width(3)

# ============================================================
# CONSTANTES DE DIMENSAO DO CAMPO (sistema de coordenadas da tela)
# ============================================================
CAMPO_ESQ = -320
CAMPO_DIR = 320
CAMPO_CIMA = 180
CAMPO_BAIXO = -180
CAMPO_MEIO_X = (CAMPO_ESQ + CAMPO_DIR) / 2
CAMPO_MEIO_Y = (CAMPO_CIMA + CAMPO_BAIXO) / 2

STAND_ESQ = -420
STAND_DIR = 420
STAND_CIMA = 250
STAND_BAIXO = -250

CORES_TORCIDA = ["red", "blue", "yellow", "white", "green", "orange", "purple"]


# ============================================================
# FUNCOES AUXILIARES DE DESENHO BASICO
# ============================================================
def ir_para(t, x, y, angulo=0):
    """Levanta a caneta, posiciona a tartaruga e define o angulo."""
    t.penup()
    t.goto(x, y)
    t.setheading(angulo)
    t.pendown()


def retangulo(t, x, y, largura, altura, cor_borda="white", cor_preenchimento=None, espessura=3):
    """Desenha um retangulo a partir do canto inferior esquerdo (x, y)."""
    t.pencolor(cor_borda)
    t.width(espessura)
    if cor_preenchimento:
        t.fillcolor(cor_preenchimento)
        t.begin_fill()
    ir_para(t, x, y, 0)
    for _ in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
    if cor_preenchimento:
        t.end_fill()


def circulo_preenchido(t, x, y, raio, cor):
    """Desenha um circulo preenchido com centro aproximado em (x, y)."""
    t.fillcolor(cor)
    t.pencolor(cor)
    t.begin_fill()
    ir_para(t, x, y - raio, 0)
    t.circle(raio)
    t.end_fill()


# ============================================================
# CENARIO: CEU, SOL, NUVENS, ARQUIBANCADA E TORCIDA
# ============================================================
def desenhar_sol():
    """Desenha o sol no canto superior direito do ceu."""
    circulo_preenchido(robo, 430, 400, 35, "yellow")
    # raios do sol
    robo.pencolor("yellow")
    robo.width(3)
    for i in range(12):
        ang = i * 30
        ir_para(robo, 430, 400, ang)
        robo.forward(35)
        robo.forward(15)
        robo.penup()
        robo.goto(430, 400)


def desenhar_uma_nuvem(t, x, y, escala=1.0):
    """Desenha uma nuvem usando varios circulos sobrepostos."""
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    ir_para(t, x, y, 0)
    t.circle(18 * escala)
    t.penup()
    t.goto(x + 18 * escala, y + 8 * escala)
    t.pendown()
    t.circle(14 * escala)
    t.penup()
    t.goto(x - 16 * escala, y + 6 * escala)
    t.pendown()
    t.circle(12 * escala)
    t.end_fill()


def desenhar_nuvens():
    """Espalha algumas nuvens pelo ceu do estadio."""
    posicoes = [(-380, 410, 1.0), (-150, 430, 0.8), (120, 415, 1.1), (260, 440, 0.7)]
    for x, y, esc in posicoes:
        desenhar_uma_nuvem(robo, x, y, esc)


def desenhar_arquibancada():
    """Desenha o retangulo cinza das arquibancadas, atras do campo."""
    largura = STAND_DIR - STAND_ESQ
    altura = STAND_CIMA - STAND_BAIXO
    retangulo(robo, STAND_ESQ, STAND_BAIXO, largura, altura,
              cor_borda="#333333", cor_preenchimento="#777777", espessura=2)
    # listras horizontais para simular degraus da arquibancada
    robo.pencolor("#555555")
    robo.width(1)
    for y in range(STAND_BAIXO + 15, STAND_CIMA, 15):
        ir_para(robo, STAND_ESQ, y, 0)
        robo.forward(largura)


def desenhar_torcida():
    """Desenha a torcida como diversos pontos coloridos na arquibancada."""
    robo.pencolor("black")
    for _ in range(900):
        x = random.uniform(STAND_ESQ + 5, STAND_DIR - 5)
        y = random.uniform(STAND_BAIXO + 5, STAND_CIMA - 5)
        # garante que o ponto fique na regiao da arquibancada (fora do campo)
        if CAMPO_ESQ - 5 < x < CAMPO_DIR + 5 and CAMPO_BAIXO - 5 < y < CAMPO_CIMA + 5:
            continue
        cor = random.choice(CORES_TORCIDA)
        robo.penup()
        robo.goto(x, y)
        robo.dot(5, cor)


# ============================================================
# CAMPO DE FUTEBOL OFICIAL
# ============================================================
def desenhar_gramado():
    """Desenha o retangulo verde do gramado, com listras claras/escuras."""
    largura = CAMPO_DIR - CAMPO_ESQ
    altura = CAMPO_CIMA - CAMPO_BAIXO
    faixas = 12
    largura_faixa = largura / faixas
    for i in range(faixas):
        cor = "#2E8B22" if i % 2 == 0 else "#36A026"
        x = CAMPO_ESQ + i * largura_faixa
        retangulo(robo, x, CAMPO_BAIXO, largura_faixa, altura,
                  cor_borda=cor, cor_preenchimento=cor, espessura=1)


def desenhar_contorno_campo():
    """Desenha as linhas brancas oficiais do campo."""
    robo.pencolor("white")
    robo.width(4)
    largura = CAMPO_DIR - CAMPO_ESQ
    altura = CAMPO_CIMA - CAMPO_BAIXO
    # contorno externo
    ir_para(robo, CAMPO_ESQ, CAMPO_BAIXO, 0)
    for _ in range(2):
        robo.forward(largura)
        robo.left(90)
        robo.forward(altura)
        robo.left(90)

    # linha central (do meio de cima ao meio de baixo)
    ir_para(robo, CAMPO_MEIO_X, CAMPO_BAIXO, 90)
    robo.forward(altura)

    # circulo central
    ir_para(robo, CAMPO_MEIO_X, CAMPO_MEIO_Y - 45, 0)
    robo.circle(45)

    # marca do meio de campo
    robo.penup()
    robo.goto(CAMPO_MEIO_X, CAMPO_MEIO_Y)
    robo.dot(8, "white")


def desenhar_area(lado):
    """Desenha grande area, pequena area, marca de penalti e meia-lua de um lado.
    lado = 'esquerda' ou 'direita' """
    robo.pencolor("white")
    robo.width(3)

    if lado == "esquerda":
        x_linha = CAMPO_ESQ
        sinal = 1
    else:
        x_linha = CAMPO_DIR
        sinal = -1

    # GRANDE AREA (60 de profundidade, 180 de altura, centrada em y=0)
    grande_prof = 60
    grande_alt = 180
    x_grande = x_linha + sinal * grande_prof
    ir_para(robo, x_linha, -grande_alt / 2, 0)
    robo.setheading(0 if sinal > 0 else 180)
    robo.forward(grande_prof)
    robo.left(90)
    robo.forward(grande_alt)
    robo.left(90)
    robo.forward(grande_prof)

    # PEQUENA AREA (20 de profundidade, 80 de altura)
    pequena_prof = 20
    pequena_alt = 80
    ir_para(robo, x_linha, -pequena_alt / 2, 0)
    robo.setheading(0 if sinal > 0 else 180)
    robo.forward(pequena_prof)
    robo.left(90)
    robo.forward(pequena_alt)
    robo.left(90)
    robo.forward(pequena_prof)

    # MARCA DE PENALTI
    x_penalti = x_linha + sinal * 40
    robo.penup()
    robo.goto(x_penalti, 0)
    robo.dot(7, "white")

    # MEIA-LUA (arco fora da grande area, ao redor da marca de penalti)
    robo.penup()
    robo.goto(x_penalti, -38)
    robo.setheading(90 if sinal > 0 else 90)
    robo.pendown()
    if lado == "esquerda":
        robo.goto(x_penalti, -38)
        robo.setheading(0)
        robo.circle(38, extent=92, steps=40) if False else None
        # desenha o arco manualmente usando passos angulares (mantem so a parte externa a area)
        robo.penup()
        robo.goto(x_penalti + 38 * math.cos(math.radians(-53)),
                   38 * math.sin(math.radians(-53)))
        robo.pendown()
        for ang in range(-53, 54, 3):
            px = x_penalti + 38 * math.cos(math.radians(ang))
            py = 38 * math.sin(math.radians(ang))
            robo.goto(px, py)
    else:
        robo.penup()
        robo.goto(x_penalti + 38 * math.cos(math.radians(127)),
                   38 * math.sin(math.radians(127)))
        robo.pendown()
        for ang in range(127, 234, 3):
            px = x_penalti + 38 * math.cos(math.radians(ang))
            py = 38 * math.sin(math.radians(ang))
            robo.goto(px, py)
    robo.penup()


def desenhar_gols():
    """Desenha o gol (pequeno retangulo) saindo de cada linha de fundo."""
    largura_gol = 15
    altura_gol = 60
    robo.pencolor("white")
    robo.width(3)

    # gol esquerdo (para fora do campo)
    retangulo(robo, CAMPO_ESQ - largura_gol, -altura_gol / 2, largura_gol, altura_gol,
              cor_borda="white", espessura=3)
    # rede simulada com linhas diagonais
    for i in range(0, altura_gol, 12):
        ir_para(robo, CAMPO_ESQ - largura_gol, -altura_gol / 2 + i, 0)
        robo.forward(largura_gol)

    # gol direito
    retangulo(robo, CAMPO_DIR, -altura_gol / 2, largura_gol, altura_gol,
              cor_borda="white", espessura=3)
    for i in range(0, altura_gol, 12):
        ir_para(robo, CAMPO_DIR, -altura_gol / 2 + i, 0)
        robo.forward(largura_gol)


def desenhar_bandeirinha(x, y, virada_direita=True):
    """Desenha uma bandeirinha de escanteio em (x, y)."""
    robo.pencolor("white")
    robo.width(2)
    ir_para(robo, x, y, 90)
    robo.forward(18)
    # bandeira triangular colorida
    robo.fillcolor("yellow")
    robo.pencolor("yellow")
    robo.begin_fill()
    largura_bandeira = 10 if virada_direita else -10
    robo.goto(robo.xcor() + largura_bandeira, robo.ycor())
    robo.goto(robo.xcor() - largura_bandeira, robo.ycor() - 6)
    robo.goto(robo.xcor(), robo.ycor() + 6)
    robo.end_fill()


def desenhar_bandeirinhas():
    """Posiciona as 4 bandeirinhas de escanteio do campo."""
    desenhar_bandeirinha(CAMPO_ESQ, CAMPO_CIMA, virada_direita=True)
    desenhar_bandeirinha(CAMPO_ESQ, CAMPO_BAIXO, virada_direita=True)
    desenhar_bandeirinha(CAMPO_DIR, CAMPO_CIMA, virada_direita=False)
    desenhar_bandeirinha(CAMPO_DIR, CAMPO_BAIXO, virada_direita=False)


def desenhar_campo():
    """Funcao principal que monta o campo de futebol completo."""
    desenhar_gramado()
    desenhar_contorno_campo()
    desenhar_area("esquerda")
    desenhar_area("direita")
    desenhar_gols()
    desenhar_bandeirinhas()


# ============================================================
# PLACAR E NOME DO ESTADIO
# ============================================================
def desenhar_placar():
    """Desenha o placar na parte superior da tela."""
    retangulo(robo, -150, 380, 300, 50, cor_borda="black", cor_preenchimento="#111111", espessura=3)
    robo.penup()
    robo.goto(0, 392)
    robo.pencolor("white")
    robo.write("BRASIL  0  x  0  ARGENTINA", align="center",
                font=("Arial", 16, "bold"))


def desenhar_estadio():
    """Escreve o nome do estadio na parte inferior da tela."""
    robo.penup()
    robo.goto(0, -430)
    robo.pencolor("white")
    robo.write("ESTADIO TURTLE ARENA", align="center", font=("Arial", 20, "bold"))


# ============================================================
# DESENHO DE JOGADORES, ARBITRO E BOLA
# ============================================================
def desenhar_jogador(t, x, y, cor_uniforme, cor_pele="#F2C99E"):
    """Desenha um jogador (boneco) com cabeca, corpo, bracos e pernas,
    usando a tartaruga 't' centrada na posicao (x, y)."""
    t.penup()
    t.goto(x, y)
    t.pendown()

    # --- PERNAS ---
    t.pencolor("black")
    t.width(3)
    t.penup(); t.goto(x, y); t.setheading(250); t.pendown(); t.forward(11)
    t.penup(); t.goto(x, y); t.setheading(290); t.pendown(); t.forward(11)

    # --- CORPO (camiseta do time) ---
    t.pencolor(cor_uniforme)
    t.width(6)
    t.penup(); t.goto(x, y); t.setheading(90); t.pendown(); t.forward(20)

    # --- BRACOS ---
    t.pencolor(cor_uniforme)
    t.width(3)
    ombro_x, ombro_y = x, y + 16
    t.penup(); t.goto(ombro_x, ombro_y); t.setheading(200); t.pendown(); t.forward(12)
    t.penup(); t.goto(ombro_x, ombro_y); t.setheading(-20); t.pendown(); t.forward(12)

    # --- CABECA ---
    t.penup()
    t.goto(x, y + 25)
    t.dot(14, cor_pele)
    # contorno da cabeca
    t.pencolor("black")


def desenhar_arbitro(t, x, y):
    """Desenha o arbitro com uniforme preto."""
    desenhar_jogador(t, x, y, cor_uniforme="black", cor_pele="#F2C99E")


def desenhar_bola(t, x, y, raio=8):
    """Desenha a bola de futebol (branca com detalhes pretos)."""
    t.penup()
    t.goto(x, y)
    t.dot(raio * 2, "white")
    t.pencolor("black")
    t.width(1)
    # alguns "gomos" para parecer bola de futebol
    for ang in (0, 72, 144, 216, 288):
        t.penup()
        t.goto(x, y)
        t.setheading(ang)
        t.pendown()
        t.forward(raio - 2)
        t.penup()
        t.goto(x, y)


# ============================================================
# MONTAGEM DOS TIMES (POSICOES TATICAS 4-4-2)
# ============================================================
def gerar_posicoes_time(lado):
    """Gera 11 posicoes de um time em esquema 4-4-2.
    lado = 'azul' (joga na esquerda) ou 'vermelho' (joga na direita)."""
    posicoes = []
    if lado == "azul":
        sinal = -1
        # goleiro
        posicoes.append((CAMPO_ESQ + 15, 0))
        # zaga (4)
        for y in (-80, -27, 27, 80):
            posicoes.append((CAMPO_ESQ + 60, y))
        # meio campo (4)
        for y in (-90, -30, 30, 90):
            posicoes.append((CAMPO_MEIO_X - 60, y))
        # ataque (2)
        for y in (-35, 35):
            posicoes.append((CAMPO_MEIO_X - 15, y))
    else:
        sinal = 1
        # goleiro
        posicoes.append((CAMPO_DIR - 15, 0))
        # zaga (4)
        for y in (-80, -27, 27, 80):
            posicoes.append((CAMPO_DIR - 60, y))
        # meio campo (4)
        for y in (-90, -30, 30, 90):
            posicoes.append((CAMPO_MEIO_X + 60, y))
        # ataque (2)
        for y in (-35, 35):
            posicoes.append((CAMPO_MEIO_X + 15, y))
    return posicoes


def criar_turtles_times():
    """Cria as tartarugas (uma por jogador) que serao usadas na animacao."""
    turtles_azul = [turtle.Turtle() for _ in range(11)]
    turtles_vermelho = [turtle.Turtle() for _ in range(11)]
    for t in turtles_azul + turtles_vermelho:
        t.hideturtle()
        t.speed(0)
        t.penup()
    return turtles_azul, turtles_vermelho


# ============================================================
# ANIMACAO: ENTRADA DOS JOGADORES, ARBITRO E BOLA
# ============================================================
def interpolar(p1, p2, fracao):
    """Calcula um ponto intermediario entre p1 e p2 (0.0 a 1.0)."""
    x = p1[0] + (p2[0] - p1[0]) * fracao
    y = p1[1] + (p2[1] - p1[1]) * fracao
    return (x, y)


def entrada_dos_jogadores():
    """Anima a entrada dos 22 jogadores, do arbitro e da bola em campo."""
    turtles_azul, turtles_vermelho = criar_turtles_times()
    destinos_azul = gerar_posicoes_time("azul")
    destinos_vermelho = gerar_posicoes_time("vermelho")

    # pontos de partida: jogadores saem de fora do campo (tunel de vestiario)
    inicio_azul = (CAMPO_ESQ - 80, -250)
    inicio_vermelho = (CAMPO_DIR + 80, -250)

    origens_azul = [inicio_azul for _ in range(11)]
    origens_vermelho = [inicio_vermelho for _ in range(11)]

    # arbitro e bola
    arbitro = turtle.Turtle()
    arbitro.hideturtle()
    arbitro.speed(0)
    arbitro.penup()
    origem_arbitro = (0, -260)
    destino_arbitro = (CAMPO_MEIO_X, 15)

    bola_t = turtle.Turtle()
    bola_t.hideturtle()
    bola_t.speed(0)
    bola_t.penup()
    origem_bola = (0, -270)
    destino_bola = (CAMPO_MEIO_X, 0)

    passos = 40
    for passo in range(1, passos + 1):
        fracao = passo / passos
        # time azul
        for i, t in enumerate(turtles_azul):
            t.clear()
            x, y = interpolar(origens_azul[i], destinos_azul[i], fracao)
            desenhar_jogador(t, x, y, "#1E5FFF")
        # time vermelho
        for i, t in enumerate(turtles_vermelho):
            t.clear()
            x, y = interpolar(origens_vermelho[i], destinos_vermelho[i], fracao)
            desenhar_jogador(t, x, y, "#E61C1C")
        # arbitro entra um pouco depois (apenas na segunda metade da animacao)
        if fracao > 0.4:
            fracao_arb = min(1.0, (fracao - 0.4) / 0.6)
            arbitro.clear()
            x, y = interpolar(origem_arbitro, destino_arbitro, fracao_arb)
            desenhar_arbitro(arbitro, x, y)
        # bola entra junto com o arbitro
        if fracao > 0.5:
            fracao_bola = min(1.0, (fracao - 0.5) / 0.5)
            bola_t.clear()
            x, y = interpolar(origem_bola, destino_bola, fracao_bola)
            desenhar_bola(bola_t, x, y)

        tela.update()
        time.sleep(0.03)

    # garante posicionamento final exato de todos
    for i, t in enumerate(turtles_azul):
        t.clear()
        desenhar_jogador(t, destinos_azul[i][0], destinos_azul[i][1], "#1E5FFF")
    for i, t in enumerate(turtles_vermelho):
        t.clear()
        desenhar_jogador(t, destinos_vermelho[i][0], destinos_vermelho[i][1], "#E61C1C")
    arbitro.clear()
    desenhar_arbitro(arbitro, destino_arbitro[0], destino_arbitro[1])
    bola_t.clear()
    desenhar_bola(bola_t, destino_bola[0], destino_bola[1])
    tela.update()

    return turtles_azul, turtles_vermelho, destinos_azul, destinos_vermelho, bola_t


# ============================================================
# INICIO DA PARTIDA
# ============================================================
def mostrar_apito_inicial():
    """Mostra a mensagem 'APITO INICIAL!' no centro da tela por alguns segundos."""
    aviso = turtle.Turtle()
    aviso.hideturtle()
    aviso.penup()
    aviso.goto(0, 0)
    aviso.pencolor("yellow")
    aviso.write("APITO INICIAL!", align="center", font=("Arial", 36, "bold"))
    tela.update()
    time.sleep(3)
    aviso.clear()
    tela.update()


def iniciar_partida(bola_t, destinos_azul):
    """Move a bola ate o centro e simula o primeiro toque da partida."""
    # a bola ja esta no centro do campo; um atacante se aproxima e da o toque
    atacante = turtle.Turtle()
    atacante.hideturtle()
    atacante.speed(0)
    atacante.penup()

    pos_atacante_inicial = destinos_azul[9]  # um dos atacantes do time azul
    pos_atacante_final = (CAMPO_MEIO_X - 20, -10)

    passos = 20
    for passo in range(1, passos + 1):
        fracao = passo / passos
        atacante.clear()
        x, y = interpolar(pos_atacante_inicial, pos_atacante_final, fracao)
        desenhar_jogador(atacante, x, y, "#1E5FFF")
        tela.update()
        time.sleep(0.03)

    # primeiro toque: bola se move alguns metros para a frente (em direcao ao time vermelho)
    pos_bola_inicial = (CAMPO_MEIO_X, 0)
    pos_bola_final = (CAMPO_MEIO_X + 70, 25)
    passos_bola = 25
    for passo in range(1, passos_bola + 1):
        fracao = passo / passos_bola
        bola_t.clear()
        x, y = interpolar(pos_bola_inicial, pos_bola_final, fracao)
        desenhar_bola(bola_t, x, y)
        tela.update()
        time.sleep(0.03)

    # mensagem final de partida em andamento
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, -460)
    msg.pencolor("white")
    msg.write("A PARTIDA COMECOU!", align="center", font=("Arial", 18, "bold"))
    tela.update()


# ============================================================
# FUNCAO PRINCIPAL
# ============================================================
def main():
    """Funcao principal: orquestra a construcao do cenario e a animacao."""
    # 1) Cenario de fundo (ceu ja definido no bgcolor da tela)
    desenhar_sol()
    desenhar_nuvens()
    desenhar_arquibancada()
    desenhar_torcida()

    # 2) Campo de futebol oficial
    desenhar_campo()

    # 3) Placar e identificacao do estadio
    desenhar_placar()
    desenhar_estadio()

    # Atualiza a tela apos desenhar todo o cenario estatico
    tela.update()
    time.sleep(1)

    # 4) Entrada dos jogadores, arbitro e bola
    (turtles_azul, turtles_vermelho,
     destinos_azul, destinos_vermelho, bola_t) = entrada_dos_jogadores()

    time.sleep(1)

    # 5) Apito inicial
    mostrar_apito_inicial()

    # 6) Inicio da partida (toque inicial)
    iniciar_partida(bola_t, destinos_azul)

    # mantem a janela aberta ate o usuario clicar
    tela.update()
    aviso_final = turtle.Turtle()
    aviso_final.hideturtle()
    aviso_final.penup()
    aviso_final.goto(0, -480)
    aviso_final.pencolor("yellow")
    aviso_final.write("Clique na janela para encerrar.", align="center", font=("Arial", 12, "normal"))
    tela.update()
    tela.exitonclick()


# Ponto de entrada do programa
if __name__ == "__main__":
    main()