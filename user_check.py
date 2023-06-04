import psutil
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')

# MAC 주소를 추출하는 함수
def get_mac_address():
    interfaces = psutil.net_if_addrs()
    for interface in interfaces.values():
        for addr in interface:
            if addr.family == psutil.AF_LINK:
                return addr.address
    return None

# 사용자의 MAC 주소를 확인합니다.
mac_address = get_mac_address()

print('MAC : ' + get_mac_address())

# MAC 주소가 일치하는지 확인하여, 실행 여부를 결정합니다.
if mac_address == "40-B0-76-42-8F-7D": # <--- 사용자를 통해 전달받고 설정해야 하는 값입니다!
    # 현재 날짜와 초기 설정된 날짜를 비교하여, 사용 가능 기간인지 확인합니다.
    default_set_date = datetime.datetime.strptime("2023-06-04", "%Y-%m-%d").date()
    current_date = datetime.datetime.now().date()
    expiration_date = default_set_date + datetime.timedelta(days=30) # <--- 초기 설정된 날짜로부터 30일 후

    print('')
    print('default set date : ' + str(default_set_date))
    print('current date : ' + str(current_date))
    print('expiration date : ' + str(expiration_date))
    print('')

    if current_date <= expiration_date:
        # 실행 구문 작성
        print("정상적으로 실행되었습니다.")
    else:
        print("사용 기간이 만료되었습니다!")
else:
    print("인증된 사용자가 아닙니다!")