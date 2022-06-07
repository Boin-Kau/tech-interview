# CPU scheduling

## Basic Concepts
- CPU scehduling
    - 멀티프로그래밍 된 운영체제의 기초
    - CPU 활용도를 높이기 위한 방법
    - time-sharing
- CPU burst
    - 주로 running 상태
- I/O burst
    - 주로 wating->ready 상태
- burst time이 많으면 bound 상태
- CPU bound < I/O bound  

CPU scheduler  
- 메모리에 로드된 프로세스들 중 CPU를 할당해 줄 프로세스를 선택한다
- ready 상태에 있고, CPU를 할당(allocate)해줄 수 있는 프로세스
- next process 선택하는 방법
    - ready queue를
        - Linked List로 만든다
        - Binary Tree로 만든다
        - FIFO Queue(First In, First Out)
        - Priority Queue(프로세스의 우선 순위 부여)

Preemptive vs. Non-Preemptive
- 선점형(쫓아낼 수 o) vs. 비선점형(쫓아낼 수 x)
- Non-Preemptive scheduling
    - 프로세스가 CPU를 선점하면 그 프로세스가 release할 때까지(자발적으로 나오기 전까지) 종료(terminate)하거나 switching(waiting state로)하지 않는다
- Preemptive scheduling
    - 스케줄러가 프로세스를 쫓아낼 수 있다

Decision Making for CPU-scheduling
1. running -> waiting 상태로 이동
2. running -> ready
3. waiting -> ready
4. terminate  
1 & 4: 선택지 x - non-preemptive  
2 & 3: 선택지 o - **preemptive** or non-preemptive

dispatcher
- CPU core의 컨트롤을 넘겨주는 모듈  
=> context switch를 해주는 모듈
- context를 한 프로세스에서 다른 프로세스로 넘겨준다
- **user mode**로 바꿔준다
- 새로운 프로세스의 적당한 위치로 resume시킨다
- 매우 빨라야 한다 **as fast as possible** => context switch마다 일어나기 때문
- PCB0을 저장하고 PCB1을 불러와서 context switch
- dispatch latency
    - PCB0의 context saving과 PCB1의 context restoring을 하는 시간
    - 한 프로세스를 멈추고 다른 프로세스를 실행시키는 시간  

*+* 얼마나 자주 context switch가 일어나는지 확인
- vmstat 1 3 (1초마다 3개씩)
- cat /proc/1/status | grep ctxt

<br>

scheduler와 dispatcher의 역할은 다르다.
- scheduler: 프로세스를 선택하는 것
- dispatcher: 실제 switch 해주는 것
- dispatcher ⊂ scheduler

<br>

## Scheduling Criteria 
- 스케줄링 기준/목표
- CPU utilization - 가능한 CPU를 바쁘게 유지
- Throughput 향상 - 단위 시간 내에 프로세스가 완료되는 수를 높인다
- *Turnaround time
    - 프로세스의 실행에서 종료까지의 시간을 최소화
- ****Waiting time**
    - 프로세스가 ready queue에서 대기하는 시간을 최소화한다
    - ready queue 대기시간을 합친 시간을 최소화
- **Response time
    - 응답하는 시간을 최소화

<br>

## Scheduling Algorithms
CPU Scheduling Problem
: ready queue에 있는 프로세스들 중 어떤 프로세스에게 CPU core를 할당해 줄 것인가  

### The solutions for the scheduling problem
- FCFS: First-come, Firest-Served
    - 가장 간단한 CPU 스케줄링 알고리즘
    - CPU를 먼저 요청한 프로세스에게 무조건 배정해줌
    - FIFO queue에 들어온 순으로 처리(구현 쉬움)
    - 평균 대기 시간이 길다
    - CPU-burst time에 따라 대기 시간이 크게 달라진다
    - non-preemptive
    - Convoy Effect (똥차 효과)
        - 이것 때문에 FCFS로는 좋은 효율을 얻을 수 x
    - 아주 초창기 운영체제에서만 썼음
