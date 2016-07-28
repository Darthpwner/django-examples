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
    
}(window.Dashboard, jQuery));
