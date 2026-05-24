import React from "react";

export default function AnalyticsSection({

  goals,
  selectedDay,
  calculateDayProgress,

}) {

  const cardStyle = {
    background: "#181818",
    padding: "18px",
    borderRadius: "16px",
    border: "1px solid #2a2a2a",
  };

  return (

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
  );
}