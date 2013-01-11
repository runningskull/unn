import sys

commands = {}
args = []
kwargs = {}


def EXIT(msg, code=1):
    print(msg)
    sys.exit(code)

def command(fn):
    commands[fn.__name__] = fn
    return fn


def run():
    if len(sys.argv) < 2:
        EXIT('No command provided')

    cmd = sys.argv[1]

    if cmd not in commands:
        EXIT('Unkown command')

    args = [x for x in sys.argv[2:] if '=' not in x]
    kwargs = dict([x.split('=') for x in sys.argv[2:] if '=' in x])
    kwargs = dict([(k.replace('-', ''),v) for k,v in kwargs.items()])

    commands[cmd](*args, **kwargs)
