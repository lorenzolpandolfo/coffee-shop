$(document).ready(function(){

    $('.enviar').click(function(){
        var id = $(this).attr("id");
        var data = $(this).attr("data");
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                "id":id,
                "data":data
            },
            success: setTimeout(function() {
                window.location.href = "/pagamento";
            }, 50)
        })
    })
})