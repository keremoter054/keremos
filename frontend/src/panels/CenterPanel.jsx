import { useState } from "react";

import HourTaskModal from "./HourTaskModal.jsx";

import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  arrayMove,
  SortableContext,
  verticalListSortingStrategy,
  useSortable,
} from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

export default function CenterPanel({

  calendarDays,

  selectedDayId,
  setSelectedDayId,

  calculateDayProgress,
  getDateForDay,

  setCalendarDays,

}) {

  // =====================================
  // STATES
  // =====================================

  const [
    selectedBlock,
    setSelectedBlock,
  ] =
    useState(null);

  const [
    expandedDayId,
    setExpandedDayId,
  ] =
    useState(null);

  // =====================================
  // TOGGLE DAY
  // =====================================

  function toggleDay(
    dayId
  ) {

    setExpandedDayId(

      expandedDayId === dayId

        ? null

        : dayId
    );
  }

  // =====================================
  // ADD BLOCK
  // =====================================

  function addQuickHourBlock(
    e,
    dayId
  ) {

    e.stopPropagation();

    const updated =
      calendarDays.map(
        (day) => {

          if (
            day.day !== dayId
          ) {

            return day;
          }

          return {

            ...day,

            hourBlocks: [

              ...(day.hourBlocks || []),

              {

                id:
                  Date.now(),

                start:
                  "08:00",

                end:
                  "09:00",

                title:
                  "Yeni Başlık",

                tasks: [],

                developments:
                  [],
              },
            ],
          };
        }
      );

    setCalendarDays(
      updated
    );
  }

  // =====================================
  // UPDATE BLOCK
  // =====================================

  function updateHourBlock(
    blockId,
    field,
    value
  ) {

    const updated =
      calendarDays.map(
        (day) => ({

          ...day,

          hourBlocks:
            (
              day.hourBlocks ||
              []
            ).map(
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
        })
      );

    setCalendarDays(
      updated
    );
  }

  // =====================================
  // DELETE BLOCK
  // =====================================

  function deleteHourBlock(
    blockId
  ) {

    const updated =
      calendarDays.map(
        (day) => ({

          ...day,

          hourBlocks:
            (
              day.hourBlocks ||
              []
            ).filter(
              (block) =>
                block.id !==
                blockId
            ),
        })
      );

    setCalendarDays(
      updated
    );

    setSelectedBlock(
      null
    );
  }

  // =====================================
  // DRAG END
  // =====================================

  function handleDragEnd(
    event,
    day
  ) {

    const {
      active,
      over,
    } = event;

    if (
      !over ||
      active.id === over.id
    ) {

      return;
    }

    const oldIndex =
      day.hourBlocks.findIndex(
        (b) =>
          b.id === active.id
      );

    const newIndex =
      day.hourBlocks.findIndex(
        (b) =>
          b.id === over.id
      );

    const reordered =
      arrayMove(

        day.hourBlocks,

        oldIndex,

        newIndex
      );

    const updated =
      calendarDays.map(
        (d) =>

          d.day === day.day

            ? {

                ...d,

                hourBlocks:
                  reordered,
              }

            : d
      );

    setCalendarDays(
      updated
    );
  }

  // =====================================
  // BLOCK PROGRESS
  // =====================================

  function getBlockProgress(
    block
  ) {

    const allItems = [

      ...(block.tasks || []),

      ...(block.developments || []),
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

    <div>

      {/* HEADER */}

      <div
        style={{

          background:
            "#141414",

          border:
            "1px solid #222",

          borderRadius:
            "18px",

          padding:
            "22px",

          marginBottom:
            "18px",

          textAlign:
            "center",
        }}
      >

        <h2
          style={{
            margin: 0,
          }}
        >

          365 Day Timeline

        </h2>

      </div>

      {/* DAYS */}

      <div
        style={{

          display: "flex",

          flexDirection:
            "column",

          gap: "16px",

          overflowY:
            "auto",

          maxHeight:
            "78vh",

          paddingRight:
            "6px",
        }}
      >

        {
          calendarDays.map(
            (day) => {

              const progress =
                calculateDayProgress(
                  day
                );

              const isExpanded =
                expandedDayId ===
                day.day;

              return (

                <div
                  key={day.day}

                  style={{

                    background:
                      "#111",

                    border:
                      isExpanded

                        ? "1px solid #22c55e"

                        : "1px solid #222",

                    borderRadius:
                      "18px",

                    padding:
                      "18px",
                  }}
                >

                  {/* TOP */}

                  <div
                    onClick={() => {

                      setSelectedDayId(
                        day.day
                      );

                      toggleDay(
                        day.day
                      );
                    }}

                    style={{

                      display:
                        "flex",

                      justifyContent:
                        "space-between",

                      alignItems:
                        "center",

                      marginBottom:
                        "14px",

                      cursor:
                        "pointer",
                    }}
                  >

                    <div>

                      <div
                        style={{

                          fontSize:
                            "28px",

                          fontWeight:
                            "bold",
                        }}
                      >

                        Gün {day.day}

                      </div>

                      <div
                        style={{

                          marginTop:
                            "4px",

                          fontSize:
                            "13px",

                          opacity:
                            0.55,
                        }}
                      >

                        {
                          getDateForDay(
                            day.day
                          ).toLocaleDateString(
                            "tr-TR"
                          )
                        }

                      </div>

                    </div>

                    {/* PLUS */}

                    <button

                      onClick={(e) => {

                        e.stopPropagation();

                        setSelectedDayId(
                          day.day
                        );

                        if (
                          expandedDayId ===
                          day.day
                        ) {

                          setExpandedDayId(
                            null
                          );

                          return;
                        }

                        setExpandedDayId(
                          day.day
                        );

                        const currentDay =
                          calendarDays.find(
                            (d) =>
                              d.day ===
                              day.day
                          );

                        if (
                          !currentDay
                            ?.hourBlocks
                            ?.length
                        ) {

                          addQuickHourBlock(
                            e,
                            day.day
                          );
                        }
                      }}

                      style={{

                        width:
                          "38px",

                        height:
                          "38px",

                        borderRadius:
                          "12px",

                        border:
                          "none",

                        background:
                          "#22c55e",

                        color:
                          "black",

                        fontWeight:
                          "bold",

                        cursor:
                          "pointer",

                        fontSize:
                          "20px",
                      }}
                    >

                      {isExpanded
                        ? "−"
                        : "+"}

                    </button>

                  </div>

                  {/* PROGRESS */}

                  <div
                    style={{

                      height:
                        "8px",

                      background:
                        "#222",

                      borderRadius:
                        "999px",

                      overflow:
                        "hidden",

                      marginBottom:
                        "18px",
                    }}
                  >

                    <div
                      style={{

                        width:
                          `${progress}%`,

                        height:
                          "100%",

                        background:
                          "#22c55e",
                      }}
                    />

                  </div>

                  {/* COLLAPSED */}

                  {
                    !isExpanded && (

                      <div>

                        {
                          (
                            day.hourBlocks ||
                            []
                          ).map(
                            (
                              block
                            ) => (

                              <div
                                key={
                                  block.id
                                }

                                style={{

                                  display:
                                    "flex",

                                  alignItems:
                                    "center",

                                  justifyContent:
                                    "space-between",

                                  padding:
                                    "12px 14px",

                                  background:
                                    "#181818",

                                  border:
                                    "1px solid #262626",

                                  borderRadius:
                                    "14px",

                                  marginBottom:
                                    "10px",
                                }}
                              >

                                <div
                                  style={{

                                    width:
                                      "120px",

                                    fontSize:
                                      "12px",

                                    opacity:
                                      0.7,
                                  }}
                                >

                                  {
                                    block.start
                                  }

                                  {" - "}

                                  {
                                    block.end
                                  }

                                </div>

                                <div
                                  style={{

                                    flex: 1,

                                    fontWeight:
                                      "bold",
                                  }}
                                >

                                  {
                                    block.title
                                  }

                                </div>

                              </div>
                            )
                          )
                        }

                      </div>
                    )
                  }

                  {/* EXPANDED */}

                  {
                    isExpanded && (

                      <DndContext

                        collisionDetection={
                          closestCenter
                        }

                        onDragEnd={(event) =>
                          handleDragEnd(
                            event,
                            day
                          )
                        }

                      >

                        <SortableContext

                          items={
                            (
                              day.hourBlocks ||
                              []
                            ).map(
                              (b) =>
                                b.id
                            )
                          }

                          strategy={
                            verticalListSortingStrategy
                          }

                        >

                          <div>

                            {
                              (
                                day.hourBlocks ||
                                []
                              ).map(
                                (
                                  block
                                ) => {

                                  const blockProgress =
                                    getBlockProgress(
                                      block
                                    );

                                  return (

                                    <SortableBlock

                                      key={
                                        block.id
                                      }

                                      block={
                                        block
                                      }

                                      updateHourBlock={
                                        updateHourBlock
                                      }

                                      deleteHourBlock={
                                        deleteHourBlock
                                      }

                                      setSelectedBlock={
                                        setSelectedBlock
                                      }

                                      blockProgress={
                                        blockProgress
                                      }

                                    />
                                  );
                                }
                              )
                            }

                          </div>

                        </SortableContext>

                      </DndContext>
                    )
                  }

                </div>
              );
            }
          )
        }

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

            calendarDays={
              calendarDays
            }

            setCalendarDays={
              setCalendarDays
            }

          />
        )
      }

    </div>
  );
}

