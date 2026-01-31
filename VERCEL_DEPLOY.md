# Vercel Deployment for DriveX

## Quick Setup

1. **Install Vercel CLI** (optional, or use web dashboard):
```bash
npm i -g vercel
```

2. **Deploy**:
```bash
vercel
```

## Environment Variables to Set in Vercel Dashboard

After deployment, add these in Vercel Project Settings → Environment Variables:

- `SECRET_KEY`: Generate a new Django secret key
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `.vercel.app`
- `DATABASE_URL`: Your PostgreSQL database URL (use Vercel Postgres or external)

## Database Options

### Option 1: Vercel Postgres (Recommended)
- Go to Vercel Dashboard → Storage → Create Database → Postgres
- It will automatically add `DATABASE_URL` to your environment variables

### Option 2: External Database
- Use [Neon](https://neon.tech) (free PostgreSQL)
- Or [Supabase](https://supabase.com) (free PostgreSQL)
- Add the connection string as `DATABASE_URL`

### Option 3: SQLite (Development Only)
- Don't set `DATABASE_URL`
- Will use SQLite (not recommended for production)

## After Deployment

Run migrations using Vercel CLI:
```bash
vercel env pull .env.local
python manage.py migrate
```

Or create a migration script in Vercel dashboard.
