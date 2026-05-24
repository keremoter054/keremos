import {
  useEffect,
  useRef,
} from "react";

const API =
  "http://127.0.0.1:8000";

export default function useAutoSave({

  calendarDays,

  selectedDay,

  calculateDayProgress,

  getDateForDay,

  setSaveStatus,

}) {

  const saveTimeoutRef =
    useRef(null);

  const isInitialLoad =
    useRef(true);

  const lastSavedRef =
    useRef("");

  // =====================================
  // BUILD PAYLOAD
  // =====================================

  const buildSavePayload =
    (day) => {

      return {

        date:
          getDateForDay(
            day.day
          ).toLocaleDateString(
            "sv-SE"
          ),

        overall_progress:
          calculateDayProgress(
            day
          ),

        tasks:
          day.tasks.map(
            (task) => ({

              task_name:
                task.title,

              progress:
                task.progress,

              completed:
                task.progress ===
                100,

              start_time:
                task.start_time ||
                "",

              end_time:
                task.end_time ||
                "",

              pendingTasks:
                [],

              todayTasks:
                (
                  task.todos ||
                  []
                ).map(
                  (todo) => ({
                    text:
                      todo.text,

                    completed:
                      todo.completed,
                  })
                ),

              developments:
                [],
            })
          ),
      };
    };

  // =====================================
  // AUTO SAVE
  // =====================================

  useEffect(() => {

    if (
      isInitialLoad.current
    ) {

      isInitialLoad.current =
        false;

      return;
    }

    if (!selectedDay)
      return;

    const serialized =
      JSON.stringify(
        calendarDays
      );

    if (
      serialized ===
      lastSavedRef.current
    ) {

      return;
    }

    if (
      saveTimeoutRef.current
    ) {

      clearTimeout(
        saveTimeoutRef.current
      );
    }

    saveTimeoutRef.current =
      setTimeout(
        async () => {

          try {

            setSaveStatus(
              "Kaydediliyor..."
            );

            const currentDay =
              calendarDays.find(
                (day) =>
                  day.day ===
                  selectedDay.day
              );

            if (
              !currentDay
            )
              return;

            const payload =
              buildSavePayload(
                currentDay
              );

            console.log(
              "📦 SAVE PAYLOAD",
              payload
            );

            const res =
              await fetch(
                `${API}/life/save-day`,
                {
                  method:
                    "POST",

                  headers: {
                    "Content-Type":
                      "application/json",
                  },

                  body:
                    JSON.stringify(
                      payload
                    ),
                }
              );

            const data =
              await res.json();

            console.log(
              "💾 SAVE RESPONSE",
              data
            );

            if (
              data.status !==
              "ok"
            ) {

              throw new Error(
                data.message ||
                  data.error ||
                  "Save failed"
              );
            }

            lastSavedRef.current =
              serialized;

            setSaveStatus(
              "Kaydedildi"
            );

            setTimeout(() => {

              setSaveStatus("");

            }, 2000);

          } catch (err) {

            console.log(
              "❌ SAVE ERROR",
              err
            );

            setSaveStatus(
              "Save Error"
            );
          }
        },

        1000
      );

    return () => {

      if (
        saveTimeoutRef.current
      ) {

        clearTimeout(
          saveTimeoutRef.current
        );
      }
    };

  }, [calendarDays]);
}