
tmux new-session -d 'gunicorn --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app'
