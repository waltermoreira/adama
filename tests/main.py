import json

def process(args):
    print json.dumps({
        'obj': 1,
        'args': args
    })
    print '---'
    print json.dumps({
        'obj': 2,
        'args': args
    })
    print 'END'
