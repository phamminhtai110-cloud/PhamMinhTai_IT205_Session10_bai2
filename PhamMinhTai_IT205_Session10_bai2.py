playlist = []

while True:
    print("\n===== PLAYLIST =====")
    print("1. Them bai hat")
    print("2. Xem danh sach")
    print("3. Xoa bai hat")
    print("4. Sap xep / Trich xuat")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    if choice == "1":
        print("1. Them cuoi")
        print("2. Chen theo vi tri")

        sub = input("Lua chon: ")
        song = input("Nhap ten bai hat: ")

        if sub == "1":
            playlist.append(song)
            print("Them thanh cong!")
            print("So bai hat:", len(playlist))

        elif sub == "2":
            try:
                index = int(input("Nhap vi tri: "))

                if index < 0 or index > len(playlist):
                    print("Vi tri khong hop le.")
                else:
                    playlist.insert(index, song)
                    print("Them thanh cong!")
                    print("So bai hat:", len(playlist))

            except ValueError:
                print("Lua chon khong hop le, vui long nhap so nguyen")

        else:
            print("Lua chon khong hop le.")

    elif choice == "2":
        if len(playlist) == 0:
            print("Danh sach phat hien dang trong!")
        else:
            for i in range(len(playlist)):
                print(f"{i+1}. {playlist[i]}")

    elif choice == "3":
        if len(playlist) == 0:
            print("Danh sach phat hien dang trong!")
            continue

        print("1. Xoa theo ten")
        print("2. Xoa theo vi tri")

        sub = input("Lua chon: ")

        if sub == "1":
            song = input("Nhap ten bai hat: ")

            if song in playlist:
                playlist.remove(song)
                print("Da xoa bai hat", song)
            else:
                print("Khong tim thay bai hat trong danh sach phat.")

        elif sub == "2":
            try:
                index = int(input("Nhap vi tri: "))

                if index < 1 or index > len(playlist):
                    print("Vi tri khong hop le.")
                else:
                    removed = playlist.pop(index - 1)
                    print("Da xoa bai hat", removed)

            except ValueError:
                print("Lua chon khong hop le, vui long nhap so nguyen")

        else:
            print("Lua chon khong hop le.")

    elif choice == "4":
        if len(playlist) == 0:
            print("Danh sach phat hien dang trong!")
            continue

        print("1. Sap xep A-Z")
        print("2. Nghe thu 3 bai dau")

        sub = input("Lua chon: ")

        if sub == "1":
            playlist.sort()
            print("Danh sach sau khi sap xep:")
            for song in playlist:
                print(song)

        elif sub == "2":
            print("3 bai hat dau:")
            for song in playlist[:3]:
                print(song)

        else:
            print("Lua chon khong hop le.")

    elif choice == "5":
        print("Cam on ban da su dung dich vu. Tam biet!")
        break

    else:
        print("Lua chon khong hop le, vui long nhap so nguyen")