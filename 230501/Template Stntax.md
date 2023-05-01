##### Template Stntax

- 렌더링 된 DOM을 기본 뷰 인스턴스의 데이터에 선언적으로 바인딩 할 수 있는 HTML기반 template syntax를 사용

**Text Interpolation**

**RAW HTML**

**Directives**

- 표현식의 값이 

- 기본 구성
  
  v-on:submit.prevent="onSubmit"
  
  - ':'을 통해 전달인자를 받을 수 있음
  
  - '.'으로 표시되는 특수 접미사 -directive 를 특별한 방법으로 바인딩

- 새 vue instance 생성
  
  - 각각의 instance들은 연결된 DOM element에만 영향을 미침
  
  - 연결되지 않은 DOM이 Vue의 영향을 받지 않았던 것과 동일한 상황

- v-text
  
  - template interpolation과 함꼐 가장 기본적인 바인딩 방법
  
  - {{}}와 동일한 역할

- v-html
  
  - RAW HTML을 표현할 수 있는 방법
  
  - 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지

- v-show
  
  - 표현식에 작성된 값에 따라 element를 보여줄 것인지 결정
    
    - boolean값이 변경될때마다 반응
  
  - 대상 element의 display속성을 기본 속성과 none으로 toggle
  
  - 요소 자체는 항상 DOM에 렌더링 됨
  
  - 값이 false인 경우 화면에서만 사라졌을 뿐 DOM에는 존재한다
  
  - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음
  
  - display속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle비용은 적음

- v-if
  
  - v-show와 사용 방법은 동일
  
  - isActive의 값이 변경될 때 반응
  
  - 단, 값이 false인 경우 사라짐
  
  - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음
  
  - 단 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

- v-for
  
  - for .. in..형식으로 작성
  
  - 반복한 데이터 타입에 모두 사용 가능
  
  - index를 함께 출력하고자 한다면 (char, index)형태로 사용 가능
  
  - 배열 역시 문자열과 동일하게 사용 가능
  
  - 각 요소가 객체라면 dot notation으로 접근할 수 있
    
    *[참고 ] 특수 속성 key*
    
    - v-for 사용 시 반드시 key속성을 각 요소에 작성
    
    - 주로 v-for directive작성 시 사용
    
    - vue화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용 > 따라서 key가 중복되어서는 안됨
    
    - 각 요소가 고유한 값을 가지고 있다면 생략할 수 있음
  
  - 객체 순회 시 value가 할당되어 출력
  
  - 2번째 변수 할당 시 key출력 가능

- v-on
  
  - ':'를 통해 전달받은 인자를 확인
  
  - 값으로 JS표현식 작성
  
  - addEventListener의 첫번째 인자와 동일한 값들로 구성
  
  - 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
  
  - method를 통한 data조작도 가능
  
  - method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
  
  - ':'을 통해 전달된 인자에 따라 특별한 modifier(수식어)가 있을 수 있음
    
    ex) v-on:keyup.enter 등
  
  - '@' shortcut 제공
    
    ex) @keyup.click

- v-bind
  
  - html기본 속성에 vue data를 연결
  
  - class의 경우 다양한 형태로 연결 가능
    
    - 조건부 바인딩
      
      - {'class Name':'조건 표현식'}
      
      - 삼항 연산자도 가능
    
    - 다중 바인딩
      
      - ['JS표현식','JS표현식', ...]
  
  - ':' : shortcut 제공
    
    ex) :class 등



**computed**

- vue instance가 가진 options중 하나
- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
  - 계산 결과가 변하기 전까지 함수를 재호출하는것이 아닌 계산된 값을 반환



**methods vs computed**

- methods
  
  - 호출될때마다 함수를 실행
  
  - 같은 결과여도 매번 새롭게 계산

- computed
  
  - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
  
  - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환



**watch**

- 특정 데이터의 변화를 감지하는 기능
  
  1. watch 객체를 정의
  
  2. 감시할 대상 data를 지정
  
  3. data가 변할 시 실행할 함수를 정의

- 첫번째 인자는 변동 후 data

- 두번째 인자는 변동 전 data





**filter**

- 텍스트 형식화를 적용할 수 있는 필터

- interpolation 혹은 v-bind를 이용할 때 사용 가능

- 필터는 자바스크립트 표현 마지막에 |





v-for는 항상 key와 함께 사용하기

v-for를 쓴 엘리먼트에 절대 v-if를 사용하지 말기
