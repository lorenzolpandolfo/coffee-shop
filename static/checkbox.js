$(document).ready(function(){

    $('.checkbox').change(function(){
        var checkboxValue = $(this).prop('checked');
       $(this).val(checkboxValue);
    })

    $('.checkbox').click(function(){
        console.log("Checkbox enviado!")
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
            },
            success: function(response) {
            }
        })       
    })
})