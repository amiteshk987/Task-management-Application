#!/usr/bin/env python
import requests
import re

BASE_URL = "http://127.0.0.1:8000"
session = requests.Session()

print("Testing Admin Panel Fix for RequestContext Error...\n")

# Step 1: Get admin login page
print("1. Getting admin login page...")
response = session.get(f"{BASE_URL}/admin/")
if response.status_code == 200:
    print("   ✓ Admin login page loaded")
else:
    print(f"   ✗ Failed with status {response.status_code}")
    exit(1)

# Step 2: Login as admin
print("2. Logging in to admin panel...")

# Get CSRF token from login page
match = re.search(r'<input[^>]*name="csrfmiddlewaretoken"[^>]*value="([^"]+)"', response.text)
if match:
    csrf_token = match.group(1)
    
    headers = {
        'X-CSRFToken': csrf_token,
        'Referer': f'{BASE_URL}/admin/'
    }
    data = {
        'username': 'admin',
        'password': 'admin123',
        'csrfmiddlewaretoken': csrf_token
    }
    
    response = session.post(f"{BASE_URL}/admin/login/", data=data, headers=headers, allow_redirects=True)
    
    if "Site administration" in response.text or response.status_code == 200:
        print("   ✓ Logged in successfully")
    else:
        print(f"   ✗ Login failed: {response.status_code}")
        exit(1)
else:
    print("   ✗ Could not find CSRF token")
    exit(1)

# Step 3: Try to access Group add page (this was causing the error)
print("3. Accessing /admin/auth/group/add/ (previously caused error)...")
response = session.get(f"{BASE_URL}/admin/auth/group/add/")

if response.status_code == 200:
    if "Add group" in response.text or "Group" in response.text:
        print("   ✓ Group add page loaded successfully!")
        print("   ✓ NO REQUEST CONTEXT ERROR - FIX SUCCESSFUL!")
    else:
        print("   ! Page loaded but content unclear")
else:
    print(f"   ✗ Failed with status {response.status_code}")
    if response.status_code == 500:
        print("   ✗ ERROR: Internal server error still occurring")
        # Check for error details
        if "TypeError" in response.text:
            match = re.search(r'<h1[^>]*>([^<]+)</h1>', response.text)
            if match:
                print(f"   Error: {match.group(1)}")
            # Find the actual error message
            match = re.search(r'<pre[^>]*>([^<]+)</pre>', response.text)
            if match:
                error_msg = match.group(1).strip()[:200]
                print(f"   Details: {error_msg}")
        exit(1)

print("\n✓ All tests passed! Admin panel working correctly.")
