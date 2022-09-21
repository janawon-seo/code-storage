i = 0
while True:
    ip =(input("입력해주세요."))
    print(f"입력한 문자는 {ip}입니다.")
    if ip.isdigit() == True:
        i += 1
        print(int(ip) * 2)
    if i == 5:
        print("프로그램을 종료합니다.")
        break
    elif ip == "exit":
        print("프로그램을 종료합니다.")
        break    
    