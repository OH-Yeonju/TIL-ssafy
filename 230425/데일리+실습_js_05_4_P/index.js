/* 
  아래에 코드를 작성해주세요.
*/

const searchBtn = document.querySelector('.search-box__button')



const fetchAlbums = function(page=1, limit=10) {
  const keyword = document.querySelector('.search-box__input').value
  const params = {
    api_key: '465ee120205d1b2a09a20873843f5492',
    album : keyword
  }
  const musicURL = 'https://ws.audioscrobbler.com/2.0/?method=album.search&format=json'

  axios({
    method:'get',
    url:musicURL,
    params
  })
  .then(response => {
    const albums = response.data.results.albummatches.album
    return albums
  })
  .then(albums => {
    for (albumInfo of albums) {
      const name = document.createElement('h2')
      name.innerText = albumInfo.artist

      const albumname = document.createElement('p')
      albumname.innerText = albumInfo.name

      const resulttext = document.createElement('div')
      resulttext.setAttribute('class', 'search-result__text')

      const image = document.createElement('img')
      image.setAttribute('src', albumInfo.image[1]['#text'])

      const resultcard = document.createElement('div')
      resultcard.setAttribute('class', 'search-result__card')

      resulttext.appendChild(name)
      resulttext.appendChild(albumname)
      resultcard.appendChild(image)
      resultcard.appendChild(resulttext)
      
      const searchresult = document.querySelector('.search-result')
      searchresult.appendChild(resultcard)
      
    }
  })
  .catch(error => {
    alert('잠시 후 다시 시도해주세요')
})
}

searchBtn.addEventListener('click', fetchAlbums)