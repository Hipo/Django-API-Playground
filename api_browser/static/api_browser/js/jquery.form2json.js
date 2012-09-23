/*
* http://css-tricks.com/snippets/jquery/serialize-form-to-json/
* */
!function ($) {

    $.fn.form2json = function()
    {
        var o = {};
        var a = this.serializeArray();

        $.each(a, function() {
            var value = this.value || '' ;
            if (o[this.name]) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(value);
            } else {
                o[this.name] = value;
            }
        });
        return o;
    };

}(window.jQuery);