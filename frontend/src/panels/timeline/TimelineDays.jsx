import DayCard from "./DayCard.jsx";

// =====================================
// MAIN
// =====================================

export default function TimelineDays({
  calendarDays,

  setCalendarDays,

  selectedDayId,

  setSelectedDayId,

  calculateDayProgress,

  getDateForDay,

  expandedDayId,

  toggleDay,

  addHourBlock,

  updateHourBlock,

  deleteHourBlock,

  getBlockProgress,

  setSelectedBlock,

  playlists = [],
}) {
  return (
    <div
      style={{
        height: "100%",

        overflowY: "auto",

        overflowX: "hidden",

        display: "flex",

        flexDirection: "column",

        gap: "18px",

        paddingRight: "6px",

        scrollbarWidth: "thin",

        paddingBottom: "20px",
      }}
    >
      {calendarDays.map((day) => {
        const progress =
          calculateDayProgress(day);

        const isExpanded =
          expandedDayId === day.day;

        return (
          <DayCard
            key={day.day}
            day={day}
            progress={progress}
            isExpanded={isExpanded}
            playlists={playlists}
            getDateForDay={getDateForDay}
            toggleDay={toggleDay}
            addHourBlock={addHourBlock}
            selectedDayId={selectedDayId}
            setSelectedDayId={
              setSelectedDayId
            }
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
            setCalendarDays={
              setCalendarDays
            }
          />
        );
      })}
    </div>
  );
}