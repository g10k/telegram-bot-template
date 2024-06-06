
build:
	docker-compose -p kb-team build

up:
	docker-compose -p kb-team up -d
down:
	docker-compose -p kb-team down

restart:
	docker-compose -p kb-team restart bot

enter:
	docker exec -it bot sh

shell:
	docker exec -it bot ipython

logs:
	docker logs bot --tail 50 -f

psql:
	docker exec -it postgres psql -U tgbot -d bot_db

