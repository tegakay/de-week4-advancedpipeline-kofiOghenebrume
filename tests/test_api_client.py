import pytest
import requests
from unittest.mock import patch, MagicMock,Mock
from pipeline.api_client import APIClient


@pytest.fixture
def client():
    """Provides an APIClient instance for testing."""
    return APIClient(base_url="https://fakeapi.com")

@pytest.fixture
def products():
    return [
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": { "rate": 3.9, "count": 120 }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": { "rate": 4.1, "count": 259 }
  },
  {
    "id": 3,
    "title": "Mens Cotton Jacket",
    "price": 55.99,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
    "rating": { "rate": 4.7, "count": 500 }
  },
  {
    "id": 4,
    "title": "Mens Casual Slim Fit",
    "price": 15.99,
    "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png",
    "rating": { "rate": 2.1, "count": 430 }
  },
  {
    "id": 5,
    "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
    "price": 695,
    "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
    "category": "jewelery",
    "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png",
    "rating": { "rate": 4.6, "count": 400 }
  }]


#mock side effects

@patch('requests.get')
def test_get_requests(mock_get, client,products):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = products


@patch('pipeline.api_client.requests.get')
def test_get_products_side_effect(mock_get, client, products):
    # first response: returns product list
    resp1 = MagicMock()
    resp1.status_code = 200
    resp1.json.return_value = products
    resp1.raise_for_status = Mock()

    # second response: returns empty list
    resp2 = MagicMock()
    resp2.status_code = 200
    resp2.json.return_value = []
    resp2.raise_for_status = Mock()

    # simulate two successive calls
    mock_get.side_effect = [resp1, resp2]

    # first call -> products
    result1 = client.get_all_products()
    assert isinstance(result1, list)
    assert len(result1) == len(products)

    # second call -> empty list
    result2 = client.get_all_products()
    assert result2 == []

    # ensure requests.get was called twice
    assert mock_get.call_count == 2

@patch('requests.get')
def test_get_products_http_error(mock_get, client):
    """Tests how the client handles an HTTP 404 Not Found error."""
    # Arrange: Configure the mock to simulate an HTTP error
    mock_response = MagicMock()
    mock_response.status_code = 404
    # Configure raise_for_status to raise an exception, just like the real one would
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Client Error: Not Found"
    )
    mock_get.return_value = mock_response

    # Act: Call the method
    products_data = client.get_all_products()

    # Assert: Check that the method returns None as per our error handling logic
    assert products_data is None
    mock_get.assert_called_once_with("https://fakeapi.com/products")

