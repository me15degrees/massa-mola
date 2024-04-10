import tkinter as tk
from vpython import *

def simular(m, k):
    # objetos
    parede = box(pos=vector(-20,0,0), size=vector(1,10,10), color=color.yellow)
    bloco = box(pos=vector(5,-3,0), size=vector(4,4,4), color=color.red)
    solo = box(pos=vector(0,-5,0), size=vector(50,0.5,10), color=color.green)
    mola = helix(pos=vector(-20.5,-3,0), radius=1.5, thickness=0.5, coils=5, color=color.blue)

    # condições iniciais
    bloco.vel = vector(0,0,0)
    t = 0
    dt = 0.0005 # controla a atualização

    # gráficos
    g1 = graph(xtitle="tempo", ytitle='posicao')
    g2 = graph(xtitle="tempo", ytitle='velocidade')

    grafico1 = gcurve(graph=g1, color=color.red)
    grafico2 = gcurve(graph=g2, color=color.blue)

    # vínculo
    mola.axis = bloco.pos - mola.pos

    # equações para simular o movimento 
    while True:
        rate(1/dt)
        f = vector(-bloco.pos.x * k, 0, 0)
        acel = f / m
        bloco.pos = bloco.pos + (bloco.vel * dt)
        bloco.vel = bloco.vel + (acel * dt)
        
        mola.axis = bloco.pos - mola.pos
        t = t + dt
        
        grafico1.plot(t, bloco.pos.x)
        grafico2.plot(t, bloco.vel.x)

        grafico1.data.clear()
        grafico1.data.clear()

def iniciar_simulacao():
    m = float(entry_m.get())
    k = float(entry_k.get())
    simular(m, k)

# cria a aba do tkinter para inserir os dados
root = tk.Tk()
root.title("Simulação de Mola")

original_width = root.winfo_reqwidth()
original_height = root.winfo_reqheight()
new_width = int(original_width * 4)
new_height = int(original_height * 1)

root.geometry(f"{new_width}x{new_height}")

frame = tk.Frame(root)
frame.pack(expand=True, fill='both', padx=130, pady=20)

label_m = tk.Label(frame, text="Massa (kg):", font=("Helvetica", 15), justify='center')
label_m.grid(row=0, column=0, padx=5, pady=5)
entry_m = tk.Entry(frame, font=("Helvetica", 15))
entry_m.grid(row=0, column=1, padx=5, pady=5)

label_k = tk.Label(frame, text="Constante Elástica:", font=("Helvetica", 15), justify='center')
label_k.grid(row=1, column=0, padx=5, pady=5)
entry_k = tk.Entry(frame, font=("Helvetica", 15))
entry_k.grid(row=1, column=1, padx=5, pady=5)

button_iniciar = tk.Button(frame, text="Iniciar Simulação", font=("Helvetica", 15), command=iniciar_simulacao)
button_iniciar.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()