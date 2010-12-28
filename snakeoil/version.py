# Copyright: 2006 Marien Zwart <marienz@gentoo.org>
# License: BSD/GPL2


"""Version information (tied to bzr)."""


__version__ = '0.3.7'

_ver = None

def get_git_version():
    """:return: git sha1 rev"""
    import subprocess, os

    env = dict(os.environ)
    env["LC_CTYPE"] = "C"
    
    r = subprocess.Popen(["git", "log", "HEAD^..HEAD"], stdout=subprocess.PIPE, env=env)
    if r.wait() != 0:
        return "unknown (couldn't identify from git)"
    data = r.stdout.read().split("\n")
    commit = [x.split()[-1] for x in data if x.startswith("commit")][0]
    date = [x.split(":", 1)[-1].lstrip() for x in data if x.lower().startswith("date")][0]
    return "git rev %s, date %s" % (commit, date)

def get_version():
    """:return: a string describing the snakeoil version."""
    global _ver
    if _ver is not None:
        return _ver

    try:
        from snakeoil._verinfo import version_info
    except ImportError:
        version_info = get_git_version()

    _ver = 'snakeoil %s\n(%s)' % (__version__, version_info)

    return _ver
