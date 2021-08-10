html = document.querySelector('html')
body = document.querySelector('body')
popup_btn = document.querySelectorAll('.popup_btn')
for (let i = 0; i < popup_btn.length; i++) {
    (function (idx) {
        popup_btn[idx].onclick = () => {
            console.log(popup_btn[i].dataset.popup)
            popup_wrapper = document.querySelector(`.${popup_btn[i].dataset.popup}`)
            popUpWindow = document.querySelector(`.${popup_btn[i].dataset.popup} .popup_window`)
            popup_bg = document.querySelector(`.${popup_btn[i].dataset.popup} .popup_bg`)
            close_btn = document.querySelector(`.${popup_btn[i].dataset.popup} .close_btn`)
            console.log(close_btn)
            popup_wrapper.classList.toggle('hidden');
            popup_bg_modify()
            close_btn.addEventListener('click', () => {
            popup_close()
            })
            popup_bg.addEventListener('click', () => {
                popup_close()
            })
        }
        function popup_close() {
            popup_wrapper.classList.add('hidden')
            html.style.overflow = 'scroll'
            body.style.overflow = 'scroll'
        }
        function popup_bg_modify() {
            console.log(document.scrollingElement.scrollTop)
            popUpWindow.style.top = `${((window.innerHeight - popUpWindow.offsetHeight) / 2) + document.scrollingElement.scrollTop}px`
            popUpWindow.style.left = `${(window.innerWidth - popUpWindow.offsetWidth) / 2}px`
            html.style.overflow = 'hidden'
            body.style.overflow = 'hidden'
        }
    })(i);
}