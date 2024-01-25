# local: 
gunicorn -w 2 -b 127.0.0.1:3000 main:app --timeout 300

# docker:
# gunicorn -w 2 -b 0.0.0.0:3000 main:app --timeout 300