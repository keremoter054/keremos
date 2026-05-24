import { useState, useEffect } from "react";

import TopBar from "./panels/TopBar.jsx";
import CenterPanel from "./panels/CenterPanel.jsx";

import DayPage from "./panels/DayPage.jsx";

// =====================================
// FIXED TIP-1 START DATE
// =====================================

const TIP1_START_DATE =
  new Date("2026-05-14");

// =====================================
// VISUAL BAR FILL
// =====================================

const HUMANITY_TYPE1_PROGRESS =
  0.72;

// =====================================
// DISPLAYED PERCENT
// =====================================

const DISPLAYED_PROGRESS =
  0.72;

// =====================================
// GET DATE FOR DAY
// =====================================

function createFixedDate(
  dayNumber
) {

  const date =
    new Date(
      TIP1_START_DATE
    );

  date.setDate(

    TIP1_START_DATE.getDate()
    + (dayNumber - 1)
  );

  return date;
}

export default function App() {

  // =====================================
  // OPENED DAY
  // =====================================

  const [
    openedDay,
    setOpenedDay,
  ] =
    useState(null);

  // =====================================
  // SELECTED DAY
  // =====================================

  const [
    selectedDayId,
    setSelectedDayId,
  ] =
    useState(1);

  // =====================================
  // CALENDAR DAYS
  // =====================================

  const [
    calendarDays,
    setCalendarDays,
  ] =
    useState(() => {

      const saved =
        localStorage.getItem(
          "keremos_calendar"
        );

      if (saved) {

        try {

          const parsed =
            JSON.parse(saved);

          return parsed.map(
            (day, index) => ({

              ...day,

              day:
                day.day ||
                index + 1,

              date:
                day.date ||
                createFixedDate(
                  day.day ||
                  index + 1
                ).toISOString(),

              hourBlocks:
                (
                  day.hourBlocks ||
                  []
                ).map(
                  (block) => ({

                    ...block,

                    tasks:
                      block.tasks ||
                      [],

                    developments:
                      block.developments ||
                      [],
                  })
                ),
            })
          );

        } catch {

          localStorage.removeItem(
            "keremos_calendar"
          );
        }
      }

      return Array.from(

        { length: 365 },

        (_, i) => ({

          day: i + 1,

          date:
            createFixedDate(
              i + 1
            ).toISOString(),

          hourBlocks: [],
        })
      );
    });

  // =====================================
  // AUTO SAVE
  // =====================================

  useEffect(() => {

    localStorage.setItem(

      "keremos_calendar",

      JSON.stringify(
        calendarDays
      )
    );

  }, [calendarDays]);

  // =====================================
  // DAY PROGRESS
  // =====================================

  function calculateDayProgress(
    day
  ) {

    if (!day) {

      return 0;
    }

    const hourBlocks =
      day.hourBlocks || [];

    const allTasks =
      hourBlocks.flatMap(
        (block) => [

          ...(block.tasks || []),

          ...(block.developments || []),
        ]
      );

    if (
      allTasks.length === 0
    ) {

      return 0;
    }

    const completed =
      allTasks.filter(
        (task) =>
          task.completed
      ).length;

    return Math.round(

      (
        completed /
        allTasks.length
      ) * 100
    );
  }

  // =====================================
  // DATE SYSTEM
  // =====================================

  function getDateForDay(
    day
  ) {

    return createFixedDate(
      day
    );
  }

  // =====================================
  // USER CONTRIBUTION
  // =====================================

  function calculateKeremOSContribution() {

    const allBlocks =
      calendarDays.flatMap(
        (day) =>
          day.hourBlocks || []
      );

    const allItems =
      allBlocks.flatMap(
        (block) => [

          ...(block.tasks || []),

          ...(block.developments || []),
        ]
      );

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

    return (

      (
        completed /
        allItems.length
      ) * 0.02
    );
  }

  // =====================================
  // FINAL DISPLAY
  // =====================================

  const keremOSContribution =
    calculateKeremOSContribution();

  const visualProgress =

    Math.min(

      HUMANITY_TYPE1_PROGRESS +

      keremOSContribution,

      1
    );

  const displayedProgress =

    DISPLAYED_PROGRESS +

    keremOSContribution;

  // =====================================
  // MAIN
  // =====================================

  return (

    <div
      style={{

        background: "#0b0b0b",

        color: "white",

        height: "100vh",

        display: "flex",

        flexDirection:
          "column",

        overflow: "hidden",
      }}
    >

      {/* TOP */}

      <div
        style={{

          minHeight: "130px",

          borderBottom:
            "1px solid #1f1f1f",

          display: "flex",

          flexDirection:
            "column",

          justifyContent:
            "center",

          padding:
            "20px 34px",

          background:
            "#101010",

          flexShrink: 0,
        }}
      >

        {/* TITLE */}

        <div
          style={{

            fontSize:
              "42px",

            fontWeight:
              "bold",

            letterSpacing:
              "-1px",

            marginBottom:
              "16px",
          }}
        >

          KeremOS

        </div>

        {/* LABEL */}

        <div
          style={{

            marginBottom:
              "10px",

            fontSize:
              "14px",

            opacity:
              0.72,

            fontWeight:
              "bold",
          }}
        >

          Current Humanity Progress Toward Type-1 Civilization

        </div>

        {/* BAR */}

        <div
          style={{

            width: "100%",

            height: "28px",

            background:
              "#1d1d1d",

            borderRadius:
              "999px",

            overflow:
              "hidden",

            border:
              "1px solid #2a2a2a",

            position:
              "relative",
          }}
        >

          {/* FILL */}

          <div
            style={{

              width:
                `${visualProgress * 100}%`,

              height:
                "100%",

              background:
                "linear-gradient(90deg,#22c55e,#16a34a)",

              boxShadow:
                "0 0 20px #22c55e",

              transition:
                "0.3s",
            }}
          />

          {/* TEXT */}

          <div
            style={{

              position:
                "absolute",

              inset: 0,

              display: "flex",

              alignItems:
                "center",

              justifyContent:
                "center",

              fontSize:
                "13px",

              fontWeight:
                "bold",

              letterSpacing:
                "0.5px",
            }}
          >

            KeremOS • Civilization Operating System
            {" • "}
            %
            {
              displayedProgress.toFixed(2)
            }

          </div>

        </div>

      </div>

      {/* CENTER */}

      <div
        style={{

          flex: 1,

          overflow: "hidden",

          padding: "22px",

          display: "flex",

          justifyContent:
            "center",
        }}
      >

        <div
          style={{

            width: "100%",

            maxWidth:
              "860px",

            overflow:
              "hidden",
          }}
        >

          <CenterPanel

            calendarDays={
              calendarDays
            }

            setCalendarDays={
              setCalendarDays
            }

            selectedDayId={
              selectedDayId
            }

            setSelectedDayId={
              setSelectedDayId
            }

            calculateDayProgress={
              calculateDayProgress
            }

            getDateForDay={
              getDateForDay
            }

            openedDay={
              openedDay
            }

            setOpenedDay={
              setOpenedDay
            }

          />

        </div>

      </div>

      {/* DAY PAGE */}

      {
        openedDay && (

          <DayPage

            openedDay={
              openedDay
            }

            setOpenedDay={
              setOpenedDay
            }

            calendarDays={
              calendarDays
            }

            setCalendarDays={
              setCalendarDays
            }

            calculateDayProgress={
              calculateDayProgress
            }

          />
        )
      }

    </div>
  );
}