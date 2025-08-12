import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/auth/'

def test_register():
    url = f"{BASE_URL}register/"
    import random
    random_num = random.randint(1000, 9999)
    data = {
        "username": f"testuser{random_num}",
        "email": f"testuser{random_num}@example.com",
        "password": "TestPassword123",
        "password2": "TestPassword123",
        "first_name": "Test",
        "last_name": "User"
    }
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(f"Register Response Status: {response.status_code}")
    print(f"Register Response Body: {response.text}")
    return response.json() if response.status_code == 201 else None

def test_login(email, password):
    url = f"{BASE_URL}login/"
    data = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(f"Login Response Status: {response.status_code}")
    print(f"Login Response Body: {response.text}")
    return response.json() if response.status_code == 200 else None

def test_user_profile(token):
    url = f"{BASE_URL}profile/"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(f"Profile Response Status: {response.status_code}")
    print(f"Profile Response Body: {response.text}")
    return response.json() if response.status_code == 200 else None

def test_logout(refresh_token, access_token):
    url = f"{BASE_URL}logout/"
    data = {
        "refresh": refresh_token
    }
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"Logout Response Status: {response.status_code}")
    print(f"Logout Response Body: {response.text}")
    return True if response.status_code == 205 else False

def run_tests():
    # Test registration
    print("\n=== Testing User Registration ===")
    user = test_register()
    if not user:
        print("Registration failed. Skipping other tests.")
        return
    
    # Get the email from the registration response
    email = user.get('email')
    
    # Test login
    print("\n=== Testing User Login ===")
    tokens = test_login(email, "TestPassword123")
    if not tokens:
        print("Login failed. Skipping other tests.")
        return
    
    # Test profile
    print("\n=== Testing User Profile ===")
    profile = test_user_profile(tokens.get('access'))
    if not profile:
        print("Profile retrieval failed.")
    
    # Test logout
    print("\n=== Testing User Logout ===")
    logout_success = test_logout(tokens.get('refresh'), tokens.get('access'))
    if logout_success:
        print("Logout successful.")
    else:
        print("Logout failed.")

if __name__ == "__main__":
    run_tests()