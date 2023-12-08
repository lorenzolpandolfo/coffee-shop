$(document).ready(function(){
    var qrcode_code = "";

    $('.gerar_pix').click(function(){
        var preco = $(this).attr("preco");
        $.ajax({
            url: '',
            type: 'get',
            contentType: 'application/json',
            data: {
                "preco": preco
            },
            success: function(response) {
                $('.pix').css('display', 'block');
                $('.pix_img').attr('src', "static/pix_qr_code.png");
                qrcode_code = response;
            }
        });
    });

    $('.copiar_qr_code').click(function(){
        $('.copy_output').css('display', 'block');
        navigator.clipboard.writeText(qrcode_code);
    });
});
