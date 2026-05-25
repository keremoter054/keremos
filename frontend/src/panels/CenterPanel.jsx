import { useState } from "react";
import HourTaskModal from "./HourTaskModal.jsx";
import GoalsPanel from "./goals/GoalsPanel.jsx";
import TimelineDays from "./timeline/TimelineDays.jsx";

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
  // STATES
  // =====================================

  const [selectedBlock, setSelectedBlock] =
    useState(null);

  const [expandedDayId, setExpandedDayId] =
    useState(null);

  // =====================================
  // TOGGLE DAY
  // =====================================

  function toggleDay(dayId) {
    setExpandedDayId(
      expandedDayId === dayId
        ? null
        : dayId
    );
  }

  // =====================================
  // ADD BLOCK
  // =====================================

  function addHourBlock(dayId) {
    const updated = calendarDays.map((day) => {
      if (day.day !== dayId) {
        return day;
      }

      return {
        ...day,

        hourBlocks: [
          ...(day.hourBlocks || []),

          {
            id: Date.now(),

            start: "08:00",

            end: "09:00",

            title: "Yeni Görev",

            playlist_id: null,

            planned_minutes: 60,

            tasks: [],

            developments: [],
          },
        ],
      };
    });

    setCalendarDays(updated);
  }

  // =====================================
  // UPDATE BLOCK
  // =====================================

  function updateHourBlock(
    blockId,
    field,
    value
  ) {
    const updated = calendarDays.map(
      (day) => ({
        ...day,

        hourBlocks: (day.hourBlocks || []).map(
          (block) =>
            block.id === blockId
              ? {
                  ...block,

                  [field]: value,
                }
              : block
        ),
      })
    );

    setCalendarDays(updated);
  }

  // =====================================
  // DELETE BLOCK
  // =====================================

  function deleteHourBlock(blockId) {
    const updated = calendarDays.map(
      (day) => ({
        ...day,

        hourBlocks: (day.hourBlocks || []).filter(
          (block) => block.id !== blockId
        ),
      })
    );

    setCalendarDays(updated);

    setSelectedBlock(null);
  }

  // =====================================
  // BLOCK PROGRESS
  // =====================================

  function getBlockProgress(block) {
    const allItems = [
      ...(block.tasks || []),

      ...(block.developments || []),
    ];

    if (allItems.length === 0) {
      return 0;
    }

    const completed = allItems.filter(
      (item) => item.completed
    ).length;

    return Math.round(
      (completed / allItems.length) * 100
    );
  }

  // =====================================
  // MAIN
  // =====================================

  return (
    <div
      style={{
        height: "100vh",

        overflow: "hidden",

        display: "flex",

        flexDirection: "column",

        gap: "20px",
      }}
    >
      {/* HEADER */}

      <div
        style={{
          background: "#111",

          border: "1px solid #222",

          borderRadius: "18px",

          padding: "20px",

          flexShrink: 0,
        }}
      >
        <div
          style={{
            fontSize: "26px",

            fontWeight: "bold",
          }}
        >
          Timeline Engine
        </div>
      </div>

      {/* TIMELINE */}

      <div
        style={{
          flex: 1,

          overflow: "hidden",
        }}
      >
        <TimelineDays
          calendarDays={calendarDays}
          setCalendarDays={setCalendarDays}
          selectedDayId={selectedDayId}
          setSelectedDayId={setSelectedDayId}
          calculateDayProgress={
            calculateDayProgress
          }
          getDateForDay={getDateForDay}
          expandedDayId={expandedDayId}
          toggleDay={toggleDay}
          addHourBlock={addHourBlock}
          updateHourBlock={
            updateHourBlock
          }
          deleteHourBlock={
            deleteHourBlock
          }
          getBlockProgress={
            getBlockProgress
          }
          setSelectedBlock={
            setSelectedBlock
          }
          playlists={playlists}
        />
      </div>

      {/* GOALS */}

      <div
        style={{
          flexShrink: 0,
        }}
      >
        <GoalsPanel
          playlists={playlists}
        />
      </div>

      {/* MODAL */}

      {selectedBlock && (
        <HourTaskModal
          block={selectedBlock}
          setSelectedBlock={
            setSelectedBlock
          }
          calendarDays={calendarDays}
          setCalendarDays={
            setCalendarDays
          }
          playlists={playlists}
        />
      )}
    </div>
  );
}