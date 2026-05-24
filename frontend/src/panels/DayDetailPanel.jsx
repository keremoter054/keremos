import React from "react";

export default function DayDetailPanel({

  openedDay,
  setOpenedDay,

  calendarDays,
  setCalendarDays,

}) {

  // =====================================
  // SAFETY
  // =====================================

  if (!openedDay) {

    return null;
  }

  // =====================================
  // CURRENT DAY
  // =====================================

  const currentDay =
    calendarDays.find(
      (d) =>
        d.day === openedDay.day
    );

  // =====================================
  // TIME BLOCKS
  // =====================================

  const timeBlocks =
    currentDay?.timeBlocks || [];

  // =====================================
  // ADD BLOCK
  // =====================================

  function addTimeBlock() {

    const updated =
      calendarDays.map((day) => {

        if (
          day.day !== currentDay.day
        ) {

          return day;
        }

        return {

          ...day,

          timeBlocks: [

            ...(day.timeBlocks || []),

            {

              id: Date.now(),

              title: "",

              start: "08:00",

              end: "10:00",

              expanded: false,

              tasksText: "",

              completedTasks: [],
            },
          ],
        };
      });

    setCalendarDays(updated);
  }

  // =====================================
  // UPDATE BLOCK
  // =====================================

  function updateBlock(
    blockId,
    field,
    value
  ) {

    const updated =
      calendarDays.map((day) => {

        if (
          day.day !== currentDay.day
        ) {

          return day;
        }

        return {

          ...day,

          timeBlocks:
            day.timeBlocks.map(
              (block) => {

                if (
                  block.id !== blockId
                ) {

                  return block;
                }

                return {

                  ...block,

                  [field]: value,
                };
              }
            ),
        };
      });

    setCalendarDays(updated);
  }

  // =====================================
  // DELETE BLOCK
  // =====================================

  function deleteBlock(
    blockId
  ) {

    const updated =
      calendarDays.map((day) => {

        if (
          day.day !== currentDay.day
        ) {

          return day;
        }

        return {

          ...day,

          timeBlocks:
            day.timeBlocks.filter(
              (block) =>
                block.id !== blockId
            ),
        };
      });

    setCalendarDays(updated);
  }

  // =====================================
  // TOGGLE BLOCK
  // =====================================

  function toggleBlock(
    blockId
  ) {

    const updated =
      calendarDays.map((day) => {

        if (
          day.day !== currentDay.day
        ) {

          return day;
        }

        return {

          ...day,

          timeBlocks:
            day.timeBlocks.map(
              (block) => {

                if (
                  block.id !== blockId
                ) {

                  return block;
                }

                return {

                  ...block,

                  expanded:
                    !block.expanded,
                };
              }
            ),
        };
      });

    setCalendarDays(updated);
  }

  // =====================================
  // PANEL STYLE
  // =====================================

  const panelStyle = {

    position: "fixed",

    top: 0,

    right: 0,

    width: "700px",

    height: "100vh",

    background: "#111",

    borderLeft:
      "1px solid #333",

    zIndex: 9999,

    overflowY: "auto",

    padding: "25px",
  };

  return (

    <div style={panelStyle}>

      {/* HEADER */}

      <div
        style={{
          display: "flex",
          justifyContent:
            "space-between",
          alignItems: "center",
        }}
      >

        <div>

          <h1>
            Gün {currentDay.day}
          </h1>

          <div
            style={{
              opacity: 0.7,
            }}
          >

            Civilization Day Engine

          </div>

        </div>

        <button
          onClick={() =>
            setOpenedDay(null)
          }
        >

          Kapat

        </button>

      </div>

      {/* ADD BLOCK */}

      <div
        style={{
          marginTop: "30px",
        }}
      >

        <button
          onClick={addTimeBlock}
        >

          + Saat Bloğu Ekle

        </button>

      </div>

      {/* BLOCKS */}

      <div
        style={{
          marginTop: "25px",
        }}
      >

        {timeBlocks.map((block) => (

          <div
            key={block.id}
            style={{

              background: "#1a1a1a",

              border:
                "1px solid #2a2a2a",

              borderRadius: "16px",

              padding: "16px",

              marginBottom: "16px",
            }}
          >

            {/* TITLE */}

            <input

              placeholder="
Fabrika
KeremOS
AI
Yazılım
"

              value={block.title}

              onChange={(e) =>
                updateBlock(

                  block.id,

                  "title",

                  e.target.value
                )
              }

              style={{

                width: "100%",

                marginBottom: "12px",

                background: "#111",

                color: "white",

                border:
                  "1px solid #333",

                borderRadius: "10px",

                padding: "10px",
              }}
            />

            {/* TIMES */}

            <div
              style={{
                display: "flex",
                gap: "10px",
              }}
            >

              <input

                type="time"

                value={block.start}

                onChange={(e) =>
                  updateBlock(

                    block.id,

                    "start",

                    e.target.value
                  )
                }
              />

              <input

                type="time"

                value={block.end}

                onChange={(e) =>
                  updateBlock(

                    block.id,

                    "end",

                    e.target.value
                  )
                }
              />

            </div>

            {/* TOGGLE */}

            <button

              onClick={() =>
                toggleBlock(
                  block.id
                )
              }

              style={{
                marginTop: "12px",
              }}
            >

              {
                block.expanded
                  ? "Görevleri Kapat"
                  : "Görevleri Aç"
              }

            </button>

            {/* TASKS */}

            {
              block.expanded && (

                <div
                  style={{
                    marginTop: "15px",
                  }}
                >

                  <textarea

                    placeholder="
Her satır bir görev

Örn:

Filtre kontrolü
Vakum kontrolü
Backend sistemi
AI worker
"

                    value={
                      block.tasksText
                    }

                    onChange={(e) =>
                      updateBlock(

                        block.id,

                        "tasksText",

                        e.target.value
                      )
                    }

                    style={{

                      width: "100%",

                      minHeight: "220px",

                      background: "#0f0f0f",

                      color: "white",

                      border:
                        "1px solid #333",

                      borderRadius: "12px",

                      padding: "14px",
                    }}
                  />

                </div>
              )
            }

            {/* DELETE */}

            <button

              onClick={() =>
                deleteBlock(
                  block.id
                )
              }

              style={{

                marginTop: "15px",

                background: "#500",

                color: "white",
              }}
            >

              Bloğu Sil

            </button>

          </div>
        ))}

      </div>

    </div>
  );
}