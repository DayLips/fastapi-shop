from .products import router as products_router
from .cart import router as carts_router
from .categories import router as categories_router

__all__ = ['products_router', 'carts_router', 'categories_router']