export default function PlaylistHeader({

  dailyTarget = 0,
}) {

  return (

    <div
      style={{
        background:
          "#181818",

        border:
          "1px solid #2a2a2a",

        borderRadius:
          "18px",

        padding: "22px",

        marginBottom:
          "20px",
      }}
    >

      {/* TITLE */}

      <div
        style={{
          fontSize: "28px",

          fontWeight:
            "bold",

          marginBottom:
            "10px",
        }}
      >
        YouTube Learning OS
      </div>

      {/* DESCRIPTION */}

      <div
        style={{
          opacity: 0.7,

          lineHeight:
            "1.6",

          marginBottom:
            "18px",
        }}
      >
        Playlist tabanlı öğrenme sistemi.
        <br />
        Video → Note → Flashcard → Anki pipeline.
      </div>

      {/* STATS */}

      <div
        style={{
          display: "flex",

          flexWrap:
            "wrap",

          gap: "14px",
        }}
      >

        <div
          style={{
            background:
              "#101010",

            border:
              "1px solid #2a2a2a",

            borderRadius:
              "12px",

            padding:
              "14px",

            minWidth:
              "160px",
          }}
        >

          <div
            style={{
              opacity: 0.6,

              fontSize:
                "12px",

              marginBottom:
                "6px",
            }}
          >
            DAILY TARGET
          </div>

          <div
            style={{
              fontSize:
                "24px",

              fontWeight:
                "bold",

              color: "lime",
            }}
          >
            {dailyTarget}
            h
          </div>

        </div>

        <div
          style={{
            background:
              "#101010",

            border:
              "1px solid #2a2a2a",

            borderRadius:
              "12px",

            padding:
              "14px",

            minWidth:
              "160px",
          }}
        >

          <div
            style={{
              opacity: 0.6,

              fontSize:
                "12px",

              marginBottom:
                "6px",
            }}
          >
            SYSTEM
          </div>

          <div
            style={{
              fontSize:
                "20px",

              fontWeight:
                "bold",
            }}
          >
            ACTIVE
          </div>

        </div>

      </div>

    </div>
  );
}