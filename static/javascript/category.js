$(document).ready(function(){
    $('.category_box_pokemons_row').hide()
})

function load_pokemon_by_letter(letter){
    $('.category_box_pokemons_row').hide()
    $('#'+letter).show()
}

function move_pokemon_page(letter){
    window.location.href='/sort_pokemon/' + letter +'/1'
}