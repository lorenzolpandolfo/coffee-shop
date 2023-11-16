$(document).ready(function(){

    $('.add_button').click(function(){
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
        var self = this;
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                item: buttonValue
            },
            success: function(response) {
                var subtotal_price = parseFloat($('.subtotal').text());
                var thisItemId = self.parentNode.id
                var thisItemPrice = parseFloat($("#" + thisItemId + ".itemPrice").text().replace("R$", ''));
                
                var newSubtotal = parseFloat(subtotal_price - thisItemPrice);

                console.log('subtotal_price:', subtotal_price);
                console.log('thisItemId:', thisItemId);
                console.log('thisItemPrice:', thisItemPrice);
                console.log('newSubtotal:', newSubtotal);

                $('.subtotal').text(newSubtotal)

                if (response.quantidade_carrinho > 0) {
                    $('.item_count').text("Carrinho (" + response.quantidade_carrinho + ")")
                    $('.carrinho_vazio').hide()
                    $('.interagir_carrinho').show()
                }
                else {
                    $('.item_count').text("Carrinho")
                    $('.carrinho_vazio').show()
                    $('.interagir_carrinho').hide()
                }
                
                self.parentNode.remove()
            }
        })
        
    })
})