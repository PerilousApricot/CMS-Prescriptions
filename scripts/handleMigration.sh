#!/bin/bash

ssh se9.accre.vanderbilt.edu 'tail -f -n 100 /data/priority-install/current/install/wmagent/DBSUpload/ComponentLog' | grep --line-buffered 'No such' | awk '{print $8; fflush(stdout)}' | xargs -n1 -I{} ./das.py --query='block file={}' --format=plain  | grep --line-buffered AOD | xargs -x -n 1 ./migrateDbs.py 
