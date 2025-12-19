# Render Deployment Guide

This guide will help you deploy this ML Pipeline application to Render.

## Prerequisites

1. A GitHub account with this repository
2. A Render account (sign up at https://render.com)

## Deployment Steps

### 1. Prepare Your Repository

Make sure your repository includes:
- ✅ `app.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version specification (Python 3.11.9)
- ✅ `Procfile` - Process file for Render
- ✅ `render.yaml` - Render configuration (optional)
- ✅ `artifacts/` folder with:
  - `model.pkl` - Trained model
  - `preprocessor.pkl` - Preprocessor object
- ✅ `templates/` folder with HTML templates

### 2. Deploy on Render

#### Option A: Using Render Dashboard (Recommended)

1. Go to https://dashboard.render.com
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: ml-pipeline-app (or your preferred name)
   - **Environment**: Python 3
   - **Python Version**: **IMPORTANT** - In the "Advanced" section, set Python version to **3.11.9** (or ensure `runtime.txt` is detected)
   - **Build Command**: `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Instance Type**: Free tier is fine for testing
5. Click "Create Web Service"

**⚠️ CRITICAL**: If you see pandas compilation errors, make sure Python 3.11.9 is selected (not 3.13). The `runtime.txt` file should handle this automatically, but you can verify in the service settings.

#### Option B: Using render.yaml (Blueprints)

1. Go to https://dashboard.render.com
2. Click "New +" and select "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and configure the service

**Note**: If you encounter Python version issues with Blueprints, you can temporarily delete `render.yaml` and use Option A instead. The `runtime.txt` and `Procfile` will be automatically detected.

### 3. Important Notes

- **Artifacts Folder**: Make sure your `artifacts/` folder with `model.pkl` and `preprocessor.pkl` is committed to your repository. If these files are large, consider using Git LFS or storing them in cloud storage.

- **Environment Variables**: No environment variables are required for basic deployment. The PORT is automatically set by Render.

- **Python Version**: The project uses Python 3.11.9 (specified in `runtime.txt`). This ensures compatibility with all ML libraries.

- **Build Time**: The first build may take 5-10 minutes as it installs all dependencies including ML libraries.

- **Health Check**: The app includes a `/health` endpoint that you can use for monitoring.

### 4. Verify Deployment

Once deployed:
1. Visit your Render service URL
2. Test the `/health` endpoint: `https://your-app.onrender.com/health`
3. Test the main application at the root URL

### 5. Troubleshooting

- **Build Fails**: Check the build logs in Render dashboard. Common issues:
  - Missing dependencies in requirements.txt
  - **Python version mismatch**: This is the most common issue. Render may default to Python 3.13 which causes pandas compilation errors. 
    - **Solution**: Go to your service settings → Environment → and manually set Python version to **3.11.9**
    - Or ensure `runtime.txt` is in the root directory with `python-3.11.9`
  - Missing files (artifacts, templates)
  - If you see pandas/Cython compilation errors, it means Python 3.13 is being used. Switch to Python 3.11.9

- **App Crashes**: Check the runtime logs:
  - Pipeline loading errors
  - Missing model files
  - Port binding issues

- **Slow Performance**: Free tier instances may spin down after inactivity. First request after inactivity may take 30-60 seconds.

## File Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version (3.11.9)
├── Procfile              # Process file for Render
├── render.yaml           # Render configuration (optional)
├── artifacts/            # Model and preprocessor files
│   ├── model.pkl
│   └── preprocessor.pkl
├── templates/            # HTML templates
│   ├── index.html
│   └── home.html
└── src/                  # Source code
    └── pipeline/
        └── predict_pipeline.py
```

## Support

For issues specific to:
- **Render Platform**: Check Render documentation at https://render.com/docs
- **Application Code**: Check the application logs in Render dashboard

