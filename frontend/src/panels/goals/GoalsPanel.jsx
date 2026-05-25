import {
  useState,
  useEffect,
} from "react";

import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  SortableContext,
  verticalListSortingStrategy,
  arrayMove,
} from "@dnd-kit/sortable";

import GoalCard from "./GoalCard.jsx";

// =====================================
// MAIN
// =====================================

export default function GoalsPanel({
  playlists = [],
}) {
  // =====================================
  // STATES
  // =====================================

  const [goalsPanelOpen, setGoalsPanelOpen] =
    useState(false);

  const [expandedGoalId, setExpandedGoalId] =
    useState(null);

  const [newGoal, setNewGoal] =
    useState("");

  const [goals, setGoals] = useState(() => {
    const saved =
      localStorage.getItem(
        "keremos_goals"
      );

    return saved
      ? JSON.parse(saved)
      : [];
  });

  // =====================================
  // AUTO SAVE
  // =====================================

  useEffect(() => {
    localStorage.setItem(
      "keremos_goals",
      JSON.stringify(goals)
    );
  }, [goals]);

  // =====================================
  // PLAYLIST AUTO IMPORT
  // =====================================

  useEffect(() => {
    if (!playlists.length) {
      return;
    }

    setGoals((prevGoals) => {
      const existingTitles =
        prevGoals.map((goal) =>
          goal.title.toLowerCase()
        );

      const newGoals = playlists
        .filter(
          (playlist) =>
            !existingTitles.includes(
              playlist.title.toLowerCase()
            )
        )
        .map((playlist) => ({
          id:
            Date.now() +
            Math.random(),

          title: playlist.title,

          description: "",

          linkedPlaylists: [
            playlist.id,
          ],

          completed: false,

          order:
            prevGoals.length + 1,
        }));

      return [
        ...prevGoals,

        ...newGoals,
      ];
    });
  }, [playlists]);

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

        title: newGoal,

        description: "",

        linkedPlaylists: [],

        completed: false,

        order: goals.length + 1,
      },
    ]);

    setNewGoal("");
  }

  // =====================================
  // UPDATE DESCRIPTION
  // =====================================

  function updateGoalDescription(
    goalId,
    value
  ) {
    setGoals(
      goals.map((goal) =>
        goal.id === goalId
          ? {
              ...goal,

              description:
                value,
            }
          : goal
      )
    );
  }

  // =====================================
  // DELETE GOAL
  // =====================================

  function deleteGoal(goalId) {
    setGoals(
      goals.filter(
        (goal) =>
          goal.id !== goalId
      )
    );
  }

  // =====================================
  // TOGGLE DETAIL
  // =====================================

  function toggleDetail(goalId) {
    setExpandedGoalId(
      expandedGoalId === goalId
        ? null
        : goalId
    );
  }

  // =====================================
  // LINK PLAYLIST
  // =====================================

  function linkPlaylist(
    goalId,
    playlistId
  ) {
    setGoals(
      goals.map((goal) => {
        if (goal.id !== goalId) {
          return goal;
        }

        const exists =
          goal.linkedPlaylists?.includes(
            playlistId
          );

        if (exists) {
          return goal;
        }

        return {
          ...goal,

          linkedPlaylists: [
            ...(goal.linkedPlaylists ||
              []),

            playlistId,
          ],
        };
      })
    );
  }

  // =====================================
  // DRAG END
  // =====================================

  function handleDragEnd(event) {
    const { active, over } =
      event;

    if (
      !over ||
      active.id === over.id
    ) {
      return;
    }

    const oldIndex =
      goals.findIndex(
        (goal) =>
          goal.id === active.id
      );

    const newIndex =
      goals.findIndex(
        (goal) =>
          goal.id === over.id
      );

    const reordered = arrayMove(
      goals,
      oldIndex,
      newIndex
    );

    const updated =
      reordered.map(
        (goal, index) => ({
          ...goal,

          order: index + 1,
        })
      );

    setGoals(updated);
  }

  // =====================================
  // MAIN
  // =====================================

  return (
    <>
      {/* BUTTON */}

      <div
        style={{
          marginTop: "24px",

          display: "flex",

          justifyContent:
            "center",

          paddingBottom: "40px",
        }}
      >
        <button
          onClick={() =>
            setGoalsPanelOpen(true)
          }
          style={{
            background: "#181818",

            color: "white",

            border:
              "1px solid #333",

            borderRadius: "16px",

            padding: "16px 28px",

            fontSize: "18px",

            fontWeight: "bold",

            cursor: "pointer",

            width: "100%",
          }}
        >
          Hedefler
        </button>
      </div>

      {/* MODAL */}

      {goalsPanelOpen && (
        <div
          style={{
            position: "fixed",

            inset: 0,

            background:
              "rgba(0,0,0,0.72)",

            zIndex: 9999,

            overflowY: "auto",

            padding: "40px",
          }}
        >
          {/* CONTAINER */}

          <div
            style={{
              width: "100%",

              maxWidth: "1400px",

              margin: "0 auto",

              background: "#111",

              border:
                "1px solid #262626",

              borderRadius: "24px",

              padding: "24px",

              minHeight: "80vh",
            }}
          >
            {/* HEADER */}

            <div
              style={{
                display: "flex",

                justifyContent:
                  "space-between",

                alignItems:
                  "center",

                marginBottom: "24px",
              }}
            >
              <div
                style={{
                  fontSize: "34px",

                  fontWeight: "bold",

                  color: "white",
                }}
              >
                Hedef Sistemi
              </div>

              <button
                onClick={() =>
                  setGoalsPanelOpen(false)
                }
                style={{
                  background:
                    "#7f1d1d",

                  color: "white",

                  border: "none",

                  borderRadius:
                    "12px",

                  padding:
                    "12px 18px",

                  cursor: "pointer",

                  fontWeight:
                    "bold",
                }}
              >
                Kapat
              </button>
            </div>

            {/* INPUT */}

            <div
              style={{
                display: "flex",

                gap: "12px",

                marginBottom: "28px",
              }}
            >
              <input
                value={newGoal}
                onChange={(e) =>
                  setNewGoal(
                    e.target.value
                  )
                }
                placeholder="Yeni hedef oluştur..."
                style={{
                  flex: 1,

                  background:
                    "#181818",

                  border:
                    "1px solid #333",

                  borderRadius:
                    "16px",

                  padding: "18px",

                  color: "white",

                  fontSize: "16px",

                  outline: "none",
                }}
              />

              <button
                onClick={addGoal}
                style={{
                  background:
                    "#22c55e",

                  color: "black",

                  border: "none",

                  borderRadius:
                    "16px",

                  padding:
                    "0 28px",

                  cursor: "pointer",

                  fontWeight:
                    "bold",

                  fontSize: "16px",
                }}
              >
                Ekle
              </button>
            </div>

            {/* GOALS */}

            <DndContext
              collisionDetection={
                closestCenter
              }
              onDragEnd={
                handleDragEnd
              }
            >
              <SortableContext
                items={goals.map(
                  (goal) =>
                    goal.id
                )}
                strategy={
                  verticalListSortingStrategy
                }
              >
                <div
                  style={{
                    display: "flex",

                    flexDirection:
                      "column",

                    gap: "20px",
                  }}
                >
                  {goals
                    .sort(
                      (a, b) =>
                        (a.order ||
                          0) -
                        (b.order ||
                          0)
                    )
                    .map((goal) => (
                      <GoalCard
                        key={goal.id}
                        goal={goal}
                        playlists={
                          playlists
                        }
                        expandedGoalId={
                          expandedGoalId
                        }
                        toggleDetail={
                          toggleDetail
                        }
                        deleteGoal={
                          deleteGoal
                        }
                        linkPlaylist={
                          linkPlaylist
                        }
                        updateGoalDescription={
                          updateGoalDescription
                        }
                      />
                    ))}
                </div>
              </SortableContext>
            </DndContext>
          </div>
        </div>
      )}
    </>
  );
}