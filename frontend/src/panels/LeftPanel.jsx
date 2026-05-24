// =====================================
// LEFT PANEL
// =====================================

import React from "react";

export default function LeftPanel({

  goals,
  selectedGoalId,
  setSelectedGoalId,

  goalForm,
  setGoalForm,

  createGoal,
  predictGoal,

  selectedDay,
  calculateDayProgress,
  calculateGoalProgress,

  error,

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

  return (

    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "20px",
      }}
    >

      {/* GOALS */}

      <div style={cardStyle}>

        <h2>Goals</h2>

        <input
          placeholder="Goal"
          value={goalForm.title}
          onChange={(e) =>
            setGoalForm({
              ...goalForm,
              title: e.target.value,
            })
          }
          style={inputStyle}
        />

        <textarea
          placeholder="Goal Description"
          value={goalForm.description}
          onChange={(e) =>
            setGoalForm({
              ...goalForm,
              description: e.target.value,
            })
          }
          style={{
            ...inputStyle,
            minHeight: "100px",
            resize: "vertical",
          }}
        />

        <input
          type="date"
          value={goalForm.deadline_date}
          onChange={(e) =>
            setGoalForm({
              ...goalForm,
              deadline_date: e.target.value,
            })
          }
          style={inputStyle}
        />

        <button
          onClick={createGoal}
          style={buttonStyle}
        >
          Goal Create
        </button>

        <div
          style={{
            marginTop: "20px",
          }}
        >

          {goals.length === 0 && (

            <div
              style={{
                opacity: 0.6,
                fontSize: "14px",
              }}
            >
              Henüz goal oluşturulmadı.
            </div>
          )}

          {goals.map((goal) => {

            const progress =
              calculateGoalProgress(goal);

            return (

              <div
                key={goal.id}
                onClick={() => {

                  setSelectedGoalId(goal.id);

                  predictGoal(goal.id);
                }}
                style={{
                  background:
                    selectedGoalId === goal.id
                      ? "#333"
                      : "#222",

                  padding: "15px",

                  marginBottom: "10px",

                  borderRadius: "10px",

                  cursor: "pointer",
                }}
              >

                <div
                  style={{
                    fontWeight: "bold",
                  }}
                >
                  {goal.title}
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
                      width: `${progress}%`,
                      height: "100%",
                      background: "lime",
                    }}
                  />
                </div>

                <div
                  style={{
                    marginTop: "8px",
                    fontSize: "12px",
                    opacity: 0.8,
                  }}
                >
                  Requirement:
                  {" "}
                  {goal.requirements?.length || 0}
                  {" "}
                  • %
                  {progress}
                </div>

                <div
                  style={{
                    marginTop: "6px",
                    fontSize: "12px",
                    opacity: 0.7,
                  }}
                >
                  Deadline:
                  {" "}
                  {goal.deadline_date || "Yok"}
                </div>

              </div>
            );
          })}

        </div>

      </div>

      {/* ANALYTICS */}

      <div style={cardStyle}>

        <h2>Analytics</h2>

        <div>
          Total Goals:
          {" "}
          {goals.length}
        </div>

        <div
          style={{
            marginTop: "8px",
          }}
        >
          Selected Day Progress:
          {" "}
          {selectedDay
            ? `%${calculateDayProgress(selectedDay)}`
            : "-"}
        </div>

      </div>

      {/* FACTORY */}

      <div style={cardStyle}>

        <h2>Factory Mode</h2>

        <div
          style={{
            opacity: 0.7,
            fontSize: "14px",
          }}
        >
          Vacuum • Integrity • Sensor Map • Shift
        </div>

      </div>

      {/* ERROR */}

      {error && (

        <div
          style={{
            ...cardStyle,
            border: "1px solid red",
            color: "#ff8a8a",
          }}
        >
          ERROR:
          {" "}
          {error}
        </div>
      )}

    </div>
  );
}