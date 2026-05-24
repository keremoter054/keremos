import React from "react";

export default function GoalSection({

  selectedGoal,

  goalForm,
  setGoalForm,

  addRequirement,
  toggleRequirement,

  calculateGoalProgress,

  goalPrediction,

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

  if (!selectedGoal) {

    return null;
  }

  return (

    <div style={cardStyle}>

      <h2>
        Goal Requirements
      </h2>

      <div>
        Goal:
        {" "}
        {selectedGoal.title}
      </div>

      <div
        style={{
          marginTop: "10px",
          opacity: 0.7,
        }}
      >
        {selectedGoal.description}
      </div>

      <div
        style={{
          marginTop: "12px",
          padding: "12px",
          background: "#222",
          borderRadius: "10px",
        }}
      >

        <div>
          Deadline:
          {" "}
          {selectedGoal.deadline_date ||
            "Yok"}
        </div>

        <div
          style={{
            marginTop: "8px",
            fontSize: "13px",
            opacity: 0.8,
          }}
        >
          Progress:
          {" "}
          %
          {calculateGoalProgress(
            selectedGoal
          )}
        </div>

        {goalPrediction && (

          <div
            style={{
              marginTop: "8px",
              fontSize: "13px",
              opacity: 0.8,
            }}
          >
            Remaining Requirements:
            {" "}
            {
              goalPrediction.remaining_requirements
            }
          </div>
        )}

      </div>

      <input
        placeholder="Requirement"
        value={
          goalForm.requirementInput
        }
        onChange={(e) =>
          setGoalForm({
            ...goalForm,
            requirementInput:
              e.target.value,
          })
        }
        style={inputStyle}
      />

      <button
        onClick={() =>
          addRequirement(
            selectedGoal.id,
            goalForm.requirementInput
          )
        }
        style={buttonStyle}
      >
        Requirement Add
      </button>

      <div
        style={{
          marginTop: "20px",
        }}
      >

        {(selectedGoal.requirements || [])
          .map((req) => (

          <div
            key={req.id}
            style={{
              display: "flex",
              alignItems:
                "center",
              gap: "10px",
              marginBottom:
                "10px",
              background: "#222",
              padding: "10px",
              borderRadius: "10px",
            }}
          >

            <input
              type="checkbox"
              checked={
                req.completed
              }
              onChange={() =>
                toggleRequirement(
                  req.id
                )
              }
            />

            <div
              style={{
                flex: 1,
                textDecoration:
                  req.completed
                    ? "line-through"
                    : "none",
                opacity:
                  req.completed
                    ? 0.6
                    : 1,
              }}
            >
              {req.text}
            </div>

          </div>
        ))}

      </div>

    </div>
  );
}