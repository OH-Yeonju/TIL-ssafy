axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response)
})

// 동기 : 요청한 순서대로 처리한다
// 비동기 : 요청한 결과를 기다리지 않고 처리한다. 시간이 걸리는 요청이 있을 경우 응답이 빨리 오는 순으로 처리한다