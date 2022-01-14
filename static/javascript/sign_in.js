$(document).ready(
    function (){
    $.ajax({
        type: "GET",
        url: "/common/token_check",
        data:{},
        success: function (response) {
            let id = response['user_id']
            if (id !== 'None') {
                window.location.href = '/main_page'
            }
        }
    })
})

function sign_in() {
    $.ajax({
        type: "POST",
        url: "/sign_in/login",
        data: {id_give: $('#user_id').val(), pw_give: $('#user_pw').val()},
        success: function (response) {
            if (response['result'] === 'success') {
                $.cookie('mytoken', response['token']);
                window.location.href = '/main_page'
            } else {
                $("#help-login").text('아이디 또는 비밀번호가 잘못 입력 되었습니다. 아이디와 비밀번호를 정확히 입력해 주세요.')
            }
        }
    })
}