import {
  useSortable,
} from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

import GoalDetailPanel from "./GoalDetailPanel.jsx";

// =====================================
// MAIN
// =====================================

export default function GoalCard({
  goal,

  playlists = [],

  expandedGoalId,

  toggleDetail,

  deleteGoal,

  linkPlaylist,

  updateGoalDescription,
}) {
  // =====================================
  // DND
  // =====================================

  const {
    attributes,

    listeners,

    setNodeRef,

    transform,

    transition,
  } = useSortable({
    id: goal.id,
  });

  const style = {
    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  // =====================================
  // EXPANDED
  // =====================================

  const isExpanded =
    expandedGoalId === goal.id;

  // =====================================
  // MAIN
  // =====================================

  return (
    <div
      ref={setNodeRef}
      style={{
        ...style,

        background: "#181818",

        border: "1px solid #262626",

        borderRadius: "24px",

        overflow: "hidden",
      }}
    >
      {/* CARD */}

      <div
        style={{
          display: "flex",

          justifyContent:
            "space-between",

          gap: "20px",

          padding: "24px",
        }}
      >
        {/* LEFT */}

        <div
          style={{
            display: "flex",

            gap: "20px",

            flex: 1,
          }}
        >
          {/* DRAG */}

          <div
            {...attributes}
            {...listeners}
            style={{
              cursor: "grab",

              color: "white",

              opacity: 0.5,

              fontSize: "26px",

              paddingTop: "8px",
            }}
          >
            ☰
          </div>

          {/* ICON */}

          <div
            style={{
              width: "54px",

              height: "54px",

              background: "#2a2a2a",

              border:
                "2px solid #444",

              borderRadius: "12px",

              flexShrink: 0,
            }}
          />

          {/* CONTENT */}

          <div
            style={{
              flex: 1,
            }}
          >
            {/* TITLE */}

            <div
              style={{
                color: "white",

                fontSize: "38px",

                fontWeight: "300",

                marginBottom: "10px",
              }}
            >
              {goal.title}
            </div>

            {/* TAG INPUT */}

            <input
              type="text"
              value={
                goal.description || ""
              }
              onChange={(e) =>
                updateGoalDescription?.(
                  goal.id,
                  e.target.value
                )
              }
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  e.target.blur();
                }
              }}
              style={{
                width: "120px",

                background: "#101010",

                border:
                  "1px solid #333",

                borderRadius: "999px",

                padding: "8px 12px",

                color: "white",

                outline: "none",

                fontSize: "12px",
              }}
            />
          </div>
        </div>

        {/* RIGHT */}

        <div
          style={{
            display: "flex",

            flexDirection: "column",

            gap: "12px",

            justifyContent:
              "center",
          }}
        >
          {/* DETAIL */}

          <button
            onClick={() =>
              toggleDetail(goal.id)
            }
            style={buttonStyle}
          >
            Detay
          </button>

          {/* DELETE */}

          <button
            onClick={() =>
              deleteGoal(goal.id)
            }
            style={buttonStyle}
          >
            Sil
          </button>
        </div>
      </div>

      {/* DETAIL */}

      {isExpanded && (
        <GoalDetailPanel
          goal={goal}
          playlists={playlists}
          linkPlaylist={linkPlaylist}
        />
      )}
    </div>
  );
}

// =====================================
// STYLES
// =====================================

const buttonStyle = {
  background: "#d1d5db",

  color: "black",

  border: "none",

  borderRadius: "12px",

  padding: "12px 22px",

  fontSize: "15px",

  cursor: "pointer",

  fontWeight: "600",
};