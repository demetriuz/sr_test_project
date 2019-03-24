# sr_test_project

There are 2 apps:
- alignment_tags_domain -- domain with models (non-ORM), interfaces, DTOs, etc). It is isolated from framework and can be used with any web-framework and ORM
- alignment_tags -- "domain implementation" in Django-terms

## Usage:
Run app:
```
docker-compose up web
```
and then http://localhost:8080/

Run tests:
```
docker-compose up test
```

Container is stateless -- migrations and fixture imports from CSV occurs when the container is started.

