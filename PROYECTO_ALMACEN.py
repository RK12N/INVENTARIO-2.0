from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import tkinter as tk
import pymysql
import os
import mysql.connector

pnt = Tk()
############################CONFIGURACION DE VENTANA#####################################
pnt.title("INVENTARIO")
pnt.iconbitmap('images.ico')
pnt.wm_iconbitmap('images.ico')
##############CONFIGURACION DE VENTANA####################################
wtotal = pnt.winfo_screenwidth()
htotal = pnt.winfo_screenheight()
wventana = 1200
hventana = 550
#######################################CODIGO GENERAL#######################################
connectio = pymysql.connect(
    host='localhost',
    user='root',
    password='basededatos',
    db='INVENTARIO'
 
)
ID_SQL = StringVar()
SKU_SQL = StringVar()
MARCA_SQL = StringVar()
MODELO_SQL = StringVar()
PULGADAS_SQL = StringVar()
RESOLUCION_SQL= StringVar()
SO_SQL = StringVar()
PRECIO_SQL = StringVar()
CANTIDAD_RECIBIDA_SQL = StringVar()
CANTIDAD_FISICA_SQL = StringVar()
CANTIDAD_VENDIDA_SQL = StringVar()
CANTIDAD_SQL = StringVar()

def validate_entry(text):
    return text.isdecimal()

class VENTANA_INVENTARIO():

    def ENVIO_DE_DATOS():
        if SKU_SQL.get()==""or MARCA_SQL.get()==""or MODELO_SQL.get()==""or PULGADAS_SQL.get()==""or RESOLUCION_SQL.get()==""or SO_SQL.get()=="" or PRECIO_SQL.get()=="" or CANTIDAD_RECIBIDA_SQL.get()==""or CANTIDAD_FISICA_SQL.get()=="":
            messagebox.showinfo(message="Existen espacio vacios",title="Estaus de datos")
        else:
            cursor = connectio.cursor()
            sql ="insert into INVENTARIO_TV (SKU,MARCA,MODELO,PULGADAS,RESOLUCION,SO,PRECIO,CANTIDAD_RECIBIDA,CANTIDAD_FISICA) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("SNTV00" + SKU_SQL.get(),MARCA_SQL.get(),MODELO_SQL.get(),PULGADAS_SQL.get(),RESOLUCION_SQL.get(),SO_SQL.get(),PRECIO_SQL.get(),CANTIDAD_RECIBIDA_SQL.get(),CANTIDAD_FISICA_SQL.get())
            cursor.execute(sql)
            connectio.commit()
            messagebox.showinfo(message="ELEMENTOS ENVIADO",title="Estaus de datos")
            VENTANA_INVENTARIO.LIMPIAR(set)
    def LIMPIAR(str):
        SKU_ENTRY.delete(0,END)
        MARCA_ENTRY.delete(0,END)
        MODELO_ENTRY.delete(0,END)
        PULGADAS_ENTRY.delete(0,END)
        RESOLUCION_ENTRY.delete(0,END)
        SO_ENTRY.delete(0,END)
        PRECIO_ENTRY.delete(0,END)
        CANTIDAD_RECIBIDA_ENTRY.delete(0,END)
        CANTIDAD_FISICA_ENTRY.delete(0,END)

    def VENTANA_INVENTARIO_ESTRUCTURA():
        MENU.DESTRUIR_BOTONES_PRINCIPALES()
        global SKU_ENTRY
        global MARCA_ENTRY
        global MODELO_ENTRY
        global PULGADAS_ENTRY
        global RESOLUCION_ENTRY
        global SO_ENTRY
        global PRECIO_ENTRY
        global CANTIDAD_RECIBIDA_ENTRY
        global CANTIDAD_FISICA_ENTRY
        global btn_enviar_datos
        global etiquetas
        etiquetas = []
        etiquetas.append(Label(pnt, text="SKU"))
        etiquetas.append(Label(pnt, text="MARCA"))
        etiquetas.append(Label(pnt, text="MODELO"))
        etiquetas.append(Label(pnt, text="PULGADAS"))
        etiquetas.append(Label(pnt, text="RESOLUCION"))
        etiquetas.append(Label(pnt, text="SO"))
        etiquetas.append(Label(pnt, text="PRECIO"))
        etiquetas.append(Label(pnt, text="CANTIDAD RECIBIDA"))
        etiquetas.append(Label(pnt, text="CANTIDAD FISICA"))
        for i, etiqueta in enumerate(etiquetas):
            etiqueta.place(x=50, y=50 + 50*i)
        locatiox = 165
        SKU_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=SKU_SQL)
        SKU_ENTRY.place(x=locatiox,y=50)

        MARCA_ENTRY = Entry(pnt,textvariable=MARCA_SQL)
        MARCA_ENTRY.place(x=locatiox,y=100)

        MODELO_ENTRY = Entry(pnt,textvariable=MODELO_SQL)
        MODELO_ENTRY.place(x=locatiox,y=150)

        PULGADAS_ENTRY = Entry(pnt,textvariable=PULGADAS_SQL)
        PULGADAS_ENTRY.place(x=locatiox,y=200)

        RESOLUCION_ENTRY = Entry(pnt,textvariable=RESOLUCION_SQL)
        RESOLUCION_ENTRY.place(x=locatiox,y=250)

        SO_ENTRY = Entry(pnt,textvariable=SO_SQL)
        SO_ENTRY.place(x=locatiox,y=300)
        
        PRECIO_ENTRY = Entry(pnt,textvariable=PRECIO_SQL)
        PRECIO_ENTRY.place(x=locatiox,y=350)

        CANTIDAD_RECIBIDA_ENTRY = Entry(pnt,textvariable=CANTIDAD_RECIBIDA_SQL)
        CANTIDAD_RECIBIDA_ENTRY.place(x=locatiox,y=400)

        CANTIDAD_FISICA_ENTRY = Entry(pnt,textvariable=CANTIDAD_FISICA_SQL)
        CANTIDAD_FISICA_ENTRY.place(x=locatiox,y=450)

        btn_enviar_datos = Button(pnt,text="Enviar",command=VENTANA_INVENTARIO.ENVIO_DE_DATOS)
        btn_enviar_datos.place(x=locatiox,y=500,width=125)

        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=MENU.DESTRUIR_CONTENIDO_INGRESO_DE_DATOS)
        menubar.add_cascade(label="Menu", menu=filemenu)
    def eliminar_etiquetas():
        for etiqueta in etiquetas:
            etiqueta.destroy()            
