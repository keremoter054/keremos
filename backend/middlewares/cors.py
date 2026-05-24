from fastapi.middleware.cors import (
    CORSMiddleware,
)

# =====================================
# CORS ORIGINS
# =====================================

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

# =====================================
# SETUP CORS
# =====================================


def setup_cors(
    app,
):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    print("""
✅ CORS CONFIGURED
""")
