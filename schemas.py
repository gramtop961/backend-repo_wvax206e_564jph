"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogpost" collection
- Project -> "project" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

class Project(BaseModel):
    """Portfolio projects
    Collection: "project"
    """
    title: str = Field(..., description="Project title")
    summary: str = Field(..., description="Short description")
    tags: List[str] = Field(default_factory=list, description="Tech stack / tags")
    repo_url: Optional[HttpUrl] = Field(None, description="Git repository URL")
    demo_url: Optional[HttpUrl] = Field(None, description="Live demo URL")
    featured: bool = Field(False, description="Mark as featured")

class BlogPost(BaseModel):
    """Blog posts
    Collection: "blogpost"
    """
    title: str = Field(..., description="Post title")
    slug: str = Field(..., description="URL slug")
    excerpt: str = Field(..., description="Short summary")
    content: Optional[str] = Field(None, description="Markdown content")
    tags: List[str] = Field(default_factory=list, description="Tags")
    cover_image: Optional[HttpUrl] = Field(None, description="Cover image URL")
    published: bool = Field(True, description="Is published")

# Note: The Flames database viewer may read these via /schema endpoint
