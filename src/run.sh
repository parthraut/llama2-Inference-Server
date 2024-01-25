# local: 
gunicorn -w 16 -b 127.0.0.1:3000 main:app --timeout 500

# docker:
# gunicorn -w 2 -b 0.0.0.0:3000 main:app --timeout 300