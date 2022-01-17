let hi = "";
$(document).ready(
    function () {
        $.ajax({
            type: "GET",
            url: "/common/token_check",
            data: {},
            success: function (response) {
                let id = response['user_id']
                hi = id;
                if (id == 'None') {
                    window.location.href = '/main_page'
                }
            }
        })
    },
)

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


function trade() {
    let seller = $('#seller').text()
    let price = $('#price').text()
    let sc = $('#sc_p').text()
    $.ajax({
        type: "POST",
        url: "/detail_page/trade",
        data: { "seller_give": seller, "logedin_give": hi, "price_give": price, "sc_give": sc },
        success: function (response) {
            alert(response["msg"])
            window.location.href = '/main_page'
        }
    });
}

//좋아요 버튼
function like() {
    $.ajax({
        type: 'POST',
        url: '/detail_page/api/like',
        data: {id_give: hi},
        success: function (response) {
            let now_num = response['now_like']
            let temp_html = `<span>${now_num}</span>`

            $("#like_num").append(temp_html)

            window.location.reload()
        }
    });
}