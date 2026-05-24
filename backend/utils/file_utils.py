import os
import json
import shutil
from datetime import datetime

# =====================================
# ENSURE DIRECTORY
# =====================================


def ensure_directory(
    path,
):

    os.makedirs(
        path,
        exist_ok=True,
    )

    return path


# =====================================
# FILE EXISTS
# =====================================


def file_exists(
    path,
):

    return os.path.exists(path)


# =====================================
# READ TEXT FILE
# =====================================


def read_text_file(
    path,
    encoding="utf-8",
):

    with open(
        path,
        "r",
        encoding=encoding,
    ) as file:

        return file.read()


# =====================================
# WRITE TEXT FILE
# =====================================


def write_text_file(
    path,
    content,
    encoding="utf-8",
):

    with open(
        path,
        "w",
        encoding=encoding,
    ) as file:

        file.write(content)

    return path


# =====================================
# APPEND TEXT FILE
# =====================================


def append_text_file(
    path,
    content,
    encoding="utf-8",
):

    with open(
        path,
        "a",
        encoding=encoding,
    ) as file:

        file.write(content)

    return path


# =====================================
# READ JSON FILE
# =====================================


def read_json_file(
    path,
):

    if not file_exists(path):

        return None

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# =====================================
# WRITE JSON FILE
# =====================================


def write_json_file(
    path,
    data,
):

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )

    return path


# =====================================
# DELETE FILE
# =====================================


def delete_file(
    path,
):

    if file_exists(path):

        os.remove(path)

        return True

    return False


# =====================================
# COPY FILE
# =====================================


def copy_file(
    source,
    target,
):

    shutil.copy2(
        source,
        target,
    )

    return target


# =====================================
# MOVE FILE
# =====================================


def move_file(
    source,
    target,
):

    shutil.move(
        source,
        target,
    )

    return target


# =====================================
# FILE SIZE
# =====================================


def get_file_size(
    path,
):

    if not file_exists(path):

        return 0

    return os.path.getsize(path)


# =====================================
# FORMAT FILE SIZE
# =====================================


def format_file_size(
    size_bytes,
):

    if size_bytes < 1024:

        return f"{size_bytes} B"

    if size_bytes < 1024 * 1024:

        return f"{round(size_bytes / 1024, 2)} KB"

    if size_bytes < 1024 * 1024 * 1024:

        return f"{round(size_bytes / (1024 * 1024), 2)} MB"

    return f"{round(size_bytes / (1024 * 1024 * 1024), 2)} GB"


# =====================================
# LIST FILES
# =====================================


def list_files(
    folder_path,
):

    if not os.path.exists(folder_path):

        return []

    return os.listdir(folder_path)


# =====================================
# FILE INFO
# =====================================


def get_file_info(
    path,
):

    if not file_exists(path):

        return None

    stats = os.stat(path)

    return {
        "path": path,
        "size": stats.st_size,
        "formatted_size": format_file_size(stats.st_size),
        "created_at": datetime.fromtimestamp(stats.st_ctime).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "updated_at": datetime.fromtimestamp(stats.st_mtime).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
    }


# =====================================
# CREATE TEMP FILE
# =====================================


def create_temp_file(
    folder="temp",
    extension=".txt",
):

    ensure_directory(folder)

    filename = f"{datetime.now().timestamp()}" f"{extension}"

    path = os.path.join(
        folder,
        filename,
    )

    write_text_file(
        path,
        "",
    )

    return path
