function sign_in() {
    $.ajax({
        type: "POST",
        url: "/api/login",
        data: {id_give: $('#user_id').val(), pw_give: $('#user_pw').val()},
        success: function (response) {
            if (response['result'] == 'success') {
                alert('로그인 완료!')
                $.cookie('mytoken', response['token']);
                window.location.href = '/palette'
            } else {
                $("#help-login").text('아이디 또는 비밀번호가 잘못 입력 되었습니다. 아이디와 비밀번호를 정확히 입력해 주세요.')
            }
        }
    })
}