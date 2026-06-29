import turtle
import math

# ==============================
# Configuração da tela
# ==============================

tela = turtle.Screen()
tela.title("Robô desenhista do campo de futebol")
tela.bgcolor("green")
tela.setup(width=900, height=650)

# ==============================
# Configuração do robô
# ==============================

robo = turtle.Turtle()
robo.shape("turtle")
robo.color("white")
robo.pensize(3)
robo.speed(4)

# ==============================
# Escala do desenho
# ==============================

# Nesta atividade:
# 1 metro no campo real será representado por 6 pixels na tela.
PIXELS_POR_METRO = 6

def metros_para_pixels(metros):
    return metros * PIXELS_POR_METRO

# ==============================
# Comandos do robô
# ==============================
# Atenção:
# Todas as funções abaixo recebem valores em METROS.
# A conversão para pixels acontece internamente.
# ==============================

def ir_para(x_metros, y_metros):
    x_pixels = metros_para_pixels(x_metros)
    y_pixels = metros_para_pixels(y_metros)

    robo.penup()
    robo.goto(x_pixels, y_pixels)

def caneta_baixar():
    robo.pendown()

def caneta_levantar():
    robo.penup()

def frente(distancia_metros):
    distancia_pixels = metros_para_pixels(distancia_metros)
    robo.forward(distancia_pixels)

def tras(distancia_metros):
    distancia_pixels = metros_para_pixels(distancia_metros)
    robo.backward(distancia_pixels)

def direita(graus):
    robo.right(graus)

def esquerda(graus):
    robo.left(graus)

def olhar_para(graus):
    robo.setheading(graus)

def circulo(raio_metros):
    raio_pixels = metros_para_pixels(raio_metros)
    robo.circle(raio_pixels)

def ponto(tamanho_metros=0.8):
    tamanho_pixels = metros_para_pixels(tamanho_metros)
    robo.dot(tamanho_pixels)

def arco_centralizado(x_metros, y_metros, raio_metros, angulo_inicial, angulo_final):
    """
    Desenha um arco de círculo.

    x_metros, y_metros: centro do círculo, em metros
    raio_metros: raio do círculo, em metros
    angulo_inicial: onde o arco começa
    angulo_final: onde o arco termina

    Ângulos:
    0 graus   = direita
    90 graus  = cima
    180 graus = esquerda
    270 graus = baixo
    """

    caneta_levantar()

    primeiro_ponto = True

    for angulo in range(angulo_inicial, angulo_final + 1):
        radianos = math.radians(angulo)

        ponto_x_metros = x_metros + raio_metros * math.cos(radianos)
        ponto_y_metros = y_metros + raio_metros * math.sin(radianos)

        ponto_x_pixels = metros_para_pixels(ponto_x_metros)
        ponto_y_pixels = metros_para_pixels(ponto_y_metros)

        if primeiro_ponto:
            robo.penup()
            robo.goto(ponto_x_pixels, ponto_y_pixels)
            robo.pendown()
            primeiro_ponto = False
        else:
            robo.goto(ponto_x_pixels, ponto_y_pixels)

    caneta_levantar()

# ==============================
# Funções que os alunos devem completar
# ==============================

def desenhar_contorno():
    ir_para(-52.5, 34)
    olhar_para(0)
    caneta_baixar()

    frente(105)
    direita(90)
    frente(68)
    direita(90)
    frente(105)
    direita(90)
    frente(68)

    caneta_levantar()


def desenhar_linha_do_meio():
    ir_para(0, 34)
    olhar_para(270)
    caneta_baixar()

    frente(68)

    caneta_levantar()


def desenhar_circulo_central():
    ir_para(0, -9.15)
    olhar_para(0)
    caneta_baixar()

    circulo(9.15)

    caneta_levantar()


def desenhar_grande_area_esquerda():
    ir_para(-52.5, 20.16)
    olhar_para(0)
    caneta_baixar()

    frente(16.5)
    direita(90)
    frente(40.32)
    direita(90)
    frente(16.5)

    caneta_levantar()


def desenhar_grande_area_direita():
    ir_para(52.5, 20.16)
    olhar_para(180)
    caneta_baixar()

    frente(16.5)
    esquerda(90)
    frente(40.32)
    esquerda(90)
    frente(16.5)

    caneta_levantar()


def desenhar_pequena_area_esquerda():
    ir_para(-52.5, 9.16)
    olhar_para(0)
    caneta_baixar()

    frente(5.5)
    direita(90)
    frente(18.32)
    direita(90)
    frente(5.5)

    caneta_levantar()


def desenhar_pequena_area_direita():
    ir_para(52.5, 9.16)
    olhar_para(180)
    caneta_baixar()

    frente(5.5)
    esquerda(90)
    frente(18.32)
    esquerda(90)
    frente(5.5)

    caneta_levantar()


def desenhar_marcas_penalti():
    ir_para(-41.5, 0)
    ponto()

    ir_para(41.5, 0)
    ponto()


def desenhar_meia_lua_esquerda():
    arco_centralizado(-41.5, 0, 9.15, -53, 53)


def desenhar_meia_lua_direita():
    arco_centralizado(41.5, 0, 9.15, 127, 233)


def desenhar_gol_esquerdo():
    ir_para(-52.5, 3.66)
    caneta_baixar()

    ir_para(-57.5, 3.66)
    ir_para(-57.5, -3.66)
    ir_para(-52.5, -3.66)
    ir_para(-52.5, 3.66)

    caneta_levantar()


def desenhar_gol_direito():
    ir_para(52.5, 3.66)
    caneta_baixar()

    ir_para(57.5, 3.66)
    ir_para(57.5, -3.66)
    ir_para(52.5, -3.66)
    ir_para(52.5, 3.66)

    caneta_levantar()

# ==============================
# Código principal
# ==============================
# As chamadas já estão prontas.
# O robô vai executar as funções na ordem abaixo.
# O trabalho de vocês é completar cada função acima.
# ==============================

desenhar_contorno()
desenhar_linha_do_meio()
desenhar_circulo_central()

desenhar_grande_area_esquerda()
desenhar_grande_area_direita()

desenhar_pequena_area_esquerda()
desenhar_pequena_area_direita()

desenhar_marcas_penalti()

desenhar_meia_lua_esquerda()
desenhar_meia_lua_direita()

# Desafio extra:
desenhar_gol_esquerdo()
desenhar_gol_direito()

turtle.done()