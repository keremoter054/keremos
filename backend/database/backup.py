import os
import shutil
import traceback
from datetime import datetime

from config.settings import (
    DB_PATH,
    BACKUP_DIR,
)

# =====================================
# BACKUP DB
# =====================================


def backup_db():

    try:

        # =====================================
        # ENSURE BACKUP FOLDER
        # =====================================

        os.makedirs(
            BACKUP_DIR,
            exist_ok=True,
        )

        # =====================================
        # TIMESTAMP
        # =====================================

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # =====================================
        # BACKUP PATH
        # =====================================

        backup_path = os.path.join(
            BACKUP_DIR,
            f"app_backup_{timestamp}.db",
        )

        # =====================================
        # COPY DB
        # =====================================

        shutil.copy2(
            DB_PATH,
            backup_path,
        )

        print(f"""
✅ BACKUP CREATED

PATH:
{backup_path}
""")

        return {
            "status": "ok",
            "backup_path": backup_path,
        }

    except Exception as e:

        print(f"""
❌ BACKUP ERROR

ERROR:
{e}
""")

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }


# =====================================
# LIST BACKUPS
# =====================================


def list_backups():

    try:

        os.makedirs(
            BACKUP_DIR,
            exist_ok=True,
        )

        files = []

        for file in os.listdir(BACKUP_DIR):

            if file.endswith(".db"):

                full_path = os.path.join(
                    BACKUP_DIR,
                    file,
                )

                stat = os.stat(full_path)

                files.append(
                    {
                        "file": file,
                        "path": full_path,
                        "size_mb": round(
                            stat.st_size / 1024 / 1024,
                            2,
                        ),
                        "created_at": datetime.fromtimestamp(stat.st_ctime).strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                    }
                )

        files.sort(
            key=lambda x: x["created_at"],
            reverse=True,
        )

        return {
            "status": "ok",
            "count": len(files),
            "backups": files,
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }


# =====================================
# DELETE BACKUP
# =====================================


def delete_backup(filename):

    try:

        backup_path = os.path.join(
            BACKUP_DIR,
            filename,
        )

        if not os.path.exists(backup_path):

            return {
                "status": "error",
                "error": "Backup bulunamadı",
            }

        os.remove(backup_path)

        print(f"""
🗑️ BACKUP DELETED

FILE:
{filename}
""")

        return {
            "status": "ok",
            "deleted": filename,
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }
