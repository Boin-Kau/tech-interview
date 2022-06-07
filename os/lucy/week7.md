# Mutex and Semaphore
▪ CSP 해결을 위한 Higher-level software tools
- Mutex Locks
    - 가장 간단한 동기화 툴
    - 임계영역=락커룸
    - 2개 프로세스만 제어 가능
- Semaphore
    - n개 프로세스 제어 가능
    - 더 견고하고(robust), 편리하고(convenient), 효과적인(effective) 툴
- Monitor
    - mutex와 semaphore의 문제점(demerits)을 해결한 도구
    - Java에서 사용하는 동기화 도구
- Liveness
    - 위 3가지 툴은 상호배제만 해결, liveness는 progress(deadlock) 문제도 해결

<br>

## Mutex Locks
▪ Mutex Lock
- mutex: **mut**ual **ex**clusion (상호 배제)
- critical section을 보호하고 race condition을 예방
- 들어갈 때 locker key 넣고 나갈 때 반납하는 구조로, 동시 접근으로 발생하는 race condition 예방
- 프로세스는 반드시 critical section에 들어가기 전에 lock을 `aquire`(획득)해야 한다
- critical section을 나갈 때 lock을 `release` 한다
- entry section => acquire lock, exit section => release lock
- Mutex Lock을 위해서는 two functions와 one variable만 필요
    - acquire() and release()
    - available: Boolean variable (lock의  available을 나타내는 변수)
- acquire() and release() 호출(calls)은 반드시 atomically performed(원자적으로 수행) 되어야 한다
- compare_and_swap operation을 이용해 구현
    - 간단한 컴퓨터에서는 interrupt disable을 통해 구현 (context switch 방지)

▪ Busy waiting 문제
- 다른 프로세스가 critical section에 들어가기 위해 **loop continuously** 해야 한다
- real multiprogramming system에서 clearly a problem이다
    - single CPU core가 여러 프로세스에서 공유되는 경우
    - 일부 프로세스가 생산적으로 사용하기 위해 CPU cycle을 낭비한다
- mutex lock 구현에서 가장 큰 문제

▪ Spinlock
- busy waiting하는 mutex lock
- 프로세스는 lock이 available할때까지 spin한다
- however, 유용할 때가 있다
    - CPU core가 여러 개일 때
    - lock을 기다릴 때 context switch가 필요하지 않다는 점에서
    - busy waiting할 때는 context switch가 일어나지 x
    - context switch(대기 큐->레디 큐->run)는 상당한 시간이 소요될 수 있기 때문
- multicore systems의 특정 상황(circumstances)에서, spinlock은 locking에서 preferable choice이다
    - 스레드는 한 processing core에서 spin할 수 있다 - 다른 스레드가 다른 코어에서 critical section을 performs(수행)하는 동안

<br>

## Semaphores
▪ semaphore: 신호장치, 신호기
- semaphore S는 정수 변수, 초기화를 제외하고는(apart from initialization) 두 표준(standard) atomic operation(연산)을 통해서만 접근된다
- wait() and signal()
    - 또는 P() and V()
        - by Edsger Dijkstra
        - **P**roblem(to test) and **V**erhogen(to increment)
- S--, S++ (열쇠함)
- n개의 인스턴스를 가진 자원을 공유할 때 사용 가능

▪ Binary and Counting Semaphores
- **Binary** Semaphore
    - 0과 1 사이의 범위: **mutex lock**과 유사
- **Counting** Semaphore
    - S = n (n>1)
    - range over an unrestricted domain(무제한 범위)
    - **여러 개의 인스턴스**(a finite number of instances)가 있는 리소스에 사용 가능
    - resource 사용시
        - wait() 호출 => P()
        - count 감소
    - resource release시
        - signal() => V()
        - count 증가
    - count가 0이 되면 resource가 모두 사용중이므로 나머지 프로세스는 block된다 - count가 0보다 커질 때까지

▪ Synchronization 문제 해결 using semaphore
- `순서`가 필요한 상황에서
- 프로세스가 `0으로 초기화`된 semaphore **synch**를 공유한다

