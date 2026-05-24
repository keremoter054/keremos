from fastapi import Header
from fastapi import HTTPException

from config.settings import (
    API_SECRET_KEY,
)

# =====================================
# VERIFY API KEY
# =====================================


def verify_api_key(
    x_api_key: str = Header(default=None),
):

    if not API_SECRET_KEY:

        print("""
⚠️ API SECRET KEY EMPTY
""")

        return True

    if not x_api_key:

        raise HTTPException(
            status_code=401,
            detail="API key missing",
        )

    if x_api_key != API_SECRET_KEY:

        raise HTTPException(
            status_code=403,
            detail="Invalid API key",
        )

    return True


# =====================================
# OPTIONAL AUTH
# =====================================


def optional_auth(
    x_api_key: str = Header(default=None),
):

    if not API_SECRET_KEY:

        return True

    if not x_api_key:

        return False

    return x_api_key == API_SECRET_KEY


# =====================================
# ADMIN ONLY
# =====================================


def admin_only(
    x_admin_key: str = Header(default=None),
):

    if not API_SECRET_KEY:

        raise HTTPException(
            status_code=500,
            detail="Admin key not configured",
        )

    if not x_admin_key:

        raise HTTPException(
            status_code=401,
            detail="Admin key missing",
        )

    if x_admin_key != API_SECRET_KEY:

        raise HTTPException(
            status_code=403,
            detail="Invalid admin key",
        )

    return True


# =====================================
# AUTH STATUS
# =====================================


def auth_status():

    return {
        "auth_enabled": bool(API_SECRET_KEY),
        "status": "active" if API_SECRET_KEY else "disabled",
    }
