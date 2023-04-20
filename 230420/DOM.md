##### DOM

- Brower APIs
  
  웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나 오디오를 재상하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함

- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음



**브라우저가 웹페이지를 불러오는 과정**

- 웹페이지를 브라우저로 불러오면 브라우저는 코드를 실행 환경에서 실행

- 자바스크립트는 DOM API를 통해 html과 css를 동적으로 수정, 사용자 인터페이스를 업데이트하는데 사용



**DOM**

- 문서 객체 모델(Document Object Model)

- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법을 제공
  
  - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
  
  - html콘텐츠를 추가, 제거, 변경하고 동적으로 페이지에 스타일을 추가하는 등 html/css를 조작할 수 있음

- HTML문서를 구조화하여 각 요소를 객체로 취급

- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언으적 특성을 활용한 조작이 가능함

- DOM은 문서를 논리 트리로 표현

- DOM메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고, 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음

- 웹 페이지는 일종의 문서. 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 html코드 자체로 나타나기도 함

- DOM은 동일한 문서를 표현, 저장, 조작하는 방법을 제공

- DOM은 웹 페이지의 객체 지향 표현



**DOM의 기본 구조**

- DOM tree
  
  - DOM은 문서를 논리 트리로 표현
  
  - DOM에서 모든 것은 노드(HTML요소, 속성, 텍스트 모든 것이 노드)
  
  - 각 노드는 부모, 자식 관계를 형성하고 이에 따라 상속 개념도 동일하게 적용됨
  
  - Node : HTML문서의 모든 요소를 나타냄



- DOM의 주요 객체
  
  - window
    
    - DOM을 표현하는 창
    
    - 가장 최상위 객체(작성시 생략 가능)
    
    - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
  
  - document
    
    - 브라우저가 불러온 웹 페이지
    
    - 페이지 컨텐츠의 진입점 역할. body등과 같은 수많은 다른 요소들을 포함하고 있음
    
    - document는 window의 속성이다





##### DOM 조작

- DOM 조작 순서
  
  1. 선택
  
  2. 조작

- 선택 관련 메서드
  
  - document.querySelector(selector)
    
    - 제공한 선택자와 일치하는 element한 개 선택
    
    - 제공한 CSS selector을 만족하는 첫번째 element 객체를 반환(없다면 null 반환)
  
  - document.querySelectorAll(selector)
    
    - 제공한 선택자와 일치하는 여러 element를 선택
    
    - 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    
    - 제공한 CSS selector를 만족하는 nodelist(유사 배열)를 반환
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-09-35-53-image.png)



*[참고] Nodelist*

- DOM 메서드를 사용해 선택한 노드의 목록

- 배열과 유사한 구조를 가짐

- index로만 각 항목에 접근 가능

- 배열의 forEach메서드 및 다양한 배열 메서드 사용 가능

- querySelectorAll()에 의해 반환되는 Nodelist는 DOM의 변경사항을 실시간으로 반영하지 않음





- 조작 관련 메서드(생성)
  
  - document.createElement(tagname)
    
    - 작성한 태그네임의 html요소를 생성하여 반환
  
  - HTMLelement.innerText
    
    - Node 객체와 그 자손의 텍스트 컨텐츠를 표현
    
    - 사람이 읽을 수 있는 요소만 남김
    
    - 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-10-08-27-image.png)
  
  - Node.appendChild()
    
    - 한 노드를 특정 부모 노드의 자식 노드리스트 중 마지막 자식으로 삽입
    
    - 한번에 오직 하나의 노드만 추가할 수 있음
    
    - 추가된 노드 객체를 반환

- 조작 관련 메서드(삭제)
  
  - Node.removeChild()
    
    - DOM에서 자식 노드를 제거
    
    - 제거된 노드를 반환
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-09-45-28-image.png)



*[참고] Node.appendchile*

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-09-51-43-image.png)



- 속성 조회 및 실습
  
  - Element.getAttribute(attributeName)
    
    - 해당 요소의 지정된 값(문자열)을 반환
    
    - 인자는 값을 얻고자 하는 속성의 이름
  
  - Element.setAttribute(name, value)
    
    - 지정된 요소의 값을 설정
    
    - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-10-15-37-image.png)

*[참고] 그 외 다양한 속성 조작 방법*

- Element.setAttribute(name, value)
  
  - 해당 속성이 이미 존재하는 경우 갱신 >  새로운 값을 추가 또는 수정이 아닌 주어진 value로 새롭게 설정
  
  - 기존 속성을 유지한 채로 새로운 값을 추가하고자 한다면
    
    Element.classList, Element.style 등을 통해 직접적으로 해당 요소의 각 속성들을 제어할 수 있음
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2023-04-20-10-40-15-image.png)