class ACTUALIZACION_DE_DATOS():
    
    def ACTUALIZA_DATOS():
        if ID_ENTRY_A.get()=="" or SKU_ENTRY_A.get()==""or MARCA_ENTRY_A.get()=="" or MODELO_ENTRY_A.get()=="" or PULGADAS_ENTRY_A.get()=="" or RESOLUCION_ENTRY_A.get()=="" or SO_ENTRY_A.get()==""or  PRECIO_ENTRY_A.get()=="" or CANTIDAD_RECIBIDA_ENTRY_A.get()=="" or CANTIDAD_FISICA_ENTRY_A.get()==""or cantidad_anda.get()=="":
            messagebox.showinfo(message="Existen espacios vacios")
        else:
            ID_ACTUALIZAR = ID_ENTRY_A.get()
            SKU_ACTUALIZAR= SKU_ENTRY_A.get()
            MARCA_ACTUALIZAR= MARCA_ENTRY_A.get()
            MODELO_ACTUALIZAR = MODELO_ENTRY_A.get()
            PULGADAS_ACTUALIZAR = PULGADAS_ENTRY_A.get()
            RESOLUCION_ACTUALIZAR = RESOLUCION_ENTRY_A.get()
            SO_ACTUALIZAR = SO_ENTRY_A.get()
            PRECIO_ACTUALIZAR = PRECIO_ENTRY_A.get()
            CANTIDAD_R_ACTUALIZAR = CANTIDAD_RECIBIDA_ENTRY_A.get()
            CANTIDAD_F_ACTUALIZAR = CANTIDAD_FISICA_ENTRY_A.get()
            CANTIDAD_D_ACTUALIZAR = cantidad_anda.get()

            cursor = connectio.cursor()
            consulta ="UPDATE INVENTARIO_TV SET SKU = %s,MARCA= %s,MODELO= %s,PULGADAS= %s,RESOLUCION= %s,SO= %s,PRECIO= %s,CANTIDAD_RECIBIDA= %s,CANTIDAD_FISICA= %s,CANTIDAD_DANADAS= %s WHERE ID=%s"
            valores = (SKU_ACTUALIZAR,
                       MARCA_ACTUALIZAR,
                       MODELO_ACTUALIZAR,
                       PULGADAS_ACTUALIZAR,
                       RESOLUCION_ACTUALIZAR,
                       SO_ACTUALIZAR,
                       PRECIO_ACTUALIZAR,
                       CANTIDAD_R_ACTUALIZAR,
                       CANTIDAD_F_ACTUALIZAR,
                       CANTIDAD_D_ACTUALIZAR,
                       ID_ACTUALIZAR)
            cursor.execute(consulta,valores)
            connectio.commit()
            messagebox.showinfo(message="Elementos actualizados",title="Estado de ingreso de datos")
            ACTUALIZACION_DE_DATOS.LIMPIAR(str)
            messagebox.showinfo(message="Advertencia",title="Es nesesario recargar la pagina")
            #MENU.DESTRUIR_CONTENIDO_DE_ACTUALIZACION()
            arbol.destroy()
            ACTUALIZACION_DE_DATOS.ARBOL_DE_DATOS()
    def LIMPIAR(str):
        SKU_ENTRY_A.delete(0,END)
        MARCA_ENTRY_A.delete(0,END)
        MODELO_ENTRY_A.delete(0,END)
        PULGADAS_ENTRY_A.delete(0,END)
        RESOLUCION_ENTRY_A.delete(0,END)
        SO_ENTRY_A.delete(0,END)
        PRECIO_ENTRY_A.delete(0,END)
        CANTIDAD_RECIBIDA_ENTRY_A.delete(0,END)
        CANTIDAD_FISICA_ENTRY_A.delete(0,END)
        cantidad_anda.delete(0,END)

    def VENTANA_DE_ACTUALIZACION_DE_TV():
        ACTUALIZACION_DE_DATOS.ARBOL_DE_DATOS()
        global SKU_ENTRY_A
        global MARCA_ENTRY_A
        global MODELO_ENTRY_A
        global PULGADAS_ENTRY_A
        global RESOLUCION_ENTRY_A
        global SO_ENTRY_A
        global PRECIO_ENTRY_A
        global CANTIDAD_RECIBIDA_ENTRY_A
        global CANTIDAD_FISICA_ENTRY_A
        global etiquetas2
        global ID_ENTRY_A
        global cantidad_anda

        etiquetas2 = []
        etiquetas2.append(Label(pnt, text="SKU"))
        etiquetas2.append(Label(pnt, text="MARCA"))
        etiquetas2.append(Label(pnt, text="MODELO"))
        etiquetas2.append(Label(pnt, text="PULGADAS"))
        etiquetas2.append(Label(pnt, text="RESOLUCION"))
        etiquetas2.append(Label(pnt, text="SO"))
        etiquetas2.append(Label(pnt, text="PRECIO"))
        etiquetas2.append(Label(pnt, text="CANTIDAD RECIBIDA"))
        etiquetas2.append(Label(pnt, text="CANTIDAD FISICA"))
        etiquetas2.append(Label(pnt, text="CANTIDAD DAÑADAS"))
        for i, etiqueta in enumerate(etiquetas2):
            etiqueta.place(x=10,y=250 + 30*i)

        locationxa = 140
        ID_ENTRY_A = Entry(pnt,textvariable=ID_SQL)
        ID_ENTRY_A.place(x=0,y=0)

        SKU_ENTRY_A = Entry(pnt,textvariable=SKU_SQL,font=('Bahnschrift',10))
        SKU_ENTRY_A.place(x=locationxa,y=250)

        MARCA_ENTRY_A = Entry(pnt,textvariable=MARCA_SQL,font=('Bahnschrift',10))
        MARCA_ENTRY_A.place(x=locationxa,y=280)

        MODELO_ENTRY_A = Entry(pnt,textvariable=MODELO_SQL,font=('Bahnschrift',10))
        MODELO_ENTRY_A.place(x=locationxa,y=310)

        PULGADAS_ENTRY_A = Entry(pnt,textvariable=PULGADAS_SQL,font=('Bahnschrift',10))
        PULGADAS_ENTRY_A.place(x=locationxa,y=340)

        RESOLUCION_ENTRY_A = Entry(pnt,textvariable=RESOLUCION_SQL,font=('Bahnschrift',10))
        RESOLUCION_ENTRY_A.place(x=locationxa,y=370)

        SO_ENTRY_A = Entry(pnt,textvariable=SO_SQL,font=('Bahnschrift',10))
        SO_ENTRY_A.place(x=locationxa,y=400)

        PRECIO_ENTRY_A = Entry(pnt,textvariable=PRECIO_SQL,font=('Bahnschrift',10))
        PRECIO_ENTRY_A.place(x=locationxa,y=430)

        CANTIDAD_RECIBIDA_ENTRY_A = Entry(pnt,textvariable=CANTIDAD_RECIBIDA_SQL,font=('Bahnschrift',10))
        CANTIDAD_RECIBIDA_ENTRY_A.place(x=locationxa,y=460)

        CANTIDAD_FISICA_ENTRY_A = Entry(pnt,textvariable=CANTIDAD_FISICA_SQL,font=('Bahnschrift',10))
        CANTIDAD_FISICA_ENTRY_A.place(x=locationxa,y=490)

        cantidad_anda = Entry(pnt,textvariable=CANTIDAD_SQL,font=('Bahnschrift',10))
        cantidad_anda.place(x=locationxa,y=520)

        global botonenviarven
        botonenviarven = Button(pnt,text="Actualizar",command=ACTUALIZACION_DE_DATOS.ACTUALIZA_DATOS)
        botonenviarven.place(x=300,y=520)

        global botoneliminar
        botoneliminar = Button(pnt,text="Eliminar",command=ACTUALIZACION_DE_DATOS.eliminar_datos)
        botoneliminar.place(x=700,y=520)

    def eliminar_datos():
        ID_SQL = ID_ENTRY_A.get()
        alerta = messagebox.askyesno("Advertencia","Estas seguro de eliminar la tabla la columna con el id" + ID_SQL)
        if alerta:
            cursor = connectio.cursor()
            consulta = "DELETE FROM INVENTARIO_TV WHERE ID =%s"
            valor = (ID_SQL)
            cursor.execute(consulta,valor)
            connectio.commit()
            messagebox.showinfo(message="Elemento eliminado",title="Estado de ingreso de datos")
            ACTUALIZACION_DE_DATOS.LIMPIAR(str)
            messagebox.showinfo(message="Es nesesario aplicar los cambios regresando al menu")
            MENU.DESTRUIR_CONTENIDO_DE_ACTUALIZACION()

    def ARBOL_DE_DATOS():
        MENU.DESTRUIR_BOTONES_PRINCIPALES()
        global arbol
        arbol = ttk.Treeview(pnt)
        arbol['columns'] = ('columna1', 'columna2', 'columna3','columna4','columna5','columna6','columna7','columna8','columna9','columna10')

        arbol.heading("#0", text='ID')
        arbol.column("#0", anchor=CENTER, width=20)

        arbol.heading('columna1', text='SKU')
        arbol.column('columna1', anchor=CENTER, width=80)

        arbol.heading('columna2', text='MARCA')
        arbol.column('columna2', anchor=CENTER, width=80)

        arbol.heading('columna3', text='MODELO')
        arbol.column('columna3', anchor=CENTER, width=80)

        arbol.heading('columna4', text='PULGADAS')
        arbol.column('columna4', anchor=CENTER, width=80)

        arbol.heading('columna5', text='RESOLUCION')
        arbol.column('columna5', anchor=CENTER, width=80)

        arbol.heading('columna6', text='SO')
        arbol.column('columna6', anchor=CENTER, width=80)

        arbol.heading('columna7', text='PRECIO')
        arbol.column('columna7', anchor=CENTER, width=80)

        arbol.heading('columna8', text='CANTIDAD_RECIBIDA')
        arbol.column('columna8', anchor=CENTER, width=80)
        
        arbol.heading('columna9', text='CANTIDAD_FISICA')
        arbol.column('columna9', anchor=CENTER, width=80)
        
        arbol.heading('columna10', text='CANTIDAD_DAÑADA')
        arbol.column('columna10', anchor=CENTER, width=80)
        arbol.place(x=0,y=0,width=1200)

        def mostra_datos(event):
            item = arbol.selection()[0]
            values = arbol.item(item, 'values')

            ID_ENTRY_A.delete(0, END)
            ID_ENTRY_A.insert(0, arbol.item(item, 'text'))
            
            SKU_ENTRY_A.delete(0, END)
            SKU_ENTRY_A.insert(0, values[0])

            MARCA_ENTRY_A.delete(0, END)
            MARCA_ENTRY_A.insert(0, values[1])

            MODELO_ENTRY_A.delete(0, END)
            MODELO_ENTRY_A.insert(0, values[2])

            PULGADAS_ENTRY_A.delete(0, END)
            PULGADAS_ENTRY_A.insert(0, values[3])

            RESOLUCION_ENTRY_A.delete(0, END)
            RESOLUCION_ENTRY_A.insert(0, values[4])

            SO_ENTRY_A.delete(0, END)
            SO_ENTRY_A.insert(0, values[5])

            PRECIO_ENTRY_A.delete(0, END)
            PRECIO_ENTRY_A.insert(0, values[6])

            CANTIDAD_RECIBIDA_ENTRY_A.delete(0, END)
            CANTIDAD_RECIBIDA_ENTRY_A.insert(0, values[7])

            CANTIDAD_FISICA_ENTRY_A.delete(0, END)
            CANTIDAD_FISICA_ENTRY_A.insert(0, values[8])

            cantidad_anda.delete(0, END)
            cantidad_anda.insert(0, values[9])

        arbol.bind('<<TreeviewSelect>>', mostra_datos)
        cursor = connectio.cursor()
        cursor.execute("select * from INVENTARIO_TV")
        registros = cursor.fetchall()
        for registro in registros:
            arbol.insert('', END, text=registro[0], values=(registro[1], registro[2], registro[3],registro[4],registro[5],registro[6],registro[7],registro[8],registro[9],registro[11]))
        global menubar
        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=MENU.DESTRUIR_CONTENIDO_DE_ACTUALIZACION)
        menubar.add_cascade(label="Menu", menu=filemenu)
        
    def eliminar_etiquetas():
        for etiqueta in etiquetas2:
            etiqueta.destroy()

