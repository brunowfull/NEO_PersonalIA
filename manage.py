#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NEO_PersonalIA.settings')
    try:
        from manage import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import manage module. Did you specify the right directory?"
        ) from exc
    execute_from_command_line(sys.argv)