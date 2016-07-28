(function(Dashboard, $, undefined ) {
    Ember.Handlebars.registerBoundHelper('date', function(date) {
        //moment.lang('pl');
        return moment(date).fromNow();
    });
}(window.Dashboard, jQuery));
