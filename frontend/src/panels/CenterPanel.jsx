import { useState, useEffect } from "react";

import HourTaskModal from "./HourTaskModal.jsx";

import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  SortableContext,
  useSortable,
  verticalListSortingStrategy,
  arrayMove,
} from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

// =====================================
// MAIN
// =====================================

export default function CenterPanel({

  calendarDays,

  setCalendarDays,

  selectedDayId,

  setSelectedDayId,

  calculateDayProgress,

  getDateForDay,

  playlists = [],
}) {

  // =====================================
  // MODAL
  // =====================================

  const [
    selectedBlock,
    setSelectedBlock,
  ] =
    useState(null);

  // =====================================
  // EXPANDED DAY
  // =====================================

  const [
    expandedDayId,
    setExpandedDayId,
  ] =
    useState(null);

  // =====================================
  // GOALS
  // =====================================

  const [
    goals,
    setGoals,
  ] =
    useState(() => {

      const saved =
        localStorage.getItem(
          "keremos_goals"
        );

      return saved
        ? JSON.parse(saved)
        : [];
    });

  const [
    newGoal,
    setNewGoal,
  ] =
    useState("");

  // =====================================
  // GOALS PANEL
  // =====================================

  const [
    goalsPanelOpen,
    setGoalsPanelOpen,
  ] =
    useState(false);

  // =====================================
  // AUTO SAVE GOALS
  // =====================================

  useEffect(() => {

    localStorage.setItem(

      "keremos_goals",

      JSON.stringify(
        goals
      )

    );

  }, [goals]);

  // =====================================
  // ADD GOAL
  // =====================================

  function addGoal() {

    if (!newGoal.trim()) {
      return;
    }

    setGoals([

      ...goals,

      {
        id: Date.now(),

        text: newGoal,

        completed: false,

        order:
          goals.length + 1,
      },
    ]);

    setNewGoal("");
  }

  // =====================================
  // TOGGLE GOAL
  // =====================================

  function toggleGoal(
    goalId
  ) {

    setGoals(

      goals.map(
        (goal) =>

          goal.id === goalId

            ? {

                ...goal,

                completed:
                  !goal.completed,
              }

            : goal
      )
    );
  }

  // =====================================
  // DELETE GOAL
  // =====================================

  function deleteGoal(
    goalId
  ) {

    setGoals(

      goals.filter(
        (goal) =>
          goal.id !== goalId
      )
    );
  }

  // =====================================
  // GOAL DRAG
  // =====================================

  function handleGoalDragEnd(
    event
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
      goals.findIndex(
        (goal) =>
          goal.id ===
          active.id
      );

    const newIndex =
      goals.findIndex(
        (goal) =>
          goal.id ===
          over.id
      );

    const reordered =
      arrayMove(

        goals,

        oldIndex,

        newIndex
      );

    const updated =
      reordered.map(
        (
          goal,
          index
        ) => ({

          ...goal,

          order:
            index + 1,
        })
      );

    setGoals(
      updated
    );
  }

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

  function addHourBlock(
    dayId
  ) {

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

                id: Date.now(),

                start:
                  "08:00",

                end:
                  "09:00",

                title:
                  "Yeni Görev",

                playlist_id:
                  null,

                planned_minutes:
                  60,

                tasks: [],

                developments: [],
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
              day.hourBlocks || []
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
              day.hourBlocks || []
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
        (block) =>
          block.id ===
          active.id
      );

    const newIndex =
      day.hourBlocks.findIndex(
        (block) =>
          block.id ===
          over.id
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
  // MAIN
  // =====================================

  return (

    <div>

      {/* HEADER */}

      <div
        style={{

          background:
            "#111",

          border:
            "1px solid #222",

          borderRadius:
            "18px",

          padding:
            "20px",

          marginBottom:
            "20px",
        }}
      >

        <div
          style={{

            fontSize:
              "26px",

            fontWeight:
              "bold",
          }}
        >

          Timeline Engine

        </div>

      </div>

      {/* DAYS */}

      <div
        style={{

          display:
            "flex",

          flexDirection:
            "column",

          gap: "18px",
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
                      "1px solid #222",

                    borderRadius:
                      "18px",

                    padding:
                      "18px",
                  }}
                >

                  {/* DAY HEADER */}

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

                      cursor:
                        "pointer",

                      marginBottom:
                        "14px",
                    }}
                  >

                    <div>

                      <div
                        style={{

                          fontSize:
                            "26px",

                          fontWeight:
                            "bold",
                        }}
                      >

                        Gün {day.day}

                      </div>

                      <div
                        style={{

                          fontSize:
                            "12px",

                          opacity:
                            0.6,

                          marginTop:
                            "4px",
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

                    <button

                      onClick={(e) => {

                        e.stopPropagation();

                        addHourBlock(
                          day.day
                        );
                      }}

                      style={{

                        background:
                          "#22c55e",

                        color:
                          "black",

                        border:
                          "none",

                        borderRadius:
                          "12px",

                        width:
                          "40px",

                        height:
                          "40px",

                        fontSize:
                          "22px",

                        fontWeight:
                          "bold",

                        cursor:
                          "pointer",
                      }}
                    >

                      +

                    </button>

                  </div>

                  {/* PROGRESS */}

                  <div
                    style={{

                      width:
                        "100%",

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

                  {/* EXPANDED */}

                  {
                    isExpanded && (

                      <DndContext

                        collisionDetection={
                          closestCenter
                        }

                        onDragEnd={(
                          event
                        ) =>
                          handleDragEnd(
                            event,
                            day
                          )
                        }
                      >

                        <SortableContext

                          items={
                            (
                              day.hourBlocks || []
                            ).map(
                              (block) =>
                                block.id
                            )
                          }

                          strategy={
                            verticalListSortingStrategy
                          }
                        >

                          <div>

                            {
                              (
                                day.hourBlocks || []
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

                                      playlists={
                                        playlists
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

      {/* GOALS BUTTON */}

      <div
        style={{

          marginTop:
            "24px",

          display:
            "flex",

          justifyContent:
            "center",
        }}
      >

        <button

          onClick={() =>
            setGoalsPanelOpen(true)
          }

          style={{

            background:
              "#181818",

            color:
              "white",

            border:
              "1px solid #333",

            borderRadius:
              "16px",

            padding:
              "16px 28px",

            fontSize:
              "18px",

            fontWeight:
              "bold",

            cursor:
              "pointer",

            width:
              "100%",
          }}
        >

          Hedefler

        </button>

      </div>

      {/* GOALS MODAL */}

      {
        goalsPanelOpen && (

          <div
            style={{

              position:
                "fixed",

              inset: 0,

              background:
                "rgba(0,0,0,0.7)",

              display:
                "flex",

              justifyContent:
                "center",

              alignItems:
                "center",

              zIndex:
                9999,
            }}
          >

            <div
              style={{

                width:
                  "90%",

                maxWidth:
                  "700px",

                maxHeight:
                  "80vh",

                overflowY:
                  "auto",

                background:
                  "#111",

                border:
                  "1px solid #333",

                borderRadius:
                  "22px",

                padding:
                  "24px",
              }}
            >

              {/* HEADER */}

              <div
                style={{

                  display:
                    "flex",

                  justifyContent:
                    "space-between",

                  alignItems:
                    "center",

                  marginBottom:
                    "20px",
                }}
              >

                <div
                  style={{

                    fontSize:
                      "28px",

                    fontWeight:
                      "bold",
                  }}
                >

                  Hedefler

                </div>

                <button

                  onClick={() =>
                    setGoalsPanelOpen(false)
                  }

                  style={{

                    background:
                      "#7f1d1d",

                    color:
                      "white",

                    border:
                      "none",

                    borderRadius:
                      "12px",

                    padding:
                      "10px 14px",

                    cursor:
                      "pointer",
                  }}
                >

                  Kapat

                </button>

              </div>

              {/* INPUT */}

              <div
                style={{

                  display:
                    "flex",

                  gap:
                    "10px",

                  marginBottom:
                    "18px",
                }}
              >

                <input

                  value={
                    newGoal
                  }

                  onChange={(e) =>
                    setNewGoal(
                      e.target.value
                    )
                  }

                  placeholder="Yeni hedef ekle..."

                  style={{

                    flex: 1,

                    background:
                      "#101010",

                    border:
                      "1px solid #333",

                    borderRadius:
                      "12px",

                    padding:
                      "12px",

                    color:
                      "white",

                    outline:
                      "none",
                  }}
                />

                <button

                  onClick={
                    addGoal
                  }

                  style={{

                    background:
                      "#22c55e",

                    color:
                      "black",

                    border:
                      "none",

                    borderRadius:
                      "12px",

                    padding:
                      "0 18px",

                    cursor:
                      "pointer",

                    fontWeight:
                      "bold",
                  }}
                >

                  Ekle

                </button>

              </div>

              {/* LIST */}

              <DndContext

                collisionDetection={
                  closestCenter
                }

                onDragEnd={
                  handleGoalDragEnd
                }
              >

                <SortableContext

                  items={
                    goals.map(
                      (goal) =>
                        goal.id
                    )
                  }

                  strategy={
                    verticalListSortingStrategy
                  }
                >

                  <div
                    style={{

                      display:
                        "flex",

                      flexDirection:
                        "column",

                      gap:
                        "10px",
                    }}
                  >

                    {
                      goals

                        .sort(
                          (
                            a,
                            b
                          ) =>

                            a.order -
                            b.order
                        )

                        .map(
                          (
                            goal
                          ) => (

                            <SortableGoal

                              key={
                                goal.id
                              }

                              goal={
                                goal
                              }

                              toggleGoal={
                                toggleGoal
                              }

                              deleteGoal={
                                deleteGoal
                              }
                            />
                          )
                        )
                    }

                  </div>

                </SortableContext>

              </DndContext>

            </div>

          </div>
        )
      }

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

            playlists={
              playlists
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

  playlists = [],
}) {

  const {

    attributes,

    listeners,

    setNodeRef,

    transform,

    transition,
  } =
    useSortable({

      id:
        block.id,
    });

  const style = {

    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  const linkedPlaylist =
    playlists.find(
      (playlist) =>
        playlist.id ===
        block.playlist_id
    );

  return (

    <div

      ref={
        setNodeRef
      }

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

          display:
            "grid",

          gridTemplateColumns:
            "40px 110px 110px 1fr 180px auto auto",

          gap:
            "10px",

          alignItems:
            "center",
        }}
      >

        <div

          {...attributes}

          {...listeners}

          style={{

            cursor:
              "grab",

            opacity:
              0.5,

            textAlign:
              "center",
          }}
        >

          ☰

        </div>

        <input

          value={
            block.start
          }

          onChange={(e) =>
            updateHourBlock(

              block.id,

              "start",

              e.target.value
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

              e.target.value
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

              e.target.value
            )
          }

          style={
            inputStyle
          }
        />

        <select

          value={
            block.playlist_id || ""
          }

          onChange={(e) =>

            updateHourBlock(

              block.id,

              "playlist_id",

              e.target.value

                ? Number(
                    e.target.value
                  )

                : null
            )
          }

          style={
            inputStyle
          }
        >

          <option value="">
            Playlist Yok
          </option>

          {
            playlists.map(
              (
                playlist
              ) => (

                <option

                  key={
                    playlist.id
                  }

                  value={
                    playlist.id
                  }
                >

                  {
                    playlist.title
                  }

                </option>
              )
            )
          }

        </select>

        <button

          onClick={() =>
            setSelectedBlock(
              block
            )
          }

          style={
            blueButton
          }
        >

          Todo-List

        </button>

        <button

          onClick={() =>
            deleteHourBlock(
              block.id
            )
          }

          style={
            redButton
          }
        >

          Sil

        </button>

      </div>

      {/* PLAYLIST INFO */}

      {
        linkedPlaylist && (

          <div
            style={{

              marginTop:
                "14px",

              background:
                "#101010",

              border:
                "1px solid #2a2a2a",

              borderRadius:
                "12px",

              padding:
                "12px",

              fontSize:
                "12px",

              display:
                "grid",

              gridTemplateColumns:
                "repeat(5,1fr)",

              gap:
                "12px",
            }}
          >

            <div>
              📚 Sıra:
              <br />
              <strong>
                {
                  linkedPlaylist.order_index || 0
                }
              </strong>
            </div>

            <div>
              ⏱ Toplam:
              <br />
              <strong>
                {
                  linkedPlaylist.toplam_saat || 0
                } saat
              </strong>
            </div>

            <div>
              🔥 Kalan:
              <br />
              <strong>
                {
                  linkedPlaylist.remaining_minutes || 0
                } dk
              </strong>
            </div>

            <div>
              🎯 Günlük:
              <br />
              <strong>
                {
                  linkedPlaylist.daily_target_minutes || 0
                } dk
              </strong>
            </div>

            <div>
              📅 Hedef:
              <br />
              <strong>
                {
                  linkedPlaylist.target_days || 0
                } gün
              </strong>
            </div>

          </div>
        )
      }

      {/* FOOTER */}

      <div
        style={{

          marginTop:
            "14px",

          display:
            "flex",

          justifyContent:
            "space-between",

          alignItems:
            "center",

          fontSize:
            "12px",

          opacity:
            0.7,
        }}
      >

        <div>

          ⏱ {
            block.planned_minutes || 0
          } dk

        </div>

        <div>

          %{
            blockProgress
          }

        </div>

      </div>

    </div>
  );
}

// =====================================
// SORTABLE GOAL
// =====================================

function SortableGoal({

  goal,

  toggleGoal,

  deleteGoal,
}) {

  const {

    attributes,

    listeners,

    setNodeRef,

    transform,

    transition,
  } =
    useSortable({

      id:
        goal.id,
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

      ref={
        setNodeRef
      }

      style={{

        ...style,

        display:
          "flex",

        justifyContent:
          "space-between",

        alignItems:
          "center",

        background:
          "#181818",

        border:
          "1px solid #262626",

        borderRadius:
          "12px",

        padding:
          "14px",
      }}
    >

      <div
        style={{

          display:
            "flex",

          alignItems:
            "center",

          gap:
            "12px",
        }}
      >

        <div

          {...attributes}

          {...listeners}

          style={{

            cursor:
              "grab",

            opacity:
              0.5,
          }}
        >

          ☰

        </div>

        <input

          type="checkbox"

          checked={
            goal.completed
          }

          onChange={() =>
            toggleGoal(
              goal.id
            )
          }
        />

        <div
          style={{

            textDecoration:
              goal.completed

                ? "line-through"

                : "none",

            opacity:
              goal.completed

                ? 0.5

                : 1,
          }}
        >

          {goal.text}

        </div>

      </div>

      <button

        onClick={() =>
          deleteGoal(
            goal.id
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
            "8px 12px",

          cursor:
            "pointer",
        }}
      >

        Sil

      </button>

    </div>
  );
}

// =====================================
// STYLES
// =====================================

const inputStyle = {

  background:
    "#101010",

  color:
    "white",

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
};

const redButton = {

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
};