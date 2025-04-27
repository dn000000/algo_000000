#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модульные тесты для модуля rose.
"""

import unittest
import math
import sys
import os
import numpy as np

# Добавляем директорию src в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rose import rose_curve, is_point_on_curve


class TestRose(unittest.TestCase):
    """
    Тесты для модуля rose.
    """
    
    def test_rose_curve_cos(self):
        """
        Проверка расчета значения радиус-вектора для кривой с cos.
        """
        # Проверяем значения в специфических точках
        self.assertAlmostEqual(rose_curve(0, 1, 1), 1.0)  # cos(0) = 1
        self.assertAlmostEqual(rose_curve(math.pi/2, 1, 1), 0.0, places=5)  # cos(π/2) = 0
        self.assertAlmostEqual(rose_curve(math.pi, 1, 1), -1.0)  # cos(π) = -1
        
        # Проверка с разными параметрами n и a
        self.assertAlmostEqual(rose_curve(0, 2, 3), 3.0)  # a * cos(n*0) = a
        self.assertAlmostEqual(rose_curve(math.pi/4, 2, 3), 3.0 * math.cos(math.pi/2))  # a * cos(n*θ)
    
    def test_rose_curve_sin(self):
        """
        Проверка расчета значения радиус-вектора для кривой с sin.
        """
        # Проверяем значения в специфических точках
        self.assertAlmostEqual(rose_curve(0, 1, 1, use_sin=True), 0.0)  # sin(0) = 0
        self.assertAlmostEqual(rose_curve(math.pi/2, 1, 1, use_sin=True), 1.0)  # sin(π/2) = 1
        self.assertAlmostEqual(rose_curve(math.pi, 1, 1, use_sin=True), 0.0, places=5)  # sin(π) = 0
        
        # Проверка с разными параметрами n и a
        self.assertAlmostEqual(rose_curve(math.pi/2, 2, 3, use_sin=True), 3.0 * math.sin(math.pi))  # a * sin(n*θ)
    
    def test_is_point_on_curve_exact(self):
        """
        Проверка принадлежности точки кривой (точные значения).
        """
        # Создаем точки, которые должны лежать точно на кривой
        theta = math.pi/4
        n = 2
        a = 1
        r = rose_curve(theta, n, a)
        
        self.assertTrue(is_point_on_curve(r, theta, n, a))
        
        # Проверка для sin-версии
        r_sin = rose_curve(theta, n, a, use_sin=True)
        self.assertTrue(is_point_on_curve(r_sin, theta, n, a, use_sin=True))
    
    def test_is_point_on_curve_with_tolerance(self):
        """
        Проверка принадлежности точки кривой с учетом погрешности.
        """
        theta = math.pi/3
        n = 3
        a = 2
        r_exact = rose_curve(theta, n, a)
        
        # Немного отклоняем значение и проверяем с разной погрешностью
        r_approx = r_exact + 0.01
        
        # Должно быть не на кривой при малой погрешности
        self.assertFalse(is_point_on_curve(r_approx, theta, n, a, tolerance=0.001))
        
        # Должно быть на кривой при большей погрешности
        self.assertTrue(is_point_on_curve(r_approx, theta, n, a, tolerance=0.02))
    
    def test_is_point_not_on_curve(self):
        """
        Проверка что точка не на кривой.
        """
        theta = math.pi/6
        n = 4
        a = 2
        r_exact = rose_curve(theta, n, a)
        
        # Значительно отклоняем значение
        r_far = r_exact + 1.0
        
        # Должно быть не на кривой
        self.assertFalse(is_point_on_curve(r_far, theta, n, a))


if __name__ == "__main__":
    unittest.main() 