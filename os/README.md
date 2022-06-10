# OS 스터디 

## 학습자료
- [인프런 운영체제 공룡책 강의](https://www.inflearn.com/course/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-%EA%B3%B5%EB%A3%A1%EC%B1%85-%EC%A0%84%EA%B3%B5%EA%B0%95%EC%9D%98)
- [Operating-System-Concepts-10th-edition](https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf)
- [참고 블로그1](https://parksb.github.io/article/5.html)

## 면접 예상질문
<details>
<summary>프로세스 생성 과정에 대해서 설명해보세요.</summary>
<div markdown="1">
  
- 일반적인 프로세스 생성 과정
  - PCB가 생성되며 OS가 실행한 프로그램의 코드를 읽어들여 프로세스에 할당된 메모리의 Text segment에 저장한다.
  - 초기화된 전역 변수 및 static 변수를 data segment에 할당.
  - HEAP과 Stack은 초기 메모리 주소만 초기화됨.
  - PCB에 여러 정보가 기록되면 Ready Queue에서 CPU를 할당받기까지 대기한다.

</div>
</details>

<details>
<summary>프로세스와 쓰레드의 차이를 설명해보세요.</summary>
<div markdown="1">
  
- 프로세스는 실행되는 프로그램 자체와 프로그램이 실행되는 주변 환경을 포함하는 개념이다. 실행되는 주변 환경이란 사용중인 파일, 데이터, 메모리 영역 주소 공간등을 뜻한다.
- 쓰레드는 프로세스 내부에서 프로세스의 자원을 공유하거나 공유하지 않고 실행되는 작업의 단위이다.
  
- 프로세스는 실행중인 프로그램을 의미합니다. 스레드는 실행 제어만 분리한 것을 의미합니다.
- 프로세스는 운영체제로부터 자원을 할당받지만, 스레드는 프로세스로부터 자원을 할당받고, 프로세스의 코드/데이터/힙영역을 공유하기 때문에 좀 더 효율적으로 통신할 수 있습니다. 또한 컨텍스트 스위칭도 캐시 메모리를 비우지 않아도 되는 스레드쪽이 빠릅니다. 그리고, 스레드는 자원 공유로 인해 문제가 발생할 수 있으니 이를 염두에 둔 프로그래밍을 해야합니다.
- 한 프로세스 안에 여러개의 스레드가 생성될 수 있습니다.

</div>
</details>

<details>
<summary>크롬 탭이 프로세스인지 쓰레드인지 설명해보세요.</summary>
<div markdown="1">
  
- 크롬은 탭마다 PID를 가지고 있으니 Process이며 각 Tab마다 랜더링 정보나 기타 데이터를 따로 관리한다고 한다. 그로인해 메모리를 많이 잡아먹기도 하지만 하나의 Tab에 오류가 생겼다고 모든 Tab에 영향을 끼치진 않는다.

</div>
</details>

<details>
<summary>컨텍스트 스위칭에 대해 설명해보세요.</summary>
<div markdown="1">
  
- 컨텍스트 스위칭은 한 Task가 끝날 때까지 기다리는 것이 아니라 여러 작업을 번갈아가며 실행해서 동시에 처리될 수 있도록 하는 방법입니다.
- 인터럽트가 발생하면 현재 프로세스의 상태를 PCB에 저장하고 새로운 프로세스의 상태를 레지스터에 저장하는 방식으로 동작합니다. 이 때, CPU는 아무런 일을 하지 않으므로 잦은 컨텍스트 스위칭은 성능저하를 일으킬 수 있습니다.
- 스레드와 프로세스의 동작방식이 약간 상이한데, 스레드는 캐시메모리나 PCB에 저장해야하는 내용이 적고, 비워야 하는 내용도 적기때문에 상대적으로 더 빠른 컨텍스트 스위칭이 일어날 수 있습니다.

</div>
</details>

<details>
<summary>동기와 비동기의 차이(블로킹, 넌블로킹) / 장단점에 대해 설명해보세요.</summary>
<div markdown="1">
  
- 동기/비동기는 두 개 이상의 무엇인가가 시간을 맞춘다/안맞춘다로 구분할 수 있습니다.
- 동기 방식은 메서드 리턴과 결과를 전달받는 시간이 일치하는 명령 실행 방식입니다. 또, 동기 방식은 한 함수가 끝나는 시간과 바로 다음의 함수가 시작하는 시간이 같습니다.
- 비동기 방식은 여러 개의 처리가 함께 실행되는 방식으로, 동기 방식에 비해 단위시간 당 많은 작업을 처리할 수 있습니다. 단, CPU나 메모리를 많이 사용하는 작업을 비동기로 처리하게 되면 과부하가 걸릴 수 있습니다. 프로그램의 복잡도도 증가하게 됩니다.
- 블로킹/논블로킹은 동기/비동기와는 다른 관점으로, 내가 직접 제어할 수 없는 대상(IO/멀티스레드)을 상대하는 방법에 대한 분류입니다.
- 블로킹 방식은 대상의 작업이 끝날 때 까지 제어권을 대상이 가지고 있는 것을 의미합니다. 반면에 논블로킹은 대상의 작업 완료여부와 상관없이 새로운 작업을 수행합니다.
- 동기 논블로킹은 계속해서 polling을 수행하기 때문에 컨텍스트 스위칭이 지속적으로 발생해 지연이 발생합니다.
- https://youtu.be/HKlUvCv9hvA 를 참고합시다.

</div>
</details>

<details>
<summary>동일 Process내에 있는 두개의 Threads간에 context switch가 일어날 때 어떤 정보들이 save되고 restore 될 필요가 있나요?</summary>
<div markdown="1">
  
- stack 영역을 제외한 모든 메모리 영역을 공유하므로, TCB 관련 정보인 pc, registers, stack pointer만 save & restore 되면 된다. 

</div>
</details>

<details>
<summary>두 Threads가 서로 다른 processes에 속해 있을 때 context switch될 때 어떤 정보들이 save되고 restore될 필요가 있나요?</summary>
<div markdown="1">
  
- process context-switching이 발생해야 하므로, PCB(Process state, Process number, pc, registers, CPU scheduling information 등)와 TCB 관련 정보 모두 save & restore 되어야 한다. 

</div>
</details>

<details>
<summary>Thread-safe의 개념에 대해 설명하세요.</summary>
<div markdown="1">
  
- Thread safe는 멀티 스레드 프로그래밍 환경에서 일반적으로 어떤 함수나 변수, 혹은 객체가 여러 스레드로부터 동시에 접근이 이루어져도 프로그램의 실행에 문제가 없는 것을 말한다.

- Thread-safe한 코드를 만들기 위해서는 Critical Section(임계 영역)을 동기화 기법으로 제어한다. 이를 상호 배제(mutual exclusion)라 한다.

</div>
</details>

<details>
<summary>교착상태(deadlock)가 무엇인지, 그리고 발생하는 조건을 설명하세요.</summary>
<div markdown="1">
  
- 두 개 이상의 프로세스나 스레드가 서로 자원을 기다리면서 무한히 기다리게 되는 상태를 말한다.
- 상호 배제(mutual exclusion), 점유 대기(hold and wait), 비선점(non preemptive), 순환 대기(circle wait) 네 가지 조건을 모두 만족해야 교착 상태가 발생한다. 순환 대기의 경우 점유 대기와 비선점 조건을 만족해야 성립하므로 4가지 조건은 완전히 서로 독립적이지 않다.

</div>
</details>

<details>
<summary>세마포어(Semaphore)와 뮤텍스(Mutex)의 차이를 설명하세요.</summary>
<div markdown="1">
  
- 뮤텍스는 Locking 메커니즘으로 락을 걸은 쓰레드만이 임계 영역을 나갈때 락을 해제할 수 있다. 하지만 세마포어는 Signaling 메커니즘으로 락을 걸지 않은 쓰레드도 signal을 사용해 락을 해제할 수 있다. 세마포어의 카운트를 1로 설정하면 뮤텍스처럼 활용할 수 있다.

</div>
</details>