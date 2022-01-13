function posting() {
    let photo = $('#input_writing_image')[0].files[0]
    let desc = $('#desc').val()
    let title = $('#sub-title').val()
    let price = $('#price').val()
    let form_data = new FormData()


    if(typeof photo === "undefined")
        return alert("이미지을 넣어 주세요")


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
            window.location.href='/index_page'
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


// function confirming(){
//     let photo = $('#input_writing_image')[0].files[0]
//     test_datagen = ImageDataGenerator(rescale = 1./255)
//     test_dir = photo
//     test_generator = test_datagen.flow_from_directory(
//             test_dir,
//             // # target_size 는 학습할때 설정했던 사이즈와 일치해야 함
//             target_size =(256, 256),
//             color_mode ="rgb",
//             shuffle = False,
//             // # test 셋의 경우, 굳이 클래스가 필요하지 않음
//             // # 학습할때는 꼭 binary 혹은 categorical 로 설정해줘야 함에 유의
//             class_mode = None,
//             batch_size = 1)
//     pred = model.predict(test_generator)
// }