- SJF: Shortest Job First  (SRTF: Shortest Remaining Time First)
    - shortest-next-CPU-burst-first scheduling
    - 각 프로세스의 next CPU burst 길이와 연관
    - CPU가 사용가능할 때, next CPU burst가 가장 작은 프로세스를 배정한다(오는 순서에 무관하게)
    - 프로세스별 CPU burst가 같은 경우에 FCFS
    - provably optimal (최적임을 증명 가능)
    - minimum average (최소 대기 시간)
    - **next CPU burst를 알 수 없음**
    - SJF scheduling을 엄격하게 적용할 수는 없고 approximate(근사치) 하자
        - next CPU 길이를 예측
        - 이전 CPU burst 측정 길이로 지수 평균(exponential average)을 낸다
    - 이론적으로 optimal일 뿐, 실제로 사용하지는 않는다(실제 사용하기 어려움)
    - preemptive or non-preemptive
    - SRTF Scheduling: Preemptive SJF scheduling
        - 새로 도착한 CPU burst가 running중인 프로세스의 remaining time보다 짧으면 선점시켜서 프로세스를 쫓아낸다
        - SJF는 프로세스 끝날 때까지 기다리는 반면, SRTF는 쫓아낸다
- FCFS, SJF - 프로세스 전체 시간을 다 할당해줌
- **RR**: Round-Robin
    - **time-sharing**(시분할)
    - **preemptive FCFS** with a **time quantum**(time slice)
    - 시간 단위를 줘서 시간 단위를 채우면 빠져나온다. time quantum은 보통 10-100ms
    - circular queue로 구현
    - 스케줄러가 ready queue를 돌면서 time quantum을 간격으로 두고 CPU를 각 프로세스에 넘겨준다
    - CPU burst가 time quantum보다 짧은 경우
        - 프로세스 자체가 CPU를 자발적으로 release(해제)한다
        - 스케줄러는 ready queue의 다음 프로세스로 진행한다
    - - CPU burst가 time quantum보다 긴 경우
        - 타이머가 꺼지고 OS에 interrupt 발생시킨다
        - context switch가 실행된다
        - 프로세스는 ready queue의 맨 뒤에 들어가서 대기한다
    - RR policy에서 평균 대기 시간은 길 수 있다
    - preemptive
    - time quantum의 크기에 따라 스케줄러 성능이 매우 달라진다
    - 반드시 적용되는 알고리즘, 현대 컴퓨터 운영체제에서 사용
- Priority-based
    - RR을 쓰는데, 다음 프로세스 선택에 있어서 우선순위를 부여
    - 높은 우선순위 순으로 CPU에 할당하는데, 우선순위가 같은 경우 FCFS
    - SJF가 priority-based scheduling
        - CPU burst가 클수록 우선순위가 높다
    - preemptive(SRTF) of non-preemptive(SJF)
    - **starvation** 문제 - indefinite blocking(무한대 대기)  
        -> **aging**으로 해결
        - 오래 기다리는 프로세스의 우선순위를 점차 높여준다
- MLQ: Multi-Level Queue
    - 경우에 따라 다르게(멀티 레벨로)
    - 분리된 ready queue에 각각의 priority 부여
    - 낮은 우선순위가 실행안될 수 있음 => Feedback 부여
- MLFQ: Multi-Level Feedback Queue
    - MLQ에 피드백 추가
    - Feedback - 높은 우선순위일수록 quantum을 짧게, 순위가 낮을수록 quantum 길게, 더 낮을수록 FCFS
    - 현대적인 스케줄러의 모습  

현대 OS: MLFQ + MultiCore

<br>

## Thread Scheduling
현대 OS는 프로세스 스케줄링을 하지 않고 Thread Scheduling 함(스레드를 지원하니까)
- kernel thread만 스케줄링 하면 된다
- user thread는 thread library가 관리하지, 유저 스레드는 어떤 게 도는지 모른다  
    -> mapping(user thread <-> kernal thread)만 해주면 됨
- OS kernal에서 CPU scheduling은 kernal thread로 스케줄링 한다

<br>

## Real-Time CPU Scheduling
Real-Time(실시간) 운영체제에서의 스케줄링
- 실시간: 주어진 시간 내에 task를 완료할 수 있음
- Soft realtime
    - critical한 realtime 프로세스가 반드시 그 시간을 보장할 수 없지만, noncritical보다는 빠른 수행을 보장한다.
- Hard Realtime
    - deadline 안에 반드시 task를 수행해야 한다
- Priority로 스케줄링
- Priority inversion(우선순위 역전)