import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraGeometrica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Geométrica")
        self.root.update()  # Actualiza la ventana para que se maximice de inmediato

        # Crear frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="x")
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(fill="both", expand=True)

        # Crear campos de entrada
        self.shape_label = tk.Label(self.input_frame, text="Figura:")
        self.shape_label.pack(side="left")
        self.shape_var = tk.StringVar()
        self.shape_var.set("Círculo")
        self.shape_menu = tk.OptionMenu(self.input_frame, self.shape_var, "Círculo", "Triángulo", "Rectángulo", "Paralelogramo")
        self.shape_menu.pack(side="left")

        self.param_label = tk.Label(self.input_frame, text="Parámetro:")
        self.param_label.pack(side="left")
        self.param_entry = tk.Entry(self.input_frame)
        self.param_entry.pack(side="left")

        self.calculate_button = tk.Button(self.input_frame, text="Calcular", command=self.calculate)
        self.calculate_button.pack(side="left")

        # Crear área de trazado
        self.canvas = tk.Canvas(self.plot_frame, bg="white")
        self.canvas.pack(fill="both", expand=True)
        self.draw_grid()

        # Crear lista de historial
        self.history_listbox = tk.Listbox(self.plot_frame)
        self.history_listbox.pack(side="bottom", fill="both", expand=True)

        # Crear botón para borrar historial
        self.clear_button = tk.Button(self.plot_frame, text="Borrar Historial", command=self.clear_history)
        self.clear_button.pack(side="bottom")

    def draw_grid(self):
        self.canvas.delete("grid")
        for i in range(0, 800, 20):
            self.canvas.create_line(i, 0, i, 800, fill="lightgrey", tags="grid")
            self.canvas.create_line(0, i, 800, i, fill="lightgrey", tags="grid")

    def calculate(self):
        shape = self.shape_var.get()
        param = float(self.param_entry.get())

        self.canvas.delete("shape")
        self.draw_grid()

        if shape == "Círculo":
            area = math.pi * param ** 2
            circunferencia = 2 * math.pi * param
            self.plot_circle(param)
            self.history_listbox.insert("end", f"Círculo: Área={area:.2f}, Circunferencia={circunferencia:.2f}")
        elif shape == "Triángulo":
            base = param
            altura = param
            area = (base * altura) / 2
            perímetro = base + altura + math.sqrt(base ** 2 + altura ** 2)
            self.plot_triangle(base, altura)
            self.history_listbox.insert("end", f"Triángulo: Área={area:.2f}, Perímetro={perímetro:.2f}")
        elif shape == "Rectángulo":
            base = param
            altura = param
            area = base * altura
            perímetro = 2 * (base + altura)
            self.plot_rectangle(base, altura)
            self.history_listbox.insert("end", f"Rectángulo: Área={area:.2f}, Perímetro={perímetro:.2f}")
        elif shape == "Paralelogramo":
            base = param
            altura = param
            area = base * altura
            perímetro = 2 * (base + altura)
            self.plot_parallelogram(base, altura)
            self.history_listbox.insert("end", f"Paralelogramo: Área={area:.2f}, Perímetro={perímetro:.2f}")

    def clear_history(self):
        self.history_listbox.delete(0, "end")

    def plot_circle(self, radio):
        self.canvas.create_oval(100, 100, 100 + 2 * radio, 100 + 2 * radio, outline="black", fill="lightblue", tags="shape")
        self.canvas.create_text(100 + radio, 90, text=f"Radio={radio}", fill="black", tags="shape")

    def plot_triangle(self, base, altura):
        self.canvas.create_polygon(100, 100, 100 + base, 100, 100, 100 - altura, outline="black", fill="lightgreen", width=2, tags="shape")
        self.canvas.create_text(100 + base / 2, 110, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text(90, 100 - altura / 2, text=f"Altura={altura}", fill="black", tags="shape")

    def plot_rectangle(self, base, altura):
        self.canvas.create_rectangle(100, 100, 100 + base, 100 + altura, outline="black", fill="lightcoral", tags="shape")
        self.canvas.create_text(100 + base / 2, 90, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text(90, 100 + altura / 2, text=f"Altura={altura}", fill="black", tags="shape")

    def plot_parallelogram(self, base, altura):
        self.canvas.create_polygon(100, 100, 100 + base, 100, 100 + base + altura, 100 + altura, 100 + altura, 100 + altura, outline="black", fill="lightyellow", width=2, tags="shape")
        self.canvas.create_text(100 + base / 2, 90, text=f"Base={base}", fill="black", tags="shape")
        self.canvas.create_text(100 + base + altura / 2, 110 + altura, text=f"Altura={altura}", fill="black", tags="shape")

root = tk.Tk()
calculadora = CalculadoraGeometrica(root)
root.mainloop()
