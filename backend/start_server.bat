@echo off
echo Starting E-Commerce Backend Server...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Activate virtual environment and start server
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing requirements...
pip install -r requirements.txt

echo Running migrations...
python manage.py migrate

echo.
echo Starting Django development server...
echo Server will be available at: http://localhost:8000
echo API endpoints: http://localhost:8000/api/
echo Admin interface: http://localhost:8000/admin/
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause


