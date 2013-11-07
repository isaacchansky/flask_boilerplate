from flask.ext.assets import Bundle


common_css = Bundle(
    "bower_components/bootstrap-sass/dist/css/bootstrap.min.css",
    "css/style.css",
    filters="cssmin",
    output="public/css/common.css"
)

common_js = Bundle(
    "bower_components/jquery/jquery.min.js",
    "bower_components/bootstrap-sass/dist/js/bootstrap.min.js",
    "js/plugins.js",
    Bundle(
        "js/script.js",
        filters="jsmin"
    ),
    output="public/js/common.js"
)
