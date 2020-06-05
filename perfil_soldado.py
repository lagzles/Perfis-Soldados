# -*- coding: cp1252 -*-
import calc_perfil_soldado as calc
import operator
from tkinter import *

print("Inserir dados de entrada")
##nsd = int(raw_input("nsd [kN] ="))
##vsd = raw_input("vsd [kN] =")
##msdx = raw_input("msdx [kN.m] =")
##msdy = raw_input("msdy [kN.m] =")
##l = raw_input("l [cm]= ")
##l = 300 # cm
kx = 1
ky = 1
kz = 1
fy = 29.0 # kN/cm²
fu = 41.5 #kN/cm²
E = 20000 # kN/cm²
G = 7700 # kN/cm²

class MyGui:
    def __init__(self, master):
        self.master = master
        master.title('Perfil Soldado')

        self.label_nsd = Label(master, text='Nsd [kg]', height=1).grid(row=0, column=0)
        self.label_msd = Label(master, text='MSd [kg.m]', height=1).grid(row=0, column=1)
        self.label_vsd = Label(master, text='VSd [kg]', height=1).grid(row=0, column=2)

        self.text_nsd = Text(master, height=1, width=10)
        self.text_nsd.insert(INSERT, "100.00")
        self.text_nsd.grid(row=1, column=0)

        self.text_msd = Text(master, height=1, width=12)
        self.text_msd.insert(INSERT, "100.00")
        self.text_msd.grid(row=1, column=1)

        self.text_vsd = Text(master, height=1, width=15)
        self.text_vsd.insert(INSERT, "100.00")
        self.text_vsd.grid(row=1, column=2)

        self.label_hifen1 = Label(master, text=' ', height=1).grid(row=2, column=0)
        self.label_hifen2 = Label(master, text=' ', height=1).grid(row=2, column=1)
        self.label_hifen3 = Label(master, text=' ', height=1).grid(row=2, column=2)

        #######################################################################
        self.label_d = Label(master, text='d [mm]', height=1).grid(row=3, column=0)
        self.text_d = Text(master, height=1, width=15)
        self.text_d.insert(INSERT, "300")
        self.text_d.grid(row=4, column=0)

        self.label_tw = Label(master, text='tw [mm]', height=1).grid(row=5, column=0)
        self.text_tw = Text(master, height=1, width=15)
        self.text_tw.insert(INSERT, "3.75")
        self.text_tw.grid(row=6, column=0)

        self.label_bfs = Label(master, text='bfs [mm]', height=1).grid(row=3, column=1)
        self.text_bfs = Text(master, height=1, width=15)
        self.text_bfs.insert(INSERT, "150")
        self.text_bfs.grid(row=4, column=1)

        self.label_tfs = Label(master, text='tfs [mm]', height=1).grid(row=5, column=1)
        self.text_tfs = Text(master, height=1, width=15)
        self.text_tfs.insert(INSERT, "4.75")
        self.text_tfs.grid(row=6, column=1)

        self.label_bfi = Label(master, text='bfi [mm]', height=1).grid(row=3, column=2)
        self.text_bfi = Text(master, height=1, width=15)
        self.text_bfi.insert(INSERT, "150")
        self.text_bfi.grid(row=4, column=2)

        self.label_tfi = Label(master, text='tfi [mm]', height=1).grid(row=5, column=2)
        self.text_tfi = Text(master, height=1, width=15)
        self.text_tfi.insert(INSERT, "4.75")
        self.text_tfi.grid(row=6, column=2)

        self.label_l = Label(master, text='l [cm]', height=1).grid(row=7, column=1)
        self.text_l = Text(master, height=1, width=15)
        self.text_l.tag_configure("center", justify='center')
        self.text_l.insert(INSERT, "300")
        self.text_l.grid(row=8, column=1)


        #######################################################################
        self.label_hifen4 = Label(master, text=' ', height=2).grid(row=9, column=0)
        self.label_hifen5 = Label(master, text=' ', height=2).grid(row=9, column=1)
        self.label_hifen6 = Label(master, text=' ', height=2).grid(row=9, column=2)
        #########################################################################

        self.design_button = Button(master, text='Dimensionar', command=self.dimensionar_um)
        self.design_button.grid(row=10, column=0)

        self.opt_button = Button(master, text='Otimizar', command=self.otimizar)
        self.opt_button.grid(row=10, column=2)
        ########################################################################

        self.label11 = Label(master, text='', height=2)
        self.label12 = Label(master, text='', height=2)
        self.label13 = Label(master, text='', height=2)
        self.label14 = Label(master, text='', height=2)
        self.label15 = Label(master, text='', height=2)
        self.label16 = Label(master, text='', height=2)
        self.label17 = Label(master, text='', height=2)

        self.label21 = Label(master, text='', height=2)
        self.label22 = Label(master, text='', height=2)
        self.label23 = Label(master, text='', height=2)
        self.label24 = Label(master, text='', height=2)
        self.label25 = Label(master, text='', height=2)
        self.label26 = Label(master, text='', height=2)
        self.label27 = Label(master, text='', height=2)

        self.label31 = Label(master, text='', height=2)
        self.label32 = Label(master, text='', height=2)
        self.label33 = Label(master, text='', height=2)
        self.label34 = Label(master, text='', height=2)
        self.label35 = Label(master, text='', height=2)
        self.label36 = Label(master, text='', height=2)
        self.label37 = Label(master, text='', height=2)

        self.label11.grid(row=11, column=0)
        self.label12.grid(row=12, column=0)
        self.label13.grid(row=13, column=0)
        self.label14.grid(row=14, column=0)
        self.label15.grid(row=15, column=0)
        self.label16.grid(row=16, column=0)
        self.label17.grid(row=17, column=0)
        
        self.label21.grid(row=11, column=1)
        self.label22.grid(row=12, column=1)
        self.label23.grid(row=13, column=1)
        self.label24.grid(row=14, column=1)
        self.label25.grid(row=15, column=1)
        self.label26.grid(row=16, column=1)
        self.label27.grid(row=17, column=1)
        
        self.label31.grid(row=11, column=2)
        self.label32.grid(row=12, column=2)
        self.label33.grid(row=13, column=2)
        self.label34.grid(row=14, column=2)
        self.label35.grid(row=15, column=2)
        self.label36.grid(row=16, column=2)
        self.label37.grid(row=17, column=2)


    def dimensionar_um(self):
        print("TODO")
        nsd = float(self.text_nsd.get("1.0", END))
        msd = float(self.text_msd.get("1.0", END))
        vsd = float(self.text_vsd.get("1.0", END))
        l = float(self.text_l.get("1.0", END))
                  
        if nsd == 0:
            nsd = 1

        d = float(self.text_d.get("1.0", END))
        tw = float(self.text_tw.get("1.0", END))
        bfs = float(self.text_bfs.get("1.0", END))
        tfs = float(self.text_tfs.get("1.0", END))
        bfi = float(self.text_bfi.get("1.0", END))
        tfi = float(self.text_tfi.get("1.0", END))
        
        lista = calc.calc_simples(d,tw,bfs,tfs,nsd,msd,vsd, fy, E, G, l, kx, ky, kz)

        # valores dos perfis
        self.label11.config(text=lista[0])
        self.label21.config(text='')
        self.label31.config(text='')
        #valores dos pesos lineares para cada perfil
        self.label12.config(text=lista[1])
        self.label22.config(text='')
        self.label32.config(text='')
        # eficiencia de cada seção
        self.label13.config(text=lista[2])
        self.label23.config(text='')
        self.label33.config(text='')
        # eficiencia axial
        self.label14.config(text=lista[3])
        self.label24.config(text='')
        self.label34.config(text='')
        # eficiencia FLT
        self.label15.config(text=lista[4])
        self.label25.config(text='')
        self.label35.config(text='')
        # eficiencia FLA
        self.label16.config(text=lista[5])
        self.label26.config(text='')
        self.label36.config(text='')
        # eficiencia FLM
        self.label17.config(text=lista[6])
        self.label27.config(text='')
        self.label37.config(text='')
        


    def otimizar(self):
        nsd = float(self.text_nsd.get("1.0", END))
        msd = float(self.text_msd.get("1.0", END))
        vsd = float(self.text_vsd.get("1.0", END))
        l = float(self.text_l.get("1.0", END)) 
        if nsd == 0:
            nsd = 1

        master = self.master
        lista = calc.calc_otimizado(nsd, msd, vsd, fy, E, G, l, kx, ky, kz)
        primeiro = lista[0]
        segundo = lista[1]
        terceiro = lista[2]

 

        # valores dos perfis
        self.label11.config(text=primeiro[0])
        self.label21.config(text=segundo[0])
        self.label31.config(text=terceiro[0])
        #valores dos pesos lineares para cada perfil
        self.label12.config(text=primeiro[1])
        self.label22.config(text=segundo[1])
        self.label32.config(text=terceiro[1])
        # eficiencia de cada seção
        self.label13.config(text=primeiro[2][0])
        self.label23.config(text=segundo[2][0])
        self.label33.config(text=terceiro[2][0])
        # eficiencia axial
        self.label14.config(text=primeiro[2][1])
        self.label24.config(text=primeiro[2][1])
        self.label34.config(text=primeiro[2][1])
        # eficiencia FLT
        self.label15.config(text=primeiro[2][2])
        self.label25.config(text=primeiro[2][2])
        self.label35.config(text=primeiro[2][2])
        # eficiencia FLA
        self.label16.config(text=primeiro[2][3])
        self.label26.config(text=primeiro[2][3])
        self.label36.config(text=primeiro[2][3])
        # eficiencia FLM
        self.label17.config(text=primeiro[2][4])
        self.label27.config(text=primeiro[2][4])
        self.label37.config(text=primeiro[2][4])

root = Tk()
my_gui = MyGui(root)
root.mainloop()


