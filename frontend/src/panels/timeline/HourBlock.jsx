import {
  useSortable,
} from "@dnd-kit/sortable";

import { CSS } from "@dnd-kit/utilities";

// =====================================
// MAIN
// =====================================

export default function HourBlock({
  block,

  playlists = [],

  updateHourBlock,

  deleteHourBlock,

  setSelectedBlock,

  blockProgress,
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
    id: block.id,
  });

  const style = {
    transform:
      CSS.Transform.toString(
        transform
      ),

    transition,
  };

  // =====================================
  // PLAYLIST
  // =====================================

  const linkedPlaylist =
    playlists.find(
      (playlist) =>
        playlist.id ===
        block.playlist_id
    );

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

        borderRadius: "14px",

        padding: "14px",

        marginBottom: "12px",
      }}
    >
      {/* TOP */}

      <div
        style={{
          display: "grid",

          gridTemplateColumns:
            "40px 110px 110px 1fr 180px auto auto",

          gap: "10px",

          alignItems: "center",
        }}
      >
        {/* DRAG */}

        <div
          {...attributes}
          {...listeners}
          style={{
            cursor: "grab",

            opacity: 0.5,

            textAlign: "center",

            color: "white",
          }}
        >
          ☰
        </div>

        {/* START */}

        <input
          value={block.start}
          onChange={(e) =>
            updateHourBlock(
              block.id,
              "start",
              e.target.value
            )
          }
          style={inputStyle}
        />

        {/* END */}

        <input
          value={block.end}
          onChange={(e) =>
            updateHourBlock(
              block.id,
              "end",
              e.target.value
            )
          }
          style={inputStyle}
        />

        {/* TITLE */}

        <input
          value={block.title}
          onChange={(e) =>
            updateHourBlock(
              block.id,
              "title",
              e.target.value
            )
          }
          style={inputStyle}
        />

        {/* PLAYLIST */}

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
          style={inputStyle}
        >
          <option value="">
            Playlist Yok
          </option>

          {playlists.map(
            (playlist) => (
              <option
                key={playlist.id}
                value={
                  playlist.id
                }
              >
                {playlist.title}
              </option>
            )
          )}
        </select>

        {/* TODO */}

        <button
          onClick={() =>
            setSelectedBlock(block)
          }
          style={blueButton}
        >
          Todo
        </button>

        {/* DELETE */}

        <button
          onClick={() =>
            deleteHourBlock(block.id)
          }
          style={redButton}
        >
          Sil
        </button>
      </div>

      {/* PLAYLIST INFO */}

      {linkedPlaylist && (
        <div
          style={{
            marginTop: "14px",

            background: "#101010",

            border:
              "1px solid #2a2a2a",

            borderRadius: "12px",

            padding: "12px",

            display: "grid",

            gridTemplateColumns:
              "repeat(5,1fr)",

            gap: "12px",

            fontSize: "12px",
          }}
        >
          <div>
            📚 Sıra
            <br />
            <strong>
              {linkedPlaylist.order_index ||
                0}
            </strong>
          </div>

          <div>
            ⏱ Toplam
            <br />
            <strong>
              {linkedPlaylist.toplam_saat ||
                0}{" "}
              saat
            </strong>
          </div>

          <div>
            🔥 Kalan
            <br />
            <strong>
              {linkedPlaylist.remaining_minutes ||
                0}{" "}
              dk
            </strong>
          </div>

          <div>
            🎯 Günlük
            <br />
            <strong>
              {linkedPlaylist.daily_target_minutes ||
                0}{" "}
              dk
            </strong>
          </div>

          <div>
            📅 Hedef
            <br />
            <strong>
              {linkedPlaylist.target_days ||
                0}{" "}
              gün
            </strong>
          </div>
        </div>
      )}

      {/* FOOTER */}

      <div
        style={{
          marginTop: "14px",

          display: "flex",

          justifyContent:
            "space-between",

          alignItems: "center",

          fontSize: "12px",

          opacity: 0.7,

          color: "white",
        }}
      >
        <div>
          ⏱{" "}
          {block.planned_minutes ||
            0}{" "}
          dk
        </div>

        <div>
          %{blockProgress}
        </div>
      </div>
    </div>
  );
}

// =====================================
// STYLES
// =====================================

const inputStyle = {
  background: "#101010",

  color: "white",

  border: "1px solid #333",

  borderRadius: "10px",

  padding: "10px",

  outline: "none",
};

const blueButton = {
  background: "#2563eb",

  color: "white",

  border: "none",

  borderRadius: "10px",

  padding: "10px 12px",

  cursor: "pointer",

  fontWeight: "bold",
};

const redButton = {
  background: "#7f1d1d",

  color: "white",

  border: "none",

  borderRadius: "10px",

  padding: "10px 12px",

  cursor: "pointer",

  fontWeight: "bold",
};