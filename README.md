# kme_private

[ Windows ]

시작 메뉴에서 'cmd'를 검색하여 '명령 프롬프트'를 실행합니다.
명령 프롬프트 창에서 'ipconfig /all'을 입력하고 엔터를 누릅니다.
네트워크 어댑터 정보가 나열되는데, 해당하는 네트워크 어댑터의 '물리적 주소(MAC 주소)'를 확인할 수 있습니다.

[ MacOS ]

'Launchpad'에서 '터미널'을 찾아 실행합니다.
'터미널' 창에서 'ifconfig | grep ether'를 입력하고 엔터를 누릅니다.
'ether' 다음에 표시되는 값이 'MAC 주소'입니다.
