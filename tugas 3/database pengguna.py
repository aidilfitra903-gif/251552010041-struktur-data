# database pengguna
user = {
    "aidil":"password123",
    "alya":"admin456",
    "budi":"dev789"
}
print("=== Login Manual ===")
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

if input_username in user and user[input_username] == input_password:
    print(f"Login {input_username} BERHASIL")
else:
    print(f"Login {input_username} GAGAL - Username atau password salah")