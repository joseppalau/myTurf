
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
        console.log($('#volumQuantity').css.display)
    } else {
        $('#volumQuantity-div').hide()
        $('#volumQuantity-div').css.display ='none'
        console.log($('#volumQuantity').css.display)
    }
})