class BUSQUEDA_DE_TV():

    def buscar_informacion():
        valor_busqueda = entry_busqueda.get()
        cursor = connectio.cursor()
        if valor_busqueda=="":
            messagebox.askokcancel("Espacio de busqueda vacio","Es nesesario Ingresar un paramentro para inicial la busqueda")
        else:
          query = "SELECT * FROM INVENTARIO_TV WHERE MARCA LIKE %s ORDER BY PRECIO"
          cursor.execute(query, ('%' + valor_busqueda + '%',))
          resultados = cursor.fetchall()
          for i in arbolito.get_children():
            arbolito.delete(i)
        for resultado in resultados:
            arbolito.insert("", END, text=resultado[0], values=(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10]))
            cursor.close()
        cursor.close()

    def VENTANA_DE_BUSQUEDA():
        MENU.DESTRUIR_BOTONES_PRINCIPALES()
        global arbolito
        global entry_busqueda
        global label_busqueda
        global boton_buscar

        label_busqueda = Label(pnt,text="Buscar televisiones")
        label_busqueda.pack()

        entry_busqueda =Entry(pnt)
        entry_busqueda.pack()
        
        boton_buscar = Button(pnt, text="Buscar", command=BUSQUEDA_DE_TV.buscar_informacion)
        boton_buscar.pack()

        columna = ("ID","SKU","MARCA","MODELO","PULGADAS","RESOLUCION","SO","PRECIO","CANTIDAD_RECIBIDA","CANTIDAD_FISICA","CANTIDAD_VENDIDA")
        arbolito = Treeview(pnt, columns=columna, show="headings")
        for col in columna:
            arbolito.heading(col,text=col)
            arbolito.column("ID",width=10)
            arbolito.column("SKU",width=80)
            arbolito.column("MARCA",width=60)
            arbolito.column("MODELO",width=60)
            arbolito.column("PULGADAS",width=60)
            arbolito.column("RESOLUCION",width=80)
            arbolito.column("SO",width=60)
            arbolito.column("PRECIO",width=80)
            arbolito.column("CANTIDAD_RECIBIDA",width=120)
            arbolito.column("CANTIDAD_FISICA",width=115)
            arbolito.column("CANTIDAD_VENDIDA",width=130)
        #arbolito.place(x=20,y=100, width=1200)
        arbolito.pack()
        global menubar
        menubar = Menu(pnt)
        pnt.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Inicio",command=MENU.DESTRURIR_CONTENIDO_DE_BUSQUEDA)
        menubar.add_cascade(label="Menu", menu=filemenu)
