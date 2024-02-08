pid=$(pgrep -f "python manage.py runserver 0.0.0.0:8000")

if [ -n "$pid" ]; then
    kill "$pid"
    echo "Process with PID $pid has been killed."
else
    echo "Process is not running."
fi
