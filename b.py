#!/usr/bin/env python

import logging
logging.getLogger('scss').addHandler(logging.StreamHandler())

import os, sys, shutil, subprocess
import cli, config, scss
from markdown import markdown
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from os.path import exists, join
from glob import glob


DATE_FORMAT = '%a %b %d %H:%M:%S %Y'
scss.LOAD_PATHS = [config.compass_path]

def _unslug(slug):
    return slug.replace('-', ' ').title()

def _extract_title(body_md):
    return body_md.split('\n', 1)[0]

def _ask_for_draft():
    slugs = [g.replace('drafts/', '').replace('.md', '') 
             for g in glob('drafts/*.md')]
    rng = ['[{}]'.format(x) for x in range(len(slugs))]
    print '\n'.join([' '.join(x) for x in zip(rng, slugs)])
    return slugs[int(raw_input('Which draft? '))]


@cli.command
def draft(slug):
    _exists = lambda folder: exists('{}/{}.md'.format(folder, slug))

    if _exists('drafts') or _exists('posts'):
        cli.EXIT('That slug already exists!')

    content = open('_template/_new_draft.md').read().format(
        date = datetime.now().strftime(DATE_FORMAT),
        title = _unslug(slug)
    )

    filename = 'drafts/{}.md'.format(slug)
    with open(filename, 'w') as _draft:
        _draft.write(content)
    cmd = config.editor.format(join(os.getcwd(), filename))
    subprocess.call(cmd, shell=True)


@cli.command
def publish(slug=None):
    slug = slug or _ask_for_draft()

    if not exists('drafts/{}.md'.format(slug)):
        cli.EXIT('No draft by that name!')

    if exists('posts/{}.md'.format(slug)):
        cli.EXIT('That post already exists!')

    shutil.move('drafts/{}.md'.format(slug), 'posts/{}.md'.format(slug))
    build()


@cli.command
def build():
    def write_file(slug, html):
        with open(join('_public', slug+'.html'), 'w') as output:
            output.write(html)

    def parse_post(filename):
        head, md = open(filename).read().split('\n\n', 1)
        head = dict([line.split(': ') for line in head.split('\n')])
        head['Title'] = md.split('\n', 1)[0].replace('# ', '')
        head['Date'] = datetime.strptime(head['Date'], DATE_FORMAT)
        return head, md

    def render_single(slug, md):
        ctx = dict(headers[slug], **{'post_html': markdown(md)})
        write_file(slug, tpl_single.render(ctx))

    def render_index():
        ctx = {'posts': [dict(headers[x[0]], **{'Slug':x[0]}) for x in chron_order]}
        write_file('index', tpl_index.render(ctx))

    def render_css():
        css = scss.Scss().compile(open(join('_template', 'style.scss')).read())
        with open(join('_public', 'style.css'), 'w') as output:
            output.write(css)

    def copy_assets():
        shutil.rmtree('_public/assets')
        shutil.copytree('assets', '_public/assets')

    posts = glob('posts/*.md')
    env = Environment(loader=FileSystemLoader('_template'))
    tpl_single = env.get_template('single.html')
    tpl_index = env.get_template('index.html')

    headers = {}
    chron_order = []

    for post in posts:
        slug = post.replace('.md', '').replace('posts/', '')
        headers[slug], md = parse_post(post)
        chron_order.append((slug, headers[slug]['Date']))
        render_single(slug, md)

    chron_order = sorted(chron_order, key=lambda tup: tup[1], reverse=True)
    render_index()
    render_css()
    copy_assets()
    print("BUILT!")
    

@cli.command
def deploy():
    pass


if __name__ == '__main__':
    cli.run()


