// =====================================
// PLAYLIST PAGE STYLES
// =====================================

export const pageStyle = {

  background: "#0f0f0f",

  minHeight: "100vh",

  color: "white",

  padding: "20px",
};

// =====================================
// HEADER
// =====================================

export const headerStyle = {

  display: "flex",

  justifyContent: "space-between",

  alignItems: "center",

  marginBottom: "20px",
};

// =====================================
// TITLE
// =====================================

export const titleStyle = {

  fontSize: "42px",

  margin: 0,

  fontWeight: "bold",
};

// =====================================
// SUBTITLE
// =====================================

export const subtitleStyle = {

  opacity: 0.7,

  marginTop: "8px",

  fontSize: "14px",
};

// =====================================
// GRID
// =====================================

export const layoutGridStyle = {

  display: "grid",

  gridTemplateColumns:
    "320px 1fr",

  gap: "20px",
};

// =====================================
// LEFT PANEL
// =====================================

export const sidebarStyle = {

  display: "flex",

  flexDirection: "column",

  gap: "20px",
};

// =====================================
// CONTENT
// =====================================

export const contentStyle = {

  display: "flex",

  flexDirection: "column",

  gap: "20px",
};

// =====================================
// CARD
// =====================================

export const cardStyle = {

  background: "#181818",

  border: "1px solid #2a2a2a",

  borderRadius: "16px",

  padding: "18px",
};

// =====================================
// SEARCH INPUT
// =====================================

export const inputStyle = {

  width: "100%",

  padding: "12px",

  background: "#111",

  color: "white",

  border: "1px solid #333",

  borderRadius: "10px",

  outline: "none",

  boxSizing: "border-box",
};

// =====================================
// BUTTON
// =====================================

export const buttonStyle = {

  padding: "10px 14px",

  background: "lime",

  color: "black",

  border: "none",

  borderRadius: "10px",

  cursor: "pointer",

  fontWeight: "bold",
};

// =====================================
// PLAYLIST GRID
// =====================================

export const playlistGridStyle = {

  display: "grid",

  gridTemplateColumns:
    "repeat(auto-fill,minmax(320px,1fr))",

  gap: "16px",
};

// =====================================
// PLAYLIST CARD
// =====================================

export const playlistCardStyle = {

  background: "#1b1b1b",

  border: "1px solid #2f2f2f",

  borderRadius: "16px",

  overflow: "hidden",

  cursor: "pointer",

  transition: "0.2s",
};

// =====================================
// PLAYLIST IMAGE
// =====================================

export const thumbnailStyle = {

  width: "100%",

  height: "180px",

  objectFit: "cover",

  background: "#111",
};

// =====================================
// PLAYLIST BODY
// =====================================

export const playlistBodyStyle = {

  padding: "16px",
};

// =====================================
// PLAYLIST TITLE
// =====================================

export const playlistTitleStyle = {

  fontSize: "18px",

  fontWeight: "bold",

  lineHeight: 1.4,
};

// =====================================
// PLAYLIST CHANNEL
// =====================================

export const playlistChannelStyle = {

  marginTop: "8px",

  opacity: 0.7,

  fontSize: "14px",
};

// =====================================
// PROGRESS BAR WRAPPER
// =====================================

export const progressWrapperStyle = {

  width: "100%",

  height: "10px",

  background: "#333",

  borderRadius: "999px",

  overflow: "hidden",

  marginTop: "14px",
};

// =====================================
// PROGRESS BAR
// =====================================

export const progressBarStyle = (
  progress = 0
) => ({

  width: `${progress}%`,

  height: "100%",

  background: "lime",
});

// =====================================
// VIDEO LIST
// =====================================

export const videoListStyle = {

  display: "flex",

  flexDirection: "column",

  gap: "12px",

  marginTop: "20px",
};

// =====================================
// VIDEO ITEM
// =====================================

export const videoItemStyle = {

  background: "#202020",

  border: "1px solid #333",

  borderRadius: "12px",

  padding: "14px",
};

// =====================================
// FLASHCARD PANEL
// =====================================

export const flashcardPanelStyle = {

  background: "#151515",

  border: "1px solid #2d2d2d",

  borderRadius: "12px",

  padding: "14px",

  marginTop: "12px",
};

// =====================================
// NOTE PANEL
// =====================================

export const notePanelStyle = {

  background: "#121212",

  border: "1px solid #2a2a2a",

  borderRadius: "12px",

  padding: "14px",

  marginTop: "12px",

  whiteSpace: "pre-wrap",

  lineHeight: 1.7,
};