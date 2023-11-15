$(document).ready(function(){

    /* mudando o estado da caixinha la no html
    $('.checkbox').change(function(){
        var checkboxValue = $(this).prop('checked');
       $(this).val(checkboxValue);

    }) */

    $('.checkbox').click(function(){
        var checkboxValue = $(this).prop('checked');
        $.ajax({
            url:'',
            type: 'get',
            contentType: 'application/json',
            data: {
                'checkboxValue': checkboxValue,
                'itemId': this.parentNode.parentNode.id,
                'adicionalId': this.parentNode.id
            },
            success: function(response) {
            }
        })       
    })
})