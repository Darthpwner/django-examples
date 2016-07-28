(function(Dashboard, $, undefined ) {
    Dashboard.IndexRoute = Ember.Route.extend({
        redirect: function() {
            this.transitionTo('summary');
        }
    });
    // Dashboard.PostsRoute = Ember.Route.extend({
    //     model: function() {
    //         return this.get('store').find('post');
    //     }
    // });
    // Dashboard.CategoryPostsRoute = Ember.Route.extend({
    //     model: function(params) {
    //         return this.get('store').find('post', {'category': params.id });
    //     }
    // });
    // Dashboard.PostRoute = Ember.Route.extend({
    //     model: function(params) {
    //         return this.get('store').find('post', params.id);
    //     }
    // });
    Dashboard.SummaryRoute = Ember.Route.extend({
        model: function(params) {
            return this.get('store').find('summary', {'id:' params.id})
        }
    });
}(window.Dashboard, jQuery));
