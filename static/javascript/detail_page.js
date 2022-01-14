function posting_comment() {
    let comment = $('#comment').val()
    console.log(comment)
    if (comment === "")
        return alert("댓글을 남겨주세요")

    $.ajax({
        type: "POST",
        url: "/detail_page",
        data: { "comment_give": comment },
        success: function (response) {
            alert(response["msg"])
        }
    });
}