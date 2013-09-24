_I wrote about [my reasoning](http://www.juanpatten.com/first-post.html)_

## Start your blog

1. Fork [unn-skeleton](https://github.com/runningskull/unn-skeleton)
2. Clone your new repository to your computer (optionally, run `mkvirtualenv myblog`)
3. Run `pip install -r requirements.txt`
4. Edit config.py to set up your deployment settings (default is S3)
5. Think of something good to write (this step is harder than the others)


## Use it day-to-day

`unn idea my-idea` to start a new draft. Use markdown for formatting.  
`unn publish my-idea` to convert a draft to a post.  
`unn build` to build your site's pages.  
`unn local` to serve it locally.  
`unn deploy` to push it live. (this will build first, as a convenience)


## Customize it
Check the `_template` folder for the basic file structure. `unn` uses Jinja2 for templating.

The `index.html` template gets the following context:
```
{
    "posts": [{
        "Slug": "the-file-name-without-.md"
        ... all headers included in this post ...
    }, ...]
}
```


The `single.html` template gets the following context:
```
{
    "post_html": "<p>The rendered HTML of the post</p>",
    ... all headers included in this post ...
}
```

`base.html` defines the box that `index.html` and `single.html` live inside (ie. header/footer).  
`error.html` is a generic error display page.

