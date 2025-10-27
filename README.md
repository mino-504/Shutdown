# 💤 shutdown v0.1

> 간단한 **자동 종료 타이머 프로그램**  
> 지정한 시간(1h / 2h / 3h 후)에 PC를 자동으로 종료합니다.

---

## ⚙️ 주요 기능

- ✅ 1시간 / 2시간 / 3시간 뒤 자동 종료 예약  
- 🚫 종료 예약 취소 기능 (`shutdown /a`)  
- 🧩 간단한 GUI (tkinter 기반)  
- 💡 관리자 권한 없이 작동  

---

## 🖥️ 실행 방법

### 1️⃣ Python 환경
- Python 3.10 이상 설치 필요  
- `tkinter`는 기본 내장되어 있어 별도 설치 불필요  

---

### 2️⃣ 실행
```bash
python shutdown.py
또는 Windows에서 더블클릭 실행

📜 코드 정보
python
코드 복사
PROGRAM_NAME = "shutdown"
VERSION = "v0.1"
AUTHOR = "Minho"
DESCRIPTION = "자동 종료 타이머 프로그램 (기본 GUI)"

🪄 향후 업데이트 계획
버전	예정 기능
v0.2	사용자 직접 시간 입력 기능
v0.3	남은 시간 표시 / 카운트다운
v1.0	완성형 UI, 아이콘 적용

🧠 사용 예시
버튼	기능
1시간 뒤 종료	3600초 후 PC 자동 종료
2시간 뒤 종료	7200초 후 PC 자동 종료
3시간 뒤 종료	10800초 후 PC 자동 종료
취소하기	예약된 종료 취소

🪶 License
MIT License © 2025 Minho
자유롭게 수정 및 배포 가능하며, 원작자 표기만 유지해주세요.

<p align="center"> <img src="https://img.shields.io/badge/version-v0.1-blue?style=for-the-badge"> <img src="https://img.shields.io/badge/status-Beta-orange?style=for-the-badge"> <img src="https://img.shields.io/badge/made%20by-Minho-lightgrey?style=for-the-badge"> </p>