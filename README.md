# boarddash

## Run locally
```
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py createsuperuser
docker-compose up
```
## Seed Database
```
docker-compose run web python3 manage.py seed_boards
docker-compose run web python3 manage.py seed_db_nyc_311
docker-compose run web python3 manage.py seed_db_budget_requests
```
