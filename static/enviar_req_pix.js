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
                console.log("sucesso!")
                console.log(preco)
            }
        })
    })
})