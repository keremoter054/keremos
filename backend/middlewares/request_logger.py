import time

from fastapi import Request

# =====================================
# REQUEST LOGGER MIDDLEWARE
# =====================================


async def request_logger_middleware(
    request: Request,
    call_next,
):

    start_time = time.time()

    method = request.method

    path = request.url.path

    print(f"""
➡️ REQUEST START

METHOD:
{method}

PATH:
{path}
""")

    # =====================================
    # PROCESS REQUEST
    # =====================================

    response = await call_next(request)

    # =====================================
    # CALCULATE TIME
    # =====================================

    process_time = round(
        time.time() - start_time,
        4,
    )

    print(f"""
✅ REQUEST END

METHOD:
{method}

PATH:
{path}

STATUS:
{response.status_code}

TIME:
{process_time}s
""")

    # =====================================
    # ADD HEADER
    # =====================================

    response.headers["X-Process-Time"] = str(process_time)

    return response


# =====================================
# REGISTER REQUEST LOGGER
# =====================================


def register_request_logger(
    app,
):

    app.middleware("http")(request_logger_middleware)

    print("""
✅ REQUEST LOGGER REGISTERED
""")
