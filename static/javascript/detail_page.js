function posting() {
    let comment = $('#comment').val()
    let form_data = new FormData()

    if (typeof photo === "undefined")
        return alert("이미지을 넣어 주세요")

    form_data.append("photo_give", photo)
    form_data.append("desc_give", desc)
    form_data.append("title_give", title)
    form_data.append("price_give", price)


    $.ajax({
        type: "POST",
        url: "/upload",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.href = '/index_page'
        }
    });
}