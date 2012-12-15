import sys, shutil
from os.path import exists, join
from datetime.datetime import now
from argparse import ArgumentParser
from pygit2 import Commit

parser = ArgumentParser()
cmds = parser.add_subparsers()


def _file_exists(paths=None):
    filename = args.slug + '.md'
    if not paths: paths = ('drafts', 'posts')
    existing = [exists(join(p, filename)) for p in paths]
    return len(existing)


_start = cmds.add_parser('new')
_start.add_argument('slug', required=True)
_start.set_defaults(func=start)

def start():
    if _file_exists():
        print 'File already exists'
        return sys.exit(1)

    draft = open(join('template', '_new_draft.md'), 'r').read()
    with open(join('drafts', filename), 'w', encoding='utf-8') as f:
        f.write(draft.format(date=str(now())))


_publish = cmds.add_parser('publish')
_publish.add_argument('slug', required=True)
_publish.set_defaults(func=publish)

def publish():
    if _file_exists(('posts',)):
        print 'Post is already published'
        return sys.exit(1)

    if not _file_exists(('drafts',)):
        print 'Draft does not exist'
        return sys.exit(1)

    filename = args.slug + '.md'
    swap = [join('drafts', filename), join('posts', filename)]
    shutil.copy2(swap[0], swap[1])
    # commit msg "Published {slug}"
    pass


_save = cmds.add_parser('save')
_save.add_argument('slug', required=False)
_save.set_defaults(func=save)

def save():
    if slug:
        # save file w/ commit msg "Update [post|draft] {slug}"
        pass
    else:
        # save all w/ commit msg "Snapshot: {date}"
        pass
        

_build = cmds.add_parser('build')
_build.set_defaults(func=build)

def build():
    pass


_deploy = cmds.add_parser('deploy')
_deploy.set_defaults(func=deploy)

def deploy():
    pass


_serve = cmds.add_parser('serve', aliases=('-',))
_serve.set_defaults(func=serve)

def serve():
    pass


args = parser.parse_args()


