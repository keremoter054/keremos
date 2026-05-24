import React, { useState, useEffect } from "react";

export default function DayEnginePanel({

  selectedDay,
  calendarDays,
  setCalendarDays,

}) {

  // =====================================
  // SAFETY
  // =====================================

  if (!selectedDay) {

    return null;
  }

  // =====================================
  // DEFAULT ENGINE
  // =====================================

  const defaultEngine = {

    sleepHours: 8,

    factoryHours: 8,

    tip1Hours: 8,

    aiHours: 2,

    learningHours: 2,

    sportHours: 1,

    tasks: [],

    timeBlocks: [],
  };

  // =====================================
  // FACTORY
  // =====================================

  const factory =
    selectedDay.factoryEngine
    || defaultEngine;

  // =====================================
  // UPDATE ENGINE
  // =====================================

  function updateFactoryField(
    field,
    value
  ) {

    const updatedDays =
      calendarDays.map((day) => {

        if (
          day.day !== selectedDay.day
        ) {

          return day;
        }

        return {

          ...day,

          factoryEngine: {

            ...factory,

            [field]: value,
          },
        };
      });

    setCalendarDays(
      updatedDays
    );
  }

  // =====================================
  // ADD TIME BLOCK
  // =====================================

  function addTimeBlock() {

    const updatedDays =
      calendarDays.map((day) => {

        if (
          day.day !== selectedDay.day
        ) {

          return day;
        }

        return {

          ...day,

          factoryEngine: {

            ...factory,

            timeBlocks: [

              ...factory.timeBlocks,

              {

                id: Date.now(),

                start: "08:00",

                end: "10:00",

                text: "",
              },
            ],
          },
        };
      });

    setCalendarDays(
      updatedDays
    );
  }

  // =====================================
  // UPDATE BLOCK
  // =====================================

  function updateBlock(
    id,
    field,
    value
  ) {

    const updatedDays =
      calendarDays.map((day) => {

        if (
          day.day !== selectedDay.day
        ) {

          return day;
        }

        return {

          ...day,

          factoryEngine: {

            ...factory,

            timeBlocks:
              factory.timeBlocks.map(
                (block) => {

                  if (
                    block.id !== id
                  ) {

                    return block;
                  }

                  return {

                    ...block,

                    [field]: value,
                  };
                }
              ),
          },
        };
      });

    setCalendarDays(
      updatedDays
    );
  }

  // =====================================
  // DELETE BLOCK
  // =====================================

  function deleteBlock(id) {

    const updatedDays =
      calendarDays.map((day) => {

        if (
          day.day !== selectedDay.day
        ) {

          return day;
        }

        return {

          ...day,

          factoryEngine: {

            ...factory,

            timeBlocks:
              factory.timeBlocks.filter(
                (block) =>
                  block.id !== id
              ),
          },
        };
      });

    setCalendarDays(
      updatedDays
    );
  }

  // =====================================
  // TOTAL HOURS
  // =====================================

  const totalHours =

    Number(factory.sleepHours || 0)

    + Number(factory.factoryHours || 0)

    + Number(factory.tip1Hours || 0)

    + Number(factory.aiHours || 0)

    + Number(factory.learningHours || 0)

    + Number(factory.sportHours || 0);

  // =====================================
  // PRODUCTIVITY
  // =====================================

  const productivity =
    Math.min(

      100,

      Math.round(
        (
          Number(
            factory.tip1Hours || 0
          ) * 8
        )
      )
    );

  // =====================================
  // ETA ENGINE
  // =====================================

  const TOTAL_TIP1_HOURS =
    120000;

  const dailyHours =
    Number(
      factory.tip1Hours || 0
    );

  const estimatedDays =

    dailyHours <= 0

      ? "∞"

      : Math.ceil(

          TOTAL_TIP1_HOURS
          / dailyHours
        );

  // =====================================
  // PANEL STYLE
  // =====================================

  const panelStyle = {

    background: "#181818",

    border: "1px solid #2a2a2a",

    borderRadius: "16px",

    padding: "20px",

    marginTop: "20px",
  };

  return (

    <div style={panelStyle}>

      {/* HEADER */}

      <h2>

        Gün {selectedDay.day}
        {" "}
        Civilization Engine

      </h2>

      {/* DAILY HOURS */}

      <div
        style={{
          marginTop: "20px",
        }}
      >

        <h3>
          Günlük Rutin
        </h3>

        <div
          style={{
            display: "grid",
            gridTemplateColumns:
              "1fr 1fr",
            gap: "10px",
            marginTop: "15px",
          }}
        >

          {/* SLEEP */}

          <input
            type="number"
            placeholder="Uyku Saati"
            value={
              factory.sleepHours
            }
            onChange={(e) =>
              updateFactoryField(
                "sleepHours",
                e.target.value
              )
            }
          />

          {/* FACTORY */}

          <input
            type="number"
            placeholder="Fabrika"
            value={
              factory.factoryHours
            }
            onChange={(e) =>
              updateFactoryField(
                "factoryHours",
                e.target.value
              )
            }
          />

          {/* TIP1 */}

          <input
            type="number"
            placeholder="Tip-1"
            value={
              factory.tip1Hours
            }
            onChange={(e) =>
              updateFactoryField(
                "tip1Hours",
                e.target.value
              )
            }
          />

          {/* AI */}

          <input
            type="number"
            placeholder="AI"
            value={
              factory.aiHours
            }
            onChange={(e) =>
              updateFactoryField(
                "aiHours",
                e.target.value
              )
            }
          />

          {/* LEARNING */}

          <input
            type="number"
            placeholder="Öğrenme"
            value={
              factory.learningHours
            }
            onChange={(e) =>
              updateFactoryField(
                "learningHours",
                e.target.value
              )
            }
          />

          {/* SPORT */}

          <input
            type="number"
            placeholder="Spor"
            value={
              factory.sportHours
            }
            onChange={(e) =>
              updateFactoryField(
                "sportHours",
                e.target.value
              )
            }
          />

        </div>

      </div>

      {/* TOTAL HOURS */}

      <div
        style={{
          marginTop: "20px",
          opacity: 0.8,
        }}
      >

        Toplam Saat:
        {" "}
        {totalHours}
        / 24

      </div>

      {/* PRODUCTIVITY */}

      <div
        style={{
          marginTop: "20px",
        }}
      >

        <div>
          Civilization Productivity
        </div>

        <div
          style={{
            marginTop: "10px",
            height: "10px",
            background: "#333",
            borderRadius: "999px",
            overflow: "hidden",
          }}
        >

          <div
            style={{
              width:
                `${productivity}%`,
              height: "100%",
              background: "lime",
            }}
          />

        </div>

        <div
          style={{
            marginTop: "8px",
            fontSize: "14px",
          }}
        >

          %{productivity}

        </div>

      </div>

      {/* ETA */}

      <div
        style={{
          marginTop: "25px",
        }}
      >

        <h3>
          Tip-1 ETA
        </h3>

        <div
          style={{
            marginTop: "10px",
            opacity: 0.8,
          }}
        >

          Günlük
          {" "}
          {dailyHours}
          {" "}
          saat çalışma ile:

        </div>

        <div
          style={{
            marginTop: "10px",
            fontSize: "24px",
            color: "lime",
          }}
        >

          {estimatedDays}
          {" "}
          gün

        </div>

      </div>

      {/* TIME BLOCKS */}

      <div
        style={{
          marginTop: "30px",
        }}
      >

        <h3>
          Saatlik Plan
        </h3>

        <button
          onClick={addTimeBlock}
          style={{
            marginTop: "10px",
          }}
        >

          + Saat Bloğu Ekle

        </button>

        <div
          style={{
            marginTop: "20px",
          }}
        >

          {factory.timeBlocks.map(
            (block) => (

              <div
                key={block.id}
                style={{
                  background: "#202020",
                  border:
                    "1px solid #2a2a2a",
                  padding: "15px",
                  borderRadius: "12px",
                  marginBottom: "10px",
                }}
              >

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

                <textarea
                  placeholder="Yapılacak..."
                  value={block.text}
                  onChange={(e) =>
                    updateBlock(
                      block.id,
                      "text",
                      e.target.value
                    )
                  }
                  style={{
                    width: "100%",
                    marginTop: "10px",
                    minHeight: "70px",
                  }}
                />

                <button
                  onClick={() =>
                    deleteBlock(
                      block.id
                    )
                  }
                  style={{
                    marginTop: "10px",
                    background: "#500",
                    color: "white",
                  }}
                >

                  Sil

                </button>

              </div>
            )
          )}

        </div>

      </div>

    </div>
  );
}