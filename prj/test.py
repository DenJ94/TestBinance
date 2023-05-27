# необходимое
from unittest.mock import patch, Mock
import unittest

from PytBinance import create_orders

class TestCreateOrders(unittest.TestCase):
    
    @patch("PytBinance.Client")
    def test_create_orders(self, mock_client):
        # mock для заказа
        mock_order = Mock()
        mock_client.return_value.order_limit.return_value = mock_order

        # тест данные
        data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        # вызов тестовых данных
        result = create_orders(data)

        # проверка 
        self.assertEqual(len(result), data["number"])
        self.assertEqual(result[0], mock_order)
        self.assertTrue(mock_client.return_value.order_limit.called)

    @patch("PytBinance.Client")
    def test_create_orders_exception(self, mock_client):
        # mock для ошибки
        mock_client.return_value.order_limit.side_effect = Exception("An error occurred")

        data = {
            "volume": 10000.0,
            "number": 5,
            "amountDif": 50.0,
            "side": "SELL",
            "priceMin": 200.0,
            "priceMax": 300.0
        }

        # вызов тестовых данных
        result = create_orders(data)

        # проверка 
        self.assertEqual(len(result), 0)


# запуск
if __name__ == '__main__':
    unittest.main()