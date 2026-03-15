# mkwd — Make Web Development Project

> **CLI scaffolding tool that generates a production-ready FastAPI project in one command.**  
> 60+ files · GraphRAG · SQLAlchemy · Docker · Tests · Analytics middleware · Ready to run

---

## Why This Exists

Starting a new FastAPI project from scratch means 30+ minutes of boilerplate — folder structure, database setup, middleware, templates, static files, Docker config, test stubs. Every time.

`mkwd` does all of that in under 3 seconds.

```bash
$ mkwd my_project
🚀 Creating portfolio project: my_project
  ✓ Created: app/main.py
  ✓ Created: app/core/graphrag.py
  ✓ Created: app/database/models.py
  ✓ Created: Dockerfile
  ... 60+ files
✅ Project 'my_project' created successfully!
🎯 Next steps:
   cd my_project
   python -m venv venv
   pip install -r requirements.txt
   python app/main.py
```

---

## Installation

```bash
pip install git+https://github.com/DebugJedi/mkwd.git
```

---

## Usage

```bash
mkwd my_project              # Full portfolio/web app (default)
mkwd my_api --type=api       # API-only project
mkwd my_app --type=fullstack # Full-stack project
```

---

## What Gets Generated

Running `mkwd my_project` produces a fully structured FastAPI application:

```
my_project/
├── app/
│   ├── main.py                        ← FastAPI app entry point
│   ├── config.py                      ← Settings and environment config
│   ├── dependencies.py                ← Dependency injection
│   ├── api/
│   │   ├── routes/
│   │   │   ├── pages.py               ← Page routing
│   │   │   ├── chatbot.py             ← Chatbot endpoint
│   │   │   ├── email.py               ← Email routes
│   │   │   ├── contact.py             ← Contact form
│   │   │   └── analytics.py           ← Analytics routes
│   │   └── middleware/
│   │       ├── analytics.py           ← Request tracking middleware
│   │       ├── security.py            ← Security middleware
│   │       └── error.py               ← Error handling middleware
│   ├── core/
│   │   ├── graphrag.py                ← GraphRAG integration
│   │   ├── document_processor.py      ← Document ingestion
│   │   ├── knowledgegraph.py          ← Knowledge graph logic
│   │   ├── queryengine.py             ← Query engine
│   │   └── email_generator.py         ← Email generation
│   ├── database/
│   │   ├── models.py                  ← SQLAlchemy models
│   │   ├── connection.py              ← DB connection management
│   │   └── crud.py                    ← CRUD operations
│   └── utils/
│       ├── session.py                 ← Session utilities
│       └── validators.py              ← Input validators
├── static/
│   ├── css/
│   │   ├── base.css · components.css · utils.css
│   │   └── pages/  ← home · portfolio · chatbot · contact
│   └── js/
│       ├── main.js
│       ├── components/  ← navbar · footer · typing-effect
│       └── pages/       ← chatbot · email · contact
├── templates/
│   ├── base.html
│   ├── components/  ← navbar · footer · project-card
│   └── pages/       ← home · about · portfolio · chatbot
│       └── project-details/
├── tests/
│   ├── test_api.py
│   ├── test_database.py
│   └── test_ml.py
├── alembic/env.py                     ← DB migration setup
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
└── run.py
```

**Total: 60+ files generated instantly.**

---

## What's Included Out of the Box

| Feature | Details |
|---|---|
| **FastAPI backend** | Full app with routing, middleware, dependency injection |
| **GraphRAG core** | Document processor, knowledge graph, query engine stubs |
| **Database layer** | SQLAlchemy models, CRUD operations, Alembic migrations |
| **Analytics middleware** | Request tracking built in from day one |
| **Security middleware** | Auth and security headers pre-wired |
| **Jinja2 templates** | Base layout, components, and page templates |
| **Static assets** | Organized CSS and JS with per-page structure |
| **Test stubs** | API, database, and ML test files ready to fill in |
| **Docker** | `Dockerfile` + `docker-compose.yml` included |
| **Environment config** | `.env.example` with all required variables listed |

---

## Quick Start After Scaffolding

```bash
# Navigate into your new project
cd my_project

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your settings

# Run database migrations
alembic upgrade head

# Start the app
python app/main.py
# → http://localhost:8000
# → http://localhost:8000/docs  (auto-generated API docs)
```

---

## Why FastAPI + This Structure

This scaffold follows the same architecture pattern used across production ML-serving APIs and portfolio deployments. The separation of `core/` (business logic), `api/` (routing + middleware), and `database/` (persistence) makes it easy to add ML model serving, RAG pipelines, or external API integrations without restructuring.

The GraphRAG stubs in `app/core/` are particularly useful if you're building document intelligence or knowledge graph applications on top of the web layer.

---

## Roadmap

- [x] Portfolio / web app template
- [x] API-only template (`--type=api`)
- [x] Full-stack template (`--type=fullstack`)
- [ ] Publish to PyPI (`pip install mkwd`)
- [ ] `--llm` flag — adds LLM/OpenAI integration stubs
- [ ] `--azure` flag — adds Azure Functions + SWA config
- [ ] Interactive mode — prompt-driven project setup

---

## Author

Built and maintained by **Priyank Rao** — Data Scientist / ML Engineer  
[Portfolio](https://priyankrao.co) · [GitHub](https://github.com/DebugJedi)

---

## License

MIT — use it, fork it, build on it.