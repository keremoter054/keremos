import {
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";

const API =
  "http://127.0.0.1:8000";

export default function useCalendar() {

  // =====================================
  // STATES
  // =====================================

  const [calendarDays,
    setCalendarDays] =
    useState([]);

  const [selectedDayId,
    setSelectedDayId] =
    useState(null);

  const [selectedTaskId,
    setSelectedTaskId] =
    useState(null);

  const [saveStatus,
    setSaveStatus] =
    useState("");

  const [taskInput,
    setTaskInput] =
    useState("");

  const [todoInput,
    setTodoInput] =
    useState("");

  const [loading,
    setLoading] =
    useState(false);

  const [error,
    setError] =
    useState("");

  // =====================================
  // REFS
  // =====================================

  const saveTimeoutRef =
    useRef(null);

  const isInitialLoad =
    useRef(true);

  const lastSavedRef =
    useRef("");

  // =====================================
  // DATE
  // =====================================

  const startDate =
    useMemo(() => {

      const d = new Date();

      d.setHours(
        0,
        0,
        0,
        0
      );

      return d;

    }, []);

  // =====================================
  // SELECTED
  // =====================================

  const selectedDay =
    calendarDays.find(
      (d) =>
        d.day === selectedDayId
    ) || null;

  const selectedTask =
    selectedDay?.tasks.find(
      (t) =>
        t.id === selectedTaskId
    ) || null;

  // =====================================
  // HELPERS
  // =====================================

  const getDateForDay =
    (dayNumber) => {

      return new Date(
        startDate.getTime() +
        (dayNumber - 1) *
          86400000
      );
    };

  const calculateProgress =
    (todos) => {

      if (!todos?.length)
        return 0;

      const completed =
        todos.filter(
          (t) => t.completed
        ).length;

      return Math.round(
        (
          completed /
          todos.length
        ) * 100
      );
    };

  const calculateDayProgress =
    (day) => {

      if (!day?.tasks?.length)
        return 0;

      const total =
        day.tasks.reduce(
          (acc, task) =>
            acc +
            (task.progress || 0),
          0
        );

      return Math.round(
        total /
        day.tasks.length
      );
    };

  const cloneTask =
    (task) => ({

      ...task,

      id:
        Date.now() +
        Math.random(),

      todos:
        (task.todos || []).map(
          (todo) => ({
            ...todo,
            id:
              Date.now() +
              Math.random(),
          })
        ),
    });

  // =====================================
  // SAVE PAYLOAD
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
          calculateDayProgress(day),

        tasks:
          day.tasks.map(
            (task) => ({

              task_name:
                task.title,

              progress:
                task.progress,

              completed:
                task.progress === 100,

              start_time:
                task.start_time || "",

              end_time:
                task.end_time || "",

              pendingTasks: [],

              todayTasks:
                (task.todos || []).map(
                  (todo) => ({
                    text:
                      todo.text,
                    completed:
                      todo.completed,
                  })
                ),

              developments: [],
            })
          ),
      };
    };

  // =====================================
  // LOAD HISTORY
  // =====================================

  const loadHistory =
    async () => {

      try {

        setLoading(true);

        const res =
          await fetch(
            `${API}/life/history`
          );

        const history =
          await res.json();

        const loadedDays =
          [];

        for (
          let i = 1;
          i <= 365;
          i++
        ) {

          const currentDate =
            getDateForDay(i)
              .toLocaleDateString(
                "sv-SE"
              );

          const matched =
            history.find(
              (d) =>
                d.date ===
                currentDate
            );

          loadedDays.push({

            day: i,

            tasks: matched
              ? matched.tasks.map(
                  (task) => {

                    const todos =
                      (
                        task.todayTasks ||
                        []
                      ).map(
                        (todo) => ({
                          id:
                            Date.now() +
                            Math.random(),

                          text:
                            todo.text,

                          completed:
                            todo.completed,
                        })
                      );

                    return {

                      id:
                        task.id ||
                        Date.now() +
                          Math.random(),

                      title:
                        task.title ||
                        task.task_name ||
                        task.task ||
                        "",

                      todos,

                      progress:
                        task.progress ||
                        calculateProgress(
                          todos
                        ),

                      start_time:
                        task.start_time || "",

                      end_time:
                        task.end_time || "",
                    };
                  }
                )
              : [],
          });
        }

        setCalendarDays(
          loadedDays
        );

        lastSavedRef.current =
          JSON.stringify(
            loadedDays
          );

      } catch (err) {

        console.log(err);

        setError(
          "History yüklenemedi"
        );

      } finally {

        setLoading(false);
      }
    };

  // =====================================
  // INITIAL LOAD
  // =====================================

  useEffect(() => {

    loadHistory();

  }, []);

  // =====================================
  // RETURN
  // =====================================

  return {

    calendarDays,
    setCalendarDays,

    selectedDayId,
    setSelectedDayId,

    selectedTaskId,
    setSelectedTaskId,

    selectedDay,
    selectedTask,

    saveStatus,
    setSaveStatus,

    taskInput,
    setTaskInput,

    todoInput,
    setTodoInput,

    loading,
    error,

    getDateForDay,

    calculateProgress,
    calculateDayProgress,
  };
}