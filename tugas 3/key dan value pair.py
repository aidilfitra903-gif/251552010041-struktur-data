user = {"name": "aidil", "age": 22,}

# menggunakan get agar aman dari KeyError
email = user.get("email", "Email tidak tersedia")
print(email)

# menambahkan key jika belum ada dengan setdefault
user.setdefault("email", "aidil@example.com")

#uodate data
user.update({"age": 23, "role": "DevOps"})  

# menghapus key
age = user.pop("age")

# menampilkan semua key dan value
print(user.keys())
print(user.values())

#menyalin dictionary
user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)