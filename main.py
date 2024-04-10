from vpython import *

def menu():
    m = float(input("digite o valor da massa do bloco (kg): "))
    k = float(input("digite o valor da constante elástica: "))
    return m,k

def main():
    m, k = menu()

    #objetos
    parede = box(pos=vector(-20,0,0), size = vector(1,10,10), color = color.yellow)
    bloco = box(pos=vector(5,-3,0), size = vector(4,4,4), color = color.red)
    solo = box(pos=vector(0,-5,0), size = vector(50,0.5,10), color = color.green)
    mola = helix(pos=vector(-20.5,-3,0), radius = 1.5, thickness = 0.5 , coils = 5, color = color.blue)

    #condicoes iniciais
    bloco.vel = vector(0,0,0)
    t=0
    dt=0.0005

    #graficos
    g1 = graph(xtitle="tempo", ytitle='posicao')
    g2 = graph(xtitle="tempo", ytitle='velocidade')

    grafico1 = gcurve(graph = g1, color=color.red)
    grafico2 = gcurve(graph = g2, color=color.blue)

    #vinculo
    mola.axis = bloco.pos - mola.pos

    #equacoes
    while True:
        rate(1/dt)
        f = vector(-bloco.pos.x * k, 0, 0)
        acel = f/m            
        bloco.pos = bloco.pos + (bloco.vel * dt)
        bloco.vel = bloco.vel + (acel*dt)
        
        mola.axis = bloco.pos - mola.pos
        t = t + dt
        
        grafico1.plot(t, bloco.pos.x)
        grafico2.plot(t, bloco.vel.x)

        grafico1.data.clear()
        grafico1.data.clear()

if __name__ == "__main__":
    main()
