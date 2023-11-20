from tkinter import *

ventana = Tk()
ventana.geometry('360x350')
ventana.config(bg = "white")
ventana.iconbitmap(bitmap = 'icono.ico')
ventana.title("Calculadora")
ventana.resizable(0,0)

#Hover
i = 0
class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground
  
#Operaciones
i=0
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)
	
def operacion():
	global i
	ecuacion = Resultado.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'ERROR'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

def borrar_uno():
	global i 
 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1

def borrar():
	Resultado.delete(0, END)	
	i=0
    


    
#color
frame = Frame(ventana, bg= 'black', relief = 'raised')
frame.grid(column = 0,row = 0,padx = 6, pady = 3)

Resultado = Entry(frame,bg = '#9EF8E8',width = 27,relief = 'groove',font = 'montserrat 16', justif = 'right')
Resultado.grid(columnspan = 6, row = 0, pady = 3, padx = 1, ipadx = 1, ipady = 1)

#Botones

boton1 = HoverButton(frame,text="1",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(1))
boton2 = HoverButton(frame,text="2",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(2))
boton3 = HoverButton(frame,text="3",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(3))
boton4 = HoverButton(frame,text="4",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(4))
boton5 = HoverButton(frame,text="5",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(5))
boton6 = HoverButton(frame,text="6",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(6))
boton7 = HoverButton(frame,text="7",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(7))
boton8 = HoverButton(frame,text="8",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(8))
boton9 = HoverButton(frame,text="9",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(9))
boton0 = HoverButton(frame,text="0",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#999AB8', anchor= "center",command = lambda:  obtener(0))

boton_borrar = HoverButton(frame,text="AC",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#2FEC71', anchor= "center",command = lambda: borrar())
boton_parentesis1 = HoverButton(frame,text="(",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda:  obtener("("))
boton_parentesis2 = HoverButton(frame,text=")",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda:  obtener(")"))
boton_punto = HoverButton(frame,text=".",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda: obtener("."))

boton_borrar_uno = HoverButton(frame,text="←",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = '#2FEC71', anchor= "center",command = lambda: borrar_uno())
boton_exp = HoverButton(frame,text="exp",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda:   obtener("**"))
boton_potencia = HoverButton(frame,text="^2",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda:  obtener("**2"))
boton_raiz = HoverButton(frame,text="√",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'blue', anchor= "center",command = lambda:  obtener("**(1/2)"))

boton_div = HoverButton(frame,text="/",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'red', anchor= "center",command = lambda: obtener('/'))
boton_mult = HoverButton(frame,text="x",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'red', anchor= "center",command = lambda: obtener('*'))
boton_suma = HoverButton(frame,text="+",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'red', anchor= "center",command = lambda: obtener('+'))
boton_resta = HoverButton(frame,text="-",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'red', anchor= "center",command = lambda:  obtener("-"))
boton_mod = HoverButton(frame,text="%",borderwidth = 2 , height = 2,width = 5 ,font = ('Comic sens MC',12,'bold'),relief = "raised",activebackground = "aqua", bg = 'red', anchor= "center",command = lambda:  obtener("%"))
boton_igual = HoverButton(frame, text= "=", height=2, width=5,font= ('Comic sens MC',12,'bold'), borderwidth=2,  relief = "raised", activebackground="#16FD03", bg='#2FEC71', anchor="center",command=lambda: operacion())

#Agregar botones en pantalla
boton_borrar_uno.grid(row=1,column = 0,padx = 5, pady = 5, sticky = W+E)
boton_borrar.grid(row=1 , column = 1 ,padx = 5, pady = 5,sticky=W+E)
boton_parentesis1.grid(row=1 , column = 2,padx = 5, pady = 5,sticky=W+E)
boton_parentesis2.grid(row=1 , column = 3,padx = 5, pady = 5,sticky=W+E)
boton_div.grid(row=1 , column = 4,padx = 5, pady = 5,sticky=W+E)

boton7.grid(row=2 , column = 0,padx = 5, pady = 5,sticky=W+E)
boton8.grid(row=2 , column = 1,padx = 5, pady = 5,sticky=W+E)
boton9.grid(row=2 , column = 2,padx = 5, pady = 5,sticky=W+E)
boton_mult.grid(row=2 , column = 3,padx = 5, pady = 5,sticky=W+E)
boton_exp.grid(row=2 , column = 4,padx = 5, pady = 5,sticky=W+E)

boton4.grid(row= 3, column = 0,padx = 5, pady = 5,sticky=W+E)
boton5.grid(row= 3, column = 1,padx = 5, pady = 5,sticky=W+E)
boton6.grid(row= 3, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_suma.grid(row= 3, column = 3,padx = 5, pady = 5,sticky=W+E)
boton_potencia.grid(row= 3, column = 4,padx = 5, pady = 5,sticky=W+E)

boton1.grid(row= 4, column = 0,padx = 5, pady = 5,sticky=W+E)
boton2.grid(row= 4, column = 1,padx = 5, pady = 5,sticky=W+E)
boton3.grid(row= 4, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_resta.grid(row= 4, column = 3,padx = 5, pady = 5,sticky=W+E)
boton_raiz.grid(row= 4, column = 4,padx = 5, pady = 5,sticky=W+E)

boton0.grid(row= 5, column = 0,columnspan = 2, padx = 5, pady = 5,sticky=W+E)
boton_punto.grid(row= 5, column = 2,padx = 5, pady = 5,sticky=W+E)
boton_igual.grid(row= 5, column = 4,padx = 5, pady = 5,sticky=W+E)
boton_mod.grid(row= 5, column = 3,padx = 5, pady = 5,sticky=W+E)



ventana.mainloop()