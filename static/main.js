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
                $('.btn').text(response.seconds)
            }
        })
    })
})