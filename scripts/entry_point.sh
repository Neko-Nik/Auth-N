# Run the gunicorn service
gunicorn \
    --workers=${GUNICORN_ARG_WORKERS} \
    --threads=${GUNICORN_ARG_THREADS} \
    --reload --bind 0.0.0.0:${GUNICORN_ARG_BIND_PORT} \
    --timeout ${GUNICORN_ARG_TIMEOUT} \
    --reload --capture-output \
    --error-logfile /var/log/api/error_log.txt \
    --access-logfile /var/log/api/guicorn_log.txt \
    -k uvicorn.workers.UvicornWorker api.main:app
