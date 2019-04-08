
/*Open and close modal form */
$('#add-btn-applications').on('click', function(){
    $('#modal-form').show()
})

$('#modal-form-close').on('click', function(){
    $('#modal-form').hide()
})

/*APPLICATION FORM SCRIPT*/

$('#type-dropdown').change(function(){
    if($('#volumQuantity-div').css.display == 'none'){
        $('#volumQuantity-div').show()
        $('#volumQuantity-div').css.display ='block'
    } else {
        $('#volumQuantity-div').hide()
        $('#volumQuantity-div').css.display ='none'
    }
})

// Add delete products in the application form
$('#btn-add-item').on('click', addProductSelectDiv)
function addProductSelectDiv() {
    if(('#btn-delete-item') != undefined){
        $('#btn-delete-item').remove()
    }
    $('#btn-add-item').remove()
    $('#product-selection').append('<div class="product-select-div">\n' +
        '                                <label for="">Product:</label>\n' +
        '                                <select name="product-dropdown" id="" style="width:150px;">\n' +
        '                                </select>\n' +
        '                                <label for="">Quantity</label>\n' +
        '                                <input type="text">\n' +
        '                                <img id="btn-add-item" class="btn-add-application" src="/static/images/mas.png" alt="" width="20" height="20">\n' +
        '                                <img id="btn-delete-item" class="btn-delete-application" src="/static/images/delete.png" alt="" width="20" height="20">\n' +
        '                            </div>')
    newBtnListener('btn-add-item')
    newDeleteBtnListener('btn-delete-item')
}

//$('#btn-delete-item').on('click', deleteProductSelection)

function deleteProductSelection(){
    let list_psdg = jQuery.makeArray($('.product-select-div')) // list from product-select-div-group class
    console.log(list_psdg.length)
    $('.product-select-div')[list_psdg.length - 1].remove()
    list_psdg = list_psdg.slice(0,list_psdg.length - 1)
    console.log(list_psdg.length)
    var addImg = document.createElement('img')
    addImg.src ="/static/images/mas.png"
    addImg.id = 'btn-add-item'
    addImg.width = 20
    addImg.height = 20
    addImg.class = "btn-add-application"

    var addImgDel = document.createElement('img')
    addImgDel.src ="/static/images/delete.png"
    addImgDel.id = 'btn-delete-item'
    addImgDel.width = 20
    addImgDel.height = 20
    addImgDel.class = "btn-add-application"
    $('.product-select-div')[list_psdg.length - 1].append(addImg)
    newBtnListener('btn-add-item')

    if(jQuery.makeArray($('.product-select-div')).length > 1) {
        $('.product-select-div')[list_psdg.length - 1].append(addImgDel)
        newDeleteBtnListener('btn-delete-item')
    }

}

function newBtnListener(id){
    document.getElementById(id).addEventListener('click', addProductSelectDiv)
}

function newDeleteBtnListener(id){
    document.getElementById(id).addEventListener("click", deleteProductSelection)

}

