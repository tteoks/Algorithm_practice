#!/bin/bash

LATEST_PY=`find ./ -name "*.py" -printf "%T+ %p\n" | sort -r | head -n 1 | cut -d " " -f2`

echo ${LATEST_PY}
python ${LATEST_PY}
