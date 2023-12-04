$(document).ready(function(){

    $('.add_button').click(function(){
        var rua = $('.rua').val();
        var numero = $('.numero').val();
        var bairro = $('.bairro').val();
        var cep = $('.cep').val();
        var complemento = $('.complemento').val();
        var referencia = $('.referencia').val();
        var apelido = $('.apelido').val();

        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                rua_value: rua,
                numero_value: numero,
                bairro_value: bairro,
                cep_value: cep,
                complemento_value: complemento,
                apelido_value: apelido,
                referencia_value: referencia
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
                endereco_id: buttonValue
            }
        })
        self.parentNode.remove()
        
    })
})