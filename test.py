import unittest
from calculus import transform_data

class TestTransformData(unittest.TestCase):
    def test_correct_diference(self):
        data1, data2 = transform_data("10 de Janeiro de 2022 - 23 de Fevereiro de 2022")
        diferenca_dias = abs((data2 - data1).days)
        self.assertEqual(diferenca_dias, 44)
        
        data1, data2 = transform_data("23 de Fevereiro de 2022 - 10 de Janeiro de 2022")
        diferenca_dias = abs((data2 - data1).days)
        self.assertEqual(diferenca_dias, 44)

        data1, data2 = transform_data("10 de Janeiro de 2022 - 10 de Janeiro de 2022")
        diferenca_dias = abs((data2 - data1).days)
        self.assertEqual(diferenca_dias, 0)

        data1, data2 = transform_data("31 de Dezembro de 2022 - 1 de Janeiro de 2023")
        diferenca_dias = abs((data2 - data1).days)
        self.assertEqual(diferenca_dias, 1)

if __name__ == "__main__":
    unittest.main()