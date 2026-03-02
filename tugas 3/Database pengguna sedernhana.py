# Database pengguna sedernhana
user = {
    "aidil": "password123",
    "alya": "admin456",
    "budi": "dev789"
}

# login check
username = "aidil"
password = "password123"

if username in user and user[username] == password:
    print("Login berhasil!")
else:
    print("username atau password salah!")