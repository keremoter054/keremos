import { useSortable } from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

export default function PlaylistCard({

  id,

  title,
  channel,

  thumbnail_url,

  toplam_saat,
  izlenen_saat,

  yuzde,

  kalan_gun,
  bitis_tarihi,

  onClick,
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
    id,
  });

  const style = {

    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  // =====================================
  // RENDER
  // =====================================

  return (

    <div
      ref={setNodeRef}
      style={{
        ...style,

        background:
          "#181818",

        border:
          "1px solid #2a2a2a",

        borderRadius:
          "18px",

        padding: "18px",

        marginBottom:
          "14px",

        cursor: "pointer",
      }}
      {...attributes}
      {...listeners}
      onClick={onClick}
    >

      <div
        style={{
          display: "flex",
          gap: "16px",
        }}
      >

        {/* THUMBNAIL */}

        <img
          src={thumbnail_url}
          alt={title}
          style={{
            width: "140px",

            height: "80px",

            objectFit:
              "cover",

            borderRadius:
              "12px",

            border:
              "1px solid #333",
          }}
        />

        {/* INFO */}

        <div
          style={{
            flex: 1,
          }}
        >

          <div
            style={{
              fontSize: "18px",
              fontWeight:
                "bold",
              marginBottom:
                "6px",
            }}
          >
            {title}
          </div>

          <div
            style={{
              opacity: 0.7,
              fontSize: "13px",
              marginBottom:
                "12px",
            }}
          >
            {channel}
          </div>

          {/* PROGRESS */}

          <div
            style={{
              width: "100%",
              height: "10px",

              background:
                "#2a2a2a",

              borderRadius:
                "999px",

              overflow:
                "hidden",
            }}
          >

            <div
              style={{
                width:
                  `${yuzde}%`,

                height:
                  "100%",

                background:
                  "lime",
              }}
            />

          </div>

          {/* STATS */}

          <div
            style={{
              marginTop:
                "10px",

              display: "flex",

              flexWrap:
                "wrap",

              gap: "12px",

              fontSize:
                "13px",

              opacity: 0.85,
            }}
          >

            <div>
              ⏱️
              {" "}
              {izlenen_saat}
              h /
              {" "}
              {toplam_saat}
              h
            </div>

            <div>
              📈 %
              {yuzde}
            </div>

            <div>
              📅
              {" "}
              {kalan_gun}
              gün
            </div>

            <div>
              🎯
              {" "}
              {bitis_tarihi}
            </div>

          </div>

        </div>

      </div>

    </div>
  );
}