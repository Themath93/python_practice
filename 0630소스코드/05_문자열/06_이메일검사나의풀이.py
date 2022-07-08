email_address = input("이메일 입력 : ")

#  @ 없는 경우
#  . 없는 경우
#  @과 . 위치가 바뀐 경우
#  @과 . 사이에 문자가 없는 경우
#  @ 앞에 문자가 없는 경우
#  . 뒤에 문자가 없는 경우
#  @ 두 번 이상 있는 경우
#  . 두 번 이상 있는 경우

if (email_address.find("@") == -1 or
    email_address.find(".") == -1 or
    email_address.index("@") > email_address.index(".") or
    email_address.find("@.") != -1 or
    email_address.index("@") == 0 or
    email_address.index(".") >= len(email_address) or
    email_address.count("@") > 2 or
    email_address.count(".") > 2):
    print("이메일 형식이 아닙니다.")
    print("입력한 이메일 : %s" %email_address)
else:
    print("입력한 이메일 : %s" %email_address)