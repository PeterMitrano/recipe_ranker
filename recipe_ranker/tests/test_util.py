import logging
from nose.plugins.attrib import attr

logging.getLogger('boto3').setLevel(logging.WARNING)
logging.getLogger('botocore').setLevel(logging.WARNING)
logging.getLogger('nose').setLevel(logging.WARNING)

def wip(f):
    return attr('wip')(f)
