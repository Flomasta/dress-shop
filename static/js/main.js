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

//Menu active
const menuItems = document.querySelectorAll('.main-menu-item a')
removeActiveClasses()
for (let menuItem of menuItems) {
    if (menuItem.href === location.href) {
        menuItem.classList.add('active')
    }

}

function removeActiveClasses() {
    menuItems.forEach((menuItem) => {
        menuItem.classList.remove('active')
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

//CART ADD BUTTON

let updateBtns = document.getElementsByClassName('update-cart');
for (let item of updateBtns) {
    item.addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        if (user === 'AnonymousUser') {
            addCookieItem(productId, action)
        } else {
            updateUserOrder(productId, action)
        }

    })
}

function addCookieItem(productId, action) {
    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity': 1}
        } else {
            cart[productId]['quantity']++
        }
    }
    if (action == 'remove') {
        cart[productId]['quantity']--
        if (cart[productId]['quantity'] <= 0) {
            delete cart[productId]
        }
    }
    if (action == 'delete_item') {
        delete cart[productId]
    }
    // console.log(`'cart=' + ${JSON.stringify(cart)} + ";domain=;path=/"`)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
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
