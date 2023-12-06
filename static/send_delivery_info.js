$(document).ready(function(){

    $('.enviar').click(function(){
        var informacoes = $(this).attr("id");
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                "infos":informacoes
            },
            success: setTimeout(function() {
                window.location.href = "/pagamento";
            }, 50)
        })
    })
})