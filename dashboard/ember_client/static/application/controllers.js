(function(Dashboard, $, undefined ) {
    Dashboard.ApplicationController = Ember.ObjectController.extend({
        summaries: function() {
            return this.get('store').find('summary');
        }.property(),
        makeCurrentPathGlobal: function() {
            Dashboard.set('currentPath', this.get('currentPath'));
        }.observes('currentPath')
    });
    // Dashboard.PostController = Ember.ObjectController.extend({
    //     isPython: function() {
    //         var title = this.get('content.title').toLowerCase();
    //         var category = this.get('content.category.name');
    //         if (category) {
    //             category = category.toLowerCase();
    //             return title.indexOf('python') != -1 || category.indexOf('python') != -1;
    //         }
    //     }.property('content.title', 'content.category.name')
    // });
    // Dashboard.CategoryController = Ember.ObjectController.extend({
    //     needs: ["post"],
    //     isActive: function() {
    //         var path = Dashboard.get('currentPath');
    //         return path == 'post' && this.get('content.id') == this.get('controllers.post.content.category.id');
    //     }.property('content.id', 'controllers.post.content.category.id', 'Blog.currentPath')
    // });
}(window.Dashboard, jQuery));
