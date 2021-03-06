let global_id = ''
let global_result = ''


$(document).ready(function (){
    $.ajax({
        type: "GET",
        url: "/common/token_check",
        data: {},
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            global_id = response["user_id"]
        }
    });
})


const inputImage = document.getElementById("input_file")
    inputImage.addEventListener("change", e => {
        $('#predict_writing_image').css('display','none')
        $('#pokemon_name').text("#")
        $('.alert').css('display','none')
        $('#check_alert').css('display','none')
        global_result=''
        readImage(e.target)
})

function readImage(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader()
        reader.onload = e => {
            const previewImage = document.getElementById("preview_writing_image")
            previewImage.src = e.target.result
        }
        reader.readAsDataURL(input.files[0])
    }
    confirming()
}


function confirming(){
    $('#loading').css('display','flex')
    let photo = $('#input_file')[0].files[0]
    if ( typeof photo ===  "undefined"){
        return 0
    }
    let form_data = new FormData()
    form_data.append("file_give", photo)
    const previewImage = document.getElementById("predict_writing_image")


    $.ajax({
        type: "POST",
        url: "/machine/load",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            $('#loading').css('display','none')
            $('#predict_writing_image').css('display','block')
            $('.pocket_book_image_predict_tag').css('display','block')
            if (response['result'] === 'none' )
            {
                previewImage.src = '/static/image/' + 'question' + '.jpg'
                $('#pokemon_name').text('판별 불가')
            }
            else if(response['result'] === '확장자를 확인해주세요'){
                alert('확장자를 확인해주세요!')
            }
            else{
                global_result = response['result']
                previewImage.src = '/static/image/default_pokemons_img/' + response['result'] + '.png'
                $('#pokemon_name').text('#'+response['result'])
            }
        }
    });


}


function posting() {
    let photo = $('#input_file')[0].files[0]
    let desc = $('#desc').val()
    let title = $('#title').val()
    let price = $('#price').val()
    let level = $('#level').val()
    let like_feed = $('#like_feed').val()
    let catch_location = $('#catch_location').val()
    let trade_location = $('#trade_location').val()
    let result = global_result
    let user_id = global_id
    let form_data = new FormData()

    if(typeof photo === "undefined"){
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('그림을 올려주세요!')
    }

    if(title === "") {
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('제목을 입력해 주세요')
    }
    if(desc === "") {
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('내용을 입력해주세요')
    }
    if(price === "") {
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('가격을 입력해 주세요')
    }
    if( $('#loading').css('display') === 'flex') {
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('판별중!')
    }
    if($('#pokemon_name').text() === '판별 불가') {
        $('.alert').css('display','flex')
        $('#check_alert').css('display','block')
        return $('#alert_mention').text('다른 이미지를 올려주세요')
    }


    console.log(result)

    form_data.append("photo_give", photo)
    form_data.append("desc_give", desc)
    form_data.append("title_give", title)
    form_data.append("price_give", price)
    form_data.append("result_give", result)
    form_data.append("id_give", user_id)
    form_data.append("level_give", level)
    form_data.append("like_feed_give", like_feed)
    form_data.append("catch_location_give", catch_location)
    form_data.append("trade_location_give", trade_location)
    form_data.append("id_give", user_id)


    $.ajax({
        type: "POST",
        url: "/make_new/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.href='/main_page'
        }
    });
}

function check_alert(){
    $('.alert').css('display','none')
    $('#check_alert').css('display','none')
}