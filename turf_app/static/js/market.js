//load status color
let status_list = jQuery.makeArray($('.status_fertiliser'))
for (let i = 0; i < status_list.length; i++) {
    console.log(status_list[i].innerHTML == 'In')
    if (status_list[i].innerHTML == 'In'){
        status_list[i].style.color = 'hsl(120, 61%, 25%)'
    }
}

//ADD PRODUCT (PURCHASE) FROM MARKET TO USER WAREHOUSE
//open the modal form
let fertiliser_id;
let btnIndex;
function productFormOpen(btn){
    let btnList = jQuery.makeArray($('.add-btn'))
    btnIndex = btnList.indexOf(btn)
    console.log(btnIndex)
    $('#modal-form').show()

    // Fertiliser data list from html
    let fertilisers_idsList = $('.fertilisers-ids')
    let fertilisersList = $('.fertilisers-name')
    let manufacturersList = $('.manufacturers-name')
    let typesList = $('.types')
    let unitsList = $('.units')
    let nInputsList = $('.n-inputs')
    let pInputsList = $('.p-inputs')
    let kInputsList = $('.k-inputs')
    let mgInputsList = $('.mg-inputs')

    console.log(fertilisersList[btnIndex].innerHTML)
    console.log(typesList[btnIndex].innerHTML)

    // Form inputs
    $('#id_name').val(fertilisersList[btnIndex].innerHTML)
    $('#id_manufacturer').val(manufacturersList[btnIndex].innerHTML)
    $('#id_type').val(typesList[btnIndex].innerHTML)
    $('#id_units').val(unitsList[btnIndex].innerHTML)
    $('#id_N').val(nInputsList[btnIndex].innerHTML)
    $('#id_P').val(pInputsList[btnIndex].innerHTML)
    $('#id_K').val(kInputsList[btnIndex].innerHTML)
    $('#id_Mg').val(mgInputsList[btnIndex].innerHTML)

    fertiliser_id = fertilisers_idsList[btnIndex].innerHTML
}

// listening form button
$('#btn-fertiliser-submit').on('click', function(event){
    event.preventDefault();
    add_user_fertiliser()
    $('#modal-form').hide()
})

//ajax function to send data to server and get back response from it
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
                let status = $('.status_fertiliser')[btnIndex]
                status.innerHTML = json.status_fertiliser
                status.style.color = 'hsl(120, 61%, 25%)'
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




