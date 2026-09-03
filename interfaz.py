import tkinter as tt
import matplotlib.pyplot as plt





'''
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [2, 4, 6, 8, 10]

#plt.plot (x, y)
plt.title("Gráfica de ejemplo")
#plt.bar(x, y)
plt.scatter(x, y,z)
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

'''
'''
def saludar (): 
    nombre = entry.get().strip()
    if not nombre:
        nombre = "Alejandro"
    lbl.config(text=f"Hola {nombre}")

root = tt.Tk()
root.title("Saludar")
root.geometry("360x220")
lbl = tt.Label(root, text="Ingrese su nombre", background= "blue" , foreground="black", font=("Arial", 12))
lbl.pack (pady = 20)
entry = tt.Entry(root, background= "aqua")
entry.pack(pady=10)
bot = tt.Button(root, text="Mostrar", background="lightgray", command=saludar)
bot.pack(pady=10)



root.mainloop()
'''