#!/usr/bin/env python3
"""
mkwd - Make Web Development Project
A CLI tool to scaffold professional web development projects

Usage:
    mkwd <project_name> [--type=<type>]

Options:
    --type=<type>    Project type: portfolio, api, fullstack [default: portfolio]

Examples:
    mkwd my_portfolio
    mkwd my_api --type=api
    mkwd my_app --type=fullstack
"""

import os
import sys
from pathlib import Path
from typing import Dict, List
import argparse

class ProjectScaffolder:
    """Generate professional project structures"""
    
    def __init__(self, project_name: str, project_type: str = "portfolio"):
        self.project_name = project_name
        self.project_type = project_type
        self.project_root = Path.cwd() / project_name
        
    def create(self):
        """Create the entire project structure"""
        print(f"🚀 Creating {self.project_type} project: {self.project_name}")
        
        if self.project_root.exists():
            print(f"❌ Error: Directory '{self.project_name}' already exists!")
            sys.exit(1)
        
        # Create structure based on type
        if self.project_type == "portfolio":
            self._create_portfolio_structure()
        elif self.project_type == "api":
            self._create_api_structure()
        elif self.project_type == "fullstack":
            self._create_fullstack_structure()
        else:
            print(f"❌ Unknown project type: {self.project_type}")
            sys.exit(1)
        
        print(f"\n✅ Project '{self.project_name}' created successfully!")
        print(f"\n📂 Location: {self.project_root}")
        print("\n🎯 Next steps:")
        print(f"   cd {self.project_name}")
        print("   python -m venv venv")
        print("   source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
        print("   pip install -r requirements.txt")
        print("   python app/main.py")
        
    def _create_portfolio_structure(self):
        """Create portfolio project structure"""
        
        # Define the complete structure
        structure = {
            "app": {
                "__init__.py": self._get_app_init(),
                "main.py": self._get_main_py(),
                "config.py": self._get_config_py(),
                "dependencies.py": "",
                
                "api": {
                    "__init__.py": "",
                    "routes": {
                        "__init__.py": "",
                        "pages.py": self._get_pages_routes(),
                        "chatbot.py": self._get_chatbot_routes(),
                        "email.py": self._get_email_routes(),
                        "contact.py": self._get_contact_routes(),
                        "analytics.py": self._get_analytics_routes(),
                    },
                    "middleware": {
                        "__init__.py": "",
                        "analytics.py": self._get_analytics_middleware(),
                        "security.py": self._get_security_middleware(),
                        "error.py": "",
                    }
                },
                
                "core": {
                    "__init__.py": "",
                    "graphrag.py": "# Your GraphRAG implementation goes here",
                    "document_processor.py": "# Your document processor goes here",
                    "knowledgegraph.py": "# Your knowledge graph goes here",
                    "queryengine.py": "# Your query engine goes here",
                    "email_generator.py": "# Your email generator goes here",
                },
                
                "database": {
                    "__init__.py": "",
                    "models.py": self._get_models_py(),
                    "connection.py": self._get_connection_py(),
                    "crud.py": "# CRUD operations go here",
                },
                
                "utils": {
                    "__init__.py": "",
                    "session.py": "",
                    "validators.py": "",
                }
            },
            
            "static": {
                "css": {
                    "base.css": self._get_base_css(),
                    "components.css": "",
                    "utils.css": "",
                    "pages": {
                        "home.css": "",
                        "portfolio.css": "",
                        "chatbot.css": "",
                        "contact.css": "",
                    }
                },
                "js": {
                    "main.js": self._get_main_js(),
                    "components": {
                        "navbar.js": "",
                        "footer.js": "",
                        "typing-effect.js": "",
                    },
                    "pages": {
                        "chatbot.js": "",
                        "email.js": "",
                        "contact.js": "",
                    }
                },
                "img": {
                    "logo": {},
                    "projects": {},
                    "backgrounds": {},
                }
            },
            
            "templates": {
                "base.html": self._get_base_template(),
                "components": {
                    "navbar.html": self._get_navbar_component(),
                    "footer.html": self._get_footer_component(),
                    "project-card.html": "",
                },
                "pages": {
                    "home.html": self._get_home_page(),
                    "about.html": "",
                    "portfolio.html": "",
                    "chatbot.html": "",
                    "email-generator.html": "",
                    "project-details": {
                        "cancer-prediction.html": "",
                        "cold-email.html": "",
                        "object-detection.html": "",
                    }
                }
            },
            
            "tests": {
                "__init__.py": "",
                "test_api.py": "",
                "test_database.py": "",
                "test_ml.py": "",
            },
            
            "alembic": {
                "versions": {},
                "env.py": "",
            }
        }
        
        # Create all directories and files
        self._build_structure(self.project_root, structure)
        
        # Create root-level files
        self._create_file(self.project_root / ".env.example", self._get_env_example())
        self._create_file(self.project_root / ".gitignore", self._get_gitignore())
        self._create_file(self.project_root / "requirements.txt", self._get_requirements())
        self._create_file(self.project_root / "README.md", self._get_readme())
        self._create_file(self.project_root / "Dockerfile", self._get_dockerfile())
        self._create_file(self.project_root / "docker-compose.yml", self._get_docker_compose())
        self._create_file(self.project_root / "run.py", self._get_run_py())
        
    def _create_api_structure(self):
        """Create API-only project structure"""
        structure = {
            "app": {
                "__init__.py": "",
                "main.py": self._get_main_py(),
                "config.py": self._get_config_py(),
                "api": {
                    "__init__.py": "",
                    "routes": {
                        "__init__.py": "",
                        "users.py": "",
                        "auth.py": "",
                    }
                },
                "database": {
                    "__init__.py": "",
                    "models.py": "",
                    "connection.py": self._get_connection_py(),
                }
            },
            "tests": {
                "__init__.py": "",
                "test_api.py": "",
            }
        }
        
        self._build_structure(self.project_root, structure)
        self._create_file(self.project_root / ".env.example", self._get_env_example())
        self._create_file(self.project_root / ".gitignore", self._get_gitignore())
        self._create_file(self.project_root / "requirements.txt", self._get_requirements())
        self._create_file(self.project_root / "README.md", self._get_readme())
        
    def _create_fullstack_structure(self):
        """Create full-stack project with frontend framework"""
        # Combine portfolio structure with additional frontend tooling
        self._create_portfolio_structure()
        
    def _build_structure(self, base_path: Path, structure: Dict):
        """Recursively build directory structure"""
        for name, content in structure.items():
            path = base_path / name
            
            if isinstance(content, dict):
                # It's a directory
                path.mkdir(parents=True, exist_ok=True)
                self._build_structure(path, content)
            else:
                # It's a file
                path.parent.mkdir(parents=True, exist_ok=True)
                self._create_file(path, content)
    
    def _create_file(self, filepath: Path, content: str):
        """Create a file with content"""
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  ✓ Created: {filepath.relative_to(self.project_root)}")
    
    # ========== TEMPLATE CONTENT METHODS ==========
    
    def _get_app_init(self):
        return '"""Portfolio Application Package"""\n__version__ = "1.0.0"\n'
    
    def _get_main_py(self):
        return '''"""
Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from app.config import settings
from app.database.connection import init_db
from app.api.routes import pages, chatbot, email, contact, analytics
from app.api.middleware.analytics import AnalyticsMiddleware
from app.api.middleware.security import SecurityHeadersMiddleware

def create_app() -> FastAPI:
    """Application factory"""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        docs_url="/api/docs" if settings.DEBUG else None,
    )
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Custom Middleware
    app.add_middleware(AnalyticsMiddleware)
    app.add_middleware(SecurityHeadersMiddleware)
    
    # Static Files
    app.mount(
        "/static",
        StaticFiles(directory=Path(__file__).parent.parent / "static"),
        name="static"
    )
    
    # Routes
    app.include_router(pages.router, tags=["Pages"])
    app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot"])
    app.include_router(email.router, prefix="/api/v1/email", tags=["Email"])
    app.include_router(contact.router, prefix="/api/v1/contact", tags=["Contact"])
    app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
    
    @app.on_event("startup")
    async def startup():
        init_db()
        print(f"🚀 {settings.PROJECT_NAME} started!")
    
    @app.get("/health")
    async def health():
        return {"status": "healthy"}
    
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=settings.DEBUG)
'''
    
    def _get_config_py(self):
        return '''"""Configuration Management"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Portfolio"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "change-me-in-production"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:8080"]
    
    OPENAI_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    WEBHOOK_URL: str = ""
    
    ENABLE_ANALYTICS: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
'''
    
    def _get_models_py(self):
        return '''"""Database Models"""
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class ContactMessage(Base):
    __tablename__ = 'contact_messages'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    submitted_at = Column(DateTime, default=func.now())
    read = Column(Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'submitted_at': self.submitted_at.isoformat()
        }

class Visitor(Base):
    __tablename__ = 'visitors'
    
    id = Column(Integer, primary_key=True)
    ip_hash = Column(String(64))
    page = Column(String(200))
    timestamp = Column(DateTime, default=func.now())
'''
    
    def _get_connection_py(self):
        return '''"""Database Connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

def init_db():
    from app.database.models import Base
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")
'''
    
    def _get_pages_routes(self):
        return '''"""Page Routes"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("pages/home.html", {
        "request": request,
        "title": "Home"
    })
'''
    
    def _get_chatbot_routes(self):
        return '''"""Chatbot Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
async def upload_pdf():
    return {"message": "Upload endpoint - implement your logic here"}

@router.post("/query")
async def query_pdf():
    return {"message": "Query endpoint - implement your logic here"}
'''
    
    def _get_email_routes(self):
        return '''"""Email Generator Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
async def generate_email():
    return {"message": "Email generation - implement your logic here"}
'''
    
    def _get_contact_routes(self):
        return '''"""Contact Form Routes"""
from fastapi import APIRouter, Request, Body
from app.database.models import ContactMessage
from app.database.connection import get_db

router = APIRouter()

@router.post("/message")
async def submit_contact(request: Request, payload: dict = Body(...)):
    with get_db() as db:
        msg = ContactMessage(
            name=payload['name'],
            email=payload['email'],
            message=payload['message']
        )
        db.add(msg)
    return {"status": "success"}
'''
    
    def _get_analytics_routes(self):
        return '''"""Analytics Routes"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")
async def get_analytics():
    return {"message": "Analytics - implement your logic here"}
'''
    
    def _get_analytics_middleware(self):
        return '''"""Analytics Middleware"""
from starlette.middleware.base import BaseHTTPMiddleware
from app.database.models import Visitor
from app.database.connection import get_db
import hashlib

class AnalyticsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        
        if not request.url.path.startswith('/static'):
            try:
                ip_hash = hashlib.sha256(request.client.host.encode()).hexdigest()
                with get_db() as db:
                    visitor = Visitor(ip_hash=ip_hash, page=request.url.path)
                    db.add(visitor)
            except:
                pass
        
        return response
'''
    
    def _get_security_middleware(self):
        return '''"""Security Headers Middleware"""
from starlette.middleware.base import BaseHTTPMiddleware

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response
'''
    
    def _get_base_css(self):
        return '''/* Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --text-color: #333;
    --bg-color: #ffffff;
    --transition: all 0.3s ease;
}

body {
    font-family: 'Poppins', sans-serif;
    color: var(--text-color);
    background-color: var(--bg-color);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
'''
    
    def _get_main_js(self):
        return '''// Main JavaScript
console.log('Portfolio loaded!');

// Add your global JavaScript here
'''
    
    def _get_base_template(self):
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ title }}{% endblock %}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', path='css/base.css') }}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    {% include 'components/navbar.html' %}
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    {% include 'components/footer.html' %}
    
    <script src="{{ url_for('static', path='js/main.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
