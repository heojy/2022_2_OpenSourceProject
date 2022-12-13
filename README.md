# 2022_2_OpenSourceProject

키보드는 특별한 드라이버 필요 없이 바로 사용 가능합니다.

키 맵핑을 수정하고 싶다면 본 프로그램과 \n
https://github.com/qmk/qmk_firmware 및 \n
https://msys.qmk.fm/, \n
https://github.com/qmk/qmk_toolbox/releases를 다운 받으면 됩니다.

https://docs.qmk.fm/#/keycodes 를 참고하여
본 프로그램의 juyoung/keymaps/via/keymap 파일을 수정한 뒤, 
다운 받은 qmk_firmware/keyboards에 파일을 juyoung 파일을 넣고,
qmk msys를 통해 컴파일 한 뒤 qmk toolbox를 통해 아두이노에 flash 하면 변경된 키 맵핑을 사용할 수 있습니다.

타자 게임을 하려면, dist 파일을 다운받아 압축을 풀고 파일을 열어 Typing_game.exe를 실행하면 됩니다.

Typing_game은 text 엑셀 파일의 데이터를 이용하여 만들었습니다.
