# crums html renderer

Template generator via [Jinja2](http://jinja.pocoo.org/). Made as a microservice.

## Usage

### Server

Run server over docker:

```bash
docker run --rm -v $PWD/public:/code/public -v $PWD/templates:/code/templates -p '5000:5000' crusat/crums_html_renderer
```

or `docker-compose.yml`:

```yaml
version: '3.6'

services:

  crums_html_renderer:
    image: crusat/crums_html_renderer
    volumes:
      - ./templates:/code/templates
      - ./public:/code/public
    ports:
      - '5000:5000'
```

### Client

Examples of client requests with `httpie`:

```bash
sudo apt install httpie
```

Get rendered template:

```bash
http POST http://localhost:5000/ template='pages/index.html' context='{"title": "Home page"}'
```

Render and save template:

```bash
http POST http://localhost:5000/render_and_save/ template='pages/index.html' context='{"title": "Home page"}' save_as='public/index.html'
```

