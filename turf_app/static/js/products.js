function productFormOpen(btn){
    let btnList = Array.from(document.getElementsByClassName('add-btn'))
    let btnIndex = btnList.indexOf(btn)
    console.log(btnIndex)
    $('#modal-form').show()

    // Fertiliser name to be put in the form
    let fertilisersList = document.getElementsByClassName('fertilisers-name')
    let manufacturersList = document.getElementsByClassName('manufacturers-name')
    let nInputsList = document.getElementsByClassName('n-inputs')
    console.log(fertilisersList[btnIndex].innerHTML)

    // Manufacturer name to be put in the form
    let form_name = document.getElementById('id_name')
    let form_manufacturer = document.getElementById('id_manufacturer')
    let form_N = document.getElementById('#id_N')

    form_name.value = fertilisersList[btnIndex].innerHTML
    form_manufacturer.value = manufacturersList[btnIndex].innerHTML
    form_N.value = nInputsList[btnIndex].value
    console.log(form_name.value)
    let form = $('#form-new-product')
    console.log(form)

}

form_data = {}
$('#btn-fertiliser-submit').on('submit', function(even){
    event.preventDefault();
    form_data['name'] = $('#id_name').val()
    form_data['manufacturer'] = $('#id_manufacturer').val()
    form_data['type_fertiliser'] = $('#id_type').val()
    add_user_fertiliser()
})

function add_user_fertiliser(){
    $.ajax({
        url: '/products/add_user_fertiliser/',
        type: 'POST',
        data: {
            'name': $('#id_name').val(),
            'manufacturer': $('#id_manufacturer').val(),
            'type_fertiliser': $('#id_type').val(),
            'N': $('#id_N').val(),
            'P': $('#id_P').val(),
            'K': $('#id_K').val(),
            'Mg': $('#id_Mg').val(),
            'price': $('#id_price').val(),
            },
        success: function(json){

            } ,
        error: function(xhr, errmsg, err){

        } ,
    })

}

// close the modal form
$('#modal-form-close').on('click', function(){
    $('#modal-form').hide()
})



