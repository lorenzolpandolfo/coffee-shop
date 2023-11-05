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
        var removeButtonValue = $(this).attr('value');
        
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                item: removeButtonValue
            },
            success: function(response) {
                if (response.quantidade_carrinho > 0) {
                    $('.item_count').text("Carrinho (" + response.quantidade_carrinho + ")")
                }
                else {
                    $('.item_count').text("Carrinho")
                }
            }
        })

        var elementoPai = this.parentNode;
        elementoPai.remove();
    })
})