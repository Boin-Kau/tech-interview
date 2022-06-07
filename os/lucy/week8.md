# 동시성 제어의 고전적 문제들

## Classic Problems of Synchronization (Concurrency-Control)
### 전통적인 동시성 제어 문제 3가지
1. The Bounded-Buffer Problem  
  *-* The Producer-Consumer Problem
2. The Readers-Writers Problem
3. The Dining-Philosophers Problem

<br>

▪ The Bounded-Buffer Problem
- The Producer-Consumer Problem
- producer가 full buffer를 만들고, consumer가 empty buffer를 만든다
- Shared Data Structures
    - A binary semaphore **mutex**
        - buffer pool 접근에 대한 mutual exclusion(동시 접근x)를 제공
        - 1로 초기화
    - Two counting semaphores **empty** and **full** 
        - empty/full buffers를 counting하기 위해 사용
        - empty는 n으로, full은 0으로 초기화

▪ The Readers-Writers Problem
- Producer-Consumer 문제와는 다름
- 동시에(concurrently) 실행중인 프로세스가 읽기만/쓰기만 하는 경우
- readers는 read만 원하고, writers는 update(read & write)하길 원한다
- 둘 이상의 readers가 shared data에 동시에 접근해도 문제가 발생하지 않음
    - read만 하는 경우 data integrity가 보장되기 때문
- writer와 writer, writer와 reader가 동시에 접근하는 경우 문제가 발생할 수 있다
- Readers-Writers Problem의 일부 변형(some variations)
    - Priorities(우선순위)와 연관됨
    - The first readers-writers problem
        - reader process에 writer보다 우선순위를 주는 것
        - writers in ***starvation*** 발생 (writer process 접근 x)
        - solution
            - binary semaphores rw_mutex and mutex = 1
            - read_count 변수를 통해 rw_mutex 활용
            - read_count == 0 이면 writer 진입 가능
    - The second readers-writers problem
        - 정확한 최신 데이터를 보장하는 곳에서 발생
        - writer process에 reader보다 우선순위를 주는 것
        - writer가 대기중인 상황에서는 reader들은 reading할 수 x
        - readers in ***starvation*** 발생

▪ Solution to the Readers-Writers Problem
- writer가 critical section에 있고, n readers가 waiting하고 있으면
    - one reader is queued on **rw_mutex** -> writer와 동기화되어 있음
    - n-1 readers are queued on **mutex** -> readers끼리 동기화
- writer가 signal(rw_mutex)해야
    - the waiting readers or a single waiting writer를 resume execution할 수 있다
    - The selection is made by the scheduler

▪ The Reader-Writer Locks
- readers-writers 문제는 일반적으로 **reader-writer locks** 해결책을 제공
- read/write process의 동기화 해결책
- reader-writer lock을 획득(acuire)할 때는 read/write인지 mode 지정
- read mode에서는 multiple processes가 reader-writer lock을 acquire할 수 있지만
- writing에서는 only one process만 lock을 획득
    - writer에게는 exclusive access가 필요하기 때문

▪ The Dining-Philosophers Problem
1. 일정 시간 생각을 한다.
2. 왼쪽 포크가 사용 가능해질 때까지 대기한다. 만약 사용 가능하다면 집어든다.
3. 오른쪽 포크가 사용 가능해질 때까지 대기한다. 만약 사용 가능하다면 집어든다.
4. 양쪽의 포크를 잡으면 일정 시간만큼 식사를 한다.
5. 오른쪽 포크를 내려놓는다.
6. 왼쪽 포크를 내려놓는다.
7. 다시 1번으로 돌아간다.
- deadlock-free & starvation-free, 즉 교착 상태와 기아 상태가 없는 방식으로 프로세스 간에 여러 리소스를 할당해야 한다.
- Semaphore Solution
    - mutual exclusion을 보장, 가장 simple한 해결책
    - 각 젓가락을 세마포어로(binary) 구현
    - 젓가락 acquire할 때 wait(), release할 때 signal() operation 실행
    - 상호배제 문제는 해결하지만, 데드락(&starvation) 발생
    - 상호배제 문제가 발생하도록 놔두면 지엽적인 문제는 발생하지만, 데드락은 발생 x
- Possible remedies to the deadlock problem
    - 최대 4명의 철학자만 동시에 앉는다
    - 양쪽 젓가락을 집을 수 있을 때만 젓가락을 집게 한다
    - 비대칭 방식
        - 홀수번째 철학자는 왼쪽-오른쪽 젓가락 순으로, 짝수번째는 오른쪽-왼쪽 순으로 젓가락을 집도록 한다.
    - `deadlock-free solution이 반드시 starvation 문제를 해결하지는 않는다`
    - starvation 문제까지 해결하려면 아주 복잡해짐
    - 8장 - deadlock을 완전히 방지(prevent)하려면 너무 어렵고 비용도 많이 들기 때문에 avoid하자. 발생하도록 내버려두고 발생하면 detect해서 수정하자. but 지금 내용은 동기화 도구로 어떻게 해결하는지 배우는 것.
- Monitor Solution
    - 양쪽 젓가락을 집을 수 있을 때만 젓가락을 집게 한다
    - 철학자들의 상태를 3가지로 구분
        - thinking, hungry, and eating
    - 철학자는 두 이웃이 eating 상태가 아닐 때만 eating 상태로 설정할 수 있다
    - `monitior` 구현 시에는 `condition variable`을 선언해야 한다
        - 철학자가 hungry일 때 delay할 수 있도록 허용
        - eating 후에는 signal(notify)

▪ Solution to the Dining-Philosophers Problem
- 젓가락 분배는 monitor, DiningPhilosopher에 의해 컨트롤된다
- monitor가 제공하는 operation
    - 젓가락 집을 때 pickup(), 내려놓을 때 putdown()
- mutual exclusion이 보장되고, no deadlock이 발생하지만
- starvation은 여전히 possible하다
- in Java solution
    - reentrant : 재진입 가능한
    - cpu에서 context switch 일어난 후 레디큐에서 다시 cpu에 들어감 - 재진입
    - reentrantlock이 재진입 가능하게 해준다
    - condition variable에서는 signal()과 await()

<br>

▪ Thread-Safe Concurrent Applications
- concurrent applications는 mutex locks, semaphores, and monitors와 같은 기술로 멀티코어 시스템에서 우수한 성능을 보인다
- 하지만 race conditions, liveness hazard(=deadlock) 문제 위험이 크다
- 그래서, 대체 방안(alternative approaches)이 있다
    - **thread-safe** concurrent applications
    1. Transactional Memory
        - transaction: atomic operation, 입출금 중에 하나만 일어나면 실행 안한걸로 친다, rollback
        - 메모리 영역 자체를 transactional하게 만들자 
    2. OpenMP
        - OpenMP가 알아서 critical section을 만들게 한다
    3. Functional Programming Language
        - 프로그램 패러다임 자체가 함수형 프로그래밍을 쓰면 위의 문제들이 발생 안함
        - 명령형(imperative) 프로그래밍을 가정하기 때문에 문제가 발생하는 것 - 함수형은 완전히 다른 철학
        - 함수형 프로그래밍은 명령어 기반의 프로그래밍을 아예 무시함. 모든 것이 다 함수
        - 함수형 프로그래밍이 인기 있는 이유
            - 하드웨어 성능이 상당히 발전해서 sw 속도를 고민할 필요가 없기 때문
            - 하드웨어 instruction을 고민할 필요 없이 함수로만 프로그램을 짜면 된다
            - 알고리즘 속도는 중요