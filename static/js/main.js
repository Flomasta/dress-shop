const bar = document.getElementById('bar');
const nav = document.getElementById('navbar');
const close = document.getElementById('close');
('MainImg');
const small_img = document.getElementsByClassName('small-img');

// CLOSE NAV BUTTON
const MainImg = document.getElementById
if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}

if (close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}
// SIMPLE GALLERY
// small_img[0].onclick = function () {
//     MainImg.src = small_img[0].src;
//
// }
// small_img[1].onclick = function () {
//     MainImg.src = small_img[1].src;
//
// }
// small_img[2].onclick = function () {
//     MainImg.src = small_img[2].src;
//
// }
// small_img[3].onclick = function () {
//     MainImg.src = small_img[3].src;
//
// }

//CART BUTTON

let updateBtns = document.getElementsByClassName('update-cart');
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('USER', user)
        if (user === 'AnonymousUser') {
            console.log('User is not authenticated')
        } else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...')
    let url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })


}
