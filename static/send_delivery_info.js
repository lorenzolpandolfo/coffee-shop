$(document).ready(function(){

    $('.enviar').click(function(){
        var id = $(this).attr("id");
        var data = $(this).attr("data");
        console.log(id)
        console.log(data)
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                "id":id,
                "data":data
            },
            success: function(response) {
                window.location.href = "/pagamento";
            }
        })
    })
})