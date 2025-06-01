import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Константы для настройки модели
X_RANGE = 100
SIGMA_MAX_RANDOM = 7
SEED = 42  # Для воспроизводимости случайного поля


def simulate(alpha_s, kappa, sigma_0, show_gravity=False):
    """
    Строит график семонного поля и каузонов по заданным параметрам.
    """
    np.random.seed(SEED)  # Воспроизводимость
    x = np.linspace(0, X_RANGE, X_RANGE)
    sigma = np.random.rand(X_RANGE) * SIGMA_MAX_RANDOM
    P = alpha_s * (1 - np.exp(-kappa * sigma))
    causons = sigma >= sigma_0

    fig, axs = plt.subplots(2 + int(show_gravity), 1, figsize=(8, 6), tight_layout=True)

    # График σ(x)
    axs[0].plot(x, sigma, label="σ(x)", color='blue')
    axs[0].axhline(sigma_0, color='red', linestyle='--', label="σ₀ (порог)")
    axs[0].set_title("Семонное поле и порог реализации")
    axs[0].set_ylabel("σ(x)")
    axs[0].legend()
    axs[0].grid(True)

    # График каузонов
    axs[1].plot(x[causons], np.ones(sum(causons)), '|', markersize=20, color='green', label="Каузон")
    axs[1].set_ylim(0, 2)
    axs[1].set_title("Реализованные события (каузоны)")
    axs[1].set_yticks([])
    axs[1].set_xlabel("Позиция x")
    axs[1].legend()
    axs[1].grid(True)

    # Гравитационный аналог
    if show_gravity:
        g = -np.gradient(sigma)
        axs[2].plot(x, g, color='purple', label="g(x) = -∇σ(x)")
        axs[2].set_title("Гравитационный аналог")
        axs[2].set_ylabel("g(x)")
        axs[2].legend()
        axs[2].grid(True)

    return fig


def launch_gui():
    root = tk.Tk()
    root.title("SCCL — Симулятор коллапса семонов")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0)

    # Параметры αₛ (когерентность)
    ttk.Label(frame, text="αₛ (когерентность):").grid(column=0, row=0, sticky=tk.W)
    alpha_s_slider = ttk.Scale(frame, from_=0.0, to=1.0, orient=tk.HORIZONTAL)
    alpha_s_slider.set(0.7)
    alpha_s_slider.grid(column=1, row=0)

    # Параметр κ (чувствительность)
    ttk.Label(frame, text="κ (чувствительность):").grid(column=0, row=1, sticky=tk.W)
    kappa_slider = ttk.Scale(frame, from_=0.1, to=5.0, orient=tk.HORIZONTAL)
    kappa_slider.set(1.0)
    kappa_slider.grid(column=1, row=1)

    # Параметр σ₀ (порог коллапса)
    ttk.Label(frame, text="σ₀ (порог коллапса):").grid(column=0, row=2, sticky=tk.W)
    sigma0_slider = ttk.Scale(frame, from_=1.0, to=7.0, orient=tk.HORIZONTAL)
    sigma0_slider.set(5.0)
    sigma0_slider.grid(column=1, row=2)

    # Флаг отображения гравитационного аналога
    gravity_var = tk.BooleanVar()
    gravity_check = ttk.Checkbutton(frame, text="Показать гравитационный аналог (∇σ)", variable=gravity_var)
    gravity_check.grid(column=0, row=3, columnspan=2)

    # Область для графика
    graph_frame = ttk.Frame(root)
    graph_frame.grid(row=1, column=0)

    def update_plot():
        try:
            # Очистка предыдущего графика
            for widget in graph_frame.winfo_children():
                widget.destroy()

            # Получение значений из GUI
            alpha_s = alpha_s_slider.get()
            kappa = kappa_slider.get()
            sigma_0 = sigma0_slider.get()
            show_gravity = gravity_var.get()

            # Генерация нового графика
            fig = simulate(alpha_s, kappa, sigma_0, show_gravity)

            # Интеграция в Tkinter
            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка при построении графика:\n{e}")

    # Кнопка запуска
    ttk.Button(frame, text="▶ Обновить", command=update_plot).grid(
        column=0, row=4, columnspan=2, pady=10
    )

    # Первичный запуск
    update_plot()

    root.mainloop()


# Запуск GUI
launch_gui()