(function(Dashboard, $, undefined) {
    Dashboard.Router.map(function() {
        // this.route('posts');
        // this.route('categoryPosts', {path: 'category/:id'});
        // this.route('post', {path: 'posts/:id'});
        this.route('summary');
    });
    if (window.history && window.history.pushState) {
        Dashboard.Router.reopen({
          location: 'history'
        });
    }
}(window.Dashboard, jQuery));

