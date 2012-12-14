from argparse import ArgumentParser

parser = ArgumentParser()
cmds = parser.add_subparsers()

_start = cmds.add_parser('new')
_start.add_argument('slug', required=True)
_start.set_defaults(func=start)

def start():
    pass


_publish = cmds.add_parser('publish')
_publish.add_argument('slug', required=True)
_publish.set_defaults(func=publish)

def publish():
    # move from drafts/ to posts/
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


