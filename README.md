# VideoRecorder
Simple video recorder using OpenCV

이 프로그램은 OpenCV를 사용하여 컴퓨터의 웹캠이나 카메라 영상을 녹화하는 도구입니다.
이 프로그램은 다음의 기능을 제공합니다:

1. Preview 및 Record 모드
프로그램 실행 시 웹캠으로부터 실시간 영상을 미리보기할 수 있습니다.
스페이스 키를 눌러서 Record 모드를 활성화하거나 비활성화할 수 있습니다.
Record 모드가 활성화되면 빨간색 원이 화면에 표시되어 녹화 중임을 나타냅니다.
<img width="479" alt="image" src="https://github.com/JIAYOOON/VideoRecorder/assets/113532368/bbaa7f7b-74d6-4eed-ba4d-70ae3ec932af"> 

2. Filter 기능
Contrast, Brightness, Flip 세 가지 필터가 제공됩니다.
각각의 필터는 'c', 'b', 'f' 키를 눌러 토글할 수 있습니다.
<img width="481" alt="image" src="https://github.com/JIAYOOON/VideoRecorder/assets/113532368/080852e6-6525-43b8-a5d4-6af89f8d3900"> 1)contrast <img width="480" alt="image" src="https://github.com/JIAYOOON/VideoRecorder/assets/113532368/a559e8a2-b545-4719-ae35-fb022da9b46d"> 2)contrast+flip <img width="481" alt="image" src="https://github.com/JIAYOOON/VideoRecorder/assets/113532368/32493cec-3ada-4246-b66e-516ecd693634"> 3)brightness

3. 화면 표시 및 종료
프로그램 실행 시 화면에 현재 카메라 영상이 표시됩니다.
'ESC' 키를 눌러 프로그램을 종료할 수 있습니다.

4. 녹화된 동영상 파일 저장
녹화된 동영상은 현재 디렉토리에 'output.avi'라는 이름으로 저장됩니다.
녹화 중인 경우 'output.avi' 파일이 생성되고, 녹화가 중지되면 해당 파일이 완료되어 저장됩니다.

[사용법]
프로그램을 실행하면 웹캠 영상이 표시됩니다.
필요에 따라 Contrast, Brightness, Flip 필터를 적용하거나 토글합니다.
녹화하려면 'p' 키를 눌러 Record 모드로 전환합니다. 다시 한 번 누르면 녹화가 중지됩니다.
프로그램을 종료하려면 'ESC' 키를 누릅니다.
