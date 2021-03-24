from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from functools import partial
from starter.config import common

user_engine = create_engine(
    common.USER_MYSQL,
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
    pool_timeout=30,
    pool_recycle=120
)

new_engine = create_engine(
    common.MYSQL,
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=10,  # 连接池大小
    pool_timeout=30,
    pool_recycle=120
)

UserSession = sessionmaker(bind=user_engine)
NewSession = sessionmaker(bind=new_engine)

# 使用上下文管理session
# with xxx_session_scope() as session:
#     pass
@contextmanager
def session_scope(maker):
    session = maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

user_session_scope = partial(session_scope, maker=UserSession)
new_session_scope = partial(session_scope, maker=NewSession)

__all__ = ('user_session_scope', 'new_session_scope')
