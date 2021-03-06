$(function () {
    let category;
    $.ajax({
        type: "GET",
        url: "/sign_up/pokemon_search",
        data: {},
        success: function (response) {
            category = response['category']['poket_category']
        }
    });

    $('#interest-poket').keyup(function () {
        let txt = $(this).val();
        let check_reg = false;
        let interest_poket = document.querySelector('label[for="interest-poket"]');


        if (txt != '') {
            $('#auto-poket').children().remove();

            category.forEach(function (arg) {
                if (arg.indexOf(txt) > -1) {
                    $("#auto-poket").append(
                        $("<div>").text(arg)
                    );
                }
                if (txt === arg) {
                    check_reg = true;
                }
            });

            if (check_reg) {
                interest_poket.nextElementSibling.src = "../static/image/check_yes.png";
            } else {
                interest_poket.nextElementSibling.src = "../static/image/check_no.png";
            }

            $('#auto-poket').children().each(function () {
                $(this).click(function () {
                    $('#interest-poket').val($(this).text());

                    interest_poket.nextElementSibling.src = "../static/image/check_yes.png";
                    $('#auto-poket').children().remove();
                })
            })

        } else {
            $('#auto-poket').children().remove();
            interest_poket.nextElementSibling.src = "";
        }
    });


})

function check_user_id(obj) {
    let regExp = /^(?=.*[a-zA-Z])[-a-zA-Z0-9_.]{2,10}$/;
    let user_id = $(obj).val();

    if (!(regExp.test(user_id))) {
        check_on_off(obj, false);
        return
    }

    $.ajax({
        type: "POST",
        url: "/sign_up/user_id",
        data: {'user_id': user_id},
        success: function (response) {
            check_on_off(obj, response['is_user_id']);
        }
    });
}

function check_pwd(obj) {
    let value = $(obj).val();
    let regExp = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*]{8,20}$/;

    check_on_off(obj, regExp.test(value));
}

function check_phone(obj) {
    let value = $(obj).val();
    let regExp = /^01([0|1|6|7|8|9])-([0-9]{3,4})-([0-9]{4})$/;

    check_on_off(obj, regExp.test(value));
}

function check_on_off(obj, is_visible) {
    let obj_id = obj.id;
    let value = obj.value

    let check_image = document.querySelector('label[for=' + obj_id
        + ']')

    if (value.length === 0) {
        check_image.nextElementSibling.src = "";
    } else if (is_visible) {
        check_image.nextElementSibling.src = "../static/image/check_yes.png";
    } else {
        check_image.nextElementSibling.src = "../static/image/check_no.png";
    }
}

function check_sign_up(evt) {

    evt.preventDefault();

    let img_list = document.querySelectorAll(".form_common img");
    let is_check_submit = true;

    img_list.forEach(function(arg) {
        let temp = arg.src.split("/");
        temp = temp[temp.length - 1].split(".");
        temp = temp[0];
        if(temp === 'check_no'){
            is_check_submit = false;
            return false;
        }
    });

    if(is_check_submit){
        let user_id = document.getElementById('user-id').value;
        let password = document.getElementById('password').value;
        let gender = document.querySelector('input[name="gender"]:checked').value;
        let phone_number = document.getElementById('phone-number').value;
        let interest_poket = document.getElementById('interest-poket').value;

        $.ajax({
            type: "POST",
            url: "/sign_up/submit",
            data: {
                'user_id': user_id,
                'password': password,
                'gender': gender,
                'phone_number': phone_number,
                'interest_poket': interest_poket
            },
            success: function (response) {
                alert(response['msg']);
                location.href='/';
            }
        });
    }
}