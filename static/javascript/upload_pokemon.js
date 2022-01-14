let global_result = ''
let global_id = ''


$(document).ready(function (){
    $.ajax({
        type: "GET",
        url: "/common/token_check",
        data: {},
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            global_id = response["result"]


        }
    });

})

function posting() {
    let photo = $('#input_writing_image')[0].files[0]
    let desc = $('#desc').val()
    let title = $('#sub-title').val()
    let price = $('#price').val()
    let result = global_result
    let user_id = global_id
    let form_data = new FormData()
    console.log(user_id)



    if(typeof photo === "undefined")
        return alert("포켓몬 사진을 넣어 주세요")
    if(title == "")
        return alert("제목을 입력해주세요")
    if(desc == "")
        return alert("내용을 입력해주세요")



    form_data.append("photo_give", photo)
    form_data.append("desc_give", desc)
    form_data.append("title_give", title)
    form_data.append("price_give", price)
    form_data.append("result_give", result)
    form_data.append("id_give", user_id)


    $.ajax({
        type: "POST",
        url: "/upload_pokemon/",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}

function readImage(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader()
        reader.onload = e => {
            const previewImage = document.getElementById("preview_writing_image")
            previewImage.src = e.target.result
        }
        reader.readAsDataURL(input.files[0])
    }
}

const inputImage = document.getElementById("input_writing_image")
inputImage.addEventListener("change", e => {
    readImage(e.target)
})


function confirming(){
    let photo = $('#input_writing_image')[0].files[0]
    let form_data = new FormData()

    form_data.append("file_give", photo)


    $.ajax({
        type: "POST",
        url: "/machine/load",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            global_result = response["result"]
            alert(response["result"])
            // window.location.href='/machine/result'
        }
    });


}