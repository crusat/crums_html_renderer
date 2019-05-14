from flask import Flask
from flask import render_template
from flask import request
from werkzeug.middleware.proxy_fix import ProxyFix
import json

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['POST'])
def render():
    data = json.loads(request.data)
    template = data['template']
    context = json.loads(data['context'])
    result = render_template(template, **context)
    return result


@app.route('/render_and_save/', methods=['POST'])
def render_and_save():
    data = json.loads(request.data)
    template = data['template']
    save_as = data['save_as']
    context = json.loads(data['context'])
    result = render_template(template, **context)
    with open(save_as, 'w') as f:
        f.write(result)
    return '{"status": True}'


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
