from flask import Flask,render_template,jsonify,make_response,request,abort
from flask_caching import Cache
import logging

cache = Cache()
app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
cache.init_app(app, config={'CACHE_TYPE': 'simple'})




@cache.memoize(50)
@app.after_request
def add_response_header(response):
    response.headers['X-Forwarded-Host']= '127.0.0.1:5000'
    response.headers['Cache-Control'] = 'public, '
    state = cache.get('X-Cache')
    response.headers['X-Cache'] = state
    response.set_cookie('text', 'Cookie cache poision')
    return response



@app.route('/')
@cache.cached(10)
def hello_world():
    print('111')
    resp = make_response(jsonify(city="BJ", fruit="apple"))
    resp.headers["X-Cache"] = "miss"
    cache.set('X-Cache', 'miss',timeout=50)
    cache.set('count', 1, timeout=50)
    XFF = request.headers.get('X-Forwarded-Host', '127.0.0.1:5000')
    ## XFF prevention
    app.logger.info('the XXF is %s' % XFF)
    app.logger.info('the checker is %s' % str(XFF != '127.0.0.1:5000'))
    if XFF != '127.0.0.1:5000':
        abort(403)
    @app.before_request
    def handle_before():
        count = cache.get('count') or 1
        if count == 1:
            cache.set('X-Cache', 'hit', timeout=50)
        count += 1
        cache.set('count', count, timeout=50)

    ### Cookie prevention
    # if request.cookies.get('text', 'Don') not in ['Don', 'Cookie cache poision']:
    #     return abort(403)
    return render_template('home.html', XFF=XFF, Cookie=request.cookies.get('text', 'Don'))




# @app.route('/test')
# @cache.cached(10)
# def fatget():
#     cache.set('X-Cache', 'miss', timeout=50)
#     cache.set('count', 1, timeout=50)
#     return render_template('fat.html')
#
#
# @app.route('/include.js')
# @cache.cached(10)
# def include():
#     cache.set('X-Cache', 'miss', timeout=50)
#     cache.set('count', 1, timeout=50)
#     callback = cache.get('callback') or 'load'
#     cache.set('callback', callback, timeout=50)
#     print('222')
#     result = callback+'("some data")'
#
#     @app.before_request
#     def handle_before():
#         count = cache.get('count') or 1
#         if count == 1:
#             cache.set('X-Cache', 'hit', timeout=50)
#             cache.set('callback', request.headers.get('callback', 'load'))
#             print(cache.get('callback'))
#
#         count += 1
#         cache.set('count', count, timeout=50)
#         callback = cache.get('callback')
#
#
#
#     return result



if __name__ == '__main__':
    app.run()
