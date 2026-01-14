test:
	pytest -q

run:
	uvicorn main:app --host 0.0.0.0 --port 8000

dev: 
	uvicorn main:app --reload

keys:
	openssl genrsa -out private.pem 2048
	openssl req -new -x509 -key private.pem -out public.pem -days 365

