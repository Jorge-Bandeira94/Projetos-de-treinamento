# Game Ping-Pong

from tkinter import *
import random #importou uma biblioteca de randomização
import time  #importou uma biblioteca de tempo

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n")) #string de input de numero inteiro
length = 500/level #determinante do tamanho da barra de acordo com o level, elemento de divisão de acordo com u númeor escolhido


root = Tk()         # Inicialização do programa
root.title("Ping Pong")  # Título da janela
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)    # Dimensões da janela
canvas.pack()   # A janela é do tamanho necessário para o jogo aparecer por completo

root.update()   # O jogo é atualizado a cada frame para continuar jogando a menos que dê game over (lost seja true)

# Variável
count = 0
lost = False

class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas                                     # Inicia comando para dar imagem aos objetos
        self.Barra = Barra                                       # Inicia a barra
        self.id = canvas.create_oval(0, 0, 40, 40, fill=color)   # Na variável canvas (que é o quadro) vai ser criado uma forma orval (create_oval para circulo, rectangle para quadrado, line para linha)
        self.canvas.move(self.id, 250, 250)                      # Comando que faz id(a boal criada acima) mover-se nos eixos x e y começando na posição 250

        starts_x = [-1, -2, -3, 1, 2, 3]                         # Posições nos eixos X que a bola irá começar a mover-se
        random.shuffle(starts_x)                                 # Este random faz ela ir pra um local aleatório do eixo

        self.x = starts_x[0]                                     # Para começar no centro da janela
        self.y = -3                                              # Para começar indo pra cima, o quanto ele sobe por fram, quanto mais negativo mais vertical

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)               # Método para iniciar a movimentação da bola

        pos = self.canvas.coords(self.id)                       # Objeto que determina a posição da bola a cada frame
        print(pos)
        if pos[1] <= 0:                                         # Os ifs são para quando a bola bater numa parede (nas coordenadas especificadas) ela volte
            self.y = 3                                          # O 3 positivo indica que, quando a bola chegar na coordenada 0 ou negativa da janela, ela sera rebatida para baixo

        if pos[3] >= self.canvas_height:                        # O 3 positivo indica que, quando a bola chegar na posição máxima da janela em altura, ela será rebatida para cima
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)      # Bater na barra, a bola vai ser rebatida

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2] :
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3] :
                self.y = -3
                global count
                count += 1
                score()

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)                   # Se a altura da bola n coincidir com as coordenadas da barra e paredes, a def draw ocorre 1 vezes por segundo
        else:
            game_over()
            global lost
            lost = True


class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)                               # Posição inicial da barra dentro da janela

        self.x = 0                                                        # Econtra-se em 0 no eixo x
        self.y = 0

        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()                    # Adicionei o objeto de altura para barra poder detectar as paredes


        self.canvas.bind_all("<KeyPress-Left>", self.move_left)           # COmando para mover a barra
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
        self.canvas.bind_all("<KeyPress-Up>", self.move_up)               # Adicionei a opção da barra subir e descer (ver abaixo)
        self.canvas.bind_all("<KeyPress-Down>", self.move_down)


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)                             # Se no eixo Y for mudado o valor de 0, a brra subirá ou irá descer. O valor era pra ser zero, mas adicionei a opção da barra subir ou descer, dai precisei colocar self.y

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0                                                   # Enquanto a posição for menor ou igual a zero no eixo X, ele continua se mecher pra posição escolhida
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0

        if self.pos[1] <= 0:                                            # Adicioneu as colisões da barra contra as paredes
            self.y = 0

        if self.pos[3] >= self.canvas_height:
            self.y = 0


        global lost
        
        if lost == False:
            self.canvas.after(5, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

    def move_up(self, event):                               # Opção da barra subir
        if self.pos[1] >= 0:                                # Se na coordenada 1 (altura) for maior ou igual a 0, a barra pode subir
            self.y = -3

    def move_down(self, event):                             # Opção da barra descer
        if self.pos[3] <= self.canvas_height:                # Se na coordenada 3 (altura) for menor ou igual a 0, a barra pode descer
            self.y = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()


def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")


Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

root.mainloop()