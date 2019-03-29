//ADD PRODUCT FROM MARKET FOR USER AVAILABILITY
//open the modal form
let fertiliser_id;
let btnIndex;
function productFormOpen(btn){
    let btnList = Array.from(document.getElementsByClassName('add-btn'))
    btnIndex = btnList.indexOf(btn)
    console.log(btnIndex)
    $('#modal-form').show()

    // Fertiliser name to be put in the form
    let fertilisers_idsList = document.getElementsByClassName('fertilisers-ids')
    let fertilisersList = document.getElementsByClassName('fertilisers-name')
    let manufacturersList = document.getElementsByClassName('manufacturers-name')
    let typesList = document.getElementsByClassName('types')
    let unitsList = document.getElementsByClassName('units')
    let nInputsList = document.getElementsByClassName('n-inputs')
    let pInputsList = document.getElementsByClassName('p-inputs')
    let kInputsList = document.getElementsByClassName('k-inputs')
    let mgInputsList = document.getElementsByClassName('mg-inputs')

    console.log(fertilisersList[btnIndex].innerHTML)
    console.log(typesList[btnIndex].innerHTML)

    // Manufacturer name to be put in the form
    let form_name = document.getElementById('id_name')
    let form_manufacturer = document.getElementById('id_manufacturer')
    let form_type = document.getElementById('id_type')
    let form_unit = document.getElementById('id_units')
    let form_N = document.getElementById('id_N')
    let form_P = document.getElementById('id_P')
    let form_K = document.getElementById('id_K')
    let form_Mg = document.getElementById('id_Mg')

    fertiliser_id = fertilisers_idsList[btnIndex].innerHTML
    form_name.value = fertilisersList[btnIndex].innerHTML
    form_manufacturer.value = manufacturersList[btnIndex].innerHTML
    form_type.value = typesList[btnIndex].innerHTML
    form_unit.value = unitsList[btnIndex].innerHTML
    form_N.value = nInputsList[btnIndex].innerHTML
    form_P.value = pInputsList[btnIndex].innerHTML
    form_K.value = kInputsList[btnIndex].innerHTML
    form_Mg.value = mgInputsList[btnIndex].innerHTML

    console.log(form_name.value)
    let form = $('#form-new-product')
    console.log(form)

}

$('#btn-fertiliser-submit').on('click', function(event){
    event.preventDefault();
    add_user_fertiliser()
    $('#modal-form').hide()
})

function add_user_fertiliser(){
    $.ajax({
        url: '/market/add-user-fertiliser/',
        type: 'POST',
        data: {
            'id': fertiliser_id,
            'quantity': $('#id_quantity').val(),
            'price': $('#id_price').val(),
            },
        success: function(json){
                let status = document.getElementsByClassName('status_fertiliser')[btnIndex]
                status.innerHTML = json.status_fertiliser
            } ,
        error: function(xhr, errmsg, err){
            console.log(status.xhr + ":" + xhr.responseText)
        } ,
    })

}

// close the modal form
$('#modal-form-close').on('click', function(){
    $('#modal-form').hide()
})






//CSRF-TOKEN CODE FOR AJAX
$(function() {

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});




