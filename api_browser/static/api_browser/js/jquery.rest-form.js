/*
*
*   fatiherikli at gmail dot com
*   http://fatiherikli.com
*
* */
!(function ($) {

    $.fn.restForm = function (callback) {
        this.each(function () {
            $(this).submit(function () {

                var data = $(this).serialize();
                var method = $(this).attr("method");
                var url = $(this).attr("action");

                $.ajax({
                    url: url,
                    type: method,
                    data: data
                }).done(callback);

            });
        });
    };

})(window.jQuery)