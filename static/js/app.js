/**
 * Envelope app.
 */
(function ($) {
    var EnvelopeApp = {
        submitForm: function (form) {
            var $form = $(form);

            $.ajax({
                type: "POST",
                dataType: "json",
                data: $form.serialize(),
                success: this.submitSuccessCallback.bind(this),
                error: this.submitErrorCallback.bind(this)
            });
        },

        submitSuccessCallback: function (data, textStatus, jqXHR) {
            if (data && data['isResponseRecorded']) {
                window.location.href = "/response"
            } else {
                this.displayGeneralError();
            }
        },

        submitErrorCallback: function (jqXHR, textStatus, errorThrown) {
            this.displayGeneralError();
        },

        displayGeneralError: function () {
            $("#general-error-placeholder").append($("<p>").html("Something went wrong!"))
        },

        init: function () {
            $("#envelope-form").validate({
                submitHandler: this.submitForm.bind(this)
            });
        }
    };


    EnvelopeApp.init();
})(jQuery);