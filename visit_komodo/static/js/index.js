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
                document.getElementById('wishlist').className = 'btn btn-danger'
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