import React from "react";
import TaskSection from "./TaskSection";
export default function TimelineSection({

  selectedDay,

  taskInput,
  setTaskInput,

  selectedTaskId,
  setSelectedTaskId,

  todoInput,
  setTodoInput,

  addTask,
  deleteTask,
  updateTaskTime,

  addTodo,
  toggleTodo,
  deleteTodo,

  autoReschedule,
  copySelectedDayToNextDays,
  apply21DayCycleToYear,

  getDateForDay,

}) {

  const cardStyle = {
    background: "#181818",
    padding: "18px",
    borderRadius: "16px",
    border: "1px solid #2a2a2a",
  };

  const inputStyle = {
    width: "100%",
    padding: "10px",
    marginTop: "10px",
    background: "#0f0f0f",
    color: "white",
    border: "1px solid #333",
    borderRadius: "8px",
    boxSizing: "border-box",
  };

  const buttonStyle = {
    width: "100%",
    padding: "12px",
    marginTop: "10px",
    background: "lime",
    color: "black",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    fontWeight: "bold",
  };

  if (!selectedDay) {

    return null;
  }

  return (

    <div style={cardStyle}>

      <h2>
        Gün {selectedDay.day}
      </h2>

      <div
        style={{
          opacity: 0.7,
          fontSize: "13px",
        }}
      >
        {
          getDateForDay(
            selectedDay.day
          ).toLocaleDateString(
            "tr-TR"
          )
        }
      </div>

      <button
        onClick={autoReschedule}
        style={{
          ...buttonStyle,
          background: "#00d4ff",
        }}
      >
        Unfinished → Tomorrow
      </button>

      <button
        onClick={() =>
          copySelectedDayToNextDays(6)
        }
        style={{
          ...buttonStyle,
          background: "#22c55e",
        }}
      >
        Bu Günü Haftaya Kopyala
      </button>

      <button
        onClick={
          apply21DayCycleToYear
        }
        style={{
          ...buttonStyle,
          background: "#facc15",
          color: "black",
        }}
      >
        İlk 21 Günü 365 Güne Yay
      </button>

      <input
        placeholder="Task"
        value={taskInput}
        onChange={(e) =>
          setTaskInput(
            e.target.value
          )
        }
        onKeyDown={(e) => {

          if (e.key === "Enter") {

            addTask();
          }
        }}
        style={inputStyle}
      />

      <button
        onClick={addTask}
        style={buttonStyle}
      >
        Task Add
      </button>

      <div
        style={{
          marginTop: "20px",
        }}
      >

        {selectedDay.tasks.map(
          (task) => (

            <div
              key={task.id}
              onClick={() =>
                setSelectedTaskId(
                  task.id
                )
              }
              style={{
                background:
                  selectedTaskId ===
                  task.id
                    ? "#333"
                    : "#222",

                padding: "15px",

                marginBottom: "15px",

                borderRadius: "10px",

                border:
                  selectedTaskId ===
                  task.id
                    ? "1px solid lime"
                    : "1px solid #333",
              }}
            >

              <div
                style={{
                  display: "flex",
                  justifyContent:
                    "space-between",
                  gap: "10px",
                }}
              >

                <div>
                  <div
                    style={{
                      fontWeight:
                        "bold",
                    }}
                  >
                    {task.title}
                  </div>

                  <div
                    style={{
                      marginTop: "6px",
                      fontSize: "12px",
                      opacity: 0.7,
                    }}
                  >
                    Todo:
                    {" "}
                    {task.todos.length}
                  </div>
                </div>

                <button
                  onClick={(e) => {

                    e.stopPropagation();

                    deleteTask(task.id);
                  }}
                  style={{
                    background: "red",
                    color: "white",
                    border: "none",
                    borderRadius: "6px",
                    padding: "6px 8px",
                    height: "32px",
                    cursor: "pointer",
                  }}
                >
                  Sil
                </button>

              </div>

              <div
                style={{
                  display: "grid",
                  gridTemplateColumns:
                    "1fr 1fr",
                  gap: "8px",
                  marginTop: "10px",
                }}
              >

                <input
                  placeholder="Start"
                  value={
                    task.start_time || ""
                  }
                  onChange={(e) =>
                    updateTaskTime(
                      task.id,
                      "start_time",
                      e.target.value
                    )
                  }
                  style={{
                    ...inputStyle,
                    marginTop: 0,
                  }}
                />

                <input
                  placeholder="End"
                  value={
                    task.end_time || ""
                  }
                  onChange={(e) =>
                    updateTaskTime(
                      task.id,
                      "end_time",
                      e.target.value
                    )
                  }
                  style={{
                    ...inputStyle,
                    marginTop: 0,
                  }}
                />

              </div>

              <div
                style={{
                  marginTop: "10px",
                  height: "8px",
                  background: "#333",
                  borderRadius: "999px",
                  overflow: "hidden",
                }}
              >
                <div
                  style={{
                    width:
                      `${task.progress}%`,
                    height: "100%",
                    background: "lime",
                  }}
                />
              </div>

              {selectedTaskId ===
                task.id && (

                <div
                  style={{
                    marginTop: "15px",
                  }}
                >

                  <input
                    placeholder="Todo"
                    value={todoInput}
                    onChange={(e) =>
                      setTodoInput(
                        e.target.value
                      )
                    }
                    onKeyDown={(e) => {

                      if (
                        e.key === "Enter"
                      ) {

                        addTodo();
                      }
                    }}
                    style={inputStyle}
                  />

                  <button
                    onClick={addTodo}
                    style={buttonStyle}
                  >
                    Todo Add
                  </button>

                  <div
                    style={{
                      marginTop: "15px",
                    }}
                  >

                    {task.todos.map(
                      (todo) => (

                        <div
                          key={todo.id}
                          style={{
                            display:
                              "flex",
                            alignItems:
                              "center",
                            gap: "10px",
                            marginBottom:
                              "10px",
                          }}
                        >

                          <input
                            type="checkbox"
                            checked={
                              todo.completed
                            }
                            onChange={() =>
                              toggleTodo(
                                todo.id
                              )
                            }
                          />

                          <div
                            style={{
                              flex: 1,
                              textDecoration:
                                todo.completed
                                  ? "line-through"
                                  : "none",
                            }}
                          >
                            {todo.text}
                          </div>

                          <button
                            onClick={() =>
                              deleteTodo(
                                todo.id
                              )
                            }
                            style={{
                              background:
                                "red",
                              color: "white",
                              border: "none",
                              borderRadius:
                                "6px",
                              padding:
                                "4px 8px",
                              cursor:
                                "pointer",
                            }}
                          >
                            Sil
                          </button>

                        </div>
                      )
                    )}

                  </div>

                </div>
              )}

            </div>
          )
        )}

      </div>

    </div>
  );
}