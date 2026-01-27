#!/bin/bash
tmux new-session -d -s CodeHub -n 'Engine'
tmux new-window -t CodeHub:1 -n 'Radar'
tmux new-window -t CodeHub:2 -n 'Infiltrator'
tmux new-window -t CodeHub:3 -n 'Analyst'
tmux new-window -t CodeHub:4 -n 'Auditor'
tmux new-window -t CodeHub:5 -n 'Harvester'
tmux new-window -t CodeHub:6 -n 'Sniper'
tmux new-window -t CodeHub:7 -n 'AutoFix'
tmux new-window -t CodeHub:8 -n 'CloudSync'
tmux new-window -t CodeHub:9 -n 'Commander'
tmux attach-session -t CodeHub
