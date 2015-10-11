(function($){
    var EnvelopeApp = {
        init : function() {
            $("#envelope-form").validate({
                submitHandler: this.submitForm
            });
        },

        submitForm : function(form) {
            alert("TBI: Frontend validation");
            // Use hidden iframe to submit the actual form and show the custom response afterwards.
            form.submit();
            window.location.replace("/response");
        }
    };

    EnvelopeApp.init();
})(jQuery);
