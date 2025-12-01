# GitHub Setup Guide for Tune Dashboard

## Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `tune-dashboard` (or any name you prefer)
4. Description: "🎵 Tune Dashboard – JioSaavn & Wynk - Music streaming analytics dashboard"
5. Make it **Public** (required for free Streamlit Cloud deployment)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click **"Create repository"**

## Step 2: Copy Your Repository URL

After creating the repository, GitHub will show you a URL like:
```
https://github.com/YOUR_USERNAME/tune-dashboard.git
```

Copy this URL - you'll need it in Step 4.

## Step 3: Run These Commands (Already Done Below)

The commands below will:
- Add all files to git
- Create initial commit
- Connect to your GitHub repository
- Push everything to GitHub

## Step 4: Connect and Push

After creating the GitHub repository, run:
```bash
git remote add origin https://github.com/YOUR_USERNAME/tune-dashboard.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 5: Verify

Go to your GitHub repository page and you should see all your files!

## Next Steps: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `tune-dashboard`
5. Main file path: `app.py`
6. Click "Deploy!"

Your app will be live at: `https://YOUR_APP_NAME.streamlit.app`

