def weight_conversion():
    berat = int(input("Masukkan berat anda: "))
    satuan = input("Dalam satuan apa berat yang anda masukkan? (K untuk Kg, L untuk Lbs): ")
    
    if satuan.lower()== 'l':
        print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)} kg")
    elif satuan.lower() == 'k':
        print(f"Berat anda dikonversi menjadi pounds adalah {round(berat * 2.20462)} lbs")