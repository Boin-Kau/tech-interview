# Synchronization

## Cooperating processes
- 서로 영향을 주고 받음
- share a logical address space - thread
- share data - shared memory, message passing
- 공유 데이터에 concurrent(동시) access => ``data inconsistency``(불일치)
- **orderly execution**을 보장해야 함 -> **maintain data consistency**
- ``Integrity of data`` (데이터 무결성)
    - Concurrent execution
        - context switch 발생 위치에 따라 register 값이 달라짐
        - interleaved in some arbitrary order (임의의 순서로 삽입됨)
        - ``Race Condition``
    - Parallel execution
- 'count++' in machine language
    ``` c
    register = count
    register = register + 1
    count = register
    ```

## Race Condition (경쟁 상태)
- 공유 자원을 동시에 접근하는 상황
- same/shared data를 concurrently하게 실행하려할 때, 실행 결과(outcome)는 access가 발생하는 특정 순서에 따라 달라진다
- race condition 해결 방법
    - **Synchronization**: 한 번에 한 프로세스만 공유 데이터를 조작하도록 한다 (프로세스/스레드 동기화)
- race condition 사례 - kernel 영역: fork()

<br>

## The Critical Section Problem (임계 영역)
- a segment of code
- in which the process may be accessing and updating data
- that is shared with at least one other process.
- 한 프로세스가 임계 영역에서 실행중일 때, 다른 프로세스는 임계 영역에서 실행할 수 없다 => **동시에 두 프로세스가 임계 영역에서 실행할 수 없다**
- 동기화(synchronize)를 이루고 cooperatively share data할 수 있다
- Sections of codes  
    1. entry section (진입 영역)  
    2. critical section (임계 영역)  
    3. exit section  
    4. remainder section  
- 해결 조건  
    1. ``Mutual Exclution`` (상호 배제)  
    2. ``Progress``(진행)  
      - 임계 영역에 들어갈 프로세스를 결정    
      - deadlock 방지(avoid)  
      - deadlock: 무한대로 진입이 연기되는 상황
    3. ``Bounded Waiting``(한정 대기)  
      - starvation(기아) 방지(avoid)  
      - 프로세스가 임계 영역에 들어갈 수 있는 횟수 제한
- 3가지를 다 만족해야 임계 영역 문제를 해결하지만, 다 푸는 방법은 어렵다(현실 적용 가능성x)
- Mutual Exclution만 적용하고, 나머지 두 상황은 발생하면 해결
- single-core 환경에서의 간단한 해결책
    - Prevent interrupts (인터럽트 방지) - disable interrupt
    - 멀티프로세스 환경에서는 불가능(not feasible)
- non-preemptive kernel
    - race condition 발생 가능성 x
    - 하지만 non-preemptive는 느리기 때문에 현대에서 사용 x
- preemptive kernel
    - 디자인하기 어렵지만, responsive하기 때문에 유리하다(favorable)

<br>

=> 동기화(Synchronization): 데이터의 무결성(integrity)을 보장

<br>


→ 동기화 문제 해결책
# Peterson's Solution
▪ Software Solutions to the Critical-Section(임계 영역) Problem
- Dekker's Algorithm
    - 두 개의 프로세스로 해결
- Eisenberg and McGuire's Algorithm
    - n 개의 프로세스(대기시간이 n-1을 lower bound로 가지는)
- Bakery Algorithm (Laslie Lamport)
    - 두 개 이상의 프로세스가 동작하고 있을 경우의 알고리즘
    - 가장 낮은 번호를 받은 프로세스가 가장 먼저 임계 영역에 들어갈 수 있다
- **Peterson's Algorithm**
    - a classic software solution to the critical-section problem
    - 임계 영역 문제를 완전하게 해결하는 알고리즘
    - 제대로 작동한다는 보장 없음
    - 현대 컴퓨터는 기본 기계어 명령을 수행하기 때문(load and store 아키텍처)

<br>

▪ Peterson's solution
- 임계 섹션(critical sections)과 나머지 섹션(remainder sections) 사이에서 교대로 실행하는 두 개의 프로세스로 제한된다
    - n 개로 확장 가능하지만 지금은 공부하지 x
- flag 2개(i, j 산책 깃발)
    - 산책: critical section
    - 집 안: remainder section
- race condition(경쟁 상태)를 방지
- 동기화(synchronization)가 이루어짐
- 아키텍처가 load and store과 같은 기본 기계어 명령을 수행하는 경우 제대로 작동한다는 보장이 없다
- 알고리즘 면에서는 CSP의 좋은 해결책
    - mutual exclusion(상호 배제), progress(진행-데드락x), and bounded waiting(한정 대기-기아x)
- 증명 가능하다(provably correct) - 상호 배제(동시에 임계 영역에 들어갈 수 x), 진행, 대기 한정 증명

<br>

# Hardware Support for Synchronization
▪ Hardware-based Solutons
- CSP 문제 해결을 지원해 준다
- 바로(directly) 동기화 툴로 사용될 수 있다
- 다른 메커니즘의 도구로 사용될 수 있다
- Three primitive operations
    - memory barriers of fences
    - hardware instructions
    - atomic variables

<br>

▪ Atomicity(원자성)
- atomic operation은 더이상 쪼갤(중단할) 수 없는 작업의 단위
- 현대 컴퓨터 시스템은 special hardware instruction을 제공한다
    - instruction 자체를 special hardware instruction로 만드는데, 그것을 atomic instruction으로 만든다
        - test and modify 하거나 test and swap할 수 있게 하는 atomic instruction

<br>

▪ 두 타입의 conceptual atomic instruction(개념적 원자 명령)
- `test_and_set()` 와 `compare_and_swap()`
- 명령(함수)을 hardware instruction으로 만들면 더이상 쪼갤 수 없기 때문 => atomic operation(단위 명령)이 됨
- mutual exclusion(상호 배제)을 보장
    - 적어도 critical section(임계 영역)에 동시 진입하는 문제는 발생 x
    - deadlock과 starvation까지 해결되는 solution은 없음

<br>

▪ Atomic Variable
- `compare_and_swap()` 명령은 atomic variable을 만드는 도구로 사용할 수 있다
- single variable(단일 변수)의 race condition에서 상호 배제(mutual exclusion)를 보장하는 atomic operation(원자 연산, ex.정수/부울 연산)을 제공한다

### Atomic variable 구현 in Java
- static 생성자는 해당 클래스가 load될 때 초기화해준다.

<br>

### 정리
- race condition: shared data(공유 자원)에 여러 프로세스가 동시에 access하는 것
- critical section: 공유 자원에 동시에 access하는 코드 영역
- synchronization(동기화): critical section을 보호하는 것
    - entry/exit section 구분
- 동기화 문제 해결을 위한 3가지
    - 상호 배제(mutual exclusion)
    - 진행(progress) - deadlock 방지
    - 한정 대기(bounded waiting) - 기아(starvation) 방지
- 3가지를 다 만족하는 solution: Peterson's Solution
    - Pi, Pj 서로 동기화
    - flag, turn 이용
    - n개로 확장할 수 있고, 다른 알고리즘으로 보완할 수도 있지만 너무 과하고 복잡하기에 상호배제 문제만 해결하자
- 간단하게 상호 배제만 해결하는 방법(3가지 동기화 도구)
    - 뮤텍스
    - 세마포어
    - 모니터