// =====================================
// SORTABLE BLOCK
// =====================================

function SortableBlock({

  block,

  updateHourBlock,

  deleteHourBlock,

  setSelectedBlock,

  blockProgress,

}) {

  const {

    attributes,

    listeners,

    setNodeRef,

    transform,

    transition,

  } = useSortable({

    id: block.id,
  });

  const style = {

    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  return (

    <div

      ref={setNodeRef}

      style={{

        ...style,

        background:
          "#181818",

        border:
          "1px solid #262626",

        borderRadius:
          "14px",

        padding:
          "14px",

        marginBottom:
          "12px",
      }}
    >

      <div
        style={{

          display: "grid",

          gridTemplateColumns:
            "40px 110px 110px 1fr auto auto",

          gap: "10px",

          alignItems:
            "center",
        }}
      >

        {/* DRAG */}

        <div

          {...attributes}

          {...listeners}

          style={{

            cursor: "grab",

            opacity: 0.5,

            textAlign:
              "center",

            userSelect:
              "none",
          }}
        >

          ☰

        </div>

        {/* START */}

        <input

          value={block.start}

          onChange={(e) =>
            updateHourBlock(

              block.id,

              "start",

              e.target.value
            )
          }

          style={inputStyle}

        />

        {/* END */}

        <input

          value={block.end}

          onChange={(e) =>
            updateHourBlock(

              block.id,

              "end",

              e.target.value
            )
          }

          style={inputStyle}

        />

        {/* TITLE */}

        <input

          value={block.title}

          onChange={(e) =>
            updateHourBlock(

              block.id,

              "title",

              e.target.value
            )
          }

          style={inputStyle}

        />

        {/* DETAIL */}

        <button

          onClick={() =>
            setSelectedBlock(
              block
            )
          }

          style={blueButton}

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

          style={redButton}

        >

          Sil

        </button>

      </div>

      {/* FOOTER */}

      <div
        style={{

          marginTop:
            "14px",

          display: "flex",

          justifyContent:
            "space-between",

          alignItems:
            "center",

          fontSize:
            "12px",

          opacity:
            0.65,
        }}
      >

        <div>

          {
            (
              block.developments ||
              []
            ).length
          }

          {" "}
          geliştirme

        </div>

        <div>

          %{blockProgress}

        </div>

      </div>

    </div>
  );
}

const inputStyle = {

  background:
    "#101010",

  color: "white",

  border:
    "1px solid #333",

  borderRadius:
    "10px",

  padding:
    "10px",

  outline:
    "none",
};

const blueButton = {

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

  fontWeight:
    "bold",
};

const redButton = {

  background:
    "#7f1d1d",

  color: "white",

  border: "none",

  borderRadius:
    "10px",

  padding:
    "10px 12px",

  cursor:
    "pointer",

  fontWeight:
    "bold",
};