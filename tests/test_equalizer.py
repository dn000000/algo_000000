#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модульные тесты для модуля equalizer.
"""

import unittest
import sys
import os

# Добавляем директорию src в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from equalizer import can_equalize, min_operations, visualize_equalization


class TestEqualizer(unittest.TestCase):
    """
    Тесты для модуля equalizer.
    """
    
    def test_can_equalize_true(self):
        """
        Проверка возможности выравнивания на положительных примерах.
        """
        self.assertTrue(can_equalize([1, 2]))
        self.assertTrue(can_equalize([1, 1, 5, 5, 5]))
        self.assertTrue(can_equalize([1, 1, 1, 1]))
        self.assertTrue(can_equalize([0, 0, 1, 2, 3]))
    
    def test_can_equalize_false(self):
        """
        Проверка невозможности выравнивания на отрицательных примерах.
        """
        self.assertFalse(can_equalize([3, 2, 1]))
        self.assertFalse(can_equalize([5, 1, 3, 2]))
        self.assertFalse(can_equalize([10, 5, 7, 8]))
    
    def test_min_operations_example1(self):
        """
        Проверка минимального количества операций на примере 1.
        """
        self.assertEqual(min_operations([1, 2]), 1)
    
    def test_min_operations_example2(self):
        """
        Проверка минимального количества операций на примере 2.
        """
        self.assertEqual(min_operations([1, 1, 5, 5, 5]), 4)
    
    def test_min_operations_example3(self):
        """
        Проверка невозможности выравнивания на примере 3.
        """
        self.assertEqual(min_operations([3, 2, 1]), -1)
    
    def test_min_operations_additional(self):
        """
        Дополнительные тесты для min_operations.
        """
        self.assertEqual(min_operations([1, 1, 1, 1]), 0)  # Уже выровнены
        self.assertEqual(min_operations([0, 1, 2, 3]), 3)  # Требуется 3 операции
        self.assertEqual(min_operations([0, 0, 0, 5]), 5)  # Требуется 5 операций
    
    def test_visualize_equalization(self):
        """
        Тест функции визуализации.
        """
        # Тест без отображения графика
        operations, volumes = visualize_equalization([1, 2], show_plot=False)
        self.assertEqual(operations, 1)
        self.assertEqual(volumes, [2, 2])
        
        # Тест для невозможного выравнивания
        operations, volumes = visualize_equalization([3, 2, 1], show_plot=False)
        self.assertEqual(operations, -1)
        self.assertEqual(volumes, [3, 2, 1])
        
        # Тест для уже выровненных объемов
        operations, volumes = visualize_equalization([5, 5, 5], show_plot=False)
        self.assertEqual(operations, 0)
        self.assertEqual(volumes, [5, 5, 5])


if __name__ == "__main__":
    unittest.main() 