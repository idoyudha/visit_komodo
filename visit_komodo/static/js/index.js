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
    let text = document.getElementById('wishlist').textContent
    let type = document.getElementById('type').textContent
    let userId = document.getElementById('userId').textContent
    let userIDInt = parseInt(userId)
    if (text === 'Add to wishlist') {
        document.getElementById('wishlist').className = 'btn btn-warning'
        document.getElementById('wishlist').textContent = 'Remove from wishlist'
    }
    else {
        document.getElementById('wishlist').className = 'btn btn-danger'
        document.getElementById('wishlist').textContent = 'Add to wishlist'
    }
    if (type === 'destination') {
        fetch(`/destination_api_detail/${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            let wishlist = data.wishlist
            console.log('user wishlist', wishlist)
            if (wishlist.includes(userIDInt)) {
                console.log('Already wishlist')
                fetch(`/destination_api_detail/${id}`, {
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
            }
            else {
                console.log('Not yet wishlist')
                fetch(`/destination_api_detail/${id}`, {
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
            }
        })
        .catch(error => console.log(error))
    }
    else if (type === 'food') {

    }
    else if (type == 'event') {

    }
    else if (type == 'travel guide') {

    }
    else {
        console.log('wrong type')
    }
}
