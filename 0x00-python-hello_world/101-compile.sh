#!/bin/bash
python -m py_compile $PYFILE
mv __pycache__/*.pyc ./$PYFILE'c'
chmod +x $PYFILE'c'
rmdir __pycache__