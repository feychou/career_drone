---
title: career_drone
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---

# career_drone

A Gradio career-profile chatbot for Hugging Face Spaces.

## Local Setup

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
uv run app.py
```

## Hugging Face Space

Create a new Hugging Face Space with:

- **Space SDK:** Gradio
- **Space name:** `career_drone`
- **App file:** `app.py`

Then add these Space secrets in **Settings > Variables and secrets**:

- `OPENAI_API_KEY`
- `PUSHOVER_TOKEN`
- `PUSHOVER_USER`

## GitHub Sync

This repository includes a GitHub Actions workflow that syncs `main` to Hugging Face whenever you push.

In your GitHub repo, add:

- A repository secret named `HF_TOKEN` with a Hugging Face token that has write access to the Space.
