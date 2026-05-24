from fastapi import FastAPI

# =====================================
# CONFIG
# =====================================

from config.settings import (
    APP_NAME,
    APP_VERSION,
)

# =====================================
# DATABASE
# =====================================

from database.connection import (
    initialize_database,
)

from database.migrations import (
    run_migrations,
)

# =====================================
# MIDDLEWARES
# =====================================

from middlewares.cors import (
    setup_cors,
)

from middlewares.error_handler import (
    register_error_handlers,
)

from middlewares.request_logger import (
    register_request_logger,
)

# =====================================
# ROUTERS
# =====================================

from routers.playlists import (
    router as playlists_router,
)

from routers.videos import (
    router as videos_router,
)

from routers.flashcards import (
    router as flashcards_router,
)

from routers.notes import (
    router as notes_router,
)

from routers.goals import (
    router as goals_router,
)

from routers.life import (
    router as life_router,
)

from routers.analytics import (
    router as analytics_router,
)

from routers.shifts import (
    router as shifts_router,
)

from routers.workers import (
    router as workers_router,
)

from routers.health import (
    router as health_router,
)

# =====================================
# WORKERS
# =====================================

from workers.video_worker import (
    start_video_worker,
)

# =====================================
# CREATE APP
# =====================================

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)

# =====================================
# SETUP MIDDLEWARES
# =====================================

setup_cors(app)

register_error_handlers(app)

register_request_logger(app)

# =====================================
# INCLUDE ROUTERS
# =====================================

app.include_router(playlists_router)

app.include_router(videos_router)

app.include_router(flashcards_router)

app.include_router(notes_router)

app.include_router(goals_router)

app.include_router(life_router)

app.include_router(analytics_router)

app.include_router(shifts_router)

app.include_router(workers_router)

app.include_router(health_router)

# =====================================
# STARTUP EVENT
# =====================================


@app.on_event("startup")
async def startup_event():

    print("""
🚀 KEREMOS STARTING
""")

    # =====================================
    # DATABASE
    # =====================================

    initialize_database()

    run_migrations()

    # =====================================
    # WORKER
    # =====================================

    start_video_worker()

    print("""
✅ KEREMOS READY
""")


# =====================================
# ROOT ENDPOINT
# =====================================


@app.get("/")
def root():

    return {
        "status": "ok",
        "app": APP_NAME,
        "version": APP_VERSION,
        "message": "KeremOS API çalışıyor",
    }


# =====================================
# RUN SERVER
# =====================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
