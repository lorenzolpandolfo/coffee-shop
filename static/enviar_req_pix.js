$(document).ready(function(){

    $('.gerar_pix').click(function(){
        var preco = $(this).attr("preco");
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                "preco":preco
            },
            success: function(response) {
                $('.pix_img').css('display', 'block');
                $('.pix_img').attr('src', "static/pix_qr_code.png");
            }
        })
    })
})