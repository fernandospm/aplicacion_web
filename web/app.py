import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates')

app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()
        
if _name_ == "_main_":
    app.run()