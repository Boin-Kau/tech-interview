# 1주차 스터디 회고

### python 기본 문법에 익숙해지는 중! 문법이 기억이 나지 않으면 구글링 해가면서 문제를 풀고 있어요!
- 문자열 안에 백슬래시를 사용하려면, 앞에 백슬래시 하나를 더 붙여줘야한다. 
- map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해준다 => map(int, input('숫자 두 개를 입력하세요: ').split())
- for문의 기본구조는 "for 변수 in 리스트/튜플/문자열/range함수:" 이다.
- **문자열 안에 변수**를 넣어야 할 때는 [f-string](https://dejavuqa.tistory.com/270)을 사용한다. Ex) message = f"I'm {age} years old"
- **빠른 입력**을 받기 위해선, input 대신 [sys.stdin.readline()](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)을 사용한다. 
- range함수를 내림차순으로 만들려면 [range(시작, 끝, -1)](https://devpouch.tistory.com/70)로 호출하면 된다. 
- [A = list(map(int, input().split()))](https://dailylifeofdeveloper.tistory.com/119) 를 통해 띄어쓰기를 기준으로 한 줄로 입력받아 1차원 배열을 만들 수 있다. 

