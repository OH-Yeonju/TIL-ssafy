**State Management**

- 상태 : 현재에 대한 정보(data)

- 각 component는 독립적이기 때문에 각각의 상태를 가짐
  
  \> 이런 component들이 모여서 하나의 앱을 구성할 예정이기 때문에 여러개의 컴포넌트가 같은 상태를 유지할 필요가 있음 => 상태 관리 필요



**Pass Props & Emit Event**

- 같은 데이터를 공유하고 있으므로 각 컴포넌트가 동일한 상태를 유지하고 있음 > 데이터 흐름 직관적 파악 가능

- 그러나 component의 중첩이 깊어지면 데이터 전달이 쉽지 않음

- 공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐



**Centralized Store**

- 중앙 저장소에 데이터를 모아서 상태 관리

- 각 컴포넌트는 중앙 저장소의 데이터를 사용

- 컴포넌트의 계층에 상관없이 중앙 저장소에 젖ㅂ근해서 데이터를 얻거나 변경할 수 있음

- 중앙 저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함

- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리



**Vuex**

- state management pattern + library
  
  상태 관리 패턴 + 라이브러리

- 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리

- 데이터가 예측 가능한 방식으로만 변경될 수 있도록 하는 규칙을 설정하며 vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공



**Vue와 Vuex 인스턴스 비교**

- state - data
  
  getters - computed
  
  mutations, actions - methods



1. State
   
   - vue 인스턴스의 data에 해당
   
   - 중앙에서 관리하는 모든 상태 정보
   
   - 개별 componenet는 state에서 데이터를 가져와서 사용
     
     - 개별 component에서 관리하던 data를 중앙 저장소에서 관리하게 됨
   
   - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component는 자동으로 다시 렌더링
   
   - $store.state로 state데이터에 접근

2. Mutations
   
   - 실제로 state를 변경하는 유일한 방법
   
   - vue인스턴스의 methods에 해당하지만 mutations에서 호출되는 경우 핸들러 함수는 반드시 동기적이어야 함
     
     - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
   
   - 첫 번째 인자로 state를 받으며, componenet 혹은 actions에서 commit() 메서드로 호출됨

3. Actions
   
   - mutations와 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음
   
   - state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 state를 변경함
   
   - context객체를 인자로 받으며 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음(즉, state를 직접 변경할 수 있지만 하지 않아야 함)
   
   - component에서 dispatch('액션 이름') 메서드에 의해 호출됨



**Mutations & Actions**

- mutations :  state를 변경

- Actions : state변경을 제외한 나머지 로직



4. Getters
   
   - vue 인스턴스의 computed에 해당
   - state를 활용하여 계산된 값을 얻고자 할 때 사용
     
     state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
   - computed와 마찬가지로 getters의 결과는 캐시되며 종속된 값이 변경된 경우에만 재계산됨
   - getters에서 계산된 값은 state에 영향을 미치지 않음
   - 첫번째 인자로 state, 두번째 인자로 getter를 받음



[정리]

- component에서 데이터를 조작하기 위한 데이터의 흐름
  
  component => (actions) => mutations => state

- component에서 데이터를 사용하기 위한 데이터의 흐름
  
  state => (getters) => component
