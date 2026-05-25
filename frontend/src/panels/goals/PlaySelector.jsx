export default function PlaylistSelector({
  playlists = [],

  goal,

  linkPlaylist,
}) {
  // =====================================
  // MAIN
  // =====================================

  return (
    <div>
      {/* HEADER */}

      <div
        style={{
          display: "flex",

          justifyContent: "space-between",

          alignItems: "center",

          marginBottom: "22px",
        }}
      >
        <div>
          <div
            style={{
              color: "white",

              fontSize: "24px",

              fontWeight: "bold",

              marginBottom: "6px",
            }}
          >
            Playlist Importları
          </div>

          <div
            style={{
              color: "#9ca3af",

              fontSize: "14px",
            }}
          >
            Hedefe playlist bağla
          </div>
        </div>
      </div>

      {/* PLAYLISTS */}

      <div
        style={{
          display: "flex",

          flexDirection: "column",

          gap: "16px",
        }}
      >
        {playlists.map((playlist) => {
          const isLinked =
            goal.linkedPlaylists?.includes(
              playlist.id
            );

          return (
            <div
              key={playlist.id}
              style={{
                background: "#181818",

                border: "1px solid #2a2a2a",

                borderRadius: "18px",

                padding: "18px",

                display: "flex",

                justifyContent:
                  "space-between",

                alignItems: "center",

                gap: "20px",

                transition: "0.2s",
              }}
            >
              {/* LEFT */}

              <div
                style={{
                  flex: 1,
                }}
              >
                {/* TITLE */}

                <div
                  style={{
                    color: "white",

                    fontSize: "18px",

                    fontWeight: "600",

                    marginBottom: "10px",
                  }}
                >
                  {playlist.title}
                </div>

                {/* STATS */}

                <div
                  style={{
                    display: "flex",

                    flexWrap: "wrap",

                    gap: "18px",

                    color: "#9ca3af",

                    fontSize: "13px",
                  }}
                >
                  <div>
                    📚 Sıra:{" "}
                    {playlist.order_index ||
                      0}
                  </div>

                  <div>
                    ⏱{" "}
                    {playlist.toplam_saat ||
                      0}{" "}
                    saat
                  </div>

                  <div>
                    🔥{" "}
                    {playlist.remaining_minutes ||
                      0}{" "}
                    dk
                  </div>

                  <div>
                    🎯{" "}
                    {playlist.daily_target_minutes ||
                      0}{" "}
                    dk
                  </div>

                  <div>
                    📅{" "}
                    {playlist.target_days ||
                      0}{" "}
                    gün
                  </div>
                </div>

                {/* PROGRESS */}

                <div
                  style={{
                    marginTop: "14px",
                  }}
                >
                  <div
                    style={{
                      width: "100%",

                      height: "8px",

                      background: "#222",

                      borderRadius: "999px",

                      overflow: "hidden",
                    }}
                  >
                    <div
                      style={{
                        width: `${
                          playlist.yuzde ||
                          0
                        }%`,

                        height: "100%",

                        background:
                          "#22c55e",
                      }}
                    />
                  </div>

                  <div
                    style={{
                      marginTop: "6px",

                      fontSize: "12px",

                      color: "#9ca3af",
                    }}
                  >
                    %{playlist.yuzde || 0} tamamlandı
                  </div>
                </div>
              </div>

              {/* RIGHT */}

              <div
                style={{
                  display: "flex",

                  flexDirection: "column",

                  alignItems: "flex-end",

                  gap: "12px",
                }}
              >
                {/* BUTTON */}

                <button
                  onClick={() =>
                    linkPlaylist(
                      goal.id,
                      playlist.id
                    )
                  }
                  disabled={isLinked}
                  style={{
                    background: isLinked
                      ? "#14532d"
                      : "#2563eb",

                    color: "white",

                    border: "none",

                    borderRadius: "12px",

                    padding:
                      "12px 22px",

                    cursor: isLinked
                      ? "default"
                      : "pointer",

                    fontWeight: "bold",

                    minWidth: "120px",

                    opacity: isLinked
                      ? 0.7
                      : 1,
                  }}
                >
                  {isLinked
                    ? "Bağlandı"
                    : "Bağla"}
                </button>

                {/* STATUS */}

                <div
                  style={{
                    color: isLinked
                      ? "#22c55e"
                      : "#9ca3af",

                    fontSize: "12px",

                    fontWeight: "bold",
                  }}
                >
                  {isLinked
                    ? "AKTİF"
                    : "BAĞLI DEĞİL"}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}