import {
  DndContext,
  closestCenter,
} from "@dnd-kit/core";

import {
  SortableContext,
  verticalListSortingStrategy,
  arrayMove,
} from "@dnd-kit/sortable";

import HourBlock from "./HourBlock.jsx";

// =====================================
// MAIN
// =====================================

export default function DayCard({
  day,

  progress,

  isExpanded,

  playlists = [],

  getDateForDay,

  toggleDay,

  addHourBlock,

  selectedDayId,

  setSelectedDayId,

  updateHourBlock,

  deleteHourBlock,

  getBlockProgress,

  setSelectedBlock,

  setCalendarDays,
}) {
  // =====================================
  // DRAG END
  // =====================================

  function handleDragEnd(event) {
    const { active, over } = event;

    if (!over || active.id === over.id) {
      return;
    }

    const oldIndex =
      day.hourBlocks.findIndex(
        (block) =>
          block.id === active.id
      );

    const newIndex =
      day.hourBlocks.findIndex(
        (block) =>
          block.id === over.id
      );

    const reordered = arrayMove(
      day.hourBlocks,
      oldIndex,
      newIndex
    );

    setCalendarDays((prev) =>
      prev.map((d) =>
        d.day === day.day
          ? {
              ...d,

              hourBlocks: reordered,
            }
          : d
      )
    );
  }

  // =====================================
  // MAIN
  // =====================================

  return (
    <div
      style={{
        background: "#111",

        border: "1px solid #222",

        borderRadius: "18px",

        padding: "18px",
      }}
    >
      {/* HEADER */}

      <div
        onClick={() => {
          setSelectedDayId(day.day);

          toggleDay(day.day);
        }}
        style={{
          display: "flex",

          justifyContent:
            "space-between",

          alignItems: "center",

          cursor: "pointer",

          marginBottom: "14px",
        }}
      >
        {/* LEFT */}

        <div>
          <div
            style={{
              fontSize: "26px",

              fontWeight: "bold",

              color: "white",
            }}
          >
            Gün {day.day}
          </div>

          <div
            style={{
              fontSize: "12px",

              opacity: 0.6,

              marginTop: "4px",

              color: "white",
            }}
          >
            {getDateForDay(
              day.day
            ).toLocaleDateString(
              "tr-TR"
            )}
          </div>
        </div>

        {/* RIGHT */}

        <button
          onClick={(e) => {
            e.stopPropagation();

            addHourBlock(day.day);
          }}
          style={{
            background: "#22c55e",

            color: "black",

            border: "none",

            borderRadius: "12px",

            width: "40px",

            height: "40px",

            fontSize: "22px",

            fontWeight: "bold",

            cursor: "pointer",
          }}
        >
          +
        </button>
      </div>

      {/* PROGRESS */}

      <div
        style={{
          width: "100%",

          height: "8px",

          background: "#222",

          borderRadius: "999px",

          overflow: "hidden",

          marginBottom: "18px",
        }}
      >
        <div
          style={{
            width: `${progress}%`,

            height: "100%",

            background: "#22c55e",
          }}
        />
      </div>

      {/* EXPANDED */}

      {isExpanded && (
        <DndContext
          collisionDetection={
            closestCenter
          }
          onDragEnd={handleDragEnd}
        >
          <SortableContext
            items={(day.hourBlocks || []).map(
              (block) => block.id
            )}
            strategy={
              verticalListSortingStrategy
            }
          >
            <div>
              {(day.hourBlocks || []).map(
                (block) => (
                  <HourBlock
                    key={block.id}
                    block={block}
                    playlists={playlists}
                    updateHourBlock={
                      updateHourBlock
                    }
                    deleteHourBlock={
                      deleteHourBlock
                    }
                    setSelectedBlock={
                      setSelectedBlock
                    }
                    blockProgress={getBlockProgress(
                      block
                    )}
                  />
                )
              )}
            </div>
          </SortableContext>
        </DndContext>
      )}
    </div>
  );
}