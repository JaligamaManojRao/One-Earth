# One Earth

A cinematic, production-ready website dedicated to wildlife, biodiversity, conservation, and the natural world — inspired by the environmental legacy of Sir David Attenborough.

## Overview

One Earth is an interactive nature documentary experience built with a modern full-stack architecture:

- **Frontend:** Next.js 15, TypeScript, Tailwind CSS, Framer Motion
- **Backend:** Python FastAPI, SQLite, REST APIs

## Project Structure

```
One Earth/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── routers/             # API route handlers
│   │   │   ├── species.py
│   │   │   ├── stories.py
│   │   │   └── identify.py
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── services/            # Business logic
│   │   └── database/            # DB config & seed data
│   └── requirements.txt
├── frontend/
│   ├── app/                     # Next.js App Router pages
│   │   ├── page.tsx             # Home
│   │   ├── ecosystems/
│   │   ├── species/
│   │   ├── stories/
│   │   ├── identify/
│   │   └── tribute/
│   ├── components/              # Reusable UI components
│   ├── hooks/                   # Custom React hooks
│   ├── lib/                     # API client & static data
│   └── types/                   # TypeScript interfaces
└── README.md
```

## Pages

| Page | Route | Description |
|------|-------|-------------|
| Home | `/` | Hero, ecosystems preview, featured species, challenges, tribute |
| Ecosystems | `/ecosystems` | Rainforests, oceans, grasslands, deserts, polar, mountains |
| Species Explorer | `/species` | Search, filter, pagination with API integration |
| Conservation Stories | `/stories` | Success stories with timelines |
| AI Identifier | `/identify` | Upload image for species identification (mock AI) |
| Tribute | `/tribute` | Sir David Attenborough biography and legacy |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/species` | List species (paginated, filterable) |
| GET | `/species/{id}` | Get species by ID |
| GET | `/species/search?q=` | Search species |
| GET | `/stories` | List conservation stories |
| GET | `/stories/{id}` | Get story by ID |
| POST | `/identify` | Upload image for AI identification |

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.11–3.13 (Python 3.14 is not yet supported by Pydantic/FastAPI)
- npm or yarn

### Backend Setup

**Quick start (macOS/Linux):**

```bash
cd backend
chmod +x start.sh
./start.sh
```

**Manual setup:**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

On macOS, use `python3` (not `python`). Run each line separately — do not paste inline comments like `# first time only` onto the same line as a command.

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

On first startup, the database is automatically created and seeded with 20 species and 6 conservation stories.

### Frontend Setup

**Quick start (macOS/Linux):**

```bash
cd frontend
chmod +x start.sh
./start.sh
```

**Manual setup:**

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

The website will be available at `http://localhost:3000`.

## Features

- Full-screen cinematic hero sections with parallax
- Dark/light mode toggle
- Smooth page transitions (Framer Motion)
- Scroll progress indicator
- Species search, habitat/status filters, pagination
- AI wildlife identifier (mock — ready for real ML model)
- SEO optimization with Open Graph metadata
- Lazy-loaded images via Next.js Image
- Accessibility: ARIA labels, keyboard navigation, reduced motion support
- Mobile-first responsive design

## Design System

| Token | Value | Usage |
|-------|-------|-------|
| Forest Green | `#0B3D2E` | Primary accent |
| Ocean Blue | `#0D3B66` | Secondary accent |
| Earth Brown | `#6B4F3A` | Tertiary accent |
| Warm Sand | `#D9C6A5` | Highlights, CTAs |
| Display Font | Cormorant Garamond | Headings |
| Body Font | Inter | Body text |

## Deployment (share on the internet)

See **[DEPLOY.md](./DEPLOY.md)** for step-by-step instructions to publish on **Vercel + Render** (free).

Quick summary:

1. Push the repo to GitHub
2. Deploy backend with Render using `render.yaml` (repo root)
3. Deploy frontend on Vercel (root directory: `frontend`)
4. Set `NEXT_PUBLIC_API_URL` on Vercel to your Render API URL
5. Set `CORS_ORIGINS` on Render to your Vercel site URL

Share your **Vercel URL** with anyone — e.g. `https://one-earth.vercel.app`

### Environment variables

| Service | Variable | Example |
|---------|----------|---------|
| Vercel | `NEXT_PUBLIC_API_URL` | `https://one-earth-api.onrender.com` |
| Render | `CORS_ORIGINS` | `https://one-earth.vercel.app` |
| Render | `DATABASE_URL` | Auto-set by Render PostgreSQL |

### Docker (optional)

```bash
cd backend
docker build -t one-earth-api .
docker run -p 8000:8000 \
  -e CORS_ORIGINS=https://your-app.vercel.app \
  one-earth-api
```

## Extending the AI Identifier

The current `/identify` endpoint uses a deterministic mock based on image hash. To integrate a real model:

1. Replace logic in `backend/app/services/identify_service.py`
2. Add model weights to `backend/app/services/models/`
3. Use Pillow to preprocess uploaded images
4. Return predictions via the existing `IdentifyResponse` schema

## License

Built for educational and conservation awareness purposes. Wildlife images courtesy of [Unsplash](https://unsplash.com) contributors.
