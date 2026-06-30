import turtle
import math
import random

# ==============================
# Configuração da tela
# ==============================

tela = turtle.Screen()
tela.title("Robô desenhista do campo de futebol - Estádio Completo")
tela.bgcolor("#228B22") # Verde floresta realista para o gramado
tela.setup(width=1000, height=750)
# Desativa a atualização em tempo real para desenhar instantaneamente os elementos complexos
tela.tracer(0)

# ==============================
# Configuração do robô (Turtle)
# ==============================

robo = turtle.Turtle()
robo.shape("turtle")
robo.color("white")
robo.pensize(2)
robo.speed(0) # Velocidade máxima

# ==============================
# Escala do desenho
# ==============================

# 1 metro no campo real será representado por 6 pixels na tela.
PIXELS_POR_METRO = 6

def metros_para_pixels(metros):
    return metros * PIXELS_POR_METRO

# ==============================
# Comandos do robô (Funções Auxiliares)
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
# Funções de Desenho das Marcações do Campo
# ==============================

def desenhar_contorno():
    robo.color("white")
    robo.pensize(3)
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
    robo.color("white")
    robo.pensize(3)
    ir_para(0, 34)
    olhar_para(270)
    caneta_baixar()
    frente(68)
    caneta_levantar()

def desenhar_circulo_central():
    robo.color("white")
    robo.pensize(3)
    ir_para(0, -9.15)
    olhar_para(0)
    caneta_baixar()
    circulo(9.15)
    caneta_levantar()
    ir_para(0, 0)
    ponto(0.6)

def desenhar_grande_area_esquerda():
    robo.color("white")
    robo.pensize(3)
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
    robo.color("white")
    robo.pensize(3)
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
    robo.color("white")
    robo.pensize(3)
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
    robo.color("white")
    robo.pensize(3)
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
    robo.color("white")
    ir_para(-41.5, 0)
    ponto(0.6)
    ir_para(41.5, 0)
    ponto(0.6)

def desenhar_meia_lua_esquerda():
    robo.color("white")
    robo.pensize(3)
    arco_centralizado(-41.5, 0, 9.15, -53, 53)

def desenhar_meia_lua_direita():
    robo.color("white")
    robo.pensize(3)
    arco_centralizado(41.5, 0, 9.15, 127, 233)

def desenhar_gol_esquerdo():
    robo.color("white")
    robo.pensize(4)
    ir_para(-52.5, 3.66)
    caneta_baixar()
    ir_para(-55.5, 3.66)
    ir_para(-55.5, -3.66)
    ir_para(-52.5, -3.66)
    caneta_levantar()

def desenhar_gol_direito():
    robo.color("white")
    robo.pensize(4)
    ir_para(52.5, 3.66)
    caneta_baixar()
    ir_para(55.5, 3.66)
    ir_para(55.5, -3.66)
    ir_para(52.5, -3.66)
    caneta_levantar()

# ==============================
# Funções Reutilizáveis Solicitadas
# ==============================

def desenhar_jogador(x, y, cor_camisa, cor_pele, num_camisa="", e_goleiro=False):
    # Corpo (Tronco)
    ir_para(x, y)
    olhar_para(90)
    robo.color(cor_camisa)
    robo.pensize(5 if e_goleiro else 4)
    caneta_baixar()
    frente(2.5)
    caneta_levantar()
    
    # Cabeça
    ir_para(x, y + 2.5)
    robo.color(cor_pele)
    ponto(1.2)
    
    # Braços
    ir_para(x, y + 1.8)
    olhar_para(180)
    caneta_baixar()
    frente(1.2)
    tras(1.2)
    olhar_para(0)
    frente(1.2)
    caneta_levantar()
    
    # Pernas
    ir_para(x, y)
    olhar_para(240)
    caneta_baixar()
    frente(1.5)
    caneta_levantar()
    ir_para(x, y)
    olhar_para(300)
    caneta_baixar()
    frente(1.5)
    caneta_levantar()
    
    # Número identificador
    if num_camisa:
        ir_para(x - 0.4, y + 0.6)
        robo.color("white" if cor_camisa != "white" else "black")
        robo.write(num_camisa, font=("Arial", 6, "bold"))

def desenhar_bola(x, y):
    ir_para(x, y)
    robo.color("white")
    ponto(1.2)
    robo.color("black")
    ponto(0.5)

def desenhar_banco(x, y, cor):
    ir_para(x - 6, y + 1.5)
    robo.color(cor)
    olhar_para(0)
    caneta_baixar()
    frente(12)
    direita(90)
    frente(3)
    direita(90)
    frente(12)
    direita(90)
    frente(3)
    caneta_levantar()
    ir_para(x - 4, y - 0.5)
    robo.color("gray")
    ponto(1.0)
    ir_para(x, y - 0.5)
    ponto(1.0)
    ir_para(x + 4, y - 0.5)
    ponto(1.0)

def desenhar_bandeirinha(x, y):
    ir_para(x, y)
    robo.color("yellow")
    olhar_para(90)
    caneta_baixar()
    robo.pensize(2)
    frente(2)
    robo.color("red")
    olhar_para(0)
    direita(30)
    frente(1.2)
    direita(120)
    frente(1.2)
    caneta_levantar()

def desenhar_arvore(x, y):
    ir_para(x, y)
    robo.color("#8B4513")
    robo.pensize(4)
    olhar_para(90)
    caneta_baixar()
    frente(3)
    caneta_levantar()
    ir_para(x, y + 3)
    robo.color("#2E8B57")
    ponto(3.5)
    ir_para(x - 0.8, y + 4)
    ponto(2.5)
    ir_para(x + 0.8, y + 4)
    ponto(2.5)

