function productFormOpen(btn){
    let btnList = Array.from(document.getElementsByClassName('add-btn'))
    let btnIndex = btnList.indexOf(btn)
    console.log(btnIndex)
    $('#modal-form').show()
}

$('#modal-form-close').on('click', function(){
    $('#modal-form').hide()
})

