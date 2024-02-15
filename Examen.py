import tkinter as tk
from tkinter import *
import ply.lex as lex

tokens = ['DELIMITADOR','ERROR','RESERVADO','NUMERO','OPERADOR','IDENTIFICADOR','DATATIPO','CADENA']

def t_DELIMITADOR(t):
    r'[\(\)\{\}\[\];]'
    return t

def t_OPERADOR(t):
    r'(\+|\-|=|\*|\/|\+\+)+'
    return t

def t_IDENTIFICADOR(t):
    r'\b(suma|progrma|a|b|c|programa)\b'
    t.type = 'IDENTIFICADOR'
    t.value = t.value.strip()
    return t

def t_CADENA(t):
    r'\b"([^"]+)"\b'
    t.type = 'CADENA'
    t.value = t.value.strip()
    return t

def t_DATATIPO(t):
    r'\b(int|double|decimal|float|str|char)\b'
    t.type = 'DATATIPO'
    t.value = t.value.strip()
    return t  

def t_RESERVADO(t):
    r'\b(for|do|while|else|if|main|read|printf|end|static|void|public)\b'
    t.type = 'RESERVADO'
    t.value = t.value.strip()
    return t

def t_NUMERO(t):
    r'(\d+)(\.?\d*)'
    t.value = float(t.value)
    return t

def t_error(t):
    error_texto.insert(tk.END, f"Carácter no válido: '{t.value[0]}'\n")
    t.lexer.skip(1)

lexer = lex.lex()

class Lexer:
    def __init__(self, data):
        self.lexer = lex.lex()
        self.lexer.input(data)
    
    def reset(self, line):
        line = line.strip()
        self.lexer.input(line)

def analizar():
    borrar_resultados()
    lexer = Lexer(entrada_texto.get("1.0", "end-1c"))
    line_number = 1
    for linea in entrada_texto.get("1.0", "end-1c").splitlines():
        lexer.reset(linea)
        while True:
            token = lexer.lexer.token()
            if not token:
                break      # No more input
            resultado_token.insert(tk.END, f"{token.type}\n")
            resultado_lexema.insert(tk.END, f"{token.value}\n")
            resultado_pos.insert(tk.END, f"{token.lexpos}\n")
            resultado_lineno.insert(tk.END, f"{line_number}\n")
            if token.type == 'ERROR':
                error_texto.insert(tk.END, f"Carácter no válido: '{token.value[0]}' en la línea {line_number}\n")
        line_number += 1

def borrar_resultados():
    resultado_token.delete("1.0", tk.END)
    resultado_lexema.delete("1.0", tk.END)
    resultado_pos.delete("1.0", tk.END)
    resultado_lineno.delete("1.0", tk.END)
    error_texto.delete("1.0", tk.END)

def borrar():
    entrada_texto.delete("1.0", tk.END)
    borrar_resultados()

ventana = tk.Tk()
ventana.geometry("845x780")
ventana.resizable(width=False, height=False)
ventana.title ("Analizador Lexico")
ventana.config(bg="#17A589")

##Entrada de texto

entrada_texto = tk.Text(ventana, font=("Arial",12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=40, y=55, width = 350, height=380)
entrada_texto.configure(insertbackground="black")

##Etiquetas para marcar columnas de resultados

reja_token = tk.Label(ventana, text= "Token", font=("Arial",12), bg="white", fg="black")
reja_token.place (x=200, y=460, width = 86, height=15)

reja_lex = tk.Label(ventana, text= "Lexema", font=("Arial",12), bg="white", fg="black")
reja_lex.place (x=300, y=460, width = 86, height=15)

reja_lineno = tk.Label(ventana, text= "No de linea", font=("Arial",12), bg="white", fg="black")
reja_lineno.place (x=400, y=460, width = 86, height=15)

reja_pos = tk.Label(ventana, text= "Poscicion", font=("Arial",12), bg="white", fg="black")
reja_pos.place (x=500, y=460, width = 86, height=15)

##Resultados

resultado_token = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
resultado_token.place(x=200, y=480, width = 106, height=240)

resultado_lexema = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
resultado_lexema.place(x=300, y=480, width = 100, height=240)

resultado_lineno = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
resultado_lineno.place(x=400, y=480, width = 100, height=240)

resultado_pos = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
resultado_pos.place(x=500, y=480, width = 100, height=240)

##Errores

reja_pos = tk.Label(ventana, text= "Errores", justify= ["left"], font=("Arial",12), bg="white", fg="black")
reja_pos.place (x=420, y=60, width = 370, height=23)

error_texto = tk.Text(ventana, font=("Arial",10), bg="white", fg="black", height=10, width=40)
error_texto.place(x=420, y=90, width = 370, height=345)

##Botones

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial",12),bg="#95A5A6",fg="black",command=analizar)
boton_analizar.place(x=40, y=15)

boton_borrar = tk.Button(ventana, text="Borrar", font=("Arial",12),bg="#95A5A6",fg="black",command = borrar)
boton_borrar.place(x=420, y=15)

ventana.mainloop()