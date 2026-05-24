import React from "react";

export default function TopBar() {

  return (

    <div
      style={{
        height: "70px",
        background: "#181818",
        borderBottom: "1px solid #2a2a2a",

        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",

        padding: "0 20px",
      }}
    >

      <div
        style={{
          fontSize: "22px",
          fontWeight: "bold",
        }}
      >
        KeremOS
      </div>

      <div
        style={{
          width: "300px",
        }}
      >

        <div
          style={{
            fontSize: "12px",
            opacity: 0.7,
            marginBottom: "5px",
          }}
        >
          Tip-1 Civilization Progress
        </div>

        <div
          style={{
            height: "10px",
            background: "#333",
            borderRadius: "999px",
            overflow: "hidden",
          }}
        >

          <div
            style={{
              width: "0.0001%",
              height: "100%",
              background: "lime",
            }}
          />

        </div>

      </div>

    </div>
  );
}