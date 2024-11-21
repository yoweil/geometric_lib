import unittest
from testing.rectangle import area_rectangle, perimeter_rectangle
from testing.circle import area_circle, perimeter_circle
from testing.triangle import area_triangle, perimeter_triangle
from testing.square import area_square, perimeter_square

class GeometricalLibTestCase(unittest.TestCase):
    # Тесты для прямоугольника
    def test_area_rectangle_zero(self):
        res = area_rectangle(0, 10)
        self.assertEqual(res, 0, "Площадь должна быть равна 0, если одна из сторон равна 0.")

    def test_area_rectangle_positive(self):
        res = area_rectangle(5, 10)
        self.assertEqual(res, 50, "Площадь прямоугольника с шириной 5 и высотой 10 должна быть равна 50.")

    def test_perimeter_rectangle(self):
        res = perimeter_rectangle(5, 10)
        self.assertEqual(res, 30, "Периметр прямоугольника с шириной 5 и высотой 10 должен быть равен 30.")

    # Тесты для круга
    def test_area_circle_zero(self):
        res = area_circle(0)
        self.assertEqual(res, 0, "Площадь круга с радиусом 0 должна быть равна 0.")

    def test_area_circle_positive(self):
        res = area_circle(2)
        self.assertAlmostEqual(res, 12.5664, places=4, msg="Площадь круга с радиусом 2 должна быть приблизительно равна 12.5664.")

    def test_perimeter_circle(self):
        res = perimeter_circle(3)
        self.assertAlmostEqual(res, 18.8496, places=4, msg="Длина окружности с радиусом 3 должна быть приблизительно равна 18.8496.")

    # Тесты для треугольника
    def test_area_triangle_zero(self):
        res = area_triangle(0, 10)
        self.assertEqual(res, 0, "Площадь треугольника должна быть равна 0, если основание равно 0.")

    def test_area_triangle_positive(self):
        res = area_triangle(5, 4)
        self.assertEqual(res, 10, "Площадь треугольника с основанием 5 и высотой 4 должна быть равна 10.")

    def test_perimeter_triangle(self):
        res = perimeter_triangle(3, 4, 5)
        self.assertEqual(res, 12, "Периметр треугольника со сторонами 3, 4, 5 должен быть равен 12.")
        
    # Тесты для квадрата
    def test_area_square_zero(self):
        res = area_square(0)
        self.assertEqual(res, 0, "Площадь квадрата со стороной 0 должна быть равна 0.")

    def test_area_square_positive(self):
        res = area_square(4)
        self.assertEqual(res, 16, "Площадь квадрата со стороной 4 должна быть равна 16.")

    def test_perimeter_square_zero(self):
        res = perimeter_square(0)
        self.assertEqual(res, 0, "Периметр квадрата со стороной 0 должен быть равен 0.")

    def test_perimeter_square_positive(self):
        res = perimeter_square(4)
        self.assertEqual(res, 16, "Периметр квадрата со стороной 4 должен быть равен 16.")

if __name__ == '__main__':
    unittest.main()
