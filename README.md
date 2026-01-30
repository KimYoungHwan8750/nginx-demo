Auto Scaleout 방식

`docker compose -f auto_round_robin.yml up --scale fastapi=2 -d --build`

Docker DNS에 의해 같은 서비스에 접근시 요청이 자동으로 각 컨테이너에 분산된다.

Load Balance 방식

`docker compose -f round_robin.yml up -d --build`

http://localhost:3336/으로 접속시 특정 해시값이 로테이션으로 나타난다.

```nginx
upstream roundrobin {
    server fastapi1:8000;
    server fastapi2:8000 weight=2;
    server fastapi3:8000;
}
```

그 중 특정 해시값이 두 번 연속 나타나는 경우가 있는데 그것이 가중치 2로 설정된 fastapi2 서버다.
