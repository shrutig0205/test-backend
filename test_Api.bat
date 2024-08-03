@echo off
REM Set the URL for the FastAPI endpoint
set URL=http://127.0.0.1:8000/items/

REM Set the JSON payload for the POST request
set PAYLOAD={"name":"Sample Item","description":"A sample item description","price":25.5,"tax":1.5}

REM Send the POST request using curl
curl -X POST %URL% -H "Content-Type: application/json" -d "%PAYLOAD%"

REM Pause to view the output
pause
