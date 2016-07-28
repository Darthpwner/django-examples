(function(Dashboard, $, undefined ) {
    Dashboard.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
        namespace: "api"
    });

    Dashboard.Summary = DS.Model.extend({
        id: DS.attr('string'),
        total_runs: DS.attr('int'),
        total_tests: DS.attr('int'),
        average_yield: DS.attr('float'),
        created_at: DS.attr('date')
    });
}(window.Dashboard, jQuery));