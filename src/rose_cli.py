#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Командный интерфейс для работы с кривой Розы Гвидо.

Этот модуль предоставляет интерфейс командной строки для определения принадлежности
точки кривой Розы Гвидо и визуализации этой кривой.
"""

import sys
import argparse
import numpy as np
from rose import is_point_on_curve, visualize_rose_curve, interactive_rose_visualization


def parse_arguments():
    """
    Обрабатывает аргументы командной строки.
    
    Returns:
        argparse.Namespace: Объект с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(
        description='Определение принадлежности точки кривой Розы Гвидо'
    )
    parser.add_argument(
        '--r', type=float, 
        help='Радиус-вектор точки'
    )
    parser.add_argument(
        '--theta', type=float, 
        help='Полярный угол точки (в радианах)'
    )
    parser.add_argument(
        '--n', type=float, required=True,
        help='Параметр кривой n (определяет количество лепестков)'
    )
    parser.add_argument(
        '--a', type=float, default=1.0,
        help='Масштабный коэффициент a (по умолчанию 1.0)'
    )
    parser.add_argument(
        '--sin', action='store_true',
        help='Использовать sin вместо cos для уравнения кривой'
    )
    parser.add_argument(
        '--tolerance', type=float, default=1e-6,
        help='Допустимая погрешность (по умолчанию 1e-6)'
    )
    parser.add_argument(
        '--no-visual', action='store_true',
        help='Не отображать визуализацию'
    )
    parser.add_argument(
        '--interactive', action='store_true',
        help='Показать интерактивную визуализацию с разными параметрами'
    )
    parser.add_argument(
        '--n-values', type=str, default='1,2,3,4,5,7',
        help='Значения параметра n для интерактивной визуализации (через запятую)'
    )
    parser.add_argument(
        '--a-values', type=str, default='1',
        help='Значения параметра a для интерактивной визуализации (через запятую)'
    )
    
    return parser.parse_args()


def main():
    """
    Основная функция программы.
    """
    args = parse_arguments()
    
    try:
        # Если выбран интерактивный режим, отображаем разные кривые
        if args.interactive:
            n_values = [float(x) for x in args.n_values.split(',')]
            a_values = [float(x) for x in args.a_values.split(',')]
            interactive_rose_visualization(n_values, a_values, args.sin)
            return
        
        # Если заданы координаты точки, проверяем принадлежность кривой
        if args.r is not None and args.theta is not None:
            result = is_point_on_curve(args.r, args.theta, args.n, args.a, 
                                     args.sin, args.tolerance)
            print(f"Точка (r={args.r}, θ={args.theta}) {'принадлежит' if result else 'не принадлежит'} "
                  f"кривой Розы Гвидо с параметрами n={args.n}, a={args.a}")
            
            # Визуализация, если не отключена
            if not args.no_visual:
                visualize_rose_curve(args.n, args.a, args.r, args.theta, args.sin)
        else:
            # Если точка не задана, просто отображаем кривую
            if not args.no_visual:
                visualize_rose_curve(args.n, args.a, use_sin=args.sin)
            else:
                print(f"Визуализация отключена. Для просмотра кривой Розы Гвидо с параметрами "
                      f"n={args.n}, a={args.a} уберите флаг --no-visual.")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
        sys.exit(0)


if __name__ == "__main__":
    main() 