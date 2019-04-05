
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
}

function deleteProductSelection(){
    let arrayProducts = jQuery.makeArray($('.product-select-div'))

}


function newBtnListener(id){
    document.getElementById(id).addEventListener('click', addProductSelectDiv)
}

