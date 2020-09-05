from werkzeug.wrappers import Request,Response

class Shortly(object):
    def __call__(self, environ,stat_response):
        # stat_response('200 Ok', [('content-Type','text/plain')])
        # return [b'hello world~~']
        request = Request( environ )
        text = "hello world~~"
        reponse = Response(text,mimetype="text/plain" )
        return stat_response(environ,stat_response)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0',5000,app)