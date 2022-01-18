$(function(){
    let category;
    $.ajax({
        type: "GET",
        url: "/main_page/pokemon_search",
        data: {},
        success: function (response) {
            category = response['category']['poket_category']
        }
    });

    $('#search').keyup(function () {
        let txt = $(this).val();
        let auto_search = $('#auto-search');
        let count = 0;


        if (txt != '') {
            auto_search.children().remove();

            category.forEach(function (arg) {
                if (arg.indexOf(txt) > -1 && count < 4) {
                    console.log('g')
                    document.getElementById('auto-search').style.display = 'block';
                    auto_search.append(
                        $("<div>").text(arg)
                    );
                    count += 1;
                } else {
                    return false;
                }
            });

            if (count === 0) {
                auto_search_close();
            }

            auto_search.children().each(function () {
                $(this).click(function () {
                    $('#search').val($(this).text());
                    auto_search_close();
                    auto_search.children().remove();
                })
            })

        } else {
            auto_search_close();
            auto_search.children().remove();
        }
    });
});

function auto_search_close() {
    document.getElementById('auto-search').style.display = 'none';
}


function move_search_result(){
    let result = $('#search').val();
    if (result !==''){
        window.location.href='/sort_pokemon/' + result + '/1'
    }

}

$(function(){
    $("#category_button").click(function(){
        $('#category_button').attr('src','/static/image/main_images/Open-Pokeball_96px.png');
        $(".modal").fadeIn();
    })
    $("#modal_out").click(function(){
        $('#category_button').attr('src','/static/image/main_images/Pokeball_96px.png');
        $(".modal").fadeOut();
    })
})
