#!/usr/bin/env python3
"""
Startup script for the E-Commerce Backend
This script will start the Django development server
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Main function to start the server"""
    print("Starting E-Commerce Backend Server...")
    print("=" * 50)
    
    # Check if we're in the correct directory
    if not Path("manage.py").exists():
        print("Error: manage.py not found. Please run this script from the backend directory.")
        sys.exit(1)
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Warning: Virtual environment not detected. It's recommended to use a virtual environment.")
        print("To create and activate a virtual environment:")
        print("  python -m venv venv")
        print("  venv\\Scripts\\activate  # Windows")
        print("  source venv/bin/activate  # macOS/Linux")
        print()
    
    # Check if requirements are installed
    try:
        import django
        import rest_framework
        import rest_framework_simplejwt
        print("✓ All required packages are installed")
    except ImportError as e:
        print(f"✗ Missing required package: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        sys.exit(1)
    
    # Run migrations
    print("Running database migrations...")
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        print("✓ Migrations completed successfully")
    except subprocess.CalledProcessError:
        print("✗ Migration failed")
        sys.exit(1)
    
    # Start the server
    print("\nStarting Django development server...")
    print("Server will be available at: http://localhost:8000")
    print("API endpoints will be available at: http://localhost:8000/api/")
    print("Admin interface will be available at: http://localhost:8000/admin/")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        subprocess.run([sys.executable, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

