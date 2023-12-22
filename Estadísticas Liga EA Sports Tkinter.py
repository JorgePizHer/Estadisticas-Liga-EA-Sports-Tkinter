import tkinter as tk
from tkinter import messagebox, ttk

raiz = tk.Tk()
raiz.title("Estadísticas Liga EA Sports")
raiz.geometry("500x500")


def selection():
   selected = seleccion_boton.get()
   print("Has seleccionado",selected)

def seleccion_equipo():

      
         if seleccion_boton.get() == 1:

                indices = listado.curselection()

                if listado.get(indices)=="Real Madrid":
                    messagebox.showinfo(title=("Máximo goleador",(listado.get(indices))), message=("El máximo goleador del Real Madrid es Jude Bellingham con 13 goles"))
                elif listado.get(indices)=="Barcelona":
                    messagebox.showinfo(title=("Máximo goleador",(listado.get(indices))), message=("El máximo goleador del Barcelona es Robert Lewandowski con 8 goles"))
                elif listado.get(indices)=="Getafe":
                    messagebox.showinfo(title=("Máximo goleador",(listado.get(indices))), message=("El máximo goleador del Getafe es Borja Mayoral con 12 goles"))
                elif listado.get(indices)=="Girona":
                    messagebox.showinfo(title=("Máximo goleador",(listado.get(indices))), message=("El máximo goleador del Girona es Artem Dovbyk con 9 goles"))
                 
         elif seleccion_boton.get()== 2:
                   
               indices = listado.curselection()
               if listado.get(indices)=="Real Madrid":
                    messagebox.showinfo(title=("Máximo asistente",(listado.get(indices))), message=("El máximo asistente del Real Madrid es Toni Kroos con 6 asistencias"))
               elif listado.get(indices)=="Barcelona":
                    messagebox.showinfo(title=("Máximo asistente",(listado.get(indices))), message=("El máximo asistente del Barcelona es Raphinha con 5 asistencias"))
               elif listado.get(indices)=="Getafe":
                    messagebox.showinfo(title=("Máximo asistente",(listado.get(indices))), message=("El máximo asistente del Getafe es Diego Rico con 5 asistencias"))
               elif listado.get(indices)=="Girona":
                    messagebox.showinfo(title=("Máximo asistente",(listado.get(indices))), message=("El máximo asistente del Girona es Yan Couto con 5 asistencias"))
      
label1 = tk.Label(raiz)
label1.pack()

tk.Label(raiz,text="Selecciona una estadística").pack(padx=10,pady=10)
        
seleccion_boton = tk.IntVar()

r1= tk.Radiobutton(raiz, text="Goles",  variable = seleccion_boton, value = 1, command=selection)
r1.pack()
r1= tk.Radiobutton(raiz, text="Asistencias",  variable = seleccion_boton, value = 2,command=selection)
r1.pack()

label2 = tk.Label(raiz)
label2.pack()

tk.Label(raiz,text="Selecciona un equipo").pack(padx=10,pady=10)

equipos = ['Real Madrid','Barcelona','Getafe', 'Girona']   

listado = tk.Listbox(raiz)
for equipo in equipos:
    listado.insert(tk.END,equipo)
listado.pack(padx=20,pady=20)

boton_obtener_equipo = ttk.Button(text="Consulta la estadística seleccionada", command=seleccion_equipo)

boton_obtener_equipo.pack()


raiz.mainloop()
