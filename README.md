# 🔎 AI App Finder

A Streamlit app where you describe what you want to do and get a list of AI tools that fit, powered by Google's Gemini Flash model.

## Features

- Describe your goal in plain words (or click an example)
- Filter by **budget** and **category**
- Choose how many tools to see (3 to 8)
- Each result shows: description, best use case, pricing, pros, cons and an official link
- Download the recommendations as a text file

> Suggestions come from an AI model and can be outdated. Always check pricing and features on the official website.

## Project structure

```
ai-app-finder/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally

1. Install Python 3.10 or newer.
2. Get a free Gemini API key at https://aistudio.google.com/apikey
3. In the project folder run:

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

4. Give the app your API key (pick one):
   - Environment variable: `export GEMINI_API_KEY="your_key"` (PowerShell: `$env:GEMINI_API_KEY="your_key"`)
   - Or create `.streamlit/secrets.toml` with:
     ```toml
     GEMINI_API_KEY = "your_key"
     ```
   - Or paste the key into the app's sidebar.

5. Start the app:

```bash
streamlit run app.py
```

## Push to GitHub

The included `.gitignore` keeps your API key out of GitHub.

1. Create a new **empty** repository on https://github.com/new (for example `ai-app-finder`).
2. In your project folder run:

```bash
git init
git add .
git commit -m "Initial commit: AI App Finder"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-app-finder.git
git push -u origin main
```

If GitHub asks for a password, use a Personal Access Token instead.

You can also upload the files with **Add file > Upload files** on the GitHub website. Make sure `app.py` and `requirements.txt` sit in the **root** of the repository, not inside a subfolder.

## Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** > **Deploy a public app from GitHub**.
3. Choose your repository, branch `main`, main file `app.py`.
4. In **Advanced settings**, paste into **Secrets**:

```toml
GEMINI_API_KEY = "your_key"
```

5. Click **Deploy**. Later `git push` updates redeploy automatically.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` on Streamlit Cloud | Check `requirements.txt` is in the repo root and spelled exactly right, then **Manage app > Reboot app**. |
| Gemini request failed | Check the API key, your internet connection and your free-tier quota. |
| Model not found | Google may have renamed the model. Update `MODEL_NAME` at the top of `app.py`. |
| A link goes to a Google search | The AI gave an invalid URL, so the app safely falls back to a search for that tool. |
