# 15 - PYTHON BITWISE OPERATORS

# ================== Complement (~) (tilde symbol) ==================
# Cara Kerja :
# Misalkan ingin mencari nilai dari ~12
# 1. Cari binary format dari angka 12							0b1100
# 2. Invert (balikan) binary formatnya (1 jadi 0, 0 jadi 1)		0b0011
# 3. Cari binary format dari -13								0b1101
# 4. Invert (balikan) binary formatnya (1 jadi 0, 0 jadi 1)		0b0010
# 5. Tambahkan 1 di paling belakang								0b0011
# 6. Terbukti 0b0011 = 0b0011

# Prinsip : kebalikan
# ~1 = 0
# ~0 = 1
# Rumus : complement bin format yg dicari = complement bin format hasil(tanpa minus) + 1
# 		  ~x = -(x+1)
print(bin(-13))
print(bin(~12))
print(~12)
print(~25)
print(~-13)

# ================== And (&) (ampersand symbol) ==================
# Cara Kerja :
# Misalkan ingin mencari hasil dari 12 & 13
# 1. Cari binary format dari angka 12	0b1100
# 2. Cari binary format dari angka 13	0b1101
# 3. Ingat prinsip AND 					0b1100

# Prinsip :
# 0 & 0 = 0
# 0 & 1 = 0
# 1 & 0 = 0
# 1 & 1 = 1
print(12 & 13)
print(25 & 30)

# ================== Or (|) (pipe symbol) ==================
# Cara Kerja :
# Misalkan ingin mencari hasil dari 12 & 13
# 1. Cari binary format dari angka 12	0b1100
# 2. Cari binary format dari angka 13	0b1101
# 3. Ingat prinsip OR  					0b1101

# Prinsip :
# 0 | 0 = 0
# 0 | 1 = 1
# 1 | 0 = 1
# 1 | 1 = 1
print(12 | 13)
print(25 | 30)


# ================== XOR (^) (cap symbol) ==================
# Cara Kerja :
# Misalkan ingin mencari hasil dari 12 ^ 13
# 1. Cari binary format dari angka 12	0b1100
# 2. Cari binary format dari angka 13	0b1101
# 3. Ingat prinsip XOR					0b0001

# Prinsip :
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
print(12 ^ 13)
print(25 ^ 30)

# ================== Left-Shift (<<) ==================
# Cara Kerja :
# 1. Cari binary format dari angka 12	0b1100
# 2. Geser 2 bit ke kiri				0b0110000

# Prinsip : Menggeser bit ke kiri
# Contoh : 12 << 2	#ini akan menggeser 2 bit format dari angka 12 ke kiri
print(12 << 2)

# ================== Right Shift (>>) ==================
# Cara Kerja :
# 1. Cari binary format dari angka 12	0b1100
# 2. Geser 2 bit ke kanan				0b0011

# Prinsip : Menggeser bit ke kanan
# Contoh : 12 << 2	#ini akan menggeser 2 bit format dari angka 12 ke kanan
print(12 >> 2)


