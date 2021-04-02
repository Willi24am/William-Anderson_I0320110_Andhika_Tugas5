nama = input("Siapa nama anda: ")
nilai = int(input("Input nilai anda: "))
kalimat = 'Halo, ' + nama + "! Nilai anda setelah dikonversi adalah" + ' '
if nilai < 60:
    print(kalimat + 'E')
elif nilai < 64:
    print(kalimat + 'C')
elif nilai < 69:
    print(kalimat + 'C+')
elif nilai < 74:
    print(kalimat + 'B')
elif nilai < 79:
    print(kalimat + 'B+')
elif nilai < 84:
    print(kalimat + 'A-')
elif nilai < 100:
    print(kalimat + 'A')
else:
    print("Tidak valid")
print()