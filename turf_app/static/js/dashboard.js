var countProducts = 1 //it will count products being added or deleted
var productSelectDiv = jQuery.makeArray($('.product-select-div')) // it will save products

//open form
$('#add-btn-applications').on('click', function(){
    $('#modal-form').show()
})

//close form
$('#modal-form-close').on('click', function(){
    $('#modal-form').hide()
    if(countProducts > 1){
        for (let i = countProducts - 1; i > 0; i--) {
            productSelectDiv[i].remove()
        }
    }
    productSelectDiv[0].append(addImg)
    countProducts = 1
    newBtnListener('btn-add-item')

})

// img add btn to be added or removed from products div
var addImg = document.createElement('img')
    addImg.src ="/static/images/mas.png"
    addImg.id = 'btn-add-item'
    addImg.width = 20
    addImg.height = 20
    addImg.class = "btn-add-application"

// add volum input if application type selected is liquid
$('#type-dropdown').change(function() {
    if ($('#volumQuantity-div').css.display == 'none') {
        $('#volumQuantity-div').show()
        $('#volumQuantity-div').css.display = 'block'
    } else {
        $('#volumQuantity-div').hide()
        $('#volumQuantity-div').css.display = 'none'
    }
    typeSelect($('#product-select-1'))
    if (countProducts > 1) {
        for (let i = countProducts - 1; i > 0; i--) {
           productSelectDiv[i].remove()
        }
        productSelectDiv[0].append(addImg)
        newBtnListener('btn-add-item')
    }
    countProducts = 1
})

//change products availability depending on type application
typeSelect($('#product-select-1'))

function typeSelect(selector) {
    selector.empty()
    if ($('#type-dropdown').val() === 'Liquid') {
        for (let i = 0; i < liquidFertilisersNames.length; i++) {
            selector.append('<option value=\"' + liquidFertilisersIds[i] + '\">' + liquidFertilisersNames[i] + '</option>')
        }
    } else {
        for (let i = 0; i < solidFertilisersNames.length; i++) {
            selector.append('<option value=\"' + solidFertilisersIds[i] + '\">' + solidFertilisersNames[i] + '</option>')
        }
    }
}

// Add products in the application form
$('#btn-add-item').on('click', addProductSelectDiv)
function addProductSelectDiv() {
    if(('#btn-delete-item') != undefined){
        $('#btn-delete-item').remove()
    }
    $('#btn-add-item').remove()
    countProducts++
    console.log('countproducts:' + countProducts)
    $('#product-selection').append('<div class="product-select-div">\n' +
        '                                <label for="product-select-' + countProducts.toString() + '">Product:</label>\n' +
        '                                <select name="product-dropdown-' + countProducts.toString() + '" id="product-select-' + countProducts.toString() + '" style="width:150px;">\n' +
        '                                </select>\n' +
        '                                <label for="">Quantity</label>\n' +
        '                                <input type="text">\n' +
        '                                <img id="btn-add-item" class="btn-add-application" src="/static/images/mas.png" alt="" width="20" height="20">\n' +
        '                                <img id="btn-delete-item" class="btn-delete-application" src="/static/images/delete.png" alt="" width="20" height="20">\n' +
        '                            </div>')
    productSelectDiv = jQuery.makeArray($('.product-select-div'))
    newBtnListener('btn-add-item')
    newDeleteBtnListener('btn-delete-item')
    console.log('product-select-' + countProducts.toString())
    typeSelect($('#product-select-' + countProducts.toString()))
}

// delete products in the application form
function deleteProductSelection(){
    productSelectDiv[countProducts - 1].remove()
    countProducts--
    console.log(countProducts)

    let addImgDel = document.createElement('img')
    addImgDel.src ="/static/images/delete.png"
    addImgDel.id = 'btn-delete-item'
    addImgDel.width = 20
    addImgDel.height = 20
    addImgDel.class = "btn-add-application"
    productSelectDiv[countProducts - 1].append(addImg)
    newBtnListener('btn-add-item')

    if(countProducts > 1) {
        productSelectDiv[countProducts - 1].append(addImgDel)
        newDeleteBtnListener('btn-delete-item')
    }
}

function newBtnListener(id){
    document.getElementById(id).addEventListener('click', addProductSelectDiv)
}

function newDeleteBtnListener(id){
    document.getElementById(id).addEventListener("click", deleteProductSelection)
}





