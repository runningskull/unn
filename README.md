Since the world needs more static site generators ([it](http://nanoc.ws/about/#similar-projects) [doesn't](https://gist.github.com/2254924)), I built one. It's not "all things for all people". Not a [747](https://github.com/mojombo/jekyll), just a tiny [ultralight](http://www.homebuiltairplanes.com/forums/attachments/light-stuff-area/1382d1204108895-need-free-ultralight-plans-guidance-spratt103_cote_droit.jpg) to automate some things.

Its goals are simple:

1. Maintain a list of finished posts & unfinished ideas
2. Render finished posts into an HTML template
3. Do as little else as possible

The script is altogether &asymp;130 lines of Python code, and probably won't ever be much larger (hopefully I'll cut it down some). I chose [markdown](http://daringfireball.net/projects/markdown/basics) formatting, and [Jinja2](http://jinja.pocoo.org/docs/) for templating, and S3 for deployment.

I'm calling it `unn` because naming things is hard.

Invoked from the command line, it knows how to do 3 things:

- `unn idea post-slug` - start a new draft called "post-slug"
- `unn build` - convert "published" files into an HTML site
- `unn deploy` - deploy the site to S3 (& build it first)

To "publish" a post, I simply move the file from `/ideas` into `/posts`, and run `unn deploy`

It's not perfect, but it does the job. Feel free to open a PR for improvements.

`unn` currently powers [juanpatten.com](http://www.juanpatten.com)


## TODO:

- bundle as python package w/ binary

