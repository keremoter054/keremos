export default function GoalDetailPanel({
  goal,

  playlists = [],

  linkPlaylist,
}) {
  // =====================================
  // LINKED PLAYLISTS
  // =====================================

  const linkedPlaylists = playlists.filter(
    (playlist) =>
      goal.linkedPlaylists?.includes(
        playlist.id
      )
  );

  // =====================================
  // MAIN
  // =====================================

  return (
    <div
      style={{
        borderTop: "1px solid #2f2f2f",

        background: "#111",

        padding: "24px",
      }}
    >
      {/* HEADER */}

      <div
        style={{
          display: "flex",

          justifyContent: "space-between",

          alignItems: "center",

          marginBottom: "24px",
        }}
      >
        <div>
          <div
            style={{
              color: "white",

              fontSize: "28px",

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
            Hedefe bağlı playlist sistemi
          </div>
        </div>
      </div>

      {/* PLAYLIST IMPORTS */}

      <div
        style={{
          display: "flex",

          flexDirection: "column",

          gap: "16px",

          marginBottom: "32px",
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
              }}
            >
              {/* LEFT */}

              <div
                style={{
                  flex: 1,
                }}
              >
                <div
                  style={{
                    color: "white",

                    fontSize: "18px",

                    fontWeight: "600",

                    marginBottom: "8px",
                  }}
                >
                  {playlist.title}
                </div>

                <div
                  style={{
                    display: "flex",

                    gap: "18px",

                    flexWrap: "wrap",

                    color: "#9ca3af",

                    fontSize: "13px",
                  }}
                >
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
              </div>

              {/* RIGHT */}

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

                  padding: "12px 22px",

                  cursor: isLinked
                    ? "default"
                    : "pointer",

                  fontWeight: "bold",

                  opacity: isLinked
                    ? 0.7
                    : 1,

                  minWidth: "120px",
                }}
              >
                {isLinked
                  ? "Bağlandı"
                  : "Bağla"}
              </button>
            </div>
          );
        })}
      </div>

      {/* LINKED PLAYLISTS */}

      {linkedPlaylists.length > 0 && (
        <div>
          {/* TITLE */}

          <div
            style={{
              color: "white",

              fontSize: "24px",

              fontWeight: "bold",

              marginBottom: "20px",
            }}
          >
            Bağlı Playlistler
          </div>

          {/* LIST */}

          <div
            style={{
              display: "flex",

              flexDirection: "column",

              gap: "16px",
            }}
          >
            {linkedPlaylists.map(
              (playlist) => (
                <div
                  key={playlist.id}
                  style={{
                    background: "#181818",

                    border:
                      "1px solid #2a2a2a",

                    borderRadius: "18px",

                    padding: "20px",
                  }}
                >
                  {/* TOP */}

                  <div
                    style={{
                      display: "flex",

                      justifyContent:
                        "space-between",

                      alignItems:
                        "center",

                      marginBottom:
                        "18px",
                    }}
                  >
                    <div
                      style={{
                        color:
                          "white",

                        fontSize:
                          "20px",

                        fontWeight:
                          "bold",
                      }}
                    >
                      {playlist.title}
                    </div>

                    <div
                      style={{
                        color:
                          "#22c55e",

                        fontWeight:
                          "bold",
                      }}
                    >
                      AKTİF
                    </div>
                  </div>

                  {/* GRID */}

                  <div
                    style={{
                      display: "grid",

                      gridTemplateColumns:
                        "repeat(5,1fr)",

                      gap: "16px",
                    }}
                  >
                    {/* TOTAL */}

                    <div
                      style={statCard}
                    >
                      <div
                        style={statLabel}
                      >
                        Toplam
                      </div>

                      <div
                        style={statValue}
                      >
                        {
                          playlist.toplam_saat
                        }{" "}
                        saat
                      </div>
                    </div>

                    {/* REMAINING */}

                    <div
                      style={statCard}
                    >
                      <div
                        style={statLabel}
                      >
                        Kalan
                      </div>

                      <div
                        style={statValue}
                      >
                        {playlist.remaining_minutes ||
                          0}{" "}
                        dk
                      </div>
                    </div>

                    {/* DAILY */}

                    <div
                      style={statCard}
                    >
                      <div
                        style={statLabel}
                      >
                        Günlük
                      </div>

                      <div
                        style={statValue}
                      >
                        {playlist.daily_target_minutes ||
                          0}{" "}
                        dk
                      </div>
                    </div>

                    {/* TARGET */}

                    <div
                      style={statCard}
                    >
                      <div
                        style={statLabel}
                      >
                        Hedef
                      </div>

                      <div
                        style={statValue}
                      >
                        {playlist.target_days ||
                          0}{" "}
                        gün
                      </div>
                    </div>

                    {/* PROGRESS */}

                    <div
                      style={statCard}
                    >
                      <div
                        style={statLabel}
                      >
                        Progress
                      </div>

                      <div
                        style={statValue}
                      >
                        %
                        {playlist.yuzde ||
                          0}
                      </div>
                    </div>
                  </div>

                  {/* PROGRESS BAR */}

                  <div
                    style={{
                      marginTop: "20px",
                    }}
                  >
                    <div
                      style={{
                        width: "100%",

                        height: "10px",

                        background:
                          "#222",

                        borderRadius:
                          "999px",

                        overflow:
                          "hidden",
                      }}
                    >
                      <div
                        style={{
                          width: `${
                            playlist.yuzde ||
                            0
                          }%`,

                          height:
                            "100%",

                          background:
                            "#22c55e",
                        }}
                      />
                    </div>
                  </div>
                </div>
              )
            )}
          </div>
        </div>
      )}
    </div>
  );
}

// =====================================
// STYLES
// =====================================

const statCard = {
  background: "#101010",

  border: "1px solid #2f2f2f",

  borderRadius: "14px",

  padding: "14px",
};

const statLabel = {
  color: "#9ca3af",

  fontSize: "12px",

  marginBottom: "8px",
};

const statValue = {
  color: "white",

  fontSize: "18px",

  fontWeight: "bold",
};