import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, messagebox

# Глобальные константы
X_RANGE = 200
SIGMA_MAX_RANDOM = 3.0
SEED = 42

def simulate(alpha_s, kappa, sigma_0, show_gravity=False, stochastic=False):
    np.random.seed(SEED)
    x = np.linspace(0, X_RANGE, X_RANGE)
    sigma = np.random.rand(X_RANGE) * SIGMA_MAX_RANDOM
    P = alpha_s * (1 - np.exp(-kappa * sigma))

    if stochastic:
        causons = (sigma >= sigma_0) & (np.random.rand(X_RANGE) < P)
    else:
        causons = sigma >= sigma_0

    fig, axs = plt.subplots(2 if not show_gravity else 3, 1, figsize=(8, 7))
    axs[0].plot(x, sigma, label="σ(x) — Темпоральное напряжение")
    axs[0].axhline(sigma_0, color="r", linestyle="--", label="Порог σ₀")
    axs[0].set_ylabel("σ")
    axs[0].set_title("Случайное поле σ(x)")
    axs[0].legend(loc="upper right")
    axs[0].grid(True)

    axs[1].plot(x, causons * 1, 'o', color='purple', markersize=4, label="Каузоны (коллапсы)")
    axs[1].set_ylabel("Каузон")
    axs[1].set_xlabel("x")
    axs[1].set_title("Каузоны: σ(x) ≥ σ₀" + (" & вероятность" if stochastic else ""))
    axs[1].legend()
    axs[1].grid(True)

    if show_gravity:
        grad = np.gradient(sigma)
        axs[2].plot(x, grad, label="∇σ(x) — гравитационный аналог", color='green')
        axs[2].set_ylabel("∇σ")
        axs[2].set_xlabel("x")
        axs[2].set_title("Градиент поля σ(x)")
        axs[2].legend()
        axs[2].grid(True)

    plt.tight_layout()
    return fig

def launch_gui():
    root = tk.Tk()
    root.title("SCCL: Визуализация поля и каузонов")
    frame = ttk.Frame(root, padding=15)
    frame.grid(row=0, column=0)

    # Слайдеры
    alpha_s_var = tk.DoubleVar(value=0.6)
    kappa_var = tk.DoubleVar(value=2.5)
    sigma_0_var = tk.DoubleVar(value=1.7)
    gravity_var = tk.BooleanVar()
    stochastic_var = tk.BooleanVar()

    ttk.Label(frame, text="Когерентность αₛ:").grid(column=0, row=0, sticky="e")
    alpha_s = ttk.Scale(frame, from_=0.1, to=1.0, orient="horizontal", variable=alpha_s_var, length=180)
    alpha_s.grid(column=1, row=0)

    ttk.Label(frame, text="Чувствительность κ:").grid(column=0, row=1, sticky="e")
    kappa = ttk.Scale(frame, from_=0.1, to=5.0, orient="horizontal", variable=kappa_var, length=180)
    kappa.grid(column=1, row=1)

    ttk.Label(frame, text="Порог σ₀:").grid(column=0, row=2, sticky="e")
    sigma_0 = ttk.Scale(frame, from_=0.1, to=3.0, orient="horizontal", variable=sigma_0_var, length=180)
    sigma_0.grid(column=1, row=2)

    gravity_check = ttk.Checkbutton(frame, text="Показать ∇σ(x) (грав. аналог)", variable=gravity_var)
    gravity_check.grid(column=0, row=3, columnspan=2)

    # Новый чекбокс стохастики
    stochastic_check = ttk.Checkbutton(frame, text="Стохастическая реализация каузонов", variable=stochastic_var)
    stochastic_check.grid(column=0, row=4, columnspan=2)

    fig = simulate(alpha_s_var.get(), kappa_var.get(), sigma_0_var.get(), gravity_var.get(), stochastic_var.get())
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0, column=1, rowspan=8, padx=18, pady=5)

    def update_plot():
        try:
            fig = simulate(alpha_s_var.get(), kappa_var.get(), sigma_0_var.get(), gravity_var.get(), stochastic_var.get())
            canvas.figure = fig
            canvas.draw()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка построения: {e}")

    ttk.Button(frame, text="▶ Обновить", command=update_plot).grid(
        column=0, row=5, columnspan=2, pady=10
    )

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
