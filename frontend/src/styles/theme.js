// =====================================
// COLORS
// =====================================

export const colors = {

  background:
    "#0f0f0f",

  card:
    "#181818",

  cardSecondary:
    "#1f1f1f",

  cardHover:
    "#2a2a2a",

  border:
    "#2f2f2f",

  borderLight:
    "#3a3a3a",

  text:
    "#ffffff",

  textSecondary:
    "rgba(255,255,255,0.7)",

  textMuted:
    "rgba(255,255,255,0.5)",

  success:
    "lime",

  danger:
    "#ff4d4f",

  warning:
    "#facc15",

  info:
    "#00d4ff",

  inputBackground:
    "#101010",
};

// =====================================
// CARD STYLE
// =====================================

export const cardStyle = {

  background:
    colors.card,

  padding: "18px",

  borderRadius: "16px",

  border:
    `1px solid ${colors.border}`,
};

// =====================================
// INPUT STYLE
// =====================================

export const inputStyle = {

  width: "100%",

  padding: "10px",

  marginTop: "10px",

  background:
    colors.inputBackground,

  color:
    colors.text,

  border:
    `1px solid ${colors.borderLight}`,

  borderRadius: "8px",

  boxSizing:
    "border-box",
};

// =====================================
// BUTTON STYLE
// =====================================

export const buttonStyle = {

  width: "100%",

  padding: "12px",

  marginTop: "10px",

  background:
    colors.success,

  color: "black",

  border: "none",

  borderRadius: "8px",

  cursor: "pointer",

  fontWeight: "bold",
};

// =====================================
// PANEL TITLE STYLE
// =====================================

export const panelTitleStyle = {

  fontSize: "24px",

  fontWeight: "bold",

  marginBottom: "12px",
};

// =====================================
// SMALL TEXT STYLE
// =====================================

export const smallTextStyle = {

  fontSize: "13px",

  opacity: 0.7,
};

// =====================================
// PROGRESS BAR
// =====================================

export const progressBarStyle = {

  height: "8px",

  background: "#333",

  borderRadius: "999px",

  overflow: "hidden",
};

// =====================================
// PROGRESS FILL
// =====================================

export const getProgressFillStyle = (
  progress
) => ({

  width:
    `${progress}%`,

  height: "100%",

  background:
    colors.success,
});