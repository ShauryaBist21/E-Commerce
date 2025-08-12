#!/usr/bin/env python3
"""
Setup script for the E-Commerce Backend
This script will install dependencies and set up the Django project
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_virtual_environment():
    """Create a virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✓ Virtual environment already exists")
        return True
    
    print("Creating virtual environment...")
    try:
        venv.create("venv", with_pip=True)
        print("✓ Virtual environment created successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to create virtual environment: {e}")
        return False

def get_activate_command():
    """Get the appropriate activate command for the current OS"""
    if os.name == 'nt':  # Windows
        return "venv\\Scripts\\activate"
    else:  # Unix/Linux/macOS
        return "source venv/bin/activate"

def install_requirements():
    """Install Python requirements"""
    activate_cmd = get_activate_command()
    
    # Install requirements
    if os.name == 'nt':  # Windows
        pip_cmd = f"{activate_cmd} && pip install -r requirements.txt"
    else:  # Unix/Linux/macOS
        pip_cmd = f"{activate_cmd} && pip install -r requirements.txt"
    
    return run_command(pip_cmd, "Installing Python requirements")

def run_migrations():
    """Run Django migrations"""
    activate_cmd = get_activate_command()
    
    # Run makemigrations
    if os.name == 'nt':  # Windows
        makemigrations_cmd = f"{activate_cmd} && python manage.py makemigrations"
        migrate_cmd = f"{activate_cmd} && python manage.py migrate"
    else:  # Unix/Linux/macOS
        makemigrations_cmd = f"{activate_cmd} && python manage.py makemigrations"
        migrate_cmd = f"{activate_cmd} && python manage.py migrate"
    
    success1 = run_command(makemigrations_cmd, "Creating database migrations")
    success2 = run_command(migrate_cmd, "Applying database migrations")
    
    return success1 and success2

def create_superuser():
    """Create a superuser account"""
    print("\nWould you like to create a superuser account? (y/n): ", end="")
    response = input().lower().strip()
    
    if response in ['y', 'yes']:
        activate_cmd = get_activate_command()
        
        if os.name == 'nt':  # Windows
            createsuperuser_cmd = f"{activate_cmd} && python manage.py createsuperuser"
        else:  # Unix/Linux/macOS
            createsuperuser_cmd = f"{activate_cmd} && python manage.py createsuperuser"
        
        print("Creating superuser account...")
        print("Please follow the prompts to create your admin account.")
        try:
            subprocess.run(createsuperuser_cmd, shell=True)
            print("✓ Superuser account created successfully")
        except Exception as e:
            print(f"✗ Failed to create superuser: {e}")

def main():
    """Main setup function"""
    print("E-Commerce Backend Setup")
    print("=" * 50)
    
    # Check if we're in the correct directory
    if not Path("manage.py").exists():
        print("Error: manage.py not found. Please run this script from the backend directory.")
        sys.exit(1)
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("Error: requirements.txt not found.")
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("\nFailed to install requirements. Please try manually:")
        print("1. Activate virtual environment:")
        if os.name == 'nt':
            print("   venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print("2. Install requirements: pip install -r requirements.txt")
        sys.exit(1)
    
    # Run migrations
    if not run_migrations():
        print("\nFailed to run migrations. Please try manually:")
        print("1. Activate virtual environment")
        print("2. Run: python manage.py makemigrations")
        print("3. Run: python manage.py migrate")
        sys.exit(1)
    
    # Create superuser
    create_superuser()
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("=" * 50)
    print("\nTo start the server:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Start server: python manage.py runserver")
    print("\nOr use the startup script: python start_server.py")
    print("\nServer will be available at: http://localhost:8000")
    print("API endpoints: http://localhost:8000/api/")
    print("Admin interface: http://localhost:8000/admin/")

if __name__ == "__main__":
    main()

