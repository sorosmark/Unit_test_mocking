import pytest
from simple_calculator import SimpleCalculator
from unittest.mock import Mock

def test_add_with_mock_history_service():
    mock_history = Mock()

    calc = SimpleCalculator(history_service = mock_history)

    result = calc.add(1, 4)

    assert result == 5
    mock_history.save_operation.assert_called_once()
    mock_history.save_operation.assert_called_with("add", 1, 4, 5)

def test_multiply_with_multiple_mocks():
    mock_history = Mock()
    mock_logger = Mock()

    calc2 = SimpleCalculator(history_service=mock_history, logger=mock_logger)

    result2 = calc2.multiply(2, 4)

    assert result2 == 8
    mock_logger.log_operation.assert_called_once()
    mock_logger.log_operation.assert_called_with("multiply", 2, 4, 8)
    

def test_get_history_count_with_mock():
    pass