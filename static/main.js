$(document).ready(function(){

    $('.btn').click(function(){
        var buttonValue = $(this).attr('value');
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                button_item_value: buttonValue
            },
            success: function(response) {
                $('.item_count').text("Carrinho (" + response.quantidade_carrinho + ")")
            }
        })
    })
    
    $('.remove_button').click(function(){
        var buttonValue = $(this).attr('value');
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                item: buttonValue
            },
            success: function(response) {

                if (response.quantidade_carrinho > 0) {
                    $('.item_count').text("Carrinho (" + response.quantidade_carrinho + ")")
                    $('.carrinho_vazio').hide();
                    $('.interagir_carrinho').show()
                }
                else {
                    $('.item_count').text("Carrinho")
                    $('.carrinho_vazio').show();
                    $('.interagir_carrinho').hide()
                }
            }
        })
        this.parentNode.remove()
        
    })
})