'''
    
    def _get_navbar_component(self):
        return '''<nav class="navbar">
    <div class="container">
        <div class="logo">MyPortfolio</div>
        <ul class="nav-links">
            <li><a href="/">Home</a></li>
            <li><a href="/portfolio">Portfolio</a></li>
            <li><a href="/chatbot">Chatbot</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </div>
</nav>
'''
    
    def _get_footer_component(self):
        return '''<footer class="footer">
    <div class="container">
        <p>&copy; 2024 MyPortfolio. All rights reserved.</p>
    </div>
</footer>
'''
    
    def _get_home_page(self):
        return '''{% extends "base.html" %}

{% block content %}
<div class="hero">
    <div class="container">
        <h1>Welcome to My Portfolio</h1>
        <p>Data Scientist | ML Engineer | Problem Solver</p>
    </div>
</div>
{% endblock %}
'''
    
    def _get_env_example(self):
        return '''# Application
PROJECT_NAME="My Portfolio"
ENVIRONMENT=development
DEBUG=true

# Database
DATABASE_URL=sqlite:///./app.db

# Security
SECRET_KEY=your-secret-key-here

# API Keys
OPENAI_API_KEY=
GROQ_API_KEY=

# Webhooks
WEBHOOK_URL=

# CORS
ALLOWED_ORIGINS=http://localhost:8080
'''
    
    def _get_gitignore(self):
        return '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
*.egg-info/
dist/
build/

# Database
*.db
*.db-journal
*.sqlite
*.sqlite3

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Cache
.cache/
.pytest_cache/
'''
    
    def _get_requirements(self):
        return '''# Core
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6
jinja2==3.1.3
python-dotenv==1.0.0
pydantic-settings==2.1.0

# Database
sqlalchemy==2.0.25
alembic==1.13.1

# Utilities
httpx==0.26.0
requests==2.31.0

# Testing
pytest==7.4.4
pytest-asyncio==0.23.3
'''
    
    def _get_readme(self):
        return f'''# {self.project_name}

Professional web application built with FastAPI.

## Quick Start

```bash
# Setup
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your settings

# Run
python app/main.py
```

Visit: http://localhost:8080

## Features

- ✅ Modern FastAPI backend
- ✅ SQLAlchemy database integration
- ✅ Professional project structure
- ✅ Analytics tracking
- ✅ API documentation at /api/docs

## Project Structure

```
{self.project_name}/
├── app/           # Application code
├── static/        # Static assets
├── templates/     # HTML templates
├── tests/         # Tests
└── alembic/       # Database migrations
```

## Development

```bash
# Run with auto-reload
python app/main.py

# Run tests
pytest

# Database migrations
alembic revision --autogenerate -m "description"
alembic upgrade head
```
'''
    
    def _get_dockerfile(self):
        return '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app/main.py"]
'''
    
    def _get_docker_compose(self):
        return '''version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=sqlite:///./app.db
    volumes:
      - .:/app
'''
    
    def _get_run_py(self):
        return '''"""Development server runner"""
import uvicorn
from app.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=settings.DEBUG,
        log_level="info"
    )
'''

def main():
    parser = argparse.ArgumentParser(
        description="Make Web Development Project - Scaffold professional web projects"
    )
    parser.add_argument("project_name", help="Name of the project to create")
    parser.add_argument(
        "--type",
        choices=["portfolio", "api", "fullstack"],
        default="portfolio",
        help="Type of project to create (default: portfolio)"
    )
    
    args = parser.parse_args()
    
    scaffolder = ProjectScaffolder(args.project_name, args.type)
    scaffolder.create()


    

if __name__ == "__main__":
    main()