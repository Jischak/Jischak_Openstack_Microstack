# Tweaks to make this run nicely in a snap.

# TODO: turn this off once everything is working nicely.
DEBUG = True

# Set our webroot.
WEBROOT = '/'

# Django wants to write out compressed files even when we turn
# compression off (either a bug or something that I'm not
# understanding). Tell it to write them some place writeable.
STATIC_ROOT = '/var/snap/microstack/common/var/horizon/static'

# Disable extra themes for now. TODO: Re-enable when
# https://github.com/CanonicalLtd/microstack/issues/39 is
# addressed. (You'll need to uncomment the material theme below when testing
# the fix.)
AVAILABLE_THEMES = [
    ('default', 'Default', 'themes/default'),
    #    ('material', 'Material', 'themes/material'),
    ('ubuntu', 'Ubuntu', 'themes/ubuntu'),
]

# Point us at keystone.
OPENSTACK_HOST = "10.20.20.1"
OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "_member_"

# Turn off external access for now.  (This should be turned on once we
# have hooks for setting a non default password.)
ALLOWED_HOSTS = "*".split(",")

# Use memcached as our caching backend.
CACHES = {
    'default': {
       #
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '10.20.20.1:11211',
    }
}
SESSION_ENGINE='django.contrib.sessions.backends.cache'

