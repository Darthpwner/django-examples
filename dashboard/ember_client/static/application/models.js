(function(Dashboard, $, undefined ) {
    Dashboard.ApplicationAdapter = DS.DjangoRESTAdapter.extend({
        namespace: "api"
    });
    Dashboard.Category = DS.Model.extend({
        name: DS.attr('string'),
        slug: DS.attr('string')
    });
    Dashboard.Post = DS.Model.extend({
        title: DS.attr('string'),
        slug: DS.attr('string'),
        text: DS.attr('string'),
        category: DS.belongsTo('category', {async: true}),
        posted_date: DS.attr('date')
    });
    Dashboard.Summary = DS.Model.extend({
        id: DS.attr('string'),
        total_runs: DS.attr('int'),
        total_tests: DS.attr('int'),
        average_yield: DS.attr('float'),
        created_at: DS.attr('date')
    });
}(window.Dashboard, jQuery));