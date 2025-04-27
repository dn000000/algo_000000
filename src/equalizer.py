#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для решения задачи выравнивания жидкости в резервуарах.

Этот модуль содержит алгоритм для определения минимального количества операций,
необходимых для выравнивания уровней жидкости в резервуарах, с использованием 
только операции "добавить 1 литр в первые k резервуаров".
"""


def can_equalize(volumes):
    """
    Проверяет, возможно ли выровнять объёмы резервуаров.
    
    Для того чтобы выравнивание было возможно, массив объемов должен быть 
    неубывающим (каждый следующий элемент должен быть не меньше предыдущего).
    
    Args:
        volumes (list): Список объемов резервуаров.
        
    Returns:
        bool: True, если выравнивание возможно, иначе False.
    """
    for i in range(1, len(volumes)):
        if volumes[i] < volumes[i-1]:
            return False
    return True


def min_operations(volumes):
    """
    Рассчитывает минимальное количество операций для выравнивания всех резервуаров.
    
    Алгоритм основан на том, что для получения "ступенчатой" структуры добавлений нужно
    выполнять операции в обратном порядке: сначала добавлять жидкость в первые n-1 резервуаров,
    затем в первые n-2 и т.д.
    
    Args:
        volumes (list): Список объемов резервуаров.
        
    Returns:
        int: Минимальное количество операций, или -1 если выравнивание невозможно.
    """
    # Проверяем, возможно ли выравнивание
    if not can_equalize(volumes):
        return -1
    
    n = len(volumes)
    
    # Если все объемы одинаковы, никаких операций не требуется
    if len(set(volumes)) == 1:
        return 0
    
    # Общее количество операций
    operations = 0
    
    # Перебираем резервуары с конца, кроме последнего
    for i in range(n-2, -1, -1):
        # Если текущий объем меньше следующего, добавляем разницу
        if volumes[i] < volumes[i+1]:
            diff = volumes[i+1] - volumes[i]
            operations += diff
            # Увеличиваем объем во всех предыдущих резервуарах
            for j in range(i+1):
                volumes[j] += diff
    
    return operations


def simulate_equalization(volumes):
    """
    Симулирует процесс выравнивания резервуаров и возвращает все промежуточные состояния.
    
    Args:
        volumes (list): Список объемов резервуаров.
        
    Returns:
        tuple: (operations, states) - количество операций и список всех состояний,
               или (-1, [volumes]) если выравнивание невозможно.
    """
    if not can_equalize(volumes):
        return -1, [volumes]
    
    n = len(volumes)
    current_volumes = volumes.copy()
    states = [current_volumes.copy()]
    operations = 0
    
    # Перебираем резервуары с конца, кроме последнего
    for i in range(n-2, -1, -1):
        # Если текущий объем меньше следующего, добавляем разницу
        while current_volumes[i] < current_volumes[i+1]:
            # Увеличиваем объем во всех предыдущих резервуарах
            for j in range(i+1):
                current_volumes[j] += 1
            operations += 1
            states.append(current_volumes.copy())
    
    return operations, states


def visualize_equalization(initial_volumes, show_plot=True):
    """
    Визуализирует процесс выравнивания резервуаров.
    
    Args:
        initial_volumes (list): Исходные объемы резервуаров.
        show_plot (bool): Флаг отображения графика (по умолчанию True).
        
    Returns:
        tuple: (operations, final_volumes) - количество операций и конечные объемы,
               или (-1, initial_volumes) если выравнивание невозможно.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    operations, states = simulate_equalization(initial_volumes)
    
    if operations == -1:
        return -1, initial_volumes
    
    if show_plot and len(states) > 1:
        n = len(initial_volumes)
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Начальное состояние
        axes[0].bar(range(1, n+1), initial_volumes, color='skyblue')
        axes[0].set_title('Начальное состояние')
        axes[0].set_xlabel('Номер резервуара')
        axes[0].set_ylabel('Объем жидкости')
        axes[0].grid(axis='y', linestyle='--', alpha=0.7)
        
        # Конечное состояние
        axes[1].bar(range(1, n+1), states[-1], color='skyblue')
        axes[1].set_title(f'Конечное состояние ({operations} операций)')
        axes[1].set_xlabel('Номер резервуара')
        axes[1].set_ylabel('Объем жидкости')
        axes[1].grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()
    
    return operations, states[-1] 