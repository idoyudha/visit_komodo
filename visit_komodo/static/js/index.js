function addtoWatchlist(id) {
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
    fetch()
}
