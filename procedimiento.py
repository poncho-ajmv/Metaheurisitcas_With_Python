import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

# Función para calcular y graficar
def calcular():
    try:
        expr_input = entry_func.get()
        x = sp.Symbol('x')
        f_expr = sp.sympify(expr_input)
        
        # Obtener el intervalo
        x_min = float(entry_min.get())
        x_max = float(entry_max.get())
        
        # Calcular la primera y segunda derivada
        f_deriv = sp.diff(f_expr, x)
        f_second_deriv = sp.diff(f_deriv, x)
        
        # Encontrar los puntos críticos
        critical_points = sp.solvers.solve(f_deriv, x)
        critical_points = [round(p.evalf(), 2) for p in critical_points if p.is_real]
        
        # Filtrar los puntos críticos dentro del intervalo [x_min, x_max]
        valid_points = [p for p in critical_points if x_min <= p <= x_max]
        
        # Evaluar la función en los puntos críticos y en los extremos del intervalo
        points_to_evaluate = [x_min, x_max] + valid_points
        f_values = {p: round(f_expr.subs(x, p).evalf(), 2) for p in points_to_evaluate}
        
        # Encontrar el valor máximo global
        max_x = round(max(f_values, key=f_values.get), 2)
        max_f = f_values[max_x]
        
        # Generar valores de x en el rango [x_min, x_max]
        x_vals = np.linspace(x_min, x_max, 400)
        f_vals = [f_expr.subs(x, val).evalf() for val in x_vals]
        
        # Crear la figura con dos subgráficos
        fig, axs = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [2, 1]})
        fig.subplots_adjust(left=0.05, right=0.95)  # Ajustar la posición de la gráfica a la izquierda
        
        # Gráfico de la función
        ax = axs[0]
        ax.plot(x_vals, f_vals, label=f'$f(x) = {sp.latex(f_expr)}$', color='b', linewidth=2)
        ax.scatter(valid_points, [f_expr.subs(x, p).evalf() for p in valid_points], color='red', zorder=3, label="Óptimos locales", s=100)
        ax.scatter(max_x, max_f, color='green', zorder=3, label="Máximo global", s=100)
        ax.set_xlabel('$x$', fontsize=12)
        ax.set_ylabel('$f(x)$', fontsize=12)
        ax.set_title('Optimización de Función', fontsize=14, fontweight='bold')
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
        ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
        ax.legend(fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Cuadro de texto con información del procedimiento
        ax_text = axs[1]
        ax_text.axis('off')
        info_text = (f"Función Objetivo:\n$ f(x) = {sp.latex(f_expr)} $\n\n"
                     f"Primera Derivada:\n$ f'(x) = {sp.latex(f_deriv)} $\n\n"
                     f"Puntos Críticos:\n$ x = {', '.join(map(lambda p: f'{p:.2f}', critical_points))} $\n\n"
                     f"Óptimo Global en [{x_min}, {x_max}]:\n$ x = {max_x:.2f}, f(x) = {max_f:.2f} $")
        ax_text.text(-0.15, 0.5, info_text, fontsize=12, verticalalignment='center', bbox=dict(facecolor='white', alpha=0.5))  # Mover texto a la izquierda
        
        plt.show()
        
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Crear interfaz gráfica mejorada
root = tk.Tk()
root.title("Optimización No Lineal")
root.geometry("550x350")
root.resizable(False, False)

frame = ttk.Frame(root, padding="10")
frame.pack(fill='both', expand=True)

label_func = ttk.Label(frame, text="Ingrese la función en términos de x:")
label_func.pack()
entry_func = ttk.Entry(frame, width=50)
entry_func.insert(0, "12*x**5 - 975*x**4 + 28000*x**3 - 345000*x**2 + 1800000*x")
entry_func.pack()

label_min = ttk.Label(frame, text="Límite inferior del intervalo:")
label_min.pack()
entry_min = ttk.Entry(frame, width=10)
entry_min.insert(0, "0")
entry_min.pack()

label_max = ttk.Label(frame, text="Límite superior del intervalo:")
label_max.pack()
entry_max = ttk.Entry(frame, width=10)
entry_max.insert(0, "31")
entry_max.pack()

button_calc = ttk.Button(frame, text="Calcular", command=calcular)
button_calc.pack(pady=10)

root.mainloop()