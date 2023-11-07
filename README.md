### 프로젝트 주제 :


- 레스토랑 예약 시스템 : 고객, 호스트, 관리자, 
- 부동산 관리 체계 : 부동산업자, 토지주, 건물주, 고객, 관리자
- 병원 관리 체계 : 의사, 간호사, 간호조무사, 환자, 관리자, 
- 휴대폰...
- 책 추천 시스템 : 책, 고객, 플랫폼, 출판사
- 


Recommendation : 부동산 관리 체계
==========

부동산중개사무소(사업자등록번호, 사무소 이름, 직원 수)

부동산 중개사(주민등록번호, 사업자등록번호, 성별, 나이, 이력) : foreign key. 사업자등록번호, 이력

부동산 매매 이력(id, 토지, 건물주, 고객) : 

토지주(이름, 주민등록번호, 성별, )

[토지(토지대장)](https://post-phinf.pstatic.net/MjAxODEyMjRfMTM2/MDAxNTQ1NjM0NTY1NjY4.sMZPuEzlzysVr5gR3xUZ6Cp75Mt6hpTgem1b5wYbsXAg.sKCeivtL7YPoX6Lmbw9p8nPH3xEjYcnRcDL8UNaOe-Ug.PNG/%ED%86%A0%EC%A7%80%EB%8C%80%EC%9E%A5.png?type=w1200&type=w1200)(고유번호, 토지소재, 지번, 면적, 지목(사용용도), 토지주 주민등록번호) # foreign key : 토지주

건물주(이름, 주민등록번호, 성별,...)

[건물(건축물대장)](https://www.goldpond.kr/%EA%B1%B4%EC%B6%95%EB%AC%BC%EB%8C%80%EC%9E%A5%EB%AC%B4%EB%A3%8C%EC%97%B4%EB%9E%8C/) (고유번호, 명칭, 도로명주소, 지번, 대지면적, 용적률, 높이, 주용도, 층수, 소유자 주민등록번호 등등)

관리자(id, 성별, 나이, 주민등록번호)

