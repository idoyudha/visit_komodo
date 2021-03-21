function showForm() {
    let val = document.getElementById('profile-form')
    if (val.style.display === 'none') {
        val.style.display = 'block'
    } 
    else {
        val.style.display = 'none'
    }
}

function cancelBtn() {
    document.getElementById('profile-form').style.display = 'none'
}