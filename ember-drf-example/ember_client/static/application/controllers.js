(function(EmberClient, $, undefined ) {
    EmberClient.ApplicationController = Ember.ObjectController.extend({
        categories: function() {
            return this.get('store').find('category');
        }.property(),
        makeCurrentPathGlobal: function() {
            EmberClient.set('currentPath', this.get('currentPath'));
        }.observes('currentPath')
    });
    EmberClient.PostController = Ember.ObjectController.extend({
        isPython: function() {
            var title = this.get('content.title').toLowerCase();
            var category = this.get('content.category.name');
            if (category) {
                category = category.toLowerCase();
                return title.indexOf('python') != -1 || category.indexOf('python') != -1;
            }
        }.property('content.title', 'content.category.name')
    });
    EmberClient.CategoryController = Ember.ObjectController.extend({
        needs: ["post"],
        isActive: function() {
            var path = EmberClient.get('currentPath');
            return path == 'post' && this.get('content.id') == this.get('controllers.post.content.category.id');
        }.property('content.id', 'controllers.post.content.category.id', 'Blog.currentPath')
    });
}(window.EmberClient, jQuery));
