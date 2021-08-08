// 팝업창 모달 토글
career_btn = document.querySelectorAll('.career_info')
popup_wrapper = document.querySelector('.popup_wrapper')
popup_bg = document.querySelector('.popup_bg')
close_btn = document.querySelector('.close_btn')
html = document.querySelector('html')
body = document.querySelector('body')
const popUpWindow = document.querySelector('.popup_window')
for (i = 0; i < career_btn.length; i++) {
    career_btn[i].addEventListener('click', function () {
        popup_wrapper.classList.toggle('hidden');
        notice_list(this.dataset.team)
        console.log(document.scrollingElement.scrollTop)
        popUpWindow.style.top = `${((window.innerHeight - popUpWindow.offsetHeight) / 2) + document.scrollingElement.scrollTop}px`
        popUpWindow.style.left = `${(window.innerWidth - popUpWindow.offsetWidth) / 2}px`
        html.style.overflow = 'hidden'
        body.style.overflow = 'hidden'
    })
}
close_btn.addEventListener('click', () => {
    popup_close()
})
popup_bg.addEventListener('click', () => {
    popup_close()


})
function popup_close() {
    popup_wrapper.classList.add('hidden')
    html.style.overflow = 'scroll'
    body.style.overflow = 'scroll'
}

// 팝업창 모집 리스트 불러오기

function notice_list(team_pk) {
    var wrapper = document.querySelector('.tab_left > ul')
    wrapper.innerHTML = ''
    let url = `/api/notice_list/${team_pk}`
    console.log(url)
    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            console.log('data: ', data)
            var list = data
            for (var i in list) {
                var item = `<li class='notice_item' data-content='${list[i].id}'><h5>${list[i].title}</h5><span>${list[i].manpower}명 모집 중</span></li>`
                wrapper.innerHTML += item
            }
        })
        .then(() => {
            var notices = document.querySelectorAll('.notice_item')
            for (o = 0; o < notices.length; o++) {
                notices[o].addEventListener('click', function () {
                    notice_detail(this.dataset.content)
                })
                notice_detail(notices[o].dataset.content)
            }
        })
}

// 모집공고 상세 불러오기
function notice_detail(notice_pk) {
    var content_wrapper = document.querySelector('.tab_content')
    content_wrapper.innerHTML = ''
    let content_url = `/api/notice_detail/${notice_pk}`
    fetch(content_url)
        .then((resp) => resp.json())
        .then(function (data) {
            content_wrapper.innerHTML = data.msg
        })
}