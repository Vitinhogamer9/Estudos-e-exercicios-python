import turtle

tela = turtle.Screen()
tela.bgcolor("black")
tela.tracer(0)  # desliga animação automática — resolve o lento

t = turtle.Turtle()
t.speed(0)  # velocidade máxima

# Tartaruga 2 — só texto
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()

cores = ["red", "blue", "green", "orange", "purple"]

# Função fora do loop
def AtualizarPlacar(i, cor):
    texto.clear()
    texto.color(cor)
    texto.write(f"{i}", font=("Arial", 14, "bold"))

for i in range(100):
    cor = cores[i % 5]

    t.color(cor)
    t.forward(i * 2)
    t.right(91)

    texto.goto(t.xcor(), t.ycor())  # texto vai exatamente na posição do t
    AtualizarPlacar(i, cor)

    tela.update()  # atualiza a tela uma vez por volta

turtle.done()