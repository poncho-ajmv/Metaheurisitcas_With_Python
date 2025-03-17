import numpy as np
import matplotlib.pyplot as plt
import math
import random
from matplotlib.widgets import Button, TextBox
import sympy as sp
from matplotlib.animation import FuncAnimation

def compile_function(func_str):
    x_sym = sp.Symbol('x')
    func_sym = sp.sympify(func_str, {'math': sp, 'x': x_sym})
    return sp.lambdify(x_sym, func_sym, modules=["numpy", "math"]), sp.latex(func_sym)

def simulated_annealing(T_inicial=2.0, T_final=0.001, alpha=0.98, num_iter=210, x_min=0.0, x_max=2.0, func_str="x * math.sin(5 * x) * (1 - x)**2"):
    global ax, solution_plot, best_point, start_point, text_status, ani, text_func, mode, button_mode
    
    plt.close('all')
    fig, ax = plt.subplots(figsize=(18, 7.1))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)

    func, formula_latex = compile_function(func_str)
    
    x_values = np.linspace(x_min, x_max, 400)
    y_values = func(x_values)
    ax.plot(x_values, y_values, label="Función Objetivo", color="blue")
    ax.set_title("Optimización con Templado Simulado")
    ax.set_xlabel("Valor de x")
    ax.set_ylabel("Valor de f(x)")
    ax.legend()
    ax.grid(True)

    formula_str = f'$f(x) = {formula_latex}$'
    ax.text(0.05, 0.85, formula_str, transform=ax.transAxes,
            fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    text_status = ax.text(0.01, 0.4, "", transform=ax.transAxes, fontsize=12,
                          verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    solution_plot, = ax.plot([], [], marker='o', linestyle='-', color="red", label="Camino de Soluciones")
    best_point = ax.scatter([], [], color="green", s=100, zorder=5, label="Mejor Solución")
    start_point = ax.scatter([], [], color="orange", s=100, zorder=5, label="Inicio")
    
    ax.legend()
    
    ax_button_anim = plt.axes([0.7, 0.05, 0.1, 0.075])
    button_anim = Button(ax_button_anim, 'Animar')
    button_anim.on_clicked(lambda event: simulated_annealing_iterativo(T_inicial, T_final, alpha, num_iter, x_min, x_max, func_str))

    ax_button_reset = plt.axes([0.82, 0.05, 0.1, 0.075])
    button_reset = Button(ax_button_reset, 'Reiniciar')
    button_reset.on_clicked(lambda event: simulated_annealing())
    
    ax_button_mode = plt.axes([0.58, 0.05, 0.1, 0.075])
    button_mode = Button(ax_button_mode, f"Modo: {'Max' if mode else 'Min'}")
    
    def toggle_mode(event):
        global mode
        mode = not mode
        button_mode.label.set_text(f"Modo: {'Max' if mode else 'Min'}")
    
    button_mode.on_clicked(toggle_mode)
    
    ax_func = plt.axes([0.1, 0.05, 0.45, 0.05])
    text_func = TextBox(ax_func, "Función", initial=func_str)

    def update_function(_):
        new_func = text_func.text
        simulated_annealing(T_inicial, T_final, alpha, num_iter, x_min, x_max, new_func)

    text_func.on_submit(update_function)
    
    plt.show()

def simulated_annealing_iterativo(T_inicial, T_final, alpha, num_iter, x_min, x_max, func_str):
    global ax, solution_plot, best_point, start_point, text_status, ani, mode

    func, _ = compile_function(func_str)

    x_actual = random.uniform(x_min, x_max)
    z_actual = func(x_actual)
    best_x, best_z = x_actual, z_actual
    solution_path = [(x_actual, z_actual)]
    T = T_inicial

    start_point.set_offsets([[x_actual, z_actual]])  # Marca el inicio

    def update(frame):
        nonlocal x_actual, z_actual, best_x, best_z, T

        x_cand = np.clip(x_actual + random.uniform(-0.1, 0.1), x_min, x_max)
        z_cand = func(x_cand)

        delta_E = z_cand - z_actual if mode else z_actual - z_cand
        probabilidad = math.exp(delta_E / T)  # Fórmula explícita P = exp(ΔE / T)
        
        if random.random() < probabilidad:
            decision = f"Aceptado: \n$P = e^{{{delta_E:.3f} / {T:.3f}}} = {probabilidad:.3f}$"
            x_actual, z_actual = x_cand, z_cand
        else:
            decision = f"Rechazado: \n$P = e^{{{delta_E:.3f} / {T:.3f}}} = {probabilidad:.3f}$"

        if (z_actual > best_z and mode) or (z_actual < best_z and not mode):
            best_x, best_z = x_actual, z_actual

        solution_path.append((x_actual, z_actual))
        T = max(T_final, T * alpha)  # Enfriamiento T = max(T_final, α * T)

        solution_plot.set_data(*zip(*solution_path))
        best_point.set_offsets([[best_x, best_z]])
        text_status.set_text(f"Iteración {frame}\n{decision}\nModo: {'Max' if mode else 'Min'}")
        return solution_plot, best_point, text_status

    ani = FuncAnimation(ax.figure, update, frames=num_iter, interval=50, repeat=False)
    plt.draw()

mode = False  # True = Maximización, False = Minimización
simulated_annealing()
