from flask import Flask, render_template,url_for, request
from flask_caching import Cache
from werkzeug.wrappers import response

app= Flask(__name__)
cache=Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST':'0.0.0.0',
    'CACHE_REDIS_PORT': 6379
}
)
posts = [
    {
        'Group_10_topic': 'Web Cache Poisoning',
        'date_posted': '02 Sep 2021'
    }
]
cache.init_app(app)
@app.route("/", methods=["GET"])
@cache.cached(timeout=10)
def homePage():
    
    return render_template('home.html', posts=posts)

@cache.memoize(50)
@app.after_request
def add_response_header(response):
    response.headers['X-Forwarded-Host']= '127.0.0.1'
    response.headers['Cache-Control'] = 'public, '

    return response

@app.route("/about")
def about():
    return F"Hello: {[ _ for _ in range(1000)]}"

@app.route("/image")
def image():
    image = request.headers
    print(type(image))
    return render_template('image.html')



if __name__=='__main__':
    app.run(debug=True)

