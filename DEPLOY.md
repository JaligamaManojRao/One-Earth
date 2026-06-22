# Deploy One Earth to the Internet

This guide publishes the site so **anyone with the link** can use it.

**Stack:** Frontend on [Vercel](https://vercel.com) (free) · Backend on [Render](https://render.com) (free tier)

---

## Before you start

1. Push this project to **GitHub** (create a repo and push).
2. You will get two public URLs:
   - Frontend: `https://your-app.vercel.app`
   - Backend API: `https://one-earth-api.onrender.com` (example)

---

## Step 1 — Deploy the backend (Render)

1. Go to [render.com](https://render.com) and sign in with GitHub.
2. Click **New → Blueprint**.
3. Connect your GitHub repo and select the **One Earth** repository.
4. Render reads `backend/render.yaml` and creates:
   - A **Web Service** (`one-earth-api`)
   - A **PostgreSQL** database (`one-earth-db`)
5. When prompted for **CORS_ORIGINS**, enter your Vercel URL (you can update this after Step 2):

   ```
   https://your-app.vercel.app
   ```

   Add a comma-separated list if you use a custom domain later:

   ```
   https://your-app.vercel.app,https://www.yourdomain.com
   ```

6. Click **Apply**. Wait for the deploy to finish (~5 minutes on first build).
7. Copy your API URL from the Render dashboard, e.g.:

   ```
   https://one-earth-api.onrender.com
   ```

8. Test it in a browser:

   ```
   https://one-earth-api.onrender.com/health
   ```

   You should see: `{"status":"healthy","service":"One Earth API"}`

> **Note:** Render free tier spins down after inactivity. The first request after sleep may take ~30 seconds.

---

## Step 2 — Deploy the frontend (Vercel)

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub.
2. Click **Add New → Project** and import your repo.
3. Configure the project:

   | Setting | Value |
   |---------|--------|
   | **Root Directory** | `frontend` |
   | **Framework Preset** | Next.js (auto-detected) |

4. Add an **Environment Variable**:

   | Name | Value |
   |------|--------|
   | `NEXT_PUBLIC_API_URL` | `https://one-earth-api.onrender.com` |

   Use your actual Render API URL from Step 1.

5. Click **Deploy**. Wait for the build to finish.
6. Copy your Vercel URL, e.g. `https://one-earth.vercel.app`.

---

## Step 3 — Connect frontend and backend

1. Go back to **Render → one-earth-api → Environment**.
2. Set **CORS_ORIGINS** to your live Vercel URL:

   ```
   https://one-earth.vercel.app
   ```

3. Save and let Render redeploy (or click **Manual Deploy**).
4. Open your Vercel URL and test:
   - Home page loads
   - **Species** page shows data
   - **Stories** page loads
   - **Identify** upload works

---

## Step 4 — Custom domain (optional)

### Vercel (frontend)

1. Vercel project → **Settings → Domains**
2. Add your domain (e.g. `oneearth.com`)
3. Follow DNS instructions from Vercel

### Render (backend)

1. Render service → **Settings → Custom Domains**
2. Add e.g. `api.oneearth.com`

### Update environment variables

After adding domains, update both sides:

**Vercel** — if API has a custom domain:

```
NEXT_PUBLIC_API_URL=https://api.oneearth.com
```

**Render** — add all frontend origins:

```
CORS_ORIGINS=https://oneearth.com,https://www.oneearth.com,https://your-app.vercel.app
```

Redeploy both services after changing env vars.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Species/Stories show an error | Check `NEXT_PUBLIC_API_URL` on Vercel matches your Render URL |
| CORS error in browser console | Add your exact Vercel URL to `CORS_ORIGINS` on Render |
| API slow on first load | Render free tier cold start — normal |
| Build fails on Render | Ensure **Root Directory** is `backend` if not using Blueprint |

---

## Alternative: Docker

Build and run the backend anywhere that supports Docker:

```bash
cd backend
docker build -t one-earth-api .
docker run -p 8000:8000 \
  -e CORS_ORIGINS=https://your-app.vercel.app \
  -e DATABASE_URL=sqlite:///./one_earth.db \
  one-earth-api
```

For production, use PostgreSQL instead of SQLite.

---

## Quick checklist

- [ ] Code pushed to GitHub
- [ ] Render backend deployed, `/health` returns OK
- [ ] Vercel frontend deployed with `NEXT_PUBLIC_API_URL` set
- [ ] `CORS_ORIGINS` on Render includes Vercel URL
- [ ] Species and Stories pages work on the live site

Your public link to share is your **Vercel URL**.
