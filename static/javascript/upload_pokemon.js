function posting() {
    let photo = $('#input_writing_image')[0].files[0]
    let desc = $('#desc').val()
    let title = $('#sub-title').val()
    let price = $('#price').val()
    let form_data = new FormData()


    if(typeof photo === "undefined")
        return alert("이미지을 넣어 주세요")
    if(desc == "")
        return alert("내용을 입력하세요")
    if(title == "")
        return alert("제목을 입력하세요")


    form_data.append("photo_give", photo)
    form_data.append("desc_give", desc)
    form_data.append("title_give", title)
    form_data.append("price_give", price)


    $.ajax({
        type: "POST",
        url: "/upload_pokemon",
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


    form_data.append("photo_give", photo)

    $.ajax({
        type: "POST",
        url: "/upload_pokemon/confirming",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.href='/index_page'
        }
    });
}

