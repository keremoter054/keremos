import React from "react";

export default function RightPanel() {

  return (

    <div>

      <div
        style={{
          background: "#181818",
          border: "1px solid #2a2a2a",
          borderRadius: "16px",
          padding: "20px",
        }}
      >

        <h2>
          AI Queue
        </h2>

        <div
          style={{
            marginTop: "15px",
            opacity: 0.7,
          }}
        >
          No active AI jobs
        </div>

      </div>

      <div
        style={{
          background: "#181818",
          border: "1px solid #2a2a2a",
          borderRadius: "16px",
          padding: "20px",
          marginTop: "20px",
        }}
      >

        <h2>
          Timeline
        </h2>

        <div
          style={{
            marginTop: "15px",
            opacity: 0.7,
          }}
        >
          Timeline system ready
        </div>

      </div>

    </div>
  );
}