class VENTA():
    def VENTANA_DE_VENTA():
        MENU.DESTRUIR_BOTONES_PRINCIPALES()
        global CLIENTE_LABE
        global ENTRY_CLIENTE
        global ENTRY_SKU
        global SKU_LABE
        global BTN_AGRERAR
        global BNT_PROCESAR
        global ARBOLITOS

        CLIENTE_LABEL = Label(pnt,text="CLIENTE")
        CLIENTE_LABEL.place(x=10,y=10)

        ENTRY_CLIENTE = Entry(pnt)
        ENTRY_CLIENTE.place(x=15,y=30,width=200)

        SKU_LABE = Label(pnt,text="SKU")
        SKU_LABE.place(x=10,y=50)
        
        ENTRY_SKU = Entry(pnt)
        ENTRY_SKU.place(x=15,y=70,width=400)

        BTN_AGRERAR = Button(pnt,text="AGREGAR")
        BTN_AGRERAR.place(x=425,y=65)




class MENU():
    def DESTRURIR_CONTENIDO_DE_BUSQUEDA():
        menubar.destroy()
        arbolito.destroy()
        entry_busqueda.destroy()
        label_busqueda.destroy()
        boton_buscar.destroy()
        MENU.BOTONES_PRINCIPLAES(set)
    def DESTRUIR_CONTENIDO_DE_ACTUALIZACION():
        menubar.destroy()
        ACTUALIZACION_DE_DATOS.LIMPIAR(str)
        SKU_ENTRY_A.destroy()
        MARCA_ENTRY_A.destroy()
        MODELO_ENTRY_A.destroy()
        PULGADAS_ENTRY_A.destroy()
        RESOLUCION_ENTRY_A.destroy()
        SO_ENTRY_A.destroy()
        PRECIO_ENTRY_A.destroy()
        CANTIDAD_RECIBIDA_ENTRY_A.destroy()
        CANTIDAD_FISICA_ENTRY_A.destroy()
        cantidad_anda.destroy()
        ID_ENTRY_A.destroy()
        arbol.destroy()
        botonenviarven.destroy()
        botoneliminar.destroy()
        ACTUALIZACION_DE_DATOS.eliminar_etiquetas()
        MENU.BOTONES_PRINCIPLAES(set)
    def DESTRUIR_CONTENIDO_INGRESO_DE_DATOS():
        VENTANA_INVENTARIO.LIMPIAR(str)
        SKU_ENTRY.destroy()
        MARCA_ENTRY.destroy()
        MODELO_ENTRY.destroy()
        PULGADAS_ENTRY.destroy()
        RESOLUCION_ENTRY.destroy()
        SO_ENTRY.destroy()
        PRECIO_ENTRY.destroy()
        CANTIDAD_RECIBIDA_ENTRY.destroy()
        CANTIDAD_FISICA_ENTRY.destroy()
        VENTANA_INVENTARIO.eliminar_etiquetas()
        btn_enviar_datos.destroy()
        MENU.BOTONES_PRINCIPLAES(set)     
    def DESTRUIR_BOTONES_PRINCIPALES():
        btn_ingreso_datos.destroy()
        btn_actualizar.destroy()
        btn_buscar.destroy()
        btn_ventas.destroy()
    def BOTONES_PRINCIPLAES(SET):
        global btn_ingreso_datos
        global btn_actualizar
        global btn_buscar
        global btn_ventas
        
        btn_ingreso_datos = Button(pnt,text="AGREGAR INVENTARIO",command=VENTANA_INVENTARIO.VENTANA_INVENTARIO_ESTRUCTURA)
        btn_ingreso_datos.place(x=250,y=100,width=200,height=100)
        
        btn_actualizar = Button(pnt,text="ACTUALIZAR INVENTARIO TV",command=ACTUALIZACION_DE_DATOS.VENTANA_DE_ACTUALIZACION_DE_TV)
        btn_actualizar.place(x=540,y=100,width=200,height=100)

        btn_buscar = Button(pnt,text="BUSQUEDA DE INVENTARIO TV",command=BUSQUEDA_DE_TV.VENTANA_DE_BUSQUEDA)
        btn_buscar.place(x=800,y=100,width=208,height=100)

        
        btn_ventas= Button(pnt,text="BUSQUEDA DE INVENTARIO TV",command=VENTA.VENTANA_DE_VENTA)
        btn_ventas.place(x=540,y=250,width=208,height=100)
        
################################################################################################################3
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

ventana_principal = MENU()
ventana_principal.BOTONES_PRINCIPLAES()
pnt.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
############################ PNT MAINLOOP###########################################
pnt.mainloop()