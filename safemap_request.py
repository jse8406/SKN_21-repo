import requests
from urllib.parse import quote_plus
from typing import Optional

# 설정
BASE_URL = "http://safemap.go.kr/openApiService/data/getChargingStationData1.do"
API_KEY = "0KEH6JLX-0KEH-0KEH-0KEH-0KEH6JLX28"  # 예시 키, 실제로는 환경변수로 관리하세요


def fetch_charging_stations(numOfRows: int = 10, pageNo: int = 1, dataType: str = "XML") -> Optional[str]:
    """공공데이터 포털의 충전소 정보 API를 호출합니다.

    Args:
        numOfRows: 한 페이지에 가져올 결과 수 (기본 10)
        pageNo: 페이지 번호 (기본 1)
        dataType: 요청 자료형식 "JSON" 또는 "XML" (기본 JSON)

    Returns:
        API 응답 텍스트 (JSON 문자열 또는 XML 문자열) 또는 None (실패 시)
    """
    # URL 인코딩된 서비스키
    service_key = quote_plus(API_KEY)

    params = {
        "serviceKey": service_key,
        "numOfRows": numOfRows,
        "pageNo": pageNo,
        "dataType": dataType
    }

    try:
        resp = requests.get(BASE_URL, params=params, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    return resp.text


if __name__ == "__main__":
    # 간단한 실행 예
    data = fetch_charging_stations(numOfRows=5, pageNo=1, dataType="JSON")
    if data:
        print(data[:1000])  # 큰 응답의 경우 처음 1000자만 출력
        # 파일로 저장하려면 아래 주석 해제
        # with open('charging_stations.json', 'w', encoding='utf-8') as f:
        #     f.write(data)

# full_URL = https://www.safemap.go.kr/openApiService/data/getChargingStationData1.do?serviceKey=0KEH6JLX-0KEH-0KEH-0KEH-0KEH6JLX28&numOfRows=10&pageNo=1&dataType=JSON
