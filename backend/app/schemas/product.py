from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., gt=0, description="Pruduct price(must be greater then 0)")
    category_id: int = Field(..., description="Category id")
    image_url: Optional[str] = Field(None, description="Proudct image URL")

class ProductCreate(ProductBase):
    ...
    
class ProductResponse(ProductBase):
    id: int = Field(..., description="Unique product identifier")
    created_at: datetime
    category: CategoryResponse = Field(..., description="Product category details")
    
    class Config:
        form_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")