#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для работы с кривой Розы Гвидо (Rhodonea curve).

Этот модуль содержит функции для определения принадлежности точки кривой
Розы Гвидо в полярной системе координат и визуализации этой кривой.
"""

import numpy as np
import matplotlib.pyplot as plt


def rose_curve(theta, n, a, use_sin=False):
    """
    Вычисляет значение радиус-вектора для кривой Розы Гвидо.
    
    Кривая Розы Гвидо задается в полярных координатах уравнением:
    r = a * cos(n * θ) или r = a * sin(n * θ)
    
    Args:
        theta (float): Полярный угол.
        n (float): Параметр, определяющий количество лепестков.
        a (float): Масштабный коэффициент (амплитуда).
        use_sin (bool): Использовать sin вместо cos (по умолчанию False).
        
    Returns:
        float: Значение радиус-вектора кривой в точке с углом theta.
    """
    if use_sin:
        return a * np.sin(n * theta)
    else:
        return a * np.cos(n * theta)


def is_point_on_curve(r, theta, n, a, use_sin=False, tolerance=1e-6):
    """
    Проверяет, принадлежит ли точка с полярными координатами (r, θ) кривой Розы Гвидо.
    
    Args:
        r (float): Радиус-вектор точки.
        theta (float): Полярный угол точки (в радианах).
        n (float): Параметр кривой, определяющий количество лепестков.
        a (float): Масштабный коэффициент кривой.
        use_sin (bool): Использовать sin вместо cos (по умолчанию False).
        tolerance (float): Допустимая погрешность (по умолчанию 1e-6).
        
    Returns:
        bool: True, если точка принадлежит кривой (с учетом погрешности), иначе False.
    """
    curve_r = rose_curve(theta, n, a, use_sin)
    return abs(r - curve_r) <= tolerance


def visualize_rose_curve(n, a, r=None, theta=None, use_sin=False, show_plot=True):
    """
    Визуализирует кривую Розы Гвидо и, опционально, проверяемую точку.
    
    Args:
        n (float): Параметр кривой, определяющий количество лепестков.
        a (float): Масштабный коэффициент кривой.
        r (float, optional): Радиус-вектор проверяемой точки.
        theta (float, optional): Полярный угол проверяемой точки (в радианах).
        use_sin (bool): Использовать sin вместо cos (по умолчанию False).
        show_plot (bool): Отображать график (по умолчанию True).
        
    Returns:
        tuple: (fig, ax) - объекты для дальнейшей настройки графика.
    """
    # Создаем массив углов для построения кривой
    angles = np.linspace(0, 2*np.pi, 1000)
    
    # Вычисляем радиусы для каждого угла
    radii = [rose_curve(angle, n, a, use_sin) for angle in angles]
    
    # Преобразуем полярные координаты в декартовы для графика
    x_curve = [r * np.cos(angle) for r, angle in zip(radii, angles)]
    y_curve = [r * np.sin(angle) for r, angle in zip(radii, angles)]
    
    # Создаем график
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
    
    # Строим кривую в полярных координатах
    ax.plot(angles, radii, label=f'Роза Гвидо (n={n}, a={a})')
    
    # Если заданы координаты точки, отображаем её
    if r is not None and theta is not None:
        is_on_curve = is_point_on_curve(r, theta, n, a, use_sin)
        marker_color = 'green' if is_on_curve else 'red'
        marker_label = 'Точка на кривой' if is_on_curve else 'Точка не на кривой'
        
        ax.plot([theta], [r], marker='o', markersize=10, 
                color=marker_color, label=marker_label)
        
        # Отображаем информацию о точке
        curve_r = rose_curve(theta, n, a, use_sin)
        ax.text(0.05, 0.95, 
                f'Координаты точки: (r={r:.4f}, θ={theta:.4f})\n'
                f'Значение на кривой: r={curve_r:.4f}\n'
                f'Точка {"на" if is_on_curve else "не на"} кривой',
                transform=ax.transAxes, fontsize=12,
                bbox=dict(facecolor='white', alpha=0.8))
    
    # Настраиваем график
    ax.set_title(f'Кривая Розы Гвидо: r = a * {"sin" if use_sin else "cos"}(n * θ)')
    ax.legend(loc='upper right')
    ax.grid(True)
    
    # Добавляем вторую визуализацию в декартовой системе координат
    fig2, ax2 = plt.subplots(figsize=(10, 10))
    ax2.plot(x_curve, y_curve, label=f'Роза Гвидо (n={n}, a={a})')
    
    # Если заданы координаты точки, отображаем её на декартовом графике
    if r is not None and theta is not None:
        x_point = r * np.cos(theta)
        y_point = r * np.sin(theta)
        is_on_curve = is_point_on_curve(r, theta, n, a, use_sin)
        marker_color = 'green' if is_on_curve else 'red'
        
        ax2.plot(x_point, y_point, marker='o', markersize=10, 
                color=marker_color, label=marker_label)
    
    ax2.set_title(f'Кривая Розы Гвидо в декартовых координатах: r = a * {"sin" if use_sin else "cos"}(n * θ)')
    ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax2.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax2.grid(True)
    ax2.set_aspect('equal')
    ax2.legend()
    
    if show_plot:
        plt.tight_layout()
        plt.show()
    
    return (fig, ax), (fig2, ax2)


def interactive_rose_visualization(n_values=None, a_values=None, use_sin=False):
    """
    Создает интерактивную визуализацию с различными значениями параметров n и a.
    
    Args:
        n_values (list, optional): Список значений параметра n.
        a_values (list, optional): Список значений параметра a.
        use_sin (bool): Использовать sin вместо cos.
        
    Returns:
        None
    """
    if n_values is None:
        n_values = [1, 2, 3, 4, 5, 7]
    if a_values is None:
        a_values = [1]
    
    fig, axes = plt.subplots(len(n_values), len(a_values), figsize=(15, 15), 
                             subplot_kw={'projection': 'polar'})
    
    # Обрабатываем случай, когда только один график
    if len(n_values) == 1 and len(a_values) == 1:
        axes = np.array([[axes]])
    # Обрабатываем случай, когда только одна строка или столбец
    elif len(n_values) == 1 or len(a_values) == 1:
        axes = np.array([axes]) if len(n_values) == 1 else np.array([axes]).T
    
    # Строим графики для всех комбинаций параметров
    for i, n in enumerate(n_values):
        for j, a in enumerate(a_values):
            # Углы для построения кривой
            angles = np.linspace(0, 2*np.pi, 1000)
            # Вычисляем радиусы для каждого угла
            radii = np.array([rose_curve(angle, n, a, use_sin) for angle in angles])
            
            # Строим кривую
            axes[i, j].plot(angles, radii)
            axes[i, j].set_title(f'n={n}, a={a}')
            
            # Настраиваем график
            axes[i, j].grid(True)
            # Устанавливаем одинаковый масштаб для всех графиков
            axes[i, j].set_rmax(np.max(np.abs(radii)) * 1.1)
    
    plt.tight_layout()
    plt.suptitle(f'Кривые Розы Гвидо: r = a * {"sin" if use_sin else "cos"}(n * θ)', fontsize=16)
    plt.subplots_adjust(top=0.95)
    plt.show() 