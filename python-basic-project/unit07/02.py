import exchanges 

def show_menu():
    print("1. 원화 -> 달러")
    print("2. 원화 -> 엔 ")
    print("3. 원화 -> 유로")
    print("4. 달러 -> 원화")
    print("5. 엔  -> 원화")
    print("6. 유로 -> 원화")
    user = input("선택: ")
    return int(user)

def show_amount():
    val = input("금액: ")
    return float(val)

def cal_return(menu, amount):
    val = 0

    if menu == 1:
        val = amount / exchanges.get_usd() 
    elif menu== 2:
        val = amount / exchanges.get_jpy() * 100 
    elif menu == 3:
        val = amount / exchanges.get_eur() 
    elif menu == 1:
        val = amount / exchanges.get_usd() 
    elif menu == 4:
        val = exchanges.get_usd() * amount
    elif menu == 5:
        val = exchanges.get_jpy() / 100 * amount
    else:
        val = exchanges.get_eur() * amount

    print("금액: ", amount)
    print("환전액: ", val)

if __name__ == "__main__":
    menu = show_menu()
    amount = show_amount()
    cal_return(menu, amount)


