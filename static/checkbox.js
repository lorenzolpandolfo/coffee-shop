$(document).ready(function(){

    $('.checkbox').change(function(){
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
                console.log("Checkbox enviado!")
            }
        })
    })
})