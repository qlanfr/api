# API 문서

이 레포지토리에는 MySQL 데이터베이스를 사용하는 간단한 CRUD 애플리케이션의 FastAPI 서버 코드가 포함되어 있습니다. 애플리케이션은 상태 확인 및 기본적인 아이템 관리(생성, 조회, 수정, 삭제)를 위한 API를 제공합니다.

## 주요 기능

FastAPI를 사용하여 다음과 같은 CRUD 기능을 제공합니다.

- **/health**: 서버 상태 확인
- **/items/** [POST]: 새로운 아이템 생성
- **/items/{item_id}** [GET]: 아이템 조회
- **/items/{item_id}** [PUT]: 아이템 수정
- **/items/{item_id}** [DELETE]: 아이템 삭제

### FastAPI Swagger UI

FastAPI가 제공하는 자동 생성 문서 화면입니다. 이 화면을 통해 API의 사용 방법과 각 엔드포인트의 상세 정보를 확인할 수 있습니다.

![최종화면](https://github.com/qlanfr/api/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-10-27%2016-22-48.png)

---

## API 엔드포인트 설명

### 1. Health Check
- **엔드포인트**: `/health`
- **메소드**: `GET`
- **응답**: `{ "status": "healthy" }`

#### Health Check 결과 예시

![Health Check 예제](https://github.com/qlanfr/api/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-10-27%2016-24-21.png)

---

### 2. 아이템 생성
- **엔드포인트**: `/items/`
- **메소드**: `POST`
- **요청 본문**:
  ```json
  {
    "name": "test item",
    "description": "This is a test item"
  }
![아이템 생성,조회](https://github.com/qlanfr/api/blob/main/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202024-10-27%2016-41-06.png)
