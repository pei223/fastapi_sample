from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/posts")


class Post(BaseModel):
    id: str
    title: str
    content: str


_posts: List[Post] = [
    Post(id="test1", title="test title1", content="content1"),
    Post(id="test2", title="test title2", content="content2"),
]


@router.get("/", response_model=List[Post])
def get_posts() -> List[Post]:
    return _posts


@router.get("/{post_id}", response_model=Post)
def get_post(post_id: str) -> Post:
    post = list(filter(lambda post: post.id == post_id, _posts))
    if len(post) == 0:
        raise HTTPException(status_code=404)
    return Post(id="test1", title="test title1", content="content1")
