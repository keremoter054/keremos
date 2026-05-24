import React, { useState } from "react";

export default function DevelopmentPanel({

  title = "Geliştirmeler",

  developments = [],

  setDevelopments,

}) {

  // =====================================
  // BULK TEXT
  // =====================================

  const [
    bulkText,
    setBulkText,
  ] =
    useState("");

  // =====================================
  // ADD SINGLE
  // =====================================

  function addDevelopment() {

    const text =
      prompt("Geliştirme yaz");

    if (!text) return;

    const newDevelopment = {

      id: Date.now(),

      text,

      completed: false,

      priority:
        developments.length + 1,
    };

    setDevelopments([

      ...developments,

      newDevelopment,
    ]);
  }

  // =====================================
  // BULK IMPORT
  // =====================================

  function importBulkDevelopments() {

    const lines =
      bulkText

        .split("\n")

        .map(
          (line) =>
            line.trim()
        )

        .filter(Boolean);

    if (lines.length === 0)
      return;

    const newItems =
      lines.map(
        (line, index) => ({

          id:
            Date.now() +
            Math.random(),

          text: line,

          completed: false,

          priority:
            developments.length +
            index +
            1,
        })
      );

    setDevelopments([

      ...developments,

      ...newItems,
    ]);

    setBulkText("");
  }

  // =====================================
  // TOGGLE COMPLETE
  // =====================================

  function toggleDevelopment(
    id
  ) {

    const updated =
      developments.map(
        (dev) => {

          if (dev.id === id) {

            return {

              ...dev,

              completed:
                !dev.completed,
            };
          }

          return dev;
        }
      );

    setDevelopments(updated);
  }

  // =====================================
  // DELETE
  // =====================================

  function deleteDevelopment(
    id
  ) {

    const updated =
      developments.filter(
        (dev) =>
          dev.id !== id
      );

    setDevelopments(updated);
  }

  // =====================================
  // MOVE UP
  // =====================================

  function moveUp(index) {

    if (index === 0)
      return;

    const updated =
      [...developments];

    [
      updated[index - 1],
      updated[index],
    ] = [

      updated[index],
      updated[index - 1],
    ];

    setDevelopments(updated);
  }

  // =====================================
  // MOVE DOWN
  // =====================================

  function moveDown(index) {

    if (
      index ===
      developments.length - 1
    )
      return;

    const updated =
      [...developments];

    [
      updated[index + 1],
      updated[index],
    ] = [

      updated[index],
      updated[index + 1],
    ];

    setDevelopments(updated);
  }

  // =====================================
  // PROGRESS
  // =====================================

  const completedCount =
    developments.filter(
      (d) =>
        d.completed
    ).length;

  const progress =
    developments.length === 0

      ? 0

      : Math.round(

          (
            completedCount /
            developments.length
          ) * 100
        );

  // =====================================
  // MAIN UI
  // =====================================

  return (

    <div
      style={{

        background: "#181818",

        border:
          "1px solid #2a2a2a",

        borderRadius: "20px",

        padding: "25px",
      }}
    >

      {/* TOP */}

      <div
        style={{

          display: "flex",

          justifyContent:
            "space-between",

          alignItems: "center",
        }}
      >

        <h2>

          {title}

          {" "}

          (
          {developments.length}
          )

        </h2>

        <button
          onClick={addDevelopment}
          style={{

            padding:
              "10px 15px",

            cursor: "pointer",
          }}
        >
          + Ekle
        </button>

      </div>

      {/* PROGRESS */}

      <div
        style={{
          marginTop: "18px",
        }}
      >

        <div>

          Progress:
          {" "}
          %{progress}

        </div>

        <div
          style={{

            marginTop: "10px",

            height: "12px",

            background: "#333",

            borderRadius:
              "999px",

            overflow: "hidden",
          }}
        >

          <div
            style={{

              width:
                `${progress}%`,

              height: "100%",

              background:
                "lime",
            }}
          />

        </div>

      </div>

      {/* BULK TEXTAREA */}

      <textarea

        value={bulkText}

        onChange={(e) =>
          setBulkText(
            e.target.value
          )
        }

        placeholder={`Backend
AI Worker
Timeline Engine
Simulation Layer
Civilization Engine`}

        style={{

          width: "100%",

          minHeight: "160px",

          marginTop: "22px",

          background: "#111",

          color: "white",

          border:
            "1px solid #333",

          borderRadius: "14px",

          padding: "16px",

          fontSize: "14px",

          boxSizing:
            "border-box",
        }}
      />

      <button

        onClick={
          importBulkDevelopments
        }

        style={{

          marginTop: "14px",

          padding:
            "10px 16px",

          cursor: "pointer",
        }}
      >
        Toplu Ekle
      </button>

      {/* DEVELOPMENT LIST */}

      <div
        style={{
          marginTop: "30px",
        }}
      >

        {

          developments.map(
            (
              dev,
              index
            ) => (

              <div
                key={dev.id}

                style={{

                  background:
                    dev.completed

                      ? "#16351f"

                      : "#222",

                  padding: "16px",

                  borderRadius:
                    "14px",

                  marginBottom:
                    "14px",

                  border:
                    dev.completed

                      ? "1px solid lime"

                      : "1px solid #333",
                }}
              >

                {/* TOP */}

                <div
                  style={{

                    display: "flex",

                    justifyContent:
                      "space-between",

                    alignItems:
                      "center",
                  }}
                >

                  <div
                    style={{

                      display: "flex",

                      alignItems:
                        "center",

                      gap: "12px",
                    }}
                  >

                    <input

                      type="checkbox"

                      checked={
                        dev.completed
                      }

                      onChange={() =>
                        toggleDevelopment(
                          dev.id
                        )
                      }
                    />

                    <div>

                      #{index + 1}

                      {" - "}

                      {dev.text}

                    </div>

                  </div>

                  {/* ACTIONS */}

                  <div
                    style={{

                      display: "flex",

                      gap: "8px",
                    }}
                  >

                    <button
                      onClick={() =>
                        moveUp(index)
                      }
                    >
                      ↑
                    </button>

                    <button
                      onClick={() =>
                        moveDown(index)
                      }
                    >
                      ↓
                    </button>

                    <button
                      onClick={() =>
                        deleteDevelopment(
                          dev.id
                        )
                      }
                    >
                      ✕
                    </button>

                  </div>

                </div>

              </div>
            )
          )
        }

      </div>

    </div>
  );
}