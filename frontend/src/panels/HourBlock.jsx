export default function HourBlock({

  block,

  onClick,

}) {

  // =====================================
  // TASKS
  // =====================================

  const tasks =
    block.tasks || [];

  // =====================================
  // DEVELOPMENTS
  // =====================================

  const developments =
    block.developments ||
    [];

  // =====================================
  // ALL ITEMS
  // =====================================

  const allItems = [

    ...tasks,

    ...developments,
  ];

  // =====================================
  // COMPLETED
  // =====================================

  const completed =
    allItems.filter(
      (item) =>
        item.completed
    ).length;

  // =====================================
  // PROGRESS
  // =====================================

  const progress =

    allItems.length === 0

      ? 0

      : Math.round(

          (
            completed /
            allItems.length
          ) * 100
        );

  // =====================================
  // TIME
  // =====================================

  const startHour =
    parseInt(
      block.start.split(
        ":"
      )[0]
    );

  const endHour =
    parseInt(
      block.end.split(
        ":"
      )[0]
    );

  // =====================================
  // DURATION
  // =====================================

  const duration =
    Math.max(
      1,
      endHour - startHour
    );

  // =====================================
  // HEIGHT
  // =====================================

  const dynamicHeight =
    duration * 58;

  // =====================================
  // MAIN
  // =====================================

  return (

    <div

      onClick={onClick}

      style={{

        background:
          "#1d4ed8",

        borderRadius:
          "14px",

        cursor: "pointer",

        marginBottom:
          "8px",

        overflow:
          "hidden",

        border:
          "1px solid rgba(255,255,255,0.08)",

        transition:
          "0.2s",

        minHeight:
          `${dynamicHeight}px`,

        display: "flex",

        alignItems:
          "center",

        justifyContent:
          "center",

        textAlign:
          "center",

        padding: "12px",
      }}
    >

      {/* CENTER */}

      <div
        style={{

          width: "100%",

          display: "flex",

          flexDirection:
            "column",

          alignItems:
            "center",

          justifyContent:
            "center",
        }}
      >

        {/* HOURS */}

        <div
          style={{

            fontSize:
              "11px",

            opacity:
              0.8,
          }}
        >

          {block.start}

          {" - "}

          {block.end}

        </div>

        {/* TITLE */}

        <div
          style={{

            fontSize:
              "14px",

            fontWeight:
              "bold",

            marginTop:
              "6px",

            maxWidth:
              "100%",

            overflow:
              "hidden",

            textOverflow:
              "ellipsis",

            whiteSpace:
              "nowrap",
          }}
        >

          {
            block.title ||
            "İsimsiz Başlık"
          }

        </div>

        {/* PROGRESS */}

        <div
          style={{

            marginTop:
              "12px",

            width: "100%",
          }}
        >

          <div
            style={{

              fontSize:
                "11px",

              marginBottom:
                "6px",

              opacity:
                0.9,
            }}
          >

            Progress %{progress}

          </div>

          <div
            style={{

              height: "5px",

              background:
                "rgba(255,255,255,0.25)",

              borderRadius:
                "999px",

              overflow:
                "hidden",
            }}
          >

            <div
              style={{

                width:
                  `${progress}%`,

                height:
                  "100%",

                background:
                  "white",
              }}
            />

          </div>

        </div>

        {/* INFO */}

        <div
          style={{

            marginTop:
              "12px",

            display: "flex",

            gap: "14px",

            justifyContent:
              "center",

            alignItems:
              "center",

            flexWrap:
              "wrap",

            fontSize:
              "11px",

            opacity:
              0.9,
          }}
        >

          <div>

            Görev:
            {" "}

            {tasks.length}

          </div>

          <div>

            Geliştirme:
            {" "}

            {
              developments.length
            }

          </div>

        </div>

      </div>

    </div>
  );
}