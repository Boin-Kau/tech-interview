# 6주차 스터디 정리

### Race Condition
- 프로세스가 어떤 순서로 데이터에 접근하느냐에 따라 결과값이 달라질 수 있는 경쟁 상태
  

### "Critical-Section" Problem
- critical section : race condition이 발생할 수 있는 특정 부분
- 코드 구조
  - entry-section
  - critical-section
  - exit-section
  - remainder-section
  

### Critical-Section Problem 해결을 위한 조건 3가지
- Mutual Exclusion(상호 배제) : 이미 한 프로세스가 critical section에서 작업 중일 때, 다른 프로세스는 critical section에 진입해서는 안된다. 
- Progress(진행) : critical section에 작업 중인 프로세스가 없다면, 다른 프로세스가 critical section에 진입할 수 있어야 한다. (deadlock 해결하기!)
- Bounded-waiting(한정 대기) : critical section에 진입하려는 프로세스가 무한하게 대기해서는 안된다. (starvation 해결하기!)
  

### Peterson's Solution
- flag : critical section에서 프로세스가 작업 중인지 저장하는 변수
- turn : critical section에 진입하고자 하는 프로세스를 가리키는 변수 
- 어떤 프로세스가 critical section에 진입하면 flag를 lock하고 나오면 unlock하는 방식
```c
do {
  flag[i] = true;
  turn = j;
  while (flag[j] && turn == j);
  // Critical section
  flag[i] = false;
  // Remainder section
} while(true);
```




