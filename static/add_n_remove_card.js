$(document).ready(function(){

    $('.add_button').click(function(){
        var numeroV = $('.numero').val();
        var titularV = $('.titular').val();
        var cpfV = $('.cpf').val();
        var cvvV = $('.cvv').val();
        var validadeV = $('.validade').val();
        var apelido_cartaoV = $('.apelido_cartao').val();
            $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                numero_cartao: numeroV,
                titular: titularV,
                cpf: cpfV,
                cvv: cvvV,
                apelido_cartao: apelido_cartaoV,
                validade: validadeV
            },
            success: setTimeout(function() {
                window.location.href = "/perfil";
            }, 50)
        })
    })
    
    $('.remove_button').click(function(){
        var buttonValue = $(this).val();
        var self = this;
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                cartao_id: buttonValue
            }
        })
        self.parentNode.remove()
        
    })
})