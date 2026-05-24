from fastapi import Request
from fastapi.responses import JSONResponse

import traceback

# =====================================
# GLOBAL ERROR HANDLER
# =====================================


async def global_exception_handler(
    request: Request,
    exc: Exception,
):

    print("""
❌ GLOBAL ERROR
""")

    print(f"""
PATH:
{request.url.path}
""")

    print(f"""
METHOD:
{request.method}
""")

    print(f"""
ERROR:
{str(exc)}
""")

    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal Server Error",
            "error": str(exc),
            "path": request.url.path,
        },
    )


# =====================================
# 404 HANDLER
# =====================================


async def not_found_handler(
    request: Request,
    exc,
):

    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Route not found",
            "path": request.url.path,
        },
    )


# =====================================
# VALIDATION ERROR HANDLER
# =====================================


async def validation_exception_handler(
    request: Request,
    exc,
):

    print("""
⚠️ VALIDATION ERROR
""")

    print(exc)

    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "message": "Validation Error",
            "details": exc.errors(),
        },
    )


# =====================================
# REGISTER ERROR HANDLERS
# =====================================


def register_error_handlers(
    app,
):

    from fastapi.exceptions import (
        RequestValidationError,
    )

    app.add_exception_handler(
        Exception,
        global_exception_handler,
    )

    app.add_exception_handler(
        404,
        not_found_handler,
    )

    app.add_exception_handler(
        RequestValidationError,
        validation_exception_handler,
    )

    print("""
✅ ERROR HANDLERS REGISTERED
""")
