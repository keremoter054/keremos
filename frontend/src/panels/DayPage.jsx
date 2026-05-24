import { useState } from "react";
import HourBlock from "./HourBlock.jsx";
import HourTaskModal from "./HourTaskModal.jsx";

export default function DayPage({
  openedDay,
  setOpenedDay,
  calendarDays,
  setCalendarDays,
  calculateDayProgress,
}) {

  const [
    selectedBlock,
    setSelectedBlock,
  ] =
    useState(null);

  const [
    copyDaysText,
    setCopyDaysText,
  ] =
    useState("");

  // =====================================
  // CURRENT DAY
  // =====================================

  const dayData =
    calendarDays.find(
      (day) =>
        day.day ===
        openedDay.day
    );

  if (!dayData) {

    return null;
  }

  const hourBlocks =
    dayData.hourBlocks || [];

  // =====================================
  // UPDATE DAY
  // =====================================

  function updateDay(
    newDayData
  ) {

    setCalendarDays(

      calendarDays.map(
        (day) =>

          day.day ===
          newDayData.day

            ? newDayData

            : day
      )
    );
  }

  // =====================================
  // ADD BLOCK
  // =====================================

  function addHourBlock() {

    const newBlock = {

      id: Date.now(),

      start: "08:00",

      end: "09:00",

      title:
        "Yeni Başlık",

      tasks: [],

      developments: [],
    };

    updateDay({

      ...dayData,

      hourBlocks: [

        ...hourBlocks,

        newBlock,
      ],
    });
  }

  // =====================================
  // UPDATE BLOCK
  // =====================================

  function updateHourBlock(
    blockId,
    field,
    value
  ) {

    updateDay({

      ...dayData,

      hourBlocks:
        hourBlocks.map(
          (block) =>

            block.id ===
            blockId

              ? {

                  ...block,

                  [field]:
                    value,
                }

              : block
        ),
    });
  }

  // =====================================
  // DELETE BLOCK
  // =====================================

  function deleteHourBlock(
    blockId
  ) {

    updateDay({

      ...dayData,

      hourBlocks:
        hourBlocks.filter(
          (block) =>
            block.id !==
            blockId
        ),
    });

    if (
      selectedBlock &&
      selectedBlock.id ===
        blockId
    ) {

      setSelectedBlock(
        null
      );
    }
  }

  // =====================================
  // UPDATE TASKS
  // =====================================

  function updateBlockTasks(
    blockId,
    newTasks
  ) {

    updateDay({

      ...dayData,

      hourBlocks:
        hourBlocks.map(
          (block) =>

            block.id ===
            blockId

              ? {

                  ...block,

                  tasks:
                    newTasks,
                }

              : block
        ),
    });
  }

  // =====================================
  // COPY BLOCKS
  // =====================================

  function copyHourBlocksToDays() {

    if (
      !copyDaysText.trim()
    ) {

      return;
    }

    const targetDays =
      copyDaysText

        .split(",")

        .map((item) =>
          parseInt(
            item.trim()
          )
        )

        .filter(
          (num) =>

            !isNaN(num) &&

            num >= 1 &&

            num <= 365
        );

    if (
      targetDays.length === 0
    ) {

      return;
    }

    const copiedBlocks =
      hourBlocks.map(
        (block) => ({

          ...block,

          id:
            Date.now() +
            Math.random(),

          tasks:
            (
              block.tasks ||
              []
            ).map(
              (task) => ({

                ...task,

                id:
                  Date.now() +
                  Math.random(),
              })
            ),

          developments:
            (
              block.developments ||
              []
            ).map(
              (dev) => ({

                ...dev,

                id:
                  Date.now() +
                  Math.random(),
              })
            ),
        })
      );

    setCalendarDays(

      calendarDays.map(
        (day) => {

          if (
            targetDays.includes(
              day.day
            )
          ) {

            return {

              ...day,

              hourBlocks:
                copiedBlocks,
            };
          }

          return day;
        }
      )
    );

    setCopyDaysText("");
  }

  // =====================================
  // BLOCK PROGRESS
  // =====================================

  function getBlockProgress(
    block
  ) {

    const tasks =
      block.tasks || [];

    const developments =
      block.developments ||
      [];

    const allItems = [

      ...tasks,

      ...developments,
    ];

    if (
      allItems.length === 0
    ) {

      return 0;
    }

    const completed =
      allItems.filter(
        (item) =>
          item.completed
      ).length;

    return Math.round(

      (
        completed /
        allItems.length
      ) * 100
    );
  }

  // =====================================
  // MAIN
  // =====================================

  return (

    <div
      style={{

        position: "fixed",

        inset: 0,

        background:
          "#0f0f0f",

        color: "white",

        zIndex: 9999,

        overflow: "hidden",

        display: "flex",

        flexDirection:
          "column",
      }}
    >

      {/* TOP */}

      <div
        style={{

          height: "70px",

          borderBottom:
            "1px solid #222",

          display: "flex",

          alignItems: "center",

          justifyContent:
            "space-between",

          padding: "0 24px",

          background:
            "#151515",
        }}
      >

        <div>

          <h2
            style={{
              margin: 0,
            }}
          >

            Day {dayData.day}
            Workspace

          </h2>

        </div>

        <button

          onClick={() =>
            setOpenedDay(
              null
            )
          }

          style={{

            background:
              "#333",

            color: "white",

            border:
              "1px solid #555",

            padding:
              "10px 14px",

            borderRadius:
              "10px",

            cursor:
              "pointer",
          }}
        >

          Takvime Dön

        </button>

      </div>

      {/* PROGRESS */}

      <div
        style={{

          padding:
            "18px 24px",

          borderBottom:
            "1px solid #222",

          background:
            "#111",
        }}
      >

        <div
          style={{

            display: "flex",

            justifyContent:
              "space-between",

            marginBottom:
              "8px",
          }}
        >

          <strong>

            Gün Genel
            Progress

          </strong>

          <span>

            {
              calculateDayProgress(
                dayData
              )
            }%

          </span>

        </div>

        <div
          style={{

            height: "10px",

            background:
              "#222",

            borderRadius:
              "999px",

            overflow:
              "hidden",
          }}
        >

          <div
            style={{

              width:
                `${calculateDayProgress(
                  dayData
                )}%`,

              height: "100%",

              background:
                "#22c55e",
            }}
          />

        </div>

      </div>

      {/* GRID */}

      <div
        style={{

          flex: 1,

          display: "grid",

          gridTemplateColumns:
            "280px 1fr 340px",

          overflow:
            "hidden",
        }}
      >

        {/* LEFT */}

        <div
          style={{

            borderRight:
              "1px solid #222",

            padding: "20px",

            overflowY:
              "auto",
          }}
        >

          <button

            onClick={
              addHourBlock
            }

            style={{

              width: "100%",

              background:
                "#22c55e",

              color: "black",

              border: "none",

              padding: "12px",

              borderRadius:
                "12px",

              fontWeight:
                "bold",

              cursor:
                "pointer",

              marginBottom:
                "16px",
            }}
          >

            + Başlık Ekle

          </button>

          <h3>
            Timeline
          </h3>

          {
            Array.from(
              { length: 24 },
              (_, i) => {

                const hour =
                  String(
                    i
                  ).padStart(
                    2,
                    "0"
                  ) + ":00";

                const blocksAtHour =
                  hourBlocks.filter(
                    (block) =>

                      block.start.startsWith(
                        String(
                          i
                        ).padStart(
                          2,
                          "0"
                        )
                      )
                  );

                return (

                  <div
                    key={hour}

                    style={{

                      minHeight:
                        "54px",

                      borderBottom:
                        "1px solid #222",

                      padding:
                        "8px 0",
                    }}
                  >

                    <div
                      style={{

                        color:
                          "#777",

                        fontSize:
                          "12px",

                        marginBottom:
                          "6px",
                      }}
                    >

                      {hour}

                    </div>

                    {
                      blocksAtHour.map(
                        (block) => (

                          <HourBlock

                            key={
                              block.id
                            }

                            block={
                              block
                            }

                            onClick={() =>
                              setSelectedBlock(
                                block
                              )
                            }

                          />
                        )
                      )
                    }

                  </div>
                );
              }
            )
          }

        </div>

        {/* CENTER */}

        <div
          style={{

            padding: "24px",

            overflowY:
              "auto",
          }}
        >

          <h2>
            Başlıklar
          </h2>

          {/* COPY */}

          <div
            style={{

              background:
                "#181818",

              border:
                "1px solid #252525",

              borderRadius:
                "16px",

              padding: "16px",

              marginBottom:
                "18px",
            }}
          >

            <div
              style={{

                fontWeight:
                  "bold",

                marginBottom:
                  "8px",
              }}
            >

              Günlere Kopyala

            </div>

            <div
              style={{

                display: "flex",

                gap: "10px",
              }}
            >

              <input

                value={
                  copyDaysText
                }

                onChange={(e) =>
                  setCopyDaysText(
                    e.target.value
                  )
                }

                placeholder="
2,3,4
"

                style={{

                  flex: 1,

                  background:
                    "#0f0f0f",

                  color:
                    "white",

                  border:
                    "1px solid #333",

                  borderRadius:
                    "10px",

                  padding:
                    "12px",
                }}
              />

              <button

                onClick={
                  copyHourBlocksToDays
                }

                style={{

                  background:
                    "#2563eb",

                  color:
                    "white",

                  border:
                    "none",

                  borderRadius:
                    "10px",

                  padding:
                    "12px 16px",

                  cursor:
                    "pointer",

                  fontWeight:
                    "bold",
                }}
              >

                Kopyala

              </button>

            </div>

          </div>

          {/* BLOCKS */}

          {
            hourBlocks.map(
              (block) => (

                <div
                  key={block.id}

                  style={{

                    background:
                      "#181818",

                    border:
                      "1px solid #252525",

                    borderRadius:
                      "16px",

                    padding:
                      "16px",

                    marginBottom:
                      "16px",
                  }}
                >

                  {/* TOP */}

                  <div
                    style={{

                      display:
                        "grid",

                      gridTemplateColumns:
                        "90px 90px 1fr auto auto",

                      gap: "10px",

                      alignItems:
                        "center",
                    }}
                  >

                    <input

                      value={
                        block.start
                      }

                      onChange={(e) =>
                        updateHourBlock(

                          block.id,

                          "start",

                          e.target
                            .value
                        )
                      }

                      style={
                        inputStyle
                      }

                    />

                    <input

                      value={
                        block.end
                      }

                      onChange={(e) =>
                        updateHourBlock(

                          block.id,

                          "end",

                          e.target
                            .value
                        )
                      }

                      style={
                        inputStyle
                      }

                    />

                    <input

                      value={
                        block.title
                      }

                      onChange={(e) =>
                        updateHourBlock(

                          block.id,

                          "title",

                          e.target
                            .value
                        )
                      }

                      style={
                        inputStyle
                      }

                    />

                    {/* DETAIL */}

                    <button

                      onClick={() =>
                        setSelectedBlock(
                          block
                        )
                      }

                      style={
                        buttonStyle
                      }

                    >

                      Detay

                    </button>

                    {/* DELETE */}

                    <button

                      onClick={() =>
                        deleteHourBlock(
                          block.id
                        )
                      }

                      style={{

                        background:
                          "#7f1d1d",

                        color:
                          "white",

                        border:
                          "none",

                        borderRadius:
                          "10px",

                        padding:
                          "10px 12px",

                        cursor:
                          "pointer",

                        fontWeight:
                          "bold",
                      }}
                    >

                      Sil

                    </button>

                  </div>

                  {/* FOOTER */}

                  <div
                    style={{

                      marginTop:
                        "12px",

                      fontSize:
                        "13px",

                      color:
                        "#aaa",
                    }}
                  >

                    Görev:
                    {" "}

                    {
                      (
                        block.tasks ||
                        []
                      ).length
                    }

                    {" | "}

                    Geliştirme:
                    {" "}

                    {
                      (
                        block.developments ||
                        []
                      ).length
                    }

                    {" | "}

                    Progress:
                    {" "}

                    {
                      getBlockProgress(
                        block
                      )
                    }%

                  </div>

                </div>
              )
            )
          }

        </div>

        {/* RIGHT */}

        <div
          style={{

            borderLeft:
              "1px solid #222",

            padding: "20px",

            overflowY:
              "auto",

            background:
              "#111",
          }}
        >

          <h3>
            Gün Özeti
          </h3>

          <p
            style={{
              color: "#aaa",
            }}
          >

            Başlık:
            {" "}

            {
              hourBlocks.length
            }

          </p>

          <p
            style={{
              color: "#aaa",
            }}
          >

            Görev:
            {" "}

            {
              hourBlocks.reduce(

                (
                  sum,
                  block
                ) =>

                  sum +

                  (
                    block.tasks ||
                    []
                  ).length,

                0
              )
            }

          </p>

          <p
            style={{
              color: "#aaa",
            }}
          >

            Geliştirme:
            {" "}

            {
              hourBlocks.reduce(

                (
                  sum,
                  block
                ) =>

                  sum +

                  (
                    block.developments ||
                    []
                  ).length,

                0
              )
            }

          </p>

        </div>

      </div>

      {/* MODAL */}

      {
        selectedBlock && (

          <HourTaskModal

            block={
              selectedBlock
            }

            setSelectedBlock={
              setSelectedBlock
            }

            updateBlockTasks={
              updateBlockTasks
            }

            deleteHourBlock={
              deleteHourBlock
            }

          />
        )
      }

    </div>
  );
}

const inputStyle = {

  background:
    "#0f0f0f",

  color: "white",

  border:
    "1px solid #333",

  borderRadius:
    "10px",

  padding: "10px",
};

const buttonStyle = {

  background:
    "#2563eb",

  color: "white",

  border: "none",

  borderRadius:
    "10px",

  padding:
    "10px 12px",

  cursor:
    "pointer",
};