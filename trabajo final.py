#!/usr/bin/env python
"""
Ejenplo básico del uso de Tkinter
Basado en: https://pythonbasics.org/tkinter/
Autor: cmoralesd (http://github.com/cmoralesd)
"""

from tkinter import *
import tkinter
import time

class Window(Frame):
    clock_on = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # se crea menú principal
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)

        # se crea un menú secundario
        menu_config = Menu(main_menu)
        menu_config.add_command(label='Opción 1')
        menu_config.add_command(label='Salir', command=self.exit_window)
        # se agrega al menú principal
        main_menu.add_cascade(label='Opciones', menu=menu_config)

        # creamos un contenedor para otros widgets
        self.pack(fill=BOTH, expand=1)

        # se agrega botón
        self.exitButton = Button(self, text='Cerrar', command=self.exit_window)
        self.exitButton.place(x=230, y=440)

        #botones de inicio
        self.exitButton = Button(self, text='partir')
        self.exitButton.place(x=70, y=370)
        self.exitButton = Button(self, text='partir')
        self.exitButton.place(x=340, y=370)

        #botones de parada
        self.exitButton = Button(self, text='parar')
        self.exitButton.place(x=110, y=370)
        self.exitButton = Button(self, text='parar')
        self.exitButton.place(x=380, y=370)

        #botones de reinicio
        self.exitButton = Button(self, text='reiniciar')
        self.exitButton.place(x=150, y=370)
        self.exitButton = Button(self, text='reiniciar' )
        self.exitButton.place(x=420, y=370)
        

       

        # se agregan etiquetas
        self.label1 = Label(master, text='motor 1')
        self.label1.place(x=100, y=10)
        self.label2 = Label(master, text="motor 2")
        self.label2.place(x=350, y=10)

        # se agrega motor horizontal
        j = tkinter.Scale( self, from_=0, to=30, orient=tkinter.HORIZONTAL, length=200, resolution=0.01,)
        j.pack()
        j.place(x= 280, y= 50)


        s = tkinter.Scale( self, from_=0, to=30, orient=tkinter.HORIZONTAL, length=200, resolution=0.01,)
        s.pack()
        s.place(x= 20, y= 50)
       

        # se agrega motor Vertical
        jv = tkinter.Scale( self, from_=0, to=30, orient=tkinter.VERTICAL, length=200, resolution=0.01,)
        jv.pack()
        jv.place(x= 350, y= 130)


        sv = tkinter.Scale( self, from_=0, to=30, orient=tkinter.VERTICAL, length=200, resolution=0.01,)
        sv.pack()
        sv.place(x= 80, y= 130)
    
    
    # método salir
    def exit_window(self):
        exit()

   
    




    # método clock
    def clock(self):
        if self.clock_on == False:
            self.clock_on = True
            self.clockButton.configure(text='Desactivar reloj')
            self.update_clock()
        else:
            self.clock_on = False
            self.clockButton.configure(text='Activar reloj')



# main code
# inicializa una ventana
root = Tk()
app = Window(root)

# agrega título
root.wm_title("ventana principal")
root.geometry('500x500-0-0')

# muestra la ventana
root.mainloop()

serialport = serial.Serial('COM5', 9600)
time.sleep(0.1)


