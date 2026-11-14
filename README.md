# 📄 ATS Resume Checker

A Streamlit app that estimates how well a resume would perform in an Applicant Tracking System (ATS) and tells you exactly how to improve it. Powered by Google's Gemini Flash model.

## Features

- Upload a resume as **PDF, DOCX or TXT**
- Optional: paste a **job description** to check how well your resume matches it
- Overall **ATS score (0-100)** with a breakdown:
  - Keyword relevance (30%)
  - Impact & achievements (25%)
  - Structure & sections (20%)
  - Formatting & ATS readability (15%)
  - Language & clarity (10%)
- Strengths, critical issues and missing keywords
- Section-by-section improvement tips and example bullet rewrites
- Download the report as a text file

> The score is an AI-based estimate. Real ATS software varies by company, so treat it as guidance, not a guarantee.

## Project structure

```
ats-resume-checker/
├── app.py
├── requirements.txt
└── README.md
```

## Run locally

1. Install Python 3.10 or newer.
2. Get a free Gemini API key at https://aistudio.google.com/apikey
3. Open a terminal in the project folder and run:

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

4. Provide your API key. Pick **one** option:

   - **Environment variable**
     - Windows (PowerShell): `$env:GEMINI_API_KEY="your_key_here"`
     - macOS / Linux: `export GEMINI_API_KEY="your_key_here"`
   - **Streamlit secrets file**: create `.streamlit/secrets.toml` containing:
     ```toml
     GEMINI_API_KEY = "your_key_here"
     ```
   - Or simply paste the key into the app's sidebar when it runs.

5. Start the app:

```bash
streamlit run app.py
```

## Push to GitHub

Never upload your API key. Create a `.gitignore` file first:

```
venv/
__pycache__/
.streamlit/secrets.toml
```

Then:

1. Create a new **empty** repository on https://github.com/new (for example `ats-resume-checker`). Do not add a README there.
2. In your project folder run:

```bash
git init
git add .
git commit -m "Initial commit: ATS Resume Checker"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ats-resume-checker.git
git push -u origin main
```

If GitHub asks for a password, use a **Personal Access Token** (GitHub > Settings > Developer settings > Personal access tokens) instead of your account password.

## Deploy on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** and choose **Deploy a public app from GitHub**.
3. Select your repository, branch `main`, and main file path `app.py`.
4. Open **Advanced settings** and paste this into **Secrets**:

```toml
GEMINI_API_KEY = "your_key_here"
```

5. Click **Deploy**. After a minute or two you get a public link like `https://your-app-name.streamlit.app`.

Any later `git push` to `main` redeploys automatically.

## Troubleshooting

| Problem | Fix |
|---|---|
| "Almost no text could be extracted" | Your resume is probably a scanned image. Export it as a text-based PDF or DOCX. |
| Gemini request failed | Check the API key, your internet connection and your free-tier quota. |
| Model not found error | Google may have renamed the model. Update `MODEL_NAME` at the top of `app.py`. |
| App crashes on Streamlit Cloud | Open **Manage app > Logs** and confirm all packages are in `requirements.txt`. |

## Privacy

Resume text is sent to the Gemini API for analysis and is not stored by this app. Avoid uploading documents you are not comfortable sharing with Google's API.
