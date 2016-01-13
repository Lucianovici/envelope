/**
 * Envelope app.
 */
(function ($) {
    var EnvelopeApp = {
        submitForm: function (form) {
            var $form = $(form);

            this.$submitButton.button('loading');

            $.ajax({
                type: "POST",
                dataType: "json",
                data: $form.serialize(),
                success: this.submitSuccessCallback.bind(this),
                error: this.submitErrorCallback.bind(this)
            });
        },

        handleEntryStored: function (data) {
            if (data['is_entry_recorded']) {
                /* Brutally change the location to the response url */
                //window.location.href = this.formResponseUrl;
                console.log("SUBMITTED!");
            } else {
                this.displayGeneralError("Your entry was not stored!");
            }
        },

        handleEditLastResponse: function (data) {
            var val = data['edit_last_response_params'];

            if (val) {
                $("input[name='edit-last-response-params']").val(val)
            }
        },

        submitSuccessCallback: function (data, textStatus, jqXHR) {
            if (data) {
                this.handleEntryStored(data);
                this.handleEditLastResponse(data);
            } else {
                this.displayGeneralError("There is no data returned from the server!");
            }
        },

        submitErrorCallback: function (jqXHR, textStatus, errorThrown) {
            this.$submitButton.button('reset');
            this.displayGeneralError();
        },

        errorPlacement: function (error, element) {
            error.appendTo($("#" + element.data("id") + "-section"));
        },

        displayGeneralError: function (msg) {
            $("#general-error-placeholder").append($("<p>").html("Error! " + msg))
        },

        init: function () {
            this.$envelopeForm = $("#envelope-form");
            this.formResponseUrl = this.$envelopeForm.data("response-url");
            this.$submitButton = $("#submit");

            this.$envelopeForm.validate({
                submitHandler: this.submitForm.bind(this),
                errorPlacement: this.errorPlacement
            });
        }
    };


    EnvelopeApp.init();
})(jQuery);