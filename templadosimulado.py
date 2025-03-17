import numpy as np
import matplotlib.pyplot as plt
import math
import random
from matplotlib.widgets import Button, TextBox
import sympy as sp

def simulated_annealing(T_inicial=2.0, T_final=0.001, alpha=0.98, num_iter=1000, x_min=0.0, x_max=2.0, func_str="x * math.sin(5 * x) * (1 - x)**2", event=None):
    plt.close('all')  # Cerrar figuras anteriores para evitar bloqueos
    
    def objective_function(x):
        return eval(func_str, {"x": x, "math": math})
    
    x_actual = random.uniform(x_min, x_max)
    z_actual = objective_function(x_actual)
    best_x, best_z = x_actual, z_actual
    solution_path = [(x_actual, z_actual)]
    T = T_inicial
    
    for _ in range(num_iter):
        paso = random.uniform(-0.1, 0.1)
        x_cand = max(x_min, min(x_actual + paso, x_max))
        z_cand = objective_function(x_cand)
        
        if z_cand > z_actual or random.random() < math.exp((z_cand - z_actual) / T):
            x_actual, z_actual = x_cand, z_cand
        
        if z_actual > best_z:
            best_x, best_z = x_actual, z_actual
        
        solution_path.append((x_actual, z_actual))
        T = max(T_final, T * alpha)
    
    x_values = np.linspace(x_min, x_max, 400)
    y_values = [objective_function(x) for x in x_values]
    solution_path = np.array(solution_path)
    
    fig, ax = plt.subplots(figsize=(18, 7.1))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3) 
    ax.plot(x_values, y_values, label="Función Objetivo", color="blue")
    ax.plot(solution_path[:, 0], solution_path[:, 1], marker='o', linestyle='-', color="red", label="Camino de Soluciones")
    ax.scatter(best_x, best_z, color="green", s=100, zorder=5, label="Mejor Solución")
    ax.scatter(solution_path[0, 0], solution_path[0, 1], color="blue", s=100, zorder=5, label="Inicio")
    ax.set_title("Optimización con Templado Simulado")
    ax.set_xlabel("Valor de x")
    ax.set_ylabel("Valor de f(x)")
    ax.legend()
    ax.grid(True)
    
    x_sym = sp.Symbol('x')
    func_sym = sp.sympify(func_str, {'math': sp, 'x': x_sym})
    formula_latex = sp.latex(func_sym)
    formula_str = f'$f(x) = {formula_latex}$'
    
    ax.text(0.05, 0.85, formula_str, transform=ax.transAxes,
             fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))
    
    ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])
    button = Button(ax_button, 'Ejecutar')
    button.on_clicked(lambda event: simulated_annealing())
    
    def submit(_):
        try:
            T_in = float(text_Ti.text) if text_Ti.text else 2.0
            T_f = float(text_Tf.text) if text_Tf.text else 0.001
            alpha_v = float(text_alpha.text) if text_alpha.text else 0.98
            iter_v = int(text_iter.text) if text_iter.text else 1000
            func_input = text_func.text if text_func.text else "x * math.sin(5 * x) * (1 - x)**2"
            simulated_annealing(T_in, T_f, alpha_v, iter_v, func_str=func_input)
        except ValueError:
            pass  # Evitar errores con entradas no numéricas
    
    ax_Ti = plt.axes([0.1, 0.05, 0.1, 0.05])
    text_Ti = TextBox(ax_Ti, "Temperatura\nInicial", initial=str(T_inicial))
    ax_Tf = plt.axes([0.3, 0.05, 0.1, 0.05])
    text_Tf = TextBox(ax_Tf, "Temperatura\nFinal", initial=str(T_final))
    ax_alpha = plt.axes([0.5, 0.05, 0.1, 0.05])
    text_alpha = TextBox(ax_alpha, "Factor\nEnfriamiento", initial=str(alpha))
    ax_iter = plt.axes([0.69, 0.05, 0.1, 0.05])
    text_iter = TextBox(ax_iter, "Iteraciones", initial=str(num_iter))
    ax_func = plt.axes([0.1, 0.15, 0.55, 0.05])
    text_func = TextBox(ax_func, "Función", initial=func_str)
    
    text_Ti.on_submit(submit)
    text_Tf.on_submit(submit)
    text_alpha.on_submit(submit)
    text_iter.on_submit(submit)
    text_func.on_submit(submit)
    
    plt.show()

simulated_annealing()