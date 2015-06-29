$(document).ready(function() {
    function block_form() {
        $(".btns").hide();
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
    }

    function unblock_form() {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
    }

    var callback = {
        beforeSubmit: function(form, options) {
            // return false to cancel submit
            block_form();
        },
        success: function() {
            unblock_form();
            $("#form_complete").show();
            setTimeout(function() {
                $("#form_complete").hide();
            }, 5000);
        }
    }

    $('#register_form').ajaxForm(callback);
});