▪ Semaphore Implementation(구현)
- 세마포어도 busy waiting 문제 발생
- 해결 - P(), V()의 정의(definition)을 수정해야 한다
- wait() operation
    - not positive한 세마포어는 busy waiting하는 대신, 스스로 suspend하고 waiting queue에 들어간다 - sleep()
- signal() operation
    - waiting process는 ready queue로 간다 - wakeup(P)
    - P: process P
- => busy wait 문제 해결
- 인스턴스 하나에 n>1 인 변수 하나이면 race condition 발생
    - mutual exclusion 불가
    - n개의 instance가 있다는 전제 조건이 있는 게 세마포어
    - n개의 스레드가 하나의 변수인 shared memory에 동시 접근하면 무조건 critical section 문제 발생
    - 변수가 배열이면 critical section 문제 발생 x
    - binary semaphore이면 mutex가 되기 때문에 critical section 문제 발생 x

<br>

---

▪ mutex lock, semaphore은 모두 locking을 기반으로 동기화 - lock의 개수에 차이가 있다  
▪ 뮤텍스는 Locking 메커니즘으로 락을 걸은 쓰레드만이 임계 영역을 나갈때 락을 해제할 수 있다. 하지만 세마포어는 Signaling 메커니즘으로 락을 걸지 않은 쓰레드도 signal을 사용해 락을 해제할 수 있다. 세마포어의 카운트를 1로 설정하면 뮤텍스처럼 활용할 수 있다.  
▪ spinlock과 semaphore의 차이점
- spinlock
    - 특정한 자료구조를 획득(lock) 또는 해제(unlock) 함으로서 공유 데이터에 대한 접근 권한을 관리하는 방법이다.
    - 권한을 획득하기 전까지 CPU는 무의미한 코드를 수행하는 busy waiting 상태로 대기하고 있다가 접근 권한을 얻으면 내부 코드를 수행하고 종료후 권한을 포기한다.
    - 상태가 획득/해제 밖에 없기 때문에 공유 영역에는 하나의 컴포넌트만 접근 할 수 있으며 획득과 해제의 주체는 동일해야한다.
    - CPU를 선점하고 있는 busy waiting 상태로 대기하기 때문에 권한이 해제되는 대로 빨리 작업을 수행할 수 있는 장점이 있지만 선점 기간동안 다른 프로세스 작업이 지연될 수 있는 오버헤드도 존재한다. 그래서 짧게 수행할 수 있는 작업에 주로 사용된다.
- semaphore
    - 스핀락, 뮤텍스와는 다르게 표현형이 정수형이며 이점을 살려 하나 이상의 컴포넌트가 공유자원에 접근하도록 허용할 수 있다.
    - 예로 들면 뮤텍스와 스핀락은 옷가게에 한 개의 피팅룸만 있었던 반면 세마포어는 하나 이상의 피팅룸이존재하는 셈. 물론 세마포어를 이진수의 형태로 사용해 개념적으로 뮤텍스와 스핀락처럼 사용하는 것도 가능하다.
    - 정수형인 만큼 획득과 해제 같은 명령이 아니라 값을 올리고 줄이는 방식으로 세마포어를 사용한다. 세마포어의 값이 0이면 기다려야 한다.
    - 스핀락과 뮤텍스와 달리 세마포어는 해제(Unlock)의 주체가 획득(Lock)과 같지 않아도 된다. 즉 어떤 프로세스가 세마포어의 값을 감소시켜도 다른 프로세스가 풀어줄 수 있다. 이 특징을 고려해 세마포어를 시그널(Signal) 원리로 사용 할 수도 있다.

▪ https://selfish-developer.com/entry/%EC%8A%A4%ED%95%80%EB%9D%BD-%EB%AE%A4%ED%85%8D%EC%8A%A4-%EC%84%B8%EB%A7%88%ED%8F%AC%EC%96%B4   
▪ https://www.geeksforgeeks.org/mutex-vs-semaphore/  
▪ https://www.geeksforgeeks.org/difference-between-spinlock-and-semaphore/?ref=rp

<br>

# Monitor and Java Synchronization
▪ semaphores의 difficulty
- 동기화에 편리하고 효과적인 도구이지만
- timing error(programming error)가 발생할 수 있다
    - 특정 실행 시퀀스가 발생하는 경우(if particular execution sequences take place)
    - 이런 시퀀스들은 항상 일어나지도(occur) 않고, 감지(detect)하기도 어렵다

