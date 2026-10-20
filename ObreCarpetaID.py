# Versió 4.1 a l'Eina - Amb GUI (gener/2026)

## Gadget per obrir les antigues carpetes de documents d'usuaris de l'Eina
## sense haver de navegar per l'arbre de directoris de la unitat de xarxa Y:\
## sinó tan sols introduint l'antic ID d'usuari.
## FOAP 2020-2025; 

# Importacions per a la funcionalitat (original) d'obrir carpetes ID:
import math
import os
import subprocess
# Importacions per a la GUI (nova funcionalitat):
import tkinter as tk

# Perque funcionin les rutes relatives en qualsevol lloc:
basedir = os.path.dirname(__file__)

# Per evitar que a la barra de tasques es visualitzi la icona Python
# enlloc de la icona que assignem en aquest codi:
try:
    from ctypes import windll
    # (personalitzeu 'myappid' segons: Company.Product.SubProduct.VersionInfo)
    myappid = "lEina.Ocupacio.ObreCarpetaID.v4"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# Variables de la GUI:
lbl_0_Txt = "Obre carpeta de documents dels antics ID a la unitat Y:\\"
lbl_1_TxtIni = 'Introdueix un antic ID i clica "Cerca" (o prem Return)'
lbl_2_Txt = 'gener/2026 - "Always look on the bright side of life" (from Life of Brian)'
entrada_Txt=""

# Tres maneres de capturar entrada a GUI (només si s'ha entrat ID):
def clic_Boto(): # Clicant el botó.
    entrada_Txt=wgt_Entrada.get()
    if entrada_Txt != "ID?" and entrada_Txt != "":
        CercaCarpeta(entrada_Txt)
    else:
        lbl_1.config(text=lbl_1_TxtIni)

def Rtrn_Boto(event): # Prement return amb el focus al botó.
    entrada_Txt=wgt_Entrada.get()
    if entrada_Txt != "ID?" and entrada_Txt != "":
        CercaCarpeta(entrada_Txt)
    else:
        lbl_1.config(text=lbl_1_TxtIni, fg="black", bg="orange")

def Rtrn_Entrada(event): # Prement return amb el focus a l'input.
    entrada_Txt=event.widget.get()
    if entrada_Txt != "ID?" and entrada_Txt != "":
        CercaCarpeta(entrada_Txt)
    else:
        lbl_1.config(text=lbl_1_TxtIni, fg="black", bg="orange")

# ========= Procés principal (modificat de l'original per =======
# ========= treure partit de la nova GUI. =======================

def CercaCarpeta(IDtxt):
    try:
        IDn=int(IDtxt)
    except:
        lbl_1.config(text="--- No has escrit un nombre! ---",
                     fg="red", bg="#DADADA")
        return
    FirstID=0
    LastID=0
    if IDn<2101:
        FoldName='Del 1-2100'
    else:
        FirstID=int(math.floor((IDn-1)/100)*100+1)
        LastID=FirstID+99
        FoldName='Del '+str(FirstID)+'-'+str(LastID)
    Ruta='C:\\Candidats\\' + FoldName + '\\' + str(IDn)
    # ------------------------------------
    # Tot seguit, cal testejar i, si és el cas, obrir aquesta ruta.
    # ------------------------------------
    if os.path.exists(Ruta):
        if os.path.isdir(Ruta):
            comanda='explorer {}'.format(Ruta)
            lbl_1.config(text='Carpeta ID oberta!',
                         fg="blue", bg="white")
        else:
            lbl_1.config(text='Hi ha un fitxer "ID", pero no un directori.',
                         fg="red", bg="#DADADA")
            comanda='explorer /select,{}'.format(Ruta)
    else:
        Ruta='C:\\Candidats\\' + FoldName
        if os.path.exists(Ruta):
            comanda='explorer {}'.format(Ruta)
            lbl_1.config(text="Carpeta superior oberta: no existeix l'ID.",
                         fg="red", bg="#DADADA")
        else:
            Ruta='C:\\Candidats\\'
            if os.path.exists(Ruta):
                comanda='explorer {}'.format(Ruta)
                lbl_1.config(text="No existeix aquest rang d'IDs.",
                         fg="red", bg="#DADADA")
            else:
                lbl_1.config(text="En aquest PC no hi ha C:\\Candidats.",
                         fg="red", bg="#DADADA")
                return
    subprocess.Popen(comanda)

# ======= Fi del procés principal =========================


# ======== Maneig de la GUI sense entrada de dades: =======
# Ocultar/mostrar "ID?" al entry widget:
def focusIn_Entrada(event):
    if event.widget.get()=="ID?":
        wgt_Entrada.delete(0, tk.END)
        wgt_Entrada.insert(0, "")
        lbl_1.config(text=lbl_1_TxtIni, fg="black", bg="orange")

def focusOut_Entrada(event):
    if event.widget.get()=="":
        wgt_Entrada.insert(0, "ID?")
        lbl_1.config(text=lbl_1_TxtIni, fg="black", bg="orange")
# ==========================================================

# Configuració GUI =========================================
root = tk.Tk()

root.title("Obre carpeta d'ID antic")
root.configure(background="orange")
root.geometry("+500+300")
# Posarem una imatge tipus banner per decorar/personalitzar la GUI:
img_banner=tk.PhotoImage(file=os.path.join(basedir, "img", "banner.png"))
lbl_logo=tk.Label(root, image=img_banner)
lbl_logo.grid(row=0, column=0, columnspan=2,
              padx=5, pady=5, ipadx=5, ipady=5)
# Un petit text que explica què fa o perque serveix l'aplicació:
lbl_0=tk.Label(root, text=lbl_0_Txt, font=("Calibri", 12),
               bg="orange", wraplength=170)
lbl_0.grid(row=0, column=2, columnspan=2,
           padx=5, pady=5, ipadx=5, ipady=5)
# Un 'placeholder' per text, que donarà instruccions i explicarà resultats:
lbl_1=tk.Label(root, text=lbl_1_TxtIni, font=("Calibri", 14),
               bg="orange", wraplength=290)
lbl_1.grid(row=1, column=0, columnspan=4,
           padx=5, pady=5, ipadx=5, ipady=5)
# Un camp d'entrada de dades (l'ID de la carpeta a obrir):
wgt_Entrada=tk.Entry(root, font=("Calibri", 12))
wgt_Entrada.insert(0, "ID?")
wgt_Entrada.bind("<Return>", Rtrn_Entrada)
wgt_Entrada.bind("<FocusIn>", focusIn_Entrada)
wgt_Entrada.bind("<FocusOut>", focusOut_Entrada)
wgt_Entrada.grid(row=2, column=1, columnspan=2,
                 padx=5, pady=5, ipadx=5, ipady=5)
# El botó per a executar la consulta (tot i que hi haurà l'alternativa <return>):
Boto=tk.Button(root, text="Cerca", font=("Calibri", 14), command=clic_Boto,
               cursor="hand2")
Boto.bind("<Return>", Rtrn_Boto)
Boto.grid(row=3, column=1, columnspan=2,
          padx=5, pady=10, ipadx=40, ipady=5)
# Un text "espiritual" al peu de la GUI, i de pas al·lusiu a Monty Python:
lbl_2=tk.Label(root, text=lbl_2_Txt, font=("Calibri", 11),
               bg="orange", fg="white")
lbl_2.grid(row=4, column=0, columnspan=4, padx=5, pady=8, ipadx=10, ipady=5)
# Establim la icona que es mostrarà a la barra de títol de la finestra:
root.iconbitmap(os.path.join(basedir, "img", "logo.ico"))

root.mainloop()
# Fi configuració GUI =========================================
