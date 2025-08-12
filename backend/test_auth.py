#!/usr/bin/env python3
"""
Test script for the E-Commerce Backend Authentication API
Run this script to test all authentication endpoints
"""

import requests
import json
import sys

# API base URL
BASE_URL = 'http://localhost:8000/api/auth'

def print_response(response, title):
    """Print formatted response"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print(f"{'='*50}")

def test_register():
    """Test user registration"""
    print("\nTesting User Registration...")
    
    data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpass123",
        "password2": "testpass123",
        "first_name": "Test",
        "last_name": "User",
        "phone_number": "+1234567890",
        "address": "123 Test St, Test City",
        "is_customer": True,
        "is_merchant": False
    }
    
    response = requests.post(f"{BASE_URL}/register/", json=data)
    print_response(response, "REGISTER RESPONSE")
    
    if response.status_code == 201:
        return response.json()
    return None

def test_login(email, password):
    """Test user login"""
    print("\nTesting User Login...")
    
    data = {
        "email": email,
        "password": password
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=data)
    print_response(response, "LOGIN RESPONSE")
    
    if response.status_code == 200:
        return response.json()
    return None

def test_check_auth(access_token):
    """Test authentication check"""
    print("\nTesting Authentication Check...")
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(f"{BASE_URL}/check-auth/", headers=headers)
    print_response(response, "CHECK AUTH RESPONSE")
    
    return response.status_code == 200

def test_profile(access_token):
    """Test user profile retrieval"""
    print("\nTesting User Profile...")
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(f"{BASE_URL}/profile/", headers=headers)
    print_response(response, "PROFILE RESPONSE")
    
    return response.status_code == 200

def test_change_password(access_token, old_password, new_password):
    """Test password change"""
    print("\nTesting Password Change...")
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    data = {
        "old_password": old_password,
        "new_password": new_password
    }
    
    response = requests.put(f"{BASE_URL}/change-password/", json=data, headers=headers)
    print_response(response, "CHANGE PASSWORD RESPONSE")
    
    return response.status_code == 200

def test_logout(access_token, refresh_token):
    """Test user logout"""
    print("\nTesting User Logout...")
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    data = {
        "refresh": refresh_token
    }
    
    response = requests.post(f"{BASE_URL}/logout/", json=data, headers=headers)
    print_response(response, "LOGOUT RESPONSE")
    
    return response.status_code == 205

def test_invalid_login():
    """Test invalid login attempt"""
    print("\nTesting Invalid Login...")
    
    data = {
        "email": "invalid@example.com",
        "password": "wrongpassword"
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=data)
    print_response(response, "INVALID LOGIN RESPONSE")
    
    return response.status_code == 401

def main():
    """Main test function"""
    print("E-Commerce Backend Authentication API Test")
    print("=" * 50)
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/")
        print("✓ Django server is running")
    except requests.exceptions.ConnectionError:
        print("✗ Django server is not running. Please start it with: python manage.py runserver")
        sys.exit(1)
    
    # Test registration
    register_result = test_register()
    if not register_result:
        print("✗ Registration failed")
        return
    
    # Test login with registered user
    login_result = test_login("test@example.com", "testpass123")
    if not login_result:
        print("✗ Login failed")
        return
    
    access_token = login_result['access']
    refresh_token = login_result['refresh']
    
    # Test authentication check
    if test_check_auth(access_token):
        print("✓ Authentication check passed")
    else:
        print("✗ Authentication check failed")
    
    # Test profile retrieval
    if test_profile(access_token):
        print("✓ Profile retrieval passed")
    else:
        print("✗ Profile retrieval failed")
    
    # Test password change
    if test_change_password(access_token, "testpass123", "newpass123"):
        print("✓ Password change passed")
        
        # Test login with new password
        new_login_result = test_login("test@example.com", "newpass123")
        if new_login_result:
            access_token = new_login_result['access']
            refresh_token = new_login_result['refresh']
            print("✓ Login with new password passed")
        else:
            print("✗ Login with new password failed")
    else:
        print("✗ Password change failed")
    
    # Test invalid login
    if test_invalid_login():
        print("✓ Invalid login test passed")
    else:
        print("✗ Invalid login test failed")
    
    # Test logout
    if test_logout(access_token, refresh_token):
        print("✓ Logout passed")
    else:
        print("✗ Logout failed")
    
    print("\n" + "=" * 50)
    print("TEST COMPLETED")
    print("=" * 50)

if __name__ == "__main__":
    main()


