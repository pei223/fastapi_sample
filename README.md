## FastAPI sample

## Setup

```
poetry install
```

## deploy

```
poetry run uvicorn fastapi_sample.main:app --reload
http://127.0.0.1:8000/posts

```

### docs

```
http://127.0.0.1:8000/docs
```

## 静的解析・テスト

```
make tests
```

## やること

- SQLAlchemy で DB 連携
- VSCode での型警告など
- 静的解析
- 起動スクリプトを poetry に移行
