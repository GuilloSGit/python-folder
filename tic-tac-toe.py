import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("🎮 Tic Tac Toe")
        self.ventana.geometry("400x500")
        self.ventana.configure(bg='#FFFe50')
        
        self.tablero = [' '] * 9
        self.jugador_actual = 'X'
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz gráfica"""
        titulo = tk.Label(
            self.ventana, 
            text="🎮 TIC TAC TOE 🎮", 
            font=('Arial', 20, 'bold'),
            bg='#FFFe50',
            fg='#ecf0f1'
        )
        titulo.pack(pady=20)
        
        self.label_turno = tk.Label(
            self.ventana,
            text=f"Turno del Jugador {self.jugador_actual}",
            font=('Arial', 14),
            bg='#2c3e50',
            fg='#3498db'
        )
        self.label_turno.pack(pady=10)
        
        self.frame_tablero = tk.Frame(self.ventana, bg='#2c3e50')
        self.frame_tablero.pack(pady=20)
        
        self.botones = []
        for i in range(9):
            fila = i // 3
            columna = i % 3
            
            boton = tk.Button(
                self.frame_tablero,
                text=' ',
                font=('Arial', 24, 'bold'),
                width=4,
                height=2,
                bg='#34495e',
                fg='#ecf0f1',
                activebackground='#3498db',
                command=lambda pos=i: self.hacer_movimiento(pos)
            )
            boton.grid(row=fila, column=columna, padx=2, pady=2)
            self.botones.append(boton)
        
        boton_reiniciar = tk.Button(
            self.ventana,
            text="🔄 Nueva Partida",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            activebackground='#2ecc71',
            command=self.reiniciar_juego,
            padx=20,
            pady=10
        )
        boton_reiniciar.pack(pady=20)
        
        instrucciones = tk.Label(
            self.ventana,
            text="Haz clic en una casilla para hacer tu movimiento",
            font=('Arial', 10),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        instrucciones.pack(pady=10)
    
    def hacer_movimiento(self, posicion):
        """Procesa el movimiento del jugador en la posición dada"""
        if self.tablero[posicion] != ' ':
            return
        
        self.tablero[posicion] = self.jugador_actual
        self.botones[posicion].config(
            text=self.jugador_actual,
            fg='#e74c3c' if self.jugador_actual == 'X' else '#f39c12',
            state='disabled'
        )
        
        if self.verificar_victoria(self.tablero, self.jugador_actual):
            self.mostrar_resultado(f"🎉 ¡El Jugador {self.jugador_actual} ha ganado! 🎉")
            self.deshabilitar_botones()
            return
        
        if self.tablero_lleno(self.tablero):
            self.mostrar_resultado("🤝 ¡Es un empate! ¡Buen juego!")
            return
        
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
        self.label_turno.config(text=f"Turno del Jugador {self.jugador_actual}")
    
    def verificar_victoria(self, tablero, jugador):
        """Verifica si el jugador actual ha ganado"""
        # Combinaciones ganadoras
        combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combinacion in combinaciones_ganadoras:
            if all(tablero[i] == jugador for i in combinacion):
                return True
        return False
    
    def tablero_lleno(self, tablero):
        """Verifica si el tablero está lleno (empate)"""
        return ' ' not in tablero
    
    def mostrar_resultado(self, mensaje):
        """Muestra el resultado del juego"""
        messagebox.showinfo("Resultado", mensaje)
    
    def deshabilitar_botones(self):
        """Deshabilita todos los botones del tablero"""
        for boton in self.botones:
            boton.config(state='disabled')
    
    def reiniciar_juego(self):
        """Reinicia el juego a su estado inicial"""
        self.tablero = [' '] * 9
        self.jugador_actual = 'X'
        self.label_turno.config(text=f"Turno del Jugador {self.jugador_actual}")
        
        for boton in self.botones:
            boton.config(
                text=' ',
                state='normal',
                fg='#ecf0f1'
            )
    
    def iniciar(self):
        """Inicia el bucle principal de la aplicación"""
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = TicTacToe()
    juego.iniciar()
