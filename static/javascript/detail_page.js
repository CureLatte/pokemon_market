let hi = "";
$(document).ready(function () {

    $.ajax({
        type: "GET",
        url: "/common/token_check",
        data: {},
        success: function (response) {
            let id = response['user_id']
            console.log(response)
            hi = id;
            if (id == 'None') {
                console.log("토큰이 None입니다.")
                window.location.href = '/main_page'
            }
        }
    })
})

function posting_comment() {
    let comment = $('#comment').val()
    let sc = $('#sc_p').text()
    if (comment === "") {
        return alert("댓글을 남겨주세요")
    }
    $.ajax({
        type: "POST",
        url: "/detail_page/",
        data: { "comment_give": comment, "logedin_give": hi, "sc_give": sc },
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}