<br>

▪ semaphore's problem의 예 (illustrative example)
- 모든 프로세스는 1로 초기화된 binary semaphore mutex를 공유한다
- 각 프로세스는 critical section 진입 전에 wait(mutex)하고 이후에 signal(mutex)해야 한다
- 이 순서가 지켜지지 않으면(not observed) 두 프로세스가 동시에 CS에 있을 수 있다
- 이러한 문제는 프로그래밍 에러/프로그래머로 인해 발생할 수 있다
- 따라서 monitor로 해결

<br>

▪ Monitor
- 간단한 동기화 도구를 고급 언어로 통합
- one fundamental high-level synchronization construct
- monitor type
    - an ADT(abstract data type)
    - mutual exclusion을 제공하는 데이터 타입(class)
    - 해당 타입의 인스턴스 상태를 정의하는 변수를 함수 body와 함께 선언한다
- class 안에는 shared data, operations, initialization code
- **Conditional Variables**
    - 모니터가 자체적으로 동기화 체계(scheme)를 모델링하기엔 부족하므로
    - condition 구조를 정의해서 추가적인 동기화 메커니즘을 제공한다
        ```
        condition x, y;
        x.wait();
        x.signal();
        ```

<br>

▪ Java Monitiors
- Java는 monitor-lock 또는 intrinsic-lock이라 불리는 monitior를 제공한다
- concurrency mechanism for thread synchronization (자바는 기본 단위가 스레드)
- **synchronized** keyword
    - 임계 영역에 해당하는 코드 블록을 선언할 때 사용하는 자바 키워드
    - 해당 코드 블록(임계영역)에는 모니터락을 획득해야 진입 가능
    - 모니터락을 가진 객체 인스턴스를 지정할 수 있다
    - 메소드에 선언하면 메소드 코드 블록 전체가 임계영역으로 지정된다
        - 이 때, 모니터락을 가진 객체 인스턴스는 this 객체 인스턴스
    - lock aquire(entry section)과 release(exit section)는 JVM이 해준다
- **wait()** and **notify()** method
    - java.lang.Object 클래스에 선언됨: 모든 자바 객체가 가진 메소드
    - wait(), signal()
    - 스레드가 어떤 객체의 wait() 메소드를 호출하면 해당 객체의 모니터락을 획득하기 위해 대기 상태로 진입한다
    - 스레드가 어떤 객체의 notify() 메소드를 호출하면 해당 객체 모니터에 대기중인 스레드 **하나**를 깨운다
    - notify() 대신에 notifyAll() 메소드를 호출하면 해당 객체 모니터에 대기중인 스레드 **전부**를 깨운다
        - 하나만 깨우면 문제가 생길 수 있기 때문

<br>

# Liveness
▪ Liveness
- mutex, semaphore, monitor은 상호 배제만 해결
    - progress(deadlock), bounded waiting(starvation) 문제 해결 못하고 오히려 deadlock을 더 일으킨다
- Liveness는 progress를 보장
- deadlock과 priority inversion(우선순위 역전)을 고려해야 한다

<br>

▪ Deadlock
- 두 개 이상의 프로세스가 무한히(indefinitely) 대기하는 상황
    - waiting queue에 있는 프로세스만이 일으킬 수 있는 이벤트를 기다리는 경우
- 교착상태 - P0는 P1을 기다리는데, P1도 P0을 기다린다 - 영원히 만날 수 없음

<br>

▪ Priority Inversion
- 높은 우선순위의 프로세스가 낮은 우선순위 프로세스에게 밀리는 현상 (lower-priority process를 기다려야 하는 상황)
- higher-priority process가 kernel data를 read or modify해야 하는데, 그 kernel data를 lower-priority process가 점유하고 있을 때
    - 아빠가 막내를 TV에서 쫓아내지만, 막내가 리모콘을 줄 때까지 기다려야 한다
    - kernel data == TV 리모콘
- 일반적으로(Typically), **priority-inheritance protocol**을 구현해서 priority inversion을 방지한다
    - critical resource(임계 자원)을 보유하고 있는 task(process)가 더 높은 우선순위를 상속한다. 해당 resource를 release할 때까지
