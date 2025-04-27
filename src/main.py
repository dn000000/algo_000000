#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Основной модуль для запуска программы выравнивания жидкости в резервуарах.

Этот модуль обеспечивает интерфейс командной строки для работы с алгоритмом
выравнивания жидкости в резервуарах.
"""

import sys
import argparse
from equalizer import min_operations, visualize_equalization


def parse_arguments():
    """
    Обрабатывает аргументы командной строки.
    
    Returns:
        argparse.Namespace: Объект с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(
        description='Программа для выравнивания жидкости в резервуарах'
    )
    parser.add_argument(
        '--input', '-i', type=str, 
        help='Путь к входному файлу (по умолчанию: стандартный ввод)'
    )
    parser.add_argument(
        '--visual', '-v', action='store_true',
        help='Визуализировать процесс выравнивания'
    )
    return parser.parse_args()


def read_input(input_source=None):
    """
    Считывает входные данные из указанного источника.
    
    Args:
        input_source (str, optional): Путь к входному файлу. Если None, 
                                     используется стандартный ввод.
                                     
    Returns:
        list: Список объемов резервуаров.
    """
    try:
        if input_source:
            with open(input_source, 'r') as f:
                n = int(f.readline().strip())
                volumes = list(map(int, f.readline().strip().split()))
        else:
            n = int(input().strip())
            volumes = list(map(int, input().strip().split()))
            
        if len(volumes) != n:
            raise ValueError(f"Ожидалось {n} резервуаров, получено {len(volumes)}")
            
        return volumes
    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_source}' не найден")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка формата ввода: {e}")
        sys.exit(1)


def main():
    """
    Основная функция программы.
    """
    args = parse_arguments()
    
    try:
        volumes = read_input(args.input)
        
        if args.visual:
            operations, _ = visualize_equalization(volumes)
            if operations != -1:
                print(operations)
            else:
                print("-1")
        else:
            operations = min_operations(volumes)
            print(operations)
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем")
        sys.exit(0)


if __name__ == "__main__":
    main() 