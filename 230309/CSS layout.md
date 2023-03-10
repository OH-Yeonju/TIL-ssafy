##### float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함

- 요소가 normal flow를 벗어나도록 함

- float속성
  
  - none : 기본값
  
  - left : 요소를 왼쪽으로 띄움
  
  - right:      "     오른쪽     "

- 과거에는 레이아웃을 구성하기 위해 필수적으로 활용되었으나 최근 flexbox, grid 등장과 함께 사용도가 낮아짐

- float 활용전략 - normal flow에서 벗어난 레이아웃 구성
  
  - 원하는 요소들을 float로 구성하여 배치

##### flexbox

- css flexble box layout
  
  (수동 값 부여 없이)
  
  1. 수직 정렬
  
  2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치
  
  행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  
  - 축
    
    main axis(메인 축)
    
    cross axis(교차 축)
  
  - 구성 요소
    
    Flex Container(부모 요소)
    
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    
    - flex item들이 놓여있는 영역
    
    - display 속성을 flex 혹은 inline-flex로 지정
    
    Flex Item(자식 요소)

- flex 속성
  
  justify > 메인축기준, align > 교차축기준
  
  - 배치 설정
    
    - flex-direction
    
    - flex-wrap
  
  - 공간 나누기
  
  - 정렬
  
  