def desenhar_arquibancada(x_inicio, y_inicio, largura_m, altura_m, cor_principal):
    ir_para(x_inicio + largura_m / 2, y_inicio - altura_m / 2)
    robo.color(cor_principal)
    robo.pensize(metros_para_pixels(altura_m))
    caneta_baixar()
    olhar_para(0)
    frente(largura_m)
    caneta_levantar()
    
    robo.color("#A9A9A9")
    robo.pensize(2)
    for i in range(1, 4):
        ir_para(x_inicio, y_inicio - (altura_m / 4) * i)
        caneta_baixar()
        frente(largura_m)
        caneta_levantar()

def desenhar_placar(x, y, gols_mandante, gols_visitante):
    ir_para(x - 15, y + 5)
    robo.color("black")
    robo.pensize(metros_para_pixels(8))
    caneta_baixar()
    olhar_para(0)
    frente(30)
    caneta_levantar()
    
    ir_para(x - 12, y + 1)
    robo.color("cyan")
    robo.write("MANDANTE", font=("Courier", 10, "bold"))
    ir_para(x + 3, y + 1)
    robo.color("red")
    robo.write("VISITANTE", font=("Courier", 10, "bold"))
    
    ir_para(x - 6, y - 5)
    robo.color("yellow")
    robo.write(str(gols_mandante), font=("Courier", 18, "bold"))
    ir_para(x + 6, y - 5)
    robo.color("yellow")
    robo.write(str(gols_visitante), font=("Courier", 18, "bold"))

def desenhar_torcida(x_centro, y_centro, qtd):
    cores_torcida = ["#FF4500", "#1E90FF", "#FFD700", "#FFFFFF", "#000000", "#FF69B4", "#32CD32"]
    for _ in range(qtd):
        rx = x_centro + random.uniform(-40, 40)
        ry = y_centro + random.uniform(-4, 4)
        ir_para(rx, ry)
        robo.color(random.choice(cores_torcida))
        ponto(random.uniform(0.6, 1.0))

def desenhar_arbitro(x, y):
    ir_para(x, y)
    olhar_para(90)
    robo.color("yellow")
    robo.pensize(4)
    caneta_baixar()
    frente(2.2)
    caneta_levantar()
    ir_para(x, y + 2.2)
    robo.color("#FFD39B")
    ponto(1.0)
    ir_para(x, y)
    robo.color("black")
    olhar_para(250)
    caneta_baixar()
    frente(1.2)
    caneta_levantar()
    ir_para(x, y)
    caneta_baixar()
    olhar_para(290)
    frente(1.2)
    caneta_levantar()

# ==============================
# Código Principal
# ==============================

def main():
    # Desenhar Ambiente Externo Primeiro (Camadas Traseiras)
    desenhar_arquibancada(-45, 52, 90, 10, "#4682B4")
    desenhar_torcida(0, 47, 120)
    
    desenhar_arquibancada(-45, -42, 90, 10, "#4682B4")
    desenhar_torcida(0, -47, 120)
    
    posicoes_arvores = [
        (-70, 55), (-60, 55), (60, 55), (70, 55),
        (-70, -55), (-60, -55), (60, -55), (70, -55),
        (-75, 20), (-75, -20), (75, 20), (75, -20)
    ]
    for px, py in posicoes_arvores:
        desenhar_arvore(px, py)
        
    desenhar_banco(-20, 39, "#333333")
    desenhar_banco(20, 39, "#333333")
    
    desenhar_placar(0, 58, 2, 1)

    # Desenhar Linhas Oficiais
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
    desenhar_gol_esquerdo()
    desenhar_gol_direito()
    
    desenhar_bandeirinha(-52.5, 34)
    desenhar_bandeirinha(52.5, 34)
    desenhar_bandeirinha(-52.5, -34)
    desenhar_bandeirinha(52.5, -34)

    # Atores do jogo
    desenhar_arbitro(-5, 5)
    desenhar_bola(0, 0)

    # Equipes táticas
    cor_mandante_camisa = "red"
    cor_mandante_pele = "#FFD39B"
    cor_visitante_camisa = "blue"
    cor_visitante_pele = "#FFE4C4"
    
    pos_mandante = [
        (-50, 0, "1", True),
        (-38, 22, "2", False),
        (-40, 8, "3", False),
        (-40, -8, "4", False),
        (-38, -22, "6", False),
        (-22, 12, "5", False),
        (-20, -12, "8", False),
        (-18, 0, "10", False),
        (-5, 25, "7", False),
        (-2, 0, "9", False),
        (-5, -25, "11", False)
    ]
    
    for x, y, num, gk in pos_mandante:
        desenhar_jogador(x, y, cor_mandante_camisa, cor_mandante_pele, num, gk)

    pos_visitante = [
        (50, 0, "1", True),
        (38, -22, "2", False),
        (40, -8, "3", False),
        (40, 8, "4", False),
        (38, 22, "6", False),
        (22, -12, "5", False),
        (20, 12, "8", False),
        (18, 0, "10", False),
        (5, -25, "7", False),
        (2, 0, "9", False),
        (5, 25, "11", False)
    ]
    
    for x, y, num, gk in pos_visitante:
        desenhar_jogador(x, y, cor_visitante_camisa, cor_visitante_pele, num, gk)

    tela.update()

if __name__ == "__main__":
    main()
    turtle.done()
