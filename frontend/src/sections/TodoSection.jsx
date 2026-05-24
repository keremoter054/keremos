import React from "react";

export default function TodoSection({

  task,
  todoInput,
  setTodoInput,

  addTodo,
  toggleTodo,
  deleteTodo,

}) {

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

  return (

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

          if (e.key === "Enter") {

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

        {(task.todos || []).map(
          (todo) => (

            <div
              key={todo.id}
              style={{
                display: "flex",
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

                  opacity:
                    todo.completed
                      ? 0.6
                      : 1,
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
  );
}