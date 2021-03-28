function addtoWishlist(id) {
    let text = document.getElementById('wishlist').textContent
    let type = document.getElementById('type').textContent
    console.log(type, id)
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
        .then(data => console.log(data))
        .catch(error => console.log(error))
    }
    else if (type === 'food') {
        fetch(`/food_api_detail/${id}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
    }
    else if (type == 'event') {
        fetch(`/event_api_detail/${id}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
    }
    else if (type == 'travel guide') {
        fetch(`/travelguide_detail/${id}`)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.log(error))
    }
    else {
        console.log('wrong type')
    }
}
