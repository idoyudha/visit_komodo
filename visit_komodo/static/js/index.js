function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function addtoWishlist(id) {
    let type = document.getElementById('type').textContent
    if (type === 'destination') {
        wishlistFetch('/destination_api_detail', id)
    }
    else if (type === 'food') {
        wishlistFetch('/food_api_detail', id)
    }
    else if (type == 'event') {
        wishlistFetch('/event_api_detail', id)
    }
    else if (type == 'travel guide') {
        wishlistFetch('/travelguide_api_detail', id)
    }
    else {
        console.log('wrong type')
    }
}

function wishlistFetch(url, id) {
    let userId = document.getElementById('userId').textContent
    let userIDInt = parseInt(userId)
    fetch(`${url}/${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let wishlist = data.wishlist
            if (wishlist.includes(userIDInt)) {
                fetch(`${url}/${id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({
                        wishlist: false
                    })
                })
                .then(response => response.json())
                .then(message => console.log('Remove from wishlist', message))
                document.getElementById('wishlist').className = 'btn btn-primary'
                document.getElementById('wishlist').textContent = 'Add to wishlist'
                document.getElementById('totalWishlist').textContent = `${wishlist.length - 1}`
            }
            else {
                fetch(`${url}/${id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify({
                        wishlist: true
                    })
                })
                .then(response => response.json())
                .then(message => console.log('Add to wishlist', message))
                document.getElementById('wishlist').className = 'btn btn-warning'
                document.getElementById('wishlist').textContent = 'Remove from wishlist'
                document.getElementById('totalWishlist').textContent = `${wishlist.length + 1}`
            }
        })
        .catch(error => console.log(error))
}

function onLoadAllFunction() {
    contrib('destination')
    getWishlist('destination')
}

function resetNav() {
    document.getElementById('contrib-destination').style.backgroundColor = 'transparent'
    document.getElementById('contrib-food').style.backgroundColor = 'transparent'
    document.getElementById('contrib-event').style.backgroundColor = 'transparent'
    document.getElementById('contrib-travelguide').style.backgroundColor = 'transparent'
    document.getElementById(`contrib-destination`).style.borderBottom = 'none'
    document.getElementById(`contrib-food`).style.borderBottom = 'none'
    document.getElementById('contrib-event').style.borderBottom = 'none'
    document.getElementById(`contrib-travelguide`).style.borderBottom = 'none'
    document.querySelector(`.contribution-destination`).style.color = '#ddd'
    document.querySelector(`.contribution-food`).style.color = '#ddd'
    document.querySelector(`.contribution-event`).style.color = '#ddd'
    document.querySelector(`.contribution-travelguide`).style.color = '#ddd'
}

function contrib(str) {
    resetNav()
    if (str == 'destination') {
        // console.log('Found destination')
        contribFetch(str)
    }
    else if (str == 'food') {
        // console.log('Found food')
        contribFetch(str)
    }
    else if (str == 'event') {
        // console.log('Found event')
        contribFetch(str)
    }
    else if (str == 'travelguide') {
        // console.log('Found travel guide')
        contribFetch(str)
    }
    else {
        console.log('NOT FOUND!!')
    }
}

function contribFetch(str) {
    let authorID = document.getElementById('userId').textContent
    document.getElementById(`contrib-${str}`).style.backgroundColor = 'rgba(13, 185, 248, 0.1)'
    document.getElementById(`contrib-${str}`).style.borderBottom = '2px solid #1DA1F2'
    document.querySelector(`.contribution-${str}`).style.color = '#1DA1F2'
    fetch(`/${str}_api`)
        .then(response => response.json())
        .then(data => {
            console.log(data.filter(data => data.author == authorID))
            let filteredData = data.filter(data => data.author == authorID)
            let result = filteredData.map((item, index) => {
                if (str === 'travelguide') {
                    return `<div class="card mb-3" style="background-color: transparent;">
                                <div class="row no-gutters">
                                <div class="col-md-4 d-none d-md-block">
                                    <img class="card-img" src="${item.image_url}" alt="..." height="100%" style="object-fit: cover;">
                                </div>
                                <div class="col-md-8 p-4">
                                    <h3 class="mb-0">${item.title}</h3>
                                    <div class="mb-1 text-muted">Last updated ${item.date_created}</div>
                                    <p class="card-text mb-auto">${item.short_description}</p>
                                    <a href="view_${str}/${item.title}">Continue reading</a>
                                </div>
                                </div>
                            </div>`
                }
                else {
                    return `<div class="card mb-3" style="background-color: transparent;">
                                <div class="row no-gutters">
                                <div class="col-md-4 d-none d-md-block">
                                    <img class="card-img" src="${item.image_url}" alt="..." height="100%" style="object-fit: cover;">
                                </div>
                                <div class="col-md-8 p-4">
                                    <h3 class="mb-0">${item.title}</h3>
                                    <div class="mb-1 text-muted">Last updated ${item.date_created}</div>
                                    <p class="card-text mb-auto">${item.description}</p>
                                    <a href="view_${str}/${item.title}">Continue reading</a>
                                </div>
                                </div>
                            </div>`
                }
            })
            document.getElementById('contrib-result').innerHTML = result.join('')
            if (filteredData.length == 0) {
                console.log('You have nothing!')
                document.querySelector('#contrib-result').innerHTML = ` <div class="text-center">
                                                                            <h3>After you post, they'll show up here</h3>
                                                                            <p>You haven't write anything yet</p>
                                                                        </div>`
            }
        })
        .catch(error => console.log(error))
}

function getWishlist(str) {
    resetNav()
    if (str === 'destination') {
        userWishlist(str)
    }
    else if (str === 'food') {
        userWishlist(str)
    }
    else if (str === 'event') {
        userWishlist(str)
    }
    else if (str === 'travelguide') {
        userWishlist(str)
    }
    else {
        console.log('NOT FOUND!!')
    }
}

function userWishlist(str) {
    let userID = parseInt(document.getElementById('userId').textContent)
    document.getElementById(`contrib-${str}`).style.backgroundColor = 'rgba(13, 185, 248, 0.1)'
    document.getElementById(`contrib-${str}`).style.borderBottom = '2px solid #1DA1F2'
    document.querySelector(`.contribution-${str}`).style.color = '#1DA1F2'
    fetch(`/${str}_api`)
        .then(response => response.json())
        .then(data => {
            console.log(data.filter(data => data.wishlist.includes(userID)))
            let filteredData = data.filter(data => data.wishlist.includes(userID))
            let result = filteredData.map((item, index) => {
                if (str === 'travelguide') {
                    return `<div class="card mb-3" style="background-color: transparent;">
                                <div class="row no-gutters">
                                <div class="col-md-4 d-none d-md-block">
                                    <img class="card-img" src="${item.image_url}" alt="..." height="100%" style="object-fit: cover;">
                                </div>
                                <div class="col-md-8 p-4">
                                    <h3 class="mb-0">${item.title}</h3>
                                    <div class="mb-1 text-muted">Last updated ${item.date_created}</div>
                                    <p class="card-text mb-auto">${item.short_description}</p>
                                    <a href="view_${str}/${item.title}">Continue reading</a>
                                </div>
                                </div>
                            </div>`
                }
                else {
                    return `<div class="card mb-3" style="background-color: transparent;">
                                <div class="row no-gutters">
                                <div class="col-md-4 d-none d-md-block">
                                    <img class="card-img" src="${item.image_url}" alt="..." height="100%" style="object-fit: cover;">
                                </div>
                                <div class="col-md-8 p-4">
                                    <h3 class="mb-0">${item.title}</h3>
                                    <div class="mb-1 text-muted">Last updated ${item.date_created}</div>
                                    <p class="card-text mb-auto">${item.description}</p>
                                    <a href="view_${str}/${item.title}">Continue reading</a>
                                </div>
                                </div>
                            </div>`
                }
            })
            document.getElementById('wishlist-result').innerHTML = result.join('')
            if (filteredData.length == 0) {
                console.log('You have nothing!')
                document.querySelector('#wishlist-result').innerHTML = ` <div class="text-center">
                                                                            <h3>After you click wishlist, they'll show up here</h3>
                                                                        </div>`
            }
        })
        .catch(error => console.log